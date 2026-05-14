from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any


DEFAULT_CONFIG: dict[str, Any] = {
    "python_command": "python",
    "powershell_command": "",
    "workspace_dir": "atcoder-output",
    "env_file": ".env",
    "statement": {
        "enabled": True,
        "provider": "openai",
        "model": "gpt-4",
        "api_mode": "chat",
        "base_url": "",
        "timeout": 30,
        "overwrite": True,
        "output_format": "bilingual",
        "export_pdf": True,
        "auth_mode": "session",
        "browser_cookies": "auto",
        "session_root": "",
        "session_site": "atcoder",
        "session_env": "prod",
        "session_account": "default",
        "session_browser": "chrome",
        "session_mode": "profile",
        "login_check_selector": "",
    },
    "editorials": {
        "enabled": True,
        "dir_template": "atcoder-output/{contest}/editorials",
        "require_markdown": False,
    },
}


class DeliveryConfigError(RuntimeError):
    pass


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run the project-level AtCoder delivery workflow."
    )
    parser.add_argument("contest", help="Contest ID, for example: abc457")
    parser.add_argument(
        "--config",
        type=Path,
        default=Path(__file__).resolve().with_name("atcoder_delivery.example.json"),
        help="Path to the JSON config file.",
    )
    parser.add_argument(
        "--phase",
        choices=["precheck", "statement", "editorials", "all"],
        default="all",
        help="Which phase to run. Default: all",
    )
    parser.add_argument(
        "--editorial-dir",
        type=Path,
        default=None,
        help="Override the editorial directory.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print planned commands without executing them.",
    )
    return parser.parse_args()


def repo_root() -> Path:
    return Path(__file__).resolve().parent.parent


def statement_script_path() -> Path:
    return (
        repo_root()
        / ".codex"
        / "skills"
        / "atcoder-statement-bilingual-pdf"
        / "scripts"
        / "run_atcoder_pipeline.py"
    )


def editorial_script_path() -> Path:
    return (
        repo_root()
        / ".codex"
        / "skills"
        / "atcoder-editorial-workflow"
        / "scripts"
        / "export-editorials.ps1"
    )


def codex_home() -> Path:
    configured = os.environ.get("CODEX_HOME", "").strip()
    if configured:
        return Path(configured).expanduser().resolve()
    return (Path.home() / ".codex").resolve()


def browser_session_manager_script() -> Path:
    return codex_home() / "skills" / "browser-session-manager" / "scripts" / "session_registry.ps1"


def deep_merge(base: dict[str, Any], override: dict[str, Any]) -> dict[str, Any]:
    merged: dict[str, Any] = dict(base)
    for key, value in override.items():
        if isinstance(value, dict) and isinstance(merged.get(key), dict):
            merged[key] = deep_merge(merged[key], value)
        else:
            merged[key] = value
    return merged


def load_json(path: Path) -> dict[str, Any]:
    if not path.is_file():
        raise DeliveryConfigError(f"Missing config file: {path}")
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise DeliveryConfigError(f"Config file is not valid JSON: {path}") from exc
    if not isinstance(payload, dict):
        raise DeliveryConfigError("Config root must be a JSON object.")
    return payload


def resolve_path(value: str | Path, *, base_dir: Path) -> Path:
    path = Path(value)
    if path.is_absolute():
        return path
    return (base_dir / path).resolve()


def load_dotenv_values(env_file: Path) -> dict[str, str]:
    values: dict[str, str] = {}
    if not env_file.is_file():
        return values
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
        values[key] = value
    return values


def command_exists(command_name: str) -> bool:
    return bool(shutil.which(command_name))


def pick_powershell_command(preferred: str) -> str:
    candidates = [preferred] if preferred else []
    candidates.extend(["pwsh", "powershell"])
    seen: set[str] = set()
    for candidate in candidates:
        if not candidate or candidate in seen:
            continue
        seen.add(candidate)
        if command_exists(candidate):
            return candidate
    raise DeliveryConfigError("Could not find pwsh or powershell in PATH.")


def log(message: str) -> None:
    print(f"[delivery] {message}")


def phase_needs_statement(phase: str, config: dict[str, Any]) -> bool:
    return phase in {"statement", "all"} and bool(config["statement"]["enabled"])


def phase_needs_editorials(phase: str, config: dict[str, Any]) -> bool:
    return phase in {"editorials", "all"} and bool(config["editorials"]["enabled"])


def resolve_editorial_dir(
    contest: str,
    config: dict[str, Any],
    base_dir: Path,
    override: Path | None,
) -> Path:
    if override is not None:
        return resolve_path(override, base_dir=Path.cwd())
    template = str(config["editorials"]["dir_template"])
    return resolve_path(template.format(contest=contest), base_dir=base_dir)


def editorial_markdown_files(editorial_dir: Path) -> list[Path]:
    if not editorial_dir.is_dir():
        return []
    return sorted(editorial_dir.glob("*.editorial.md"))


def validate_prerequisites(
    *,
    contest: str,
    phase: str,
    config: dict[str, Any],
    base_dir: Path,
    editorial_dir: Path,
) -> dict[str, Any]:
    summary: dict[str, Any] = {
        "contest": contest,
        "workspace_dir": resolve_path(config["workspace_dir"], base_dir=base_dir),
        "editorial_dir": editorial_dir,
        "warnings": [],
    }
    statement_enabled = phase_needs_statement(phase, config)
    editorials_enabled = phase_needs_editorials(phase, config)
    env_file = resolve_path(config["env_file"], base_dir=base_dir)
    summary["env_file"] = env_file

    if statement_enabled:
        python_command = str(config["python_command"]).strip() or "python"
        if not command_exists(python_command):
            raise DeliveryConfigError(f"Python command not found in PATH: {python_command}")
        if not command_exists("node"):
            raise DeliveryConfigError("Node.js command not found in PATH: node")
        if not statement_script_path().is_file():
            raise DeliveryConfigError(f"Missing statement pipeline script: {statement_script_path()}")
        if config["statement"]["export_pdf"] and not command_exists("md2pdf"):
            raise DeliveryConfigError("md2pdf command not found in PATH.")
        if str(config["statement"]["provider"]).strip().lower() == "openai":
            dotenv_values = load_dotenv_values(env_file)
            if "OPENAI_API_KEY" not in os.environ and "OPENAI_API_KEY" not in dotenv_values:
                raise DeliveryConfigError(
                    "OPENAI_API_KEY is missing from both the current environment and the env file."
                )
        auth_mode = str(config["statement"]["auth_mode"]).strip().lower()
        if auth_mode == "session":
            session_script = browser_session_manager_script()
            if not session_script.is_file():
                raise DeliveryConfigError(
                    "Session auth mode requires browser-session-manager, but the helper script "
                    f"is missing: {session_script}"
                )
            summary["warnings"].append(
                "statement.auth_mode=session 仍依赖 browser-session-manager 管理的会话。"
            )

    if editorials_enabled:
        summary["powershell_command"] = pick_powershell_command(
            str(config["powershell_command"]).strip()
        )
        if not editorial_script_path().is_file():
            raise DeliveryConfigError(f"Missing editorial export script: {editorial_script_path()}")
        if not command_exists("md2pdf"):
            raise DeliveryConfigError("md2pdf command not found in PATH.")
        files = editorial_markdown_files(editorial_dir)
        summary["editorial_markdown_count"] = len(files)
        if not files:
            if config["editorials"]["require_markdown"]:
                raise DeliveryConfigError(
                    f"No editorial markdown files found in required directory: {editorial_dir}"
                )
            summary["warnings"].append(
                f"题解目录当前没有 `*.editorial.md`，导出阶段将自动跳过：{editorial_dir}"
            )

    return summary


def build_statement_command(
    *,
    contest: str,
    config: dict[str, Any],
    base_dir: Path,
) -> list[str]:
    statement = config["statement"]
    workspace_dir = resolve_path(config["workspace_dir"], base_dir=base_dir)
    env_file = resolve_path(config["env_file"], base_dir=base_dir)

    command = [
        str(config["python_command"]).strip() or "python",
        str(statement_script_path()),
        contest,
        "--workspace",
        str(workspace_dir),
        "--provider",
        str(statement["provider"]),
        "--model",
        str(statement["model"]),
        "--api-mode",
        str(statement["api_mode"]),
        "--env-file",
        str(env_file),
        "--timeout",
        str(statement["timeout"]),
        "--auth-mode",
        str(statement["auth_mode"]),
        "--output-format",
        str(statement["output_format"]),
    ]

    base_url = str(statement["base_url"]).strip()
    if base_url:
        command.extend(["--base-url", base_url])

    if statement["overwrite"]:
        command.append("--overwrite")
    else:
        command.append("--no-overwrite")

    if statement["export_pdf"]:
        command.append("--export-pdf")
    else:
        command.append("--no-export-pdf")

    auth_mode = str(statement["auth_mode"]).strip().lower()
    if auth_mode == "session":
        for key in [
            "session_site",
            "session_env",
            "session_account",
            "session_browser",
            "session_mode",
        ]:
            cli_name = "--" + key.replace("_", "-")
            command.extend([cli_name, str(statement[key])])
        session_root = str(statement["session_root"]).strip()
        if session_root:
            command.extend(
                ["--session-root", str(resolve_path(session_root, base_dir=base_dir))]
            )
        selector = str(statement["login_check_selector"]).strip()
        if selector:
            command.extend(["--login-check-selector", selector])
    else:
        command.extend(["--browser-cookies", str(statement["browser_cookies"])])

    return command


def build_editorial_command(
    *,
    editorial_dir: Path,
    powershell_command: str,
) -> list[str]:
    return [
        powershell_command,
        "-NoProfile",
        "-ExecutionPolicy",
        "Bypass",
        "-File",
        str(editorial_script_path()),
        "-EditorialDir",
        str(editorial_dir),
    ]


def run_command(command: list[str], *, cwd: Path, dry_run: bool) -> None:
    log("command=" + subprocess.list2cmdline(command))
    if dry_run:
        return
    completed = subprocess.run(command, cwd=cwd)
    if completed.returncode != 0:
        raise SystemExit(completed.returncode)


def main() -> None:
    args = parse_args()
    config_path = args.config.resolve()
    base_dir = repo_root()
    user_config = load_json(config_path)
    config = deep_merge(DEFAULT_CONFIG, user_config)
    contest = args.contest.strip().lower()
    if not contest:
        raise DeliveryConfigError("Contest ID cannot be empty.")

    editorial_dir = resolve_editorial_dir(contest, config, base_dir, args.editorial_dir)
    summary = validate_prerequisites(
        contest=contest,
        phase=args.phase,
        config=config,
        base_dir=base_dir,
        editorial_dir=editorial_dir,
    )

    log(f"contest={summary['contest']}")
    log(f"phase={args.phase}")
    log(f"config={config_path}")
    log(f"workspace_dir={summary['workspace_dir']}")
    log(f"editorial_dir={summary['editorial_dir']}")
    log(f"env_file={summary['env_file']}")
    for warning in summary["warnings"]:
        log(f"warning={warning}")

    if args.phase == "precheck":
        log("precheck passed")
        return

    if phase_needs_statement(args.phase, config):
        log("phase=statement")
        statement_command = build_statement_command(
            contest=contest,
            config=config,
            base_dir=base_dir,
        )
        run_command(statement_command, cwd=repo_root(), dry_run=args.dry_run)

    if phase_needs_editorials(args.phase, config):
        files = editorial_markdown_files(editorial_dir)
        if not files:
            log("phase=editorials skipped because no editorial markdown files were found")
        else:
            log(f"phase=editorials files={len(files)}")
            powershell_command = str(summary["powershell_command"])
            editorial_command = build_editorial_command(
                editorial_dir=editorial_dir,
                powershell_command=powershell_command,
            )
            run_command(editorial_command, cwd=repo_root(), dry_run=args.dry_run)


if __name__ == "__main__":
    try:
        main()
    except DeliveryConfigError as exc:
        print(f"[delivery] error={exc}", file=sys.stderr)
        raise SystemExit(2) from exc
