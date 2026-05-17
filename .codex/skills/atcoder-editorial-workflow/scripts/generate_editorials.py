from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import time
from dataclasses import dataclass
from pathlib import Path

import requests


DEFAULT_MAX_ATTEMPTS = 3
DEFAULT_COMPILE_TIMEOUT = 30
DEFAULT_RUN_TIMEOUT = 5
DEFAULT_MODEL = "gpt-4"
ALLOWED_REASONING_EFFORTS = {"none", "minimal", "low", "medium", "high", "xhigh"}
DEFAULT_CPP_STANDARD = "gnu++14"
SAMPLE_INPUT_PATTERN = re.compile(r"^### Sample Input(?: (\d+))?$")
SAMPLE_OUTPUT_PATTERN = re.compile(r"^### Sample Output(?: (\d+))?$")
TITLE_PATTERN = re.compile(r"^#\s+(.*)$")
CPP_BLOCK_PATTERN = re.compile(r"```cpp\s*([\s\S]*?)```", flags=re.IGNORECASE)


class EditorialGenerationError(RuntimeError):
    pass


@dataclass
class SampleCase:
    index: int
    input_text: str
    output_text: str


@dataclass
class SampleRunResult:
    index: int
    passed: bool
    expected_output: str
    actual_output: str
    stderr_text: str
    timed_out: bool
    return_code: int


@dataclass
class ValidationResult:
    passed: bool
    report_text: str
    code_text: str
    compile_command: list[str]
    compile_stdout: str
    compile_stderr: str
    compile_return_code: int
    sample_results: list[SampleRunResult]


def default_env_file() -> Path:
    cwd_env = Path.cwd() / ".env"
    if cwd_env.exists():
        return cwd_env
    return Path(__file__).resolve().parents[4] / ".env"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate AtCoder editorials with model API calls and sample validation."
    )
    parser.add_argument("contest", help="Contest ID, for example: abc458")
    parser.add_argument(
        "--workspace",
        type=Path,
        default=Path.cwd() / "atcoder-output",
        help="Base output directory. Default: ./atcoder-output",
    )
    parser.add_argument(
        "--problem",
        action="append",
        default=[],
        help="Problem id to generate, for example: a . Can be passed multiple times.",
    )
    parser.add_argument(
        "--statement-dir",
        type=Path,
        default=None,
        help="Override English statement directory. Default: <workspace>/<contest>/en",
    )
    parser.add_argument(
        "--editorial-dir",
        type=Path,
        default=None,
        help="Override editorial directory. Default: <workspace>/<contest>/editorials",
    )
    parser.add_argument(
        "--env-file",
        type=Path,
        default=default_env_file(),
        help="Path to .env file. Default: ./.env when present",
    )
    parser.add_argument(
        "--api-key-env",
        default="OPENAI_API_KEY",
        help="Environment variable name for the API key. Default: OPENAI_API_KEY",
    )
    parser.add_argument(
        "--api-mode",
        default="chat",
        choices=["chat", "responses"],
        help="OpenAI API mode. Default: chat",
    )
    parser.add_argument(
        "--base-url",
        default="",
        help="Override model API endpoint. Default uses OPENAI_BASE_URL or official endpoint.",
    )
    parser.add_argument(
        "--model",
        default="",
        help="Override model name. Default uses OPENAI_MODEL or gpt-4",
    )
    parser.add_argument(
        "--reasoning-effort",
        default="",
        help="Override reasoning effort. Default uses OPENAI_REASONING_EFFORT or model default.",
    )
    parser.add_argument(
        "--max-attempts",
        type=int,
        default=DEFAULT_MAX_ATTEMPTS,
        help=f"Maximum attempts per problem. Default: {DEFAULT_MAX_ATTEMPTS}",
    )
    parser.add_argument(
        "--compiler",
        default="g++",
        help="C++ compiler command. Default: g++",
    )
    parser.add_argument(
        "--cpp-standard",
        default=DEFAULT_CPP_STANDARD,
        help=f"C++ standard for compilation. Default: {DEFAULT_CPP_STANDARD}",
    )
    parser.add_argument(
        "--compile-timeout",
        type=int,
        default=DEFAULT_COMPILE_TIMEOUT,
        help=f"Compilation timeout in seconds. Default: {DEFAULT_COMPILE_TIMEOUT}",
    )
    parser.add_argument(
        "--run-timeout",
        type=int,
        default=DEFAULT_RUN_TIMEOUT,
        help=f"Per-sample runtime timeout in seconds. Default: {DEFAULT_RUN_TIMEOUT}",
    )
    parser.add_argument(
        "--overwrite",
        action=argparse.BooleanOptionalAction,
        default=True,
        help="Overwrite existing editorial markdown. Default: enabled",
    )
    return parser.parse_args()


def load_dotenv(env_file: Path) -> None:
    if not env_file.exists():
        return
    for raw_line in env_file.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("export "):
            line = line[len("export ") :].strip()
        if "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip()
        if not key:
            continue
        if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
            value = value[1:-1]
        os.environ.setdefault(key, value)


def default_base_url(api_mode: str) -> str:
    if api_mode == "chat":
        return "https://api.openai.com/v1/chat/completions"
    return "https://api.openai.com/v1/responses"


def resolve_api_mode(args: argparse.Namespace) -> str:
    env_mode = os.environ.get("OPENAI_API_MODE", "").strip().lower()
    if env_mode in {"chat", "responses"}:
        return env_mode
    return args.api_mode


def resolve_base_url(args: argparse.Namespace, api_mode: str) -> str:
    if args.base_url.strip():
        return args.base_url.strip()
    env_base_url = os.environ.get("OPENAI_BASE_URL", "").strip()
    if env_base_url:
        return env_base_url
    return default_base_url(api_mode)


def resolve_model(args: argparse.Namespace) -> str:
    if args.model.strip():
        return args.model.strip()
    env_model = os.environ.get("OPENAI_MODEL", "").strip()
    if env_model:
        return env_model
    return DEFAULT_MODEL


def normalize_reasoning_effort(value: str, *, source: str) -> str:
    normalized = value.strip().lower()
    if not normalized:
        return ""
    if normalized not in ALLOWED_REASONING_EFFORTS:
        allowed = ", ".join(sorted(ALLOWED_REASONING_EFFORTS))
        raise EditorialGenerationError(
            f"Unsupported reasoning effort from {source}: {value!r}. Expected one of: {allowed}"
        )
    return normalized


def resolve_reasoning_effort(args: argparse.Namespace) -> str:
    if args.reasoning_effort.strip():
        return normalize_reasoning_effort(args.reasoning_effort, source="--reasoning-effort")
    env_effort = os.environ.get("OPENAI_REASONING_EFFORT", "").strip()
    if env_effort:
        return normalize_reasoning_effort(env_effort, source="OPENAI_REASONING_EFFORT")
    return ""


def normalized_problem_ids(problem_args: list[str]) -> list[str]:
    values: list[str] = []
    for raw in problem_args:
        for token in raw.split(","):
            problem = token.strip().lower()
            if problem:
                values.append(problem)
    return values


def extract_problem_title(statement_text: str) -> str:
    for line in statement_text.splitlines():
        match = TITLE_PATTERN.match(line.strip())
        if match:
            return match.group(1).strip()
    raise EditorialGenerationError("Could not find statement title heading.")


def extract_fenced_block(lines: list[str], start_index: int) -> tuple[str, int]:
    if start_index >= len(lines) or not lines[start_index].startswith("```"):
        raise EditorialGenerationError("Expected fenced code block after sample heading.")
    content_lines: list[str] = []
    index = start_index + 1
    while index < len(lines) and not lines[index].startswith("```"):
        content_lines.append(lines[index])
        index += 1
    if index >= len(lines):
        raise EditorialGenerationError("Unclosed fenced code block while parsing samples.")
    return "\n".join(content_lines).strip("\n"), index + 1


def extract_samples(statement_text: str) -> list[SampleCase]:
    lines = statement_text.replace("\r\n", "\n").replace("\r", "\n").split("\n")
    inputs: dict[int, str] = {}
    outputs: dict[int, str] = {}
    pending_kind = ""
    pending_index = 0
    next_input_index = 1
    next_output_index = 1
    i = 0
    while i < len(lines):
        stripped = lines[i].strip()
        input_match = SAMPLE_INPUT_PATTERN.match(stripped)
        output_match = SAMPLE_OUTPUT_PATTERN.match(stripped)
        if input_match:
            pending_kind = "input"
            pending_index = int(input_match.group(1) or next_input_index)
            next_input_index = max(next_input_index, pending_index + 1)
            i += 1
            while i < len(lines) and not lines[i].strip():
                i += 1
            block_text, i = extract_fenced_block(lines, i)
            inputs[pending_index] = block_text
            pending_kind = ""
            continue
        if output_match:
            pending_kind = "output"
            pending_index = int(output_match.group(1) or next_output_index)
            next_output_index = max(next_output_index, pending_index + 1)
            i += 1
            while i < len(lines) and not lines[i].strip():
                i += 1
            block_text, i = extract_fenced_block(lines, i)
            outputs[pending_index] = block_text
            pending_kind = ""
            continue
        i += 1

    sample_ids = sorted(set(inputs) & set(outputs))
    if not sample_ids:
        raise EditorialGenerationError("No complete sample input/output pairs found in statement.")
    return [
        SampleCase(index=sample_id, input_text=inputs[sample_id], output_text=outputs[sample_id])
        for sample_id in sample_ids
    ]


def normalize_output_text(text: str) -> str:
    normalized = text.replace("\r\n", "\n").replace("\r", "\n")
    lines = [line.rstrip() for line in normalized.split("\n")]
    while lines and lines[-1] == "":
        lines.pop()
    return "\n".join(lines)


def extract_cpp_code(markdown_text: str) -> str:
    match = CPP_BLOCK_PATTERN.search(markdown_text)
    if not match:
        raise EditorialGenerationError("Model response does not contain a cpp fenced code block.")
    return match.group(1).strip() + "\n"


def build_problem_output_path(editorial_dir: Path, statement_path: Path) -> Path:
    stem = statement_path.stem
    if stem.endswith(".en"):
        stem = stem[:-3]
    return editorial_dir / f"{stem}.editorial.md"


def build_report_path(editorial_dir: Path, statement_path: Path) -> Path:
    validation_dir = editorial_dir / ".validation"
    validation_dir.mkdir(parents=True, exist_ok=True)
    stem = statement_path.stem
    if stem.endswith(".en"):
        stem = stem[:-3]
    return validation_dir / f"{stem}.sample-check.md"


def build_attempt_dir(editorial_dir: Path, statement_path: Path) -> Path:
    tmp_dir = editorial_dir / ".tmp" / "editorial-generation"
    stem = statement_path.stem
    if stem.endswith(".en"):
        stem = stem[:-3]
    target = tmp_dir / stem
    target.mkdir(parents=True, exist_ok=True)
    return target


def statement_paths_for_args(args: argparse.Namespace) -> list[Path]:
    contest = args.contest.strip().lower()
    statement_dir = args.statement_dir or (args.workspace / contest / "en")
    if not statement_dir.is_dir():
        raise EditorialGenerationError(f"English statement directory not found: {statement_dir}")
    specified = normalized_problem_ids(args.problem)
    if specified:
        paths = [statement_dir / f"{contest}_{problem}.en.md" for problem in specified]
        missing = [str(path) for path in paths if not path.is_file()]
        if missing:
            raise EditorialGenerationError("Missing statement files: " + ", ".join(missing))
        return paths
    return sorted(statement_dir.glob(f"{contest}_*.en.md"))


def build_prompt(
    *,
    contest: str,
    problem_title: str,
    statement_text: str,
    samples: list[SampleCase],
    previous_markdown: str,
    previous_report: str,
    attempt_index: int,
) -> str:
    sample_summary_parts: list[str] = []
    for sample in samples:
        sample_summary_parts.append(
            "\n".join(
                [
                    f"样例 {sample.index} 输入：",
                    "```text",
                    sample.input_text,
                    "```",
                    f"样例 {sample.index} 输出：",
                    "```text",
                    sample.output_text,
                    "```",
                ]
            )
        )
    sample_summary = "\n\n".join(sample_summary_parts)

    retry_block = ""
    if attempt_index > 1:
        retry_block = (
            "上一版题解未通过样例校验，请根据下面的失败结果修正。\n\n"
            "上一版题解：\n"
            "```markdown\n"
            f"{previous_markdown.strip()}\n"
            "```\n\n"
            "上一轮样例检测结果：\n"
            "```text\n"
            f"{previous_report.strip()}\n"
            "```\n"
        )

    return (
        f"请为 AtCoder 比赛 `{contest}` 的题目 `{problem_title}` 撰写中文题解。\n"
        "要求：\n"
        "1. 只输出最终 Markdown，不要输出额外说明。\n"
        "2. 固定结构必须按顺序包含：\n"
        "   - `# <比赛> <题号> - <题名> 题解`\n"
        "   - `## 题意概括`\n"
        "   - `## 解题思路`\n"
        "   - `## 正确性说明`\n"
        "   - `## 复杂度`\n"
        "   - `## 参考实现`\n"
        "3. 参考实现必须是 `cpp` fenced code block，且与正文思路一致。\n"
        "4. 代码风格要求：使用 `#include<bits/stdc++.h>`、`using namespace std;`、`int main(){`、4 空格缩进；关键逻辑前写简短教学注释；优先清晰可讲解的写法。\n"
        "5. 复杂度必须写时间复杂度和空间复杂度。\n"
        "6. 不要保留 `## 题目信息` 一类旧章节，不要输出 JSON。\n"
        "7. 只根据下面给出的题面与样例作答，不要虚构额外输入格式。\n\n"
        f"{retry_block}"
        "英文题面 Markdown：\n"
        "```markdown\n"
        f"{statement_text.strip()}\n"
        "```\n\n"
        "样例摘要：\n"
        f"{sample_summary}\n"
    )


def build_system_prompt() -> str:
    return (
        "You write Chinese AtCoder editorials.\n"
        "Return only the final Markdown editorial.\n"
        "Keep the explanation rigorous and classroom-friendly.\n"
        "The C++ code must be consistent with the editorial and should be written to pass the provided samples.\n"
    )


def build_chat_payload(
    model: str,
    system_prompt: str,
    user_prompt: str,
    reasoning_effort: str,
) -> dict:
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        "stream": False,
    }
    if reasoning_effort:
        payload["reasoning_effort"] = reasoning_effort
    return payload


def build_responses_payload(
    model: str,
    system_prompt: str,
    user_prompt: str,
    reasoning_effort: str,
) -> dict:
    payload = {
        "model": model,
        "input": [
            {
                "role": "system",
                "content": [{"type": "input_text", "text": system_prompt}],
            },
            {
                "role": "user",
                "content": [{"type": "input_text", "text": user_prompt}],
            },
        ],
    }
    if reasoning_effort:
        payload["reasoning"] = {"effort": reasoning_effort}
    return payload


def extract_response_text(payload: dict, api_mode: str) -> str:
    if api_mode == "chat":
        choices = payload.get("choices", [])
        if not choices:
            raise EditorialGenerationError("Model API returned no choices.")
        message = choices[0].get("message", {})
        content = message.get("content")
        if isinstance(content, str) and content.strip():
            return content.strip()
        if isinstance(content, list):
            parts: list[str] = []
            for item in content:
                if isinstance(item, dict):
                    text = item.get("text")
                    if isinstance(text, str):
                        parts.append(text)
            result = "".join(parts).strip()
            if result:
                return result
        raise EditorialGenerationError("Model API returned empty chat content.")

    direct = payload.get("output_text")
    if isinstance(direct, str) and direct.strip():
        return direct.strip()
    parts: list[str] = []
    for item in payload.get("output", []):
        if not isinstance(item, dict):
            continue
        for content in item.get("content", []):
            if isinstance(content, dict):
                text = content.get("text")
                if isinstance(text, str):
                    parts.append(text)
    result = "".join(parts).strip()
    if not result:
        raise EditorialGenerationError("Model API returned empty responses content.")
    return result


def request_editorial(
    *,
    api_key: str,
    api_mode: str,
    base_url: str,
    model: str,
    reasoning_effort: str,
    user_prompt: str,
    timeout: int,
) -> str:
    payload = (
        build_chat_payload(model, build_system_prompt(), user_prompt, reasoning_effort)
        if api_mode == "chat"
        else build_responses_payload(model, build_system_prompt(), user_prompt, reasoning_effort)
    )
    response = requests.post(
        base_url,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        json=payload,
        timeout=timeout,
    )
    if not response.ok:
        raise EditorialGenerationError(
            f"Model API request failed: HTTP {response.status_code} {response.text}"
        )
    return extract_response_text(response.json(), api_mode)


def run_subprocess(
    command: list[str],
    *,
    cwd: Path,
    timeout_seconds: int,
    input_text: str | None = None,
) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        command,
        cwd=str(cwd),
        input=input_text,
        text=True,
        capture_output=True,
        encoding="utf-8",
        errors="replace",
        timeout=timeout_seconds,
        check=False,
    )


def validate_markdown(
    *,
    markdown_text: str,
    samples: list[SampleCase],
    attempt_dir: Path,
    compiler: str,
    cpp_standard: str,
    compile_timeout: int,
    run_timeout: int,
    problem_stem: str,
) -> ValidationResult:
    code_text = extract_cpp_code(markdown_text)
    cpp_path = attempt_dir / f"{problem_stem}.cpp"
    exe_path = attempt_dir / f"{problem_stem}.exe"
    cpp_path.write_text(code_text, encoding="utf-8")
    if exe_path.exists():
        exe_path.unlink()

    compile_command = [compiler, cpp_path.name, f"-std={cpp_standard}", "-O2", "-o", exe_path.name]
    compile_result = run_subprocess(
        compile_command,
        cwd=attempt_dir,
        timeout_seconds=compile_timeout,
    )
    if compile_result.returncode != 0 or not exe_path.exists():
        report_text = "\n".join(
            [
                "编译结果：失败",
                "编译命令：" + subprocess.list2cmdline(compile_command),
                "编译退出码：" + str(compile_result.returncode),
                "",
                "stderr：",
                compile_result.stderr.strip() or "(empty)",
                "",
                "stdout：",
                compile_result.stdout.strip() or "(empty)",
            ]
        ).strip()
        return ValidationResult(
            passed=False,
            report_text=report_text,
            code_text=code_text,
            compile_command=compile_command,
            compile_stdout=compile_result.stdout,
            compile_stderr=compile_result.stderr,
            compile_return_code=compile_result.returncode,
            sample_results=[],
        )

    sample_results: list[SampleRunResult] = []
    passed = True
    for sample in samples:
        try:
            run_result = run_subprocess(
                [str(exe_path.resolve())],
                cwd=attempt_dir,
                timeout_seconds=run_timeout,
                input_text=sample.input_text,
            )
            actual_output = normalize_output_text(run_result.stdout)
            expected_output = normalize_output_text(sample.output_text)
            sample_passed = (
                run_result.returncode == 0
                and not run_result.stderr.strip()
                and actual_output == expected_output
            )
            if not sample_passed:
                passed = False
            sample_results.append(
                SampleRunResult(
                    index=sample.index,
                    passed=sample_passed,
                    expected_output=expected_output,
                    actual_output=actual_output,
                    stderr_text=run_result.stderr.strip(),
                    timed_out=False,
                    return_code=run_result.returncode,
                )
            )
        except subprocess.TimeoutExpired:
            passed = False
            sample_results.append(
                SampleRunResult(
                    index=sample.index,
                    passed=False,
                    expected_output=normalize_output_text(sample.output_text),
                    actual_output="",
                    stderr_text=f"Execution timed out after {run_timeout} seconds.",
                    timed_out=True,
                    return_code=-1,
                )
            )

    report_lines = [
        "编译结果：通过",
        "编译命令：" + subprocess.list2cmdline(compile_command),
        "",
    ]
    for result in sample_results:
        report_lines.extend(
            [
                f"样例 {result.index}：{'通过' if result.passed else '失败'}",
                "期望输出：",
                result.expected_output or "(empty)",
                "实际输出：",
                result.actual_output or "(empty)",
            ]
        )
        if result.stderr_text:
            report_lines.extend(["stderr：", result.stderr_text])
        if result.return_code not in {0, -1}:
            report_lines.append("程序退出码：" + str(result.return_code))
        report_lines.append("")
    report_lines.append("总结果：" + ("全部通过" if passed else "存在失败样例"))

    return ValidationResult(
        passed=passed,
        report_text="\n".join(report_lines).strip(),
        code_text=code_text,
        compile_command=compile_command,
        compile_stdout=compile_result.stdout,
        compile_stderr=compile_result.stderr,
        compile_return_code=compile_result.returncode,
        sample_results=sample_results,
    )


def write_report(
    *,
    report_path: Path,
    attempt_index: int,
    validation: ValidationResult,
    markdown_path: Path,
) -> None:
    parts = [
        f"# 样例校验报告：{markdown_path.stem}",
        "",
        f"- 尝试次数：{attempt_index}",
        f"- 结果：{'通过' if validation.passed else '失败'}",
        "",
        "```text",
        validation.report_text,
        "```",
        "",
    ]
    report_path.write_text("\n".join(parts), encoding="utf-8")


def generate_for_problem(
    *,
    contest: str,
    statement_path: Path,
    editorial_dir: Path,
    api_key: str,
    api_mode: str,
    base_url: str,
    model: str,
    reasoning_effort: str,
    args: argparse.Namespace,
) -> bool:
    statement_text = statement_path.read_text(encoding="utf-8")
    problem_title = extract_problem_title(statement_text)
    samples = extract_samples(statement_text)
    output_path = build_problem_output_path(editorial_dir, statement_path)
    report_path = build_report_path(editorial_dir, statement_path)
    attempt_dir = build_attempt_dir(editorial_dir, statement_path)
    problem_stem = output_path.stem.replace(".editorial", "")

    if output_path.exists() and not args.overwrite:
        print(f"[editorial-gen] skip existing {output_path}")
        return True

    previous_markdown = ""
    previous_report = ""

    print(f"[editorial-gen] problem={problem_title}")
    print(f"[editorial-gen] statement={statement_path}")
    print(f"[editorial-gen] output={output_path}")

    for attempt in range(1, args.max_attempts + 1):
        print(f"[editorial-gen] attempt {attempt}/{args.max_attempts}")
        prompt = build_prompt(
            contest=contest,
            problem_title=problem_title,
            statement_text=statement_text,
            samples=samples,
            previous_markdown=previous_markdown,
            previous_report=previous_report,
            attempt_index=attempt,
        )
        markdown_text = request_editorial(
            api_key=api_key,
            api_mode=api_mode,
            base_url=base_url,
            model=model,
            reasoning_effort=reasoning_effort,
            user_prompt=prompt,
            timeout=180,
        )
        validation = validate_markdown(
            markdown_text=markdown_text,
            samples=samples,
            attempt_dir=attempt_dir,
            compiler=args.compiler,
            cpp_standard=args.cpp_standard,
            compile_timeout=args.compile_timeout,
            run_timeout=args.run_timeout,
            problem_stem=problem_stem,
        )
        write_report(
            report_path=report_path,
            attempt_index=attempt,
            validation=validation,
            markdown_path=output_path,
        )
        print(validation.report_text)
        if validation.passed:
            output_path.write_text(markdown_text.strip() + "\n", encoding="utf-8")
            print(f"[editorial-gen] wrote {output_path}")
            print(f"[editorial-gen] report {report_path}")
            return True
        previous_markdown = markdown_text
        previous_report = validation.report_text

    print(f"[editorial-gen] failed after {args.max_attempts} attempts: {output_path.name}")
    return False


def ensure_prerequisites(args: argparse.Namespace, statement_paths: list[Path]) -> None:
    if args.max_attempts <= 0:
        raise EditorialGenerationError("--max-attempts must be positive.")
    if not statement_paths:
        raise EditorialGenerationError("No English statement files found to generate editorials.")
    if not shutil.which(args.compiler):
        raise EditorialGenerationError(f"Compiler not found in PATH: {args.compiler}")


def main() -> None:
    args = parse_args()
    contest = args.contest.strip().lower()
    load_dotenv(args.env_file)
    api_mode = resolve_api_mode(args)
    base_url = resolve_base_url(args, api_mode)
    model = resolve_model(args)
    reasoning_effort = resolve_reasoning_effort(args)
    api_key = os.environ.get(args.api_key_env, "").strip()
    if not api_key:
        raise EditorialGenerationError(
            f"Environment variable {args.api_key_env} is empty, cannot request model API."
        )

    statement_paths = statement_paths_for_args(args)
    ensure_prerequisites(args, statement_paths)
    editorial_dir = args.editorial_dir or (args.workspace / contest / "editorials")
    editorial_dir.mkdir(parents=True, exist_ok=True)

    print(f"[editorial-gen] contest={contest}")
    print(f"[editorial-gen] env_file={args.env_file}")
    print(f"[editorial-gen] api_mode={api_mode}")
    print(f"[editorial-gen] base_url={base_url}")
    print(f"[editorial-gen] model={model}")
    print(
        "[editorial-gen] reasoning_effort="
        + (reasoning_effort if reasoning_effort else "<provider-default>")
    )
    print(f"[editorial-gen] statement_count={len(statement_paths)}")
    print(f"[editorial-gen] editorial_dir={editorial_dir}")

    overall_success = True
    for statement_path in statement_paths:
        success = generate_for_problem(
            contest=contest,
            statement_path=statement_path,
            editorial_dir=editorial_dir,
            api_key=api_key,
            api_mode=api_mode,
            base_url=base_url,
            model=model,
            reasoning_effort=reasoning_effort,
            args=args,
        )
        if not success:
            overall_success = False

    if not overall_success:
        raise SystemExit(1)


if __name__ == "__main__":
    try:
        main()
    except EditorialGenerationError as exc:
        print(f"[editorial-gen] error={exc}", file=sys.stderr)
        raise SystemExit(2) from exc
