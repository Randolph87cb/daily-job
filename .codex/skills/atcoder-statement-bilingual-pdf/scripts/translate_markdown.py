from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Protocol

import requests


CODE_FENCE_PATTERN = re.compile(r"```[\s\S]*?```")
INLINE_CODE_PATTERN = re.compile(r"`[^`\n]+`")
MATH_PATTERN = re.compile(r"\$[^$\n]+\$")
URL_PATTERN = re.compile(r"https?://[^\s)]+")
INLINE_CODE_WRAPPED_MATH_PATTERN = re.compile(r"`(\$[^`\n$][^`\n]*?\$)`")
FENCED_BLOCK_PATTERN = re.compile(r"```[^\n]*\n([\s\S]*?)\n```")


class TranslationError(RuntimeError):
    pass


class Translator(Protocol):
    def translate_block(self, block: str) -> str: ...


@dataclass
class Glossary:
    heading_map: dict[str, str]
    exact_line_map: dict[str, str]
    prefix_map: dict[str, str]
    phrase_map: dict[str, str]
    term_map: dict[str, str]


@dataclass
class BlockPair:
    source: str
    translated: str


@dataclass
class Section:
    source_heading: str
    translated_heading: str
    blocks: list[BlockPair]


def default_base_url(api_mode: str) -> str:
    if api_mode == "chat":
        return "https://api.openai.com/v1/chat/completions"
    return "https://api.openai.com/v1/responses"


def default_env_file() -> Path:
    cwd_env = Path.cwd() / ".env"
    if cwd_env.exists():
        return cwd_env
    return Path(__file__).resolve().parent.parent / ".env"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Translate AtCoder-style Markdown from English to Simplified Chinese."
    )
    parser.add_argument("--input-dir", required=True, type=Path, help="Directory of .en.md files.")
    parser.add_argument("--output-dir", required=True, type=Path, help="Directory of translated files.")
    parser.add_argument(
        "--provider",
        default="rule-based",
        choices=["rule-based", "openai"],
        help="Translation provider. Default: rule-based",
    )
    parser.add_argument(
        "--glossary",
        type=Path,
        default=Path(__file__).resolve().parent.parent / "translation_assets" / "algorithm_glossary.json",
        help="Glossary JSON path.",
    )
    parser.add_argument(
        "--model",
        default="gpt-4",
        help="Model used by the openai provider. Default: gpt-4",
    )
    parser.add_argument(
        "--api-mode",
        default="responses",
        choices=["responses", "chat"],
        help="OpenAI API mode. Default: responses",
    )
    parser.add_argument(
        "--api-key-env",
        default="OPENAI_API_KEY",
        help="Environment variable name for the OpenAI API key. Default: OPENAI_API_KEY",
    )
    parser.add_argument(
        "--env-file",
        type=Path,
        default=default_env_file(),
        help="Path to a .env file. Default: ../.env",
    )
    parser.add_argument(
        "--base-url",
        default="",
        help="API endpoint for the openai provider. Default depends on api mode or OPENAI_BASE_URL.",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=0,
        help="Translate at most this many files. 0 means no limit.",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite existing translated files.",
    )
    parser.add_argument(
        "--output-format",
        default="bilingual",
        choices=["bilingual", "translation-only"],
        help="Output format. Default: bilingual",
    )
    parser.add_argument(
        "--export-pdf",
        action="store_true",
        help="Export generated Markdown files to PDF with md2pdf.",
    )
    parser.add_argument(
        "--pdf-output-dir",
        type=Path,
        default=None,
        help="Directory for generated PDFs. Default: same as output-dir.",
    )
    return parser.parse_args()


def load_glossary(path: Path) -> Glossary:
    data = json.loads(path.read_text(encoding="utf-8"))
    return Glossary(
        heading_map=data.get("heading_map", {}),
        exact_line_map=data.get("exact_line_map", {}),
        prefix_map=data.get("prefix_map", {}),
        phrase_map=data.get("phrase_map", {}),
        term_map=data.get("term_map", {}),
    )


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


def resolve_openai_api_mode(args: argparse.Namespace) -> str:
    env_mode = os.environ.get("OPENAI_API_MODE", "").strip().lower()
    if env_mode in {"responses", "chat"}:
        return env_mode
    return args.api_mode


def resolve_openai_base_url(args: argparse.Namespace, api_mode: str) -> str:
    if args.base_url.strip():
        return args.base_url.strip()
    env_base_url = os.environ.get("OPENAI_BASE_URL", "").strip()
    if env_base_url:
        return env_base_url
    return default_base_url(api_mode)


def apply_phrase_map(text: str, phrase_map: dict[str, str]) -> str:
    result = text
    for source, target in phrase_map.items():
        result = result.replace(source, target)
    return result


def translate_heading_line(line: str, glossary: Glossary) -> str:
    match = re.match(r"^(#{1,6})\s+(.*)$", line)
    if not match:
        return line

    prefix, title = match.groups()
    for source, target in glossary.heading_map.items():
        if title == source:
            return f"{prefix} {target}"
        if title.startswith(f"{source} "):
            return f"{prefix} {title.replace(source, target, 1)}"
    title = apply_phrase_map(title, glossary.phrase_map)
    return f"{prefix} {title}"


def translate_known_line(line: str, glossary: Glossary) -> str:
    stripped = line.strip()
    if not stripped:
        return line

    if line.startswith("#"):
        return translate_heading_line(line, glossary)

    for source, target in glossary.prefix_map.items():
        if line.startswith(source):
            value = line[len(source) :]
            mapped = apply_phrase_map(value, glossary.phrase_map)
            return f"{target}{mapped}"

    if stripped in glossary.exact_line_map:
        translated = glossary.exact_line_map[stripped]
        return line.replace(stripped, translated, 1)

    return apply_phrase_map(line, glossary.phrase_map)


def protect_pattern(text: str, pattern: re.Pattern[str], label: str) -> tuple[str, dict[str, str]]:
    replacements: dict[str, str] = {}

    def repl(match: re.Match[str]) -> str:
        token = f"__{label}_{len(replacements)}__"
        replacements[token] = match.group(0)
        return token

    return pattern.sub(repl, text), replacements


def restore_tokens(text: str, replacements: dict[str, str]) -> str:
    restored = text
    for token, original in replacements.items():
        restored = restored.replace(token, original)
    return restored


def translate_block_locally(block: str, glossary: Glossary) -> str:
    return "\n".join(translate_known_line(line, glossary) for line in block.splitlines())


def split_preserving_separators(text: str) -> list[str]:
    return [part for part in re.split(r"(\n\s*\n+)", text) if part]


def split_markdown_content_blocks(text: str) -> list[str]:
    masked_text, fence_tokens = protect_pattern(text, CODE_FENCE_PATTERN, "FENCE")
    parts = split_preserving_separators(masked_text)
    blocks: list[str] = []
    for part in parts:
        if not part.strip():
            continue
        blocks.append(restore_tokens(part, fence_tokens).strip())
    return blocks


def extract_tagged_content(text: str, tag_name: str) -> str:
    match = re.search(
        rf"<{tag_name}>\s*(.*?)\s*</{tag_name}>",
        text,
        flags=re.DOTALL | re.IGNORECASE,
    )
    if match:
        return match.group(1).strip()
    return text.strip()


def unwrap_inline_math_code_spans(text: str) -> str:
    return INLINE_CODE_WRAPPED_MATH_PATTERN.sub(r"\1", text)


def looks_like_pure_math_block(content: str) -> bool:
    stripped = content.strip()
    if not stripped:
        return False

    if stripped.startswith("$$") and stripped.endswith("$$") and len(stripped) >= 4:
        return True

    lines = [line.strip() for line in stripped.splitlines() if line.strip()]
    if len(lines) != 1:
        return False

    line = lines[0]
    return line.startswith("$") and line.endswith("$") and len(line) >= 2


def unwrap_fenced_math_blocks(text: str) -> str:
    def repl(match: re.Match[str]) -> str:
        content = match.group(1)
        if looks_like_pure_math_block(content):
            return content.strip()
        return match.group(0)

    return FENCED_BLOCK_PATTERN.sub(repl, text)


def build_bilingual_markdown(source_text: str, translated_text: str) -> str:
    raise NotImplementedError("Use build_bilingual_markdown_with_glossary instead.")


def is_heading_level(block: str, level: int) -> bool:
    return block.startswith("#" * level + " ")


def get_heading_level(block: str) -> int:
    match = re.match(r"^(#{1,6})\s+", block)
    if not match:
        return 0
    return len(match.group(1))


def is_source_block(block: str) -> bool:
    return block.startswith("Source: ")


def is_score_block(block: str) -> bool:
    return bool(re.match(r"^Score\s*:\s*", block))


def is_fenced_code_block(block: str) -> bool:
    stripped = block.strip()
    return stripped.startswith("```") and stripped.endswith("```")


def is_thematic_break_block(block: str) -> bool:
    return block.strip() in {"***", "* * *", "---", "- - -", "___", "_ _ _"}


def should_translate_with_model(block: str) -> bool:
    if is_thematic_break_block(block):
        return False
    if is_source_block(block) or is_score_block(block):
        return False
    if get_heading_level(block) >= 1:
        return False
    if is_fenced_code_block(block):
        return False
    return True


def is_sample_heading(block: str) -> bool:
    stripped = block.lstrip("#").strip()
    return stripped.startswith("Sample Input") or stripped.startswith("Sample Output")


def is_input_heading(block: str) -> bool:
    stripped = block.lstrip("#").strip()
    return stripped == "Input" or stripped == "Input/Output"


def is_input_intro_block(block: str) -> bool:
    stripped = block.strip()
    return (
        stripped == "The input is given from Standard Input in the following format:"
        or stripped == "Each query is given in the following format:"
        or stripped == "Then, output your chosen positive integer $m$ and $m$ permutations of $(1,2,\\dots,N)$ in the following format over $m+1$ lines. Here, the $j$-th element of the $i$-th permutation is $P_{i,j}$. Be sure to output a newline at the end."
        or stripped == "Then, the judge gives you a permutation $Q=(Q_1,Q_2,\\dots,Q_N)$ of $(1,2,\\dots,N)$ in the following format:"
        or stripped == "Then, output a sequence of positive integers $A=(A_1,A_2,\\dots,A_k)$ in the following format. Be sure to output a newline at the end."
        or stripped == "First, the judge gives you a positive integer $N$ in the following format:"
    )


def normalize_bilingual_comparison_text(text: str) -> str:
    normalized = text.replace("\r\n", "\n").strip()
    normalized = re.sub(r"\n{3,}", "\n\n", normalized)
    normalized = re.sub(r"[ \t]+", " ", normalized)
    return normalized


def blocks_are_effectively_identical(source_block: str, translated_block: str) -> bool:
    return normalize_bilingual_comparison_text(source_block) == normalize_bilingual_comparison_text(
        translated_block
    )


def fenced_code_content(block: str) -> str:
    match = re.match(r"```[^\n]*\n([\s\S]*?)\n```$", block.strip())
    if match:
        return match.group(1)
    return block.strip().strip("`")


def render_math_token(token: str) -> str:
    cleaned = token.strip()
    while cleaned.endswith("\\") and len(cleaned) > 1:
        cleaned = cleaned[:-1]
    if cleaned.startswith("$") and cleaned.endswith("$"):
        return cleaned
    return f"${cleaned}$"


def normalize_math_layout_line(line: str) -> str:
    stripped = line.strip()
    if not stripped:
        return ""

    if stripped.startswith("$$") and stripped.endswith("$$") and len(stripped) >= 4:
        inner = stripped[2:-2].strip()
        if re.search(r"\\\s+", inner):
            parts = [part.strip() for part in re.split(r"\\\s+", inner) if part.strip()]
            return " ".join(render_math_token(part) for part in parts)
        return stripped

    if stripped.startswith("$") and stripped.endswith("$") and len(stripped) >= 2:
        inner = stripped[1:-1].strip()
        if re.search(r"\\\s+", inner):
            parts = [part.strip() for part in re.split(r"\\\s+", inner) if part.strip()]
            return " ".join(render_math_token(part) for part in parts)
        return stripped

    tokens = [render_math_token(token) for token in stripped.split()]
    return " ".join(tokens)


def convert_input_fenced_block_to_markdown(block: str) -> str:
    content = fenced_code_content(block)
    rendered_lines: list[str] = []
    for raw_line in content.splitlines():
        stripped = raw_line.strip()
        if not stripped:
            if rendered_lines and rendered_lines[-1] != "":
                rendered_lines.append("")
            continue
        rendered_lines.append(normalize_math_layout_line(stripped))

    lines = [line for line in rendered_lines if line != ""]
    return "  \n".join(lines)


def normalize_score_block(source_block: str, glossary: Glossary) -> str:
    match = re.match(r"^Score\s*:\s*(.*)$", source_block)
    if match:
        value = apply_phrase_map(match.group(1), glossary.phrase_map)
        return f"分值：{value}"
    translated = translate_known_line(source_block, glossary)
    translated = translated.replace(" 分", " 分")
    return translated


def build_sections(
    source_blocks: list[str],
    translated_blocks: list[str],
    glossary: Glossary,
) -> tuple[str, str, list[Section]]:
    title_source = ""
    score_line = ""
    sections: list[Section] = []
    current_section: Section | None = None

    for source_block, translated_block in zip(source_blocks, translated_blocks, strict=True):
        if is_heading_level(source_block, 1):
            title_source = source_block
            continue
        if is_thematic_break_block(source_block):
            continue
        if is_source_block(source_block):
            continue
        if is_score_block(source_block):
            score_line = normalize_score_block(source_block, glossary)
            continue
        if get_heading_level(source_block) >= 2:
            current_section = Section(
                source_heading=source_block,
                translated_heading=translated_block,
                blocks=[],
            )
            sections.append(current_section)
            continue

        if current_section is None:
            continue
        current_section.blocks.append(BlockPair(source=source_block, translated=translated_block))

    return title_source, score_line, sections


def render_section_groups(section: Section) -> list[str]:
    groups: list[str] = []
    is_sample = is_sample_heading(section.source_heading)
    is_input = is_input_heading(section.source_heading)

    for block_pair in section.blocks:
        source_block = block_pair.source
        translated_block = block_pair.translated

        if is_fenced_code_block(source_block):
            if is_sample:
                groups.append(source_block)
                continue
            if is_input:
                rendered = convert_input_fenced_block_to_markdown(source_block)
                if groups:
                    groups[-1] = "\n\n".join([groups[-1], rendered])
                else:
                    groups.append(rendered)
                continue
            if blocks_are_effectively_identical(source_block, translated_block):
                groups.append(source_block)
            else:
                groups.append("\n\n".join([source_block, translated_block]))
            continue

        if is_input and is_input_intro_block(source_block):
            if blocks_are_effectively_identical(source_block, translated_block):
                groups.append(source_block)
            else:
                groups.append("\n\n".join([source_block, translated_block]))
            continue

        if blocks_are_effectively_identical(source_block, translated_block):
            groups.append(source_block)
        else:
            groups.append("\n\n".join([source_block, translated_block]))

    normalized_groups = [group.strip() for group in groups if group.strip()]
    if not normalized_groups:
        return [section.source_heading]

    normalized_groups[0] = "\n\n".join([section.source_heading, normalized_groups[0]])
    return normalized_groups


def fallback_bilingual_markdown(source_text: str, translated_text: str) -> str:
    if blocks_are_effectively_identical(source_text, translated_text):
        return source_text.strip() + "\n"
    return (
        f"{translated_text.strip()}\n\n---\n\n{source_text.strip()}\n"
    )


def build_bilingual_markdown_with_glossary(
    source_text: str,
    translated_text: str,
    glossary: Glossary,
) -> str:
    source_blocks = split_markdown_content_blocks(source_text)
    translated_blocks = split_markdown_content_blocks(translated_text)
    return build_bilingual_markdown_from_blocks(
        source_blocks,
        translated_blocks,
        source_text,
        translated_text,
        glossary,
    )


def build_bilingual_markdown_from_blocks(
    source_blocks: list[str],
    translated_blocks: list[str],
    source_text: str,
    translated_text: str,
    glossary: Glossary,
) -> str:

    if len(source_blocks) != len(translated_blocks):
        return fallback_bilingual_markdown(source_text, translated_text)

    title_source, score_line, sections = build_sections(
        source_blocks,
        translated_blocks,
        glossary,
    )

    if not score_line:
        for block in source_blocks:
            if is_score_block(block):
                score_line = normalize_score_block(block, glossary)
                break

    parts: list[str] = []
    title_lines = [line for line in [title_source, score_line] if line]
    if title_lines:
        parts.append("\n\n".join(title_lines))

    for section in sections:
        parts.extend(render_section_groups(section))

    if len(parts) <= 1 and sections:
        return fallback_bilingual_markdown(source_text, translated_text)

    if not parts:
        return fallback_bilingual_markdown(source_text, translated_text)

    return "\n\n---\n\n".join(parts).strip() + "\n"


def export_markdown_to_pdf(markdown_path: Path, pdf_output_dir: Path) -> Path:
    pdf_output_dir.mkdir(parents=True, exist_ok=True)
    md2pdf_cmd = shutil.which("md2pdf.cmd") or shutil.which("md2pdf")
    if not md2pdf_cmd:
        raise RuntimeError("md2pdf command not found in PATH.")
    absolute_markdown_path = markdown_path.resolve()
    absolute_pdf_output_dir = pdf_output_dir.resolve()
    command = [
        md2pdf_cmd,
        absolute_markdown_path.name,
        "--output-dir",
        str(absolute_pdf_output_dir),
    ]
    print(f"[pdf] exporting {markdown_path.name} -> {pdf_output_dir}")
    completed = subprocess.run(
        command,
        check=True,
        capture_output=True,
        text=True,
        cwd=str(absolute_markdown_path.parent),
    )
    if completed.stdout.strip():
        print(completed.stdout.strip())
    if completed.stderr.strip():
        print(completed.stderr.strip())
    generated_pdf = absolute_pdf_output_dir / f"{markdown_path.stem}.pdf"
    final_pdf = absolute_pdf_output_dir / pdf_name_for_markdown(markdown_path)
    if generated_pdf.exists() and generated_pdf != final_pdf:
        if final_pdf.exists():
            final_pdf.unlink()
        generated_pdf.replace(final_pdf)
    return final_pdf if final_pdf.exists() else generated_pdf


class RuleBasedTranslator:
    def __init__(self, glossary: Glossary) -> None:
        self.glossary = glossary

    def translate_block(self, block: str) -> str:
        return "\n".join(
            translate_known_line(line, self.glossary) for line in block.splitlines()
        )


class OpenAITranslator:
    def __init__(
        self,
        glossary: Glossary,
        model: str,
        api_key: str,
        api_mode: str,
        base_url: str,
    ) -> None:
        self.glossary = glossary
        self.model = model
        self.api_key = api_key
        self.api_mode = api_mode
        self.base_url = base_url

    def translate_block(self, block: str) -> str:
        return self.translate_blocks([block])[0]

    def translate_blocks(self, blocks: list[str]) -> list[str]:
        if not blocks:
            return []

        protected_blocks: list[str] = []
        token_sets: list[tuple[dict[str, str], dict[str, str], dict[str, str]]] = []

        for block in blocks:
            protected, code_tokens = protect_pattern(block, INLINE_CODE_PATTERN, "INLINE")
            protected, math_tokens = protect_pattern(protected, MATH_PATTERN, "MATH")
            protected, url_tokens = protect_pattern(protected, URL_PATTERN, "URL")
            protected_blocks.append(protected)
            token_sets.append((code_tokens, math_tokens, url_tokens))

        system_prompt = self._build_system_prompt_for_blocks()
        block_payload_parts: list[str] = []
        for index, text in enumerate(protected_blocks, start=1):
            block_payload_parts.append(f"<<<BLOCK:{index}>>>\n{text}\n<<<END_BLOCK:{index}>>>")
        block_payload = "\n\n".join(block_payload_parts)
        user_prompt = (
            "Translate the block payload below into Simplified Chinese.\n"
            "Return only translated blocks using the exact same block markers.\n"
            "Do not omit, merge, reorder, or add blocks.\n"
            "For each block, keep the exact marker lines unchanged:\n"
            "<<<BLOCK:id>>>\n"
            "...translated markdown...\n"
            "<<<END_BLOCK:id>>>\n"
            "Translate only the content between each pair of markers.\n"
            "Keep Markdown structure inside each block.\n"
            "Keep placeholder tokens, formulas, URLs, and inline code unchanged.\n"
            "If your endpoint enforces JSON output, return only JSON in the form "
            '{"blocks":[{"id":1,"content":"..."}]}.\n'
            f"{block_payload}"
        )

        payload = self._build_payload(system_prompt, user_prompt)
        response = self._post_with_retry(payload)
        output_text = self._extract_output_text(response.json())
        translated_blocks = self._extract_translated_blocks_tagged(output_text, len(blocks))

        restored_blocks: list[str] = []
        for translated, token_set in zip(translated_blocks, token_sets, strict=True):
            code_tokens, math_tokens, url_tokens = token_set
            restored = restore_tokens(translated, url_tokens)
            restored = restore_tokens(restored, math_tokens)
            restored = restore_tokens(restored, code_tokens)
            restored = unwrap_fenced_math_blocks(restored)
            restored = unwrap_inline_math_code_spans(restored)
            restored_blocks.append(restored)

        return restored_blocks

    def _build_payload(self, system_prompt: str, user_prompt: str) -> dict:
        if self.api_mode == "chat":
            return {
                "model": self.model,
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt},
                ],
                "stream": False,
            }

        return {
            "model": self.model,
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

    def _post_with_retry(self, payload: dict) -> requests.Response:
        last_error: Exception | None = None

        for attempt in range(1, 4):
            try:
                print(f"[translate] request attempt {attempt}/3 -> {self.base_url}")
                response = requests.post(
                    self.base_url,
                    headers={
                        "Authorization": f"Bearer {self.api_key}",
                        "Content-Type": "application/json",
                    },
                    json=payload,
                    timeout=120,
                )
                if response.ok:
                    return response

                if response.status_code in {408, 429, 500, 502, 503, 504} and attempt < 3:
                    print(
                        f"[translate] transient HTTP {response.status_code}, retrying after {attempt * 2}s"
                    )
                    time.sleep(attempt * 2)
                    continue

                raise TranslationError(
                    f"OpenAI provider request failed: HTTP {response.status_code} {response.text}"
                )
            except requests.RequestException as exc:
                last_error = exc
                if attempt < 3:
                    print(f"[translate] request error: {exc}; retrying after {attempt * 2}s")
                    time.sleep(attempt * 2)
                    continue
                raise TranslationError(f"OpenAI provider request failed after retries: {exc}") from exc

        raise TranslationError(f"OpenAI provider request failed after retries: {last_error}")

    def _build_system_prompt(self) -> str:
        glossary_lines = [
            f"- {source} -> {target}"
            for source, target in sorted(self.glossary.term_map.items(), key=lambda item: item[0])
        ]
        joined_glossary = "\n".join(glossary_lines)
        return (
            "You translate competitive programming statements into Simplified Chinese.\n"
            "Rules:\n"
            "1. Preserve Markdown structure, headings, lists, tables, and blockquotes.\n"
            "2. Keep formulas, variable names, sample input/output, URLs, and placeholder tokens unchanged.\n"
            "3. Use natural Chinese algorithm-problem phrasing, not word-for-word translation.\n"
            "4. Do not add explanations, hints, or solution ideas.\n"
            "5. Prefer the following terminology when applicable:\n"
            f"{joined_glossary}"
        )

    def _build_system_prompt_for_blocks(self) -> str:
        glossary_lines = [
            f"- {source} -> {target}"
            for source, target in sorted(self.glossary.term_map.items(), key=lambda item: item[0])
        ]
        joined_glossary = "\n".join(glossary_lines)
        return (
            "You translate competitive programming statements into Simplified Chinese.\n"
            "Rules:\n"
            "1. You will receive multiple Markdown blocks wrapped in explicit block markers.\n"
            "2. Preserve one output block for each input block, with the same id.\n"
            "3. Preserve Markdown structure inside each block.\n"
            "4. Keep formulas, variable names, sample input/output, URLs, and placeholder tokens unchanged.\n"
            "5. Use natural Chinese algorithm-problem phrasing, not word-for-word translation.\n"
            "6. Do not add explanations, hints, or solution ideas.\n"
            "7. Return only the translated blocks using the same block markers.\n"
            "8. If your serving layer requires JSON output, return only:\n"
            '{"blocks":[{"id":1,"content":"..."}]}\n'
            "9. Prefer the following terminology when applicable:\n"
            f"{joined_glossary}"
        )

    def _extract_output_text(self, payload: dict) -> str:
        if self.api_mode == "chat":
            return self._extract_chat_output_text(payload)
        return self._extract_responses_output_text(payload)

    @staticmethod
    def _extract_responses_output_text(payload: dict) -> str:
        direct = payload.get("output_text")
        if isinstance(direct, str) and direct.strip():
            return direct.strip()

        chunks: list[str] = []
        for item in payload.get("output", []):
            if not isinstance(item, dict):
                continue
            for content in item.get("content", []):
                if not isinstance(content, dict):
                    continue
                text = content.get("text")
                if isinstance(text, str):
                    chunks.append(text)
        result = "".join(chunks).strip()
        if not result:
            raise TranslationError("OpenAI provider returned an empty response.")
        return result

    @staticmethod
    def _extract_chat_output_text(payload: dict) -> str:
        choices = payload.get("choices", [])
        if not choices:
            raise TranslationError("Chat mode returned no choices.")

        message = choices[0].get("message", {})
        content = message.get("content")
        if isinstance(content, str) and content.strip():
            return content.strip()

        if isinstance(content, list):
            parts: list[str] = []
            for item in content:
                if not isinstance(item, dict):
                    continue
                text = item.get("text")
                if isinstance(text, str):
                    parts.append(text)
            result = "".join(parts).strip()
            if result:
                return result

        raise TranslationError("Chat mode returned an empty message content.")

    @staticmethod
    def _extract_translated_blocks_tagged(text: str, expected_count: int) -> list[str]:
        pattern = re.compile(
            r"<<<BLOCK:(\d+)>>>\s*([\s\S]*?)\s*<<<END_BLOCK:\1>>>",
            flags=re.MULTILINE,
        )
        translated_by_id: dict[int, str] = {}
        for match in pattern.finditer(text):
            block_id = int(match.group(1))
            translated_by_id[block_id] = match.group(2).strip()

        translated: list[str] = []
        for block_id in range(1, expected_count + 1):
            if block_id not in translated_by_id:
                return OpenAITranslator._extract_translated_blocks_json(text, expected_count)
            translated.append(translated_by_id[block_id])

        return translated

    @staticmethod
    def _extract_translated_blocks_json(text: str, expected_count: int) -> list[str]:
        candidate = text.strip()
        fence_match = re.fullmatch(r"```(?:json)?\s*([\s\S]*?)\s*```", candidate, flags=re.IGNORECASE)
        if fence_match:
            candidate = fence_match.group(1).strip()

        try:
            payload = json.loads(candidate)
        except json.JSONDecodeError as exc:
            raise TranslationError(
                "OpenAI provider tagged response is missing block markers and JSON fallback parsing failed. "
                f"Raw output: {text}"
            ) from exc

        blocks = payload.get("blocks")
        if not isinstance(blocks, list):
            raise TranslationError(
                f"OpenAI provider JSON fallback is missing a blocks array. Raw output: {text}"
            )

        translated_by_id: dict[int, str] = {}
        for item in blocks:
            if not isinstance(item, dict):
                continue
            block_id = item.get("id")
            content = item.get("content")
            if isinstance(block_id, str) and block_id.isdigit():
                block_id = int(block_id)
            if not isinstance(block_id, int) or not isinstance(content, str):
                continue
            translated_by_id[block_id] = content.strip()

        translated: list[str] = []
        for block_id in range(1, expected_count + 1):
            if block_id not in translated_by_id:
                raise TranslationError(
                    f"OpenAI provider JSON fallback is missing block id {block_id}. Raw output: {text}"
                )
            translated.append(translated_by_id[block_id])

        return translated


def create_translator(args: argparse.Namespace, glossary: Glossary) -> Translator:
    if args.provider == "rule-based":
        return RuleBasedTranslator(glossary)

    api_mode = resolve_openai_api_mode(args)
    api_key = os.environ.get(args.api_key_env, "").strip()
    if not api_key:
        raise TranslationError(
            f"Environment variable {args.api_key_env} is empty, cannot use provider=openai."
        )
    base_url = resolve_openai_base_url(args, api_mode)
    return OpenAITranslator(
        glossary=glossary,
        model=args.model,
        api_key=api_key,
        api_mode=api_mode,
        base_url=base_url,
    )


def translate_markdown_blocks(text: str, translator: Translator) -> list[str]:
    if isinstance(translator, OpenAITranslator):
        source_blocks = split_markdown_content_blocks(text)
        translated_blocks: list[str] = [""] * len(source_blocks)
        model_indices: list[int] = []
        model_blocks: list[str] = []

        for index, block in enumerate(source_blocks):
            if should_translate_with_model(block):
                model_indices.append(index)
                model_blocks.append(block)
            else:
                if is_fenced_code_block(block):
                    translated_blocks[index] = block
                else:
                    translated_blocks[index] = translate_block_locally(block, translator.glossary)

        if model_blocks:
            model_translations = translator.translate_blocks(model_blocks)
            for index, translated_block in zip(model_indices, model_translations, strict=True):
                translated_blocks[index] = translated_block

        return translated_blocks

    masked_text, fence_tokens = protect_pattern(text, CODE_FENCE_PATTERN, "FENCE")
    parts = split_preserving_separators(masked_text)
    translated_parts: list[str] = []

    for part in parts:
        if not part.strip():
            translated_parts.append(part)
            continue
        if part.strip().startswith("__FENCE_") and part.strip().endswith("__"):
            translated_parts.append(part)
            continue
        translated_parts.append(translator.translate_block(part))

    translated = "".join(translated_parts)
    translated = restore_tokens(translated, fence_tokens)
    translated = unwrap_fenced_math_blocks(translated)
    translated = unwrap_inline_math_code_spans(translated)
    return split_markdown_content_blocks(translated)


def translate_markdown(text: str, translator: Translator) -> str:
    translated_blocks = translate_markdown_blocks(text, translator)
    translated = "\n\n".join(block.strip() for block in translated_blocks if block.strip())
    if not translated.endswith("\n"):
        translated += "\n"
    return translated


def translated_name(path: Path) -> str:
    if path.name.endswith(".en.md"):
        return path.name[:-6] + ".zh-CN.md"
    return path.stem + ".zh-CN.md"


def pdf_name_for_markdown(markdown_path: Path) -> str:
    stem = markdown_path.stem
    match = re.match(r"^[a-z0-9]+_([a-z0-9]+)\.zh-CN$", stem, flags=re.IGNORECASE)
    if match:
        return f"{match.group(1).upper()}.pdf"
    merged_match = re.match(r"^([a-z0-9]+)\.zh-CN$", stem, flags=re.IGNORECASE)
    if merged_match:
        return f"{merged_match.group(1).upper()}.pdf"
    return f"{stem}.pdf"


def iter_input_files(input_dir: Path) -> list[Path]:
    return sorted(path for path in input_dir.glob("*.md") if path.is_file())


def is_problem_translation_markdown(path: Path) -> bool:
    return bool(re.match(r"^[a-z0-9]+_[a-z0-9]+\.zh-CN\.md$", path.name, flags=re.IGNORECASE))


def infer_contest_id_from_markdown_paths(markdown_paths: list[Path]) -> str:
    contest_ids: set[str] = set()
    for path in markdown_paths:
        match = re.match(r"^([a-z0-9]+)_[a-z0-9]+\.zh-CN\.md$", path.name, flags=re.IGNORECASE)
        if not match:
            return ""
        contest_ids.add(match.group(1))
    if len(contest_ids) == 1:
        return next(iter(contest_ids))
    return ""


def combined_markdown_name(markdown_paths: list[Path]) -> str:
    contest_id = infer_contest_id_from_markdown_paths(markdown_paths)
    if contest_id:
        return f"{contest_id}.zh-CN.md"
    return "combined.zh-CN.md"


def build_combined_markdown(markdown_paths: list[Path]) -> str:
    cleaned_paths = [path for path in markdown_paths if is_problem_translation_markdown(path)]
    if not cleaned_paths:
        raise ValueError("No translated problem markdown files found to combine.")

    contest_id = infer_contest_id_from_markdown_paths(cleaned_paths)
    parts: list[str] = []
    for index, path in enumerate(cleaned_paths):
        text = path.read_text(encoding="utf-8").strip()
        if not text:
            continue
        if index == 0 and contest_id:
            parts.append(f"# {contest_id.upper()}\n\n{text}")
            continue
        if parts:
            parts.append('<div style="page-break-after: always;"></div>')
        parts.append(text)

    return "\n\n".join(parts).strip() + "\n"


def write_combined_markdown(markdown_paths: list[Path], output_dir: Path) -> Path:
    combined_text = build_combined_markdown(markdown_paths)
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / combined_markdown_name(markdown_paths)
    output_path.write_text(combined_text, encoding="utf-8")
    return output_path


def main() -> None:
    args = parse_args()
    load_dotenv(args.env_file)
    args.output_dir.mkdir(parents=True, exist_ok=True)

    glossary = load_glossary(args.glossary)
    translator = create_translator(args, glossary)
    input_files = iter_input_files(args.input_dir)
    if args.limit > 0:
        input_files = input_files[: args.limit]

    print(f"[translate] input_dir={args.input_dir}")
    print(f"[translate] output_dir={args.output_dir}")
    print(f"[translate] provider={args.provider}")
    print(f"[translate] env_file={args.env_file}")
    print(f"[translate] output_format={args.output_format}")
    print(f"[translate] export_pdf={args.export_pdf}")
    print(f"[translate] files={len(input_files)}")
    if args.provider == "openai":
        api_mode = resolve_openai_api_mode(args)
        base_url = resolve_openai_base_url(args, api_mode)
        print(f"[translate] api_mode={api_mode}")
        print(f"[translate] base_url={base_url}")
        print(f"[translate] model={args.model}")
    pdf_output_dir = args.pdf_output_dir or args.output_dir
    if args.export_pdf:
        print(f"[translate] pdf_output_dir={pdf_output_dir}")

    total = len(input_files)
    output_paths: list[Path] = []
    for index, source_path in enumerate(input_files, start=1):
        output_path = args.output_dir / translated_name(source_path)
        if output_path.exists() and not args.overwrite:
            print(f"[translate] [{index}/{total}] skip existing {output_path}")
            output_paths.append(output_path)
            continue

        print(f"[translate] [{index}/{total}] translating {source_path.name}")
        source_text = source_path.read_text(encoding="utf-8")
        translated_blocks = translate_markdown_blocks(source_text, translator)
        translated_text = "\n\n".join(block.strip() for block in translated_blocks if block.strip())
        if not translated_text.endswith("\n"):
            translated_text += "\n"
        final_text = translated_text
        if args.output_format == "bilingual":
            final_text = build_bilingual_markdown_from_blocks(
                split_markdown_content_blocks(source_text),
                translated_blocks,
                source_text,
                translated_text,
                glossary,
            )
        output_path.write_text(final_text, encoding="utf-8")
        print(f"[translate] [{index}/{total}] wrote {output_path}")
        output_paths.append(output_path)
        if args.export_pdf:
            pdf_path = export_markdown_to_pdf(output_path, pdf_output_dir)
            print(f"[translate] [{index}/{total}] wrote {pdf_path}")

    combined_sources = [path for path in output_paths if path.exists() and is_problem_translation_markdown(path)]
    if combined_sources:
        combined_markdown_path = write_combined_markdown(combined_sources, args.output_dir)
        print(f"[translate] wrote combined markdown {combined_markdown_path}")
        if args.export_pdf:
            combined_pdf_path = export_markdown_to_pdf(combined_markdown_path, pdf_output_dir)
            print(f"[translate] wrote combined pdf {combined_pdf_path}")


if __name__ == "__main__":
    main()
