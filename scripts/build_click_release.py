from __future__ import annotations

import argparse
import os
import shutil
import site
import sys
from pathlib import Path


RELEASE_NAME = "atcoder-delivery-click"


class BuildError(RuntimeError):
    pass


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Build a portable click-to-run AtCoder delivery package."
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path(".tmp") / "release" / RELEASE_NAME,
        help="Portable package output directory.",
    )
    parser.add_argument(
        "--include-env",
        action="store_true",
        help="Copy the current repo .env into the release root for local testing.",
    )
    parser.add_argument(
        "--clean",
        action="store_true",
        help="Delete the existing output directory before building.",
    )
    return parser.parse_args()


def log(message: str) -> None:
    print(f"[release-build] {message}")


def repo_root() -> Path:
    return Path(__file__).resolve().parent.parent


def output_root(path: Path) -> Path:
    return path if path.is_absolute() else (repo_root() / path).resolve()


def require_file(path: Path, label: str) -> Path:
    if not path.is_file():
        raise BuildError(f"Missing {label}: {path}")
    return path


def require_dir(path: Path, label: str) -> Path:
    if not path.is_dir():
        raise BuildError(f"Missing {label}: {path}")
    return path


def copy_tree(src: Path, dst: Path, *, ignore=None) -> None:
    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(src, dst, ignore=ignore)


def ensure_parent(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)


def copy_file(src: Path, dst: Path) -> None:
    ensure_parent(dst)
    shutil.copy2(src, dst)


def python_home() -> Path:
    return Path(sys.base_prefix).resolve()


def user_site_packages() -> Path:
    return Path(site.getusersitepackages()).resolve()


def node_executable() -> Path:
    node_path = shutil.which("node")
    if not node_path:
        raise BuildError("Could not find node in PATH.")
    return Path(node_path).resolve()


def md2pdf_package_dir() -> Path:
    appdata = os.environ.get("APPDATA", "").strip()
    if not appdata:
        raise BuildError("APPDATA is empty; cannot locate md2pdf-local-cli.")
    return require_dir(
        Path(appdata) / "npm" / "node_modules" / "md2pdf-local-cli",
        "md2pdf-local-cli package",
    )


def statement_skill_dir() -> Path:
    return require_dir(
        repo_root() / ".codex" / "skills" / "atcoder-statement-bilingual-pdf",
        "statement skill directory",
    )


def editorial_skill_dir() -> Path:
    return require_dir(
        repo_root() / ".codex" / "skills" / "atcoder-editorial-workflow",
        "editorial skill directory",
    )


def env_file() -> Path:
    return repo_root() / ".env"


def ignore_statement_tree(_src: str, names: list[str]) -> set[str]:
    ignored = {
        "SKILL.md",
        "agents",
    }
    return {name for name in names if name in ignored}


def ignore_md2pdf_tree(_src: str, names: list[str]) -> set[str]:
    ignored_prefixes = (
        ".tmp",
        ".output",
    )
    ignored_exact = {
        ".git",
        ".gitignore",
        "AGENTS.md",
        "README.md",
        "题面.md",
    }
    ignored: set[str] = set()
    for name in names:
        if name in ignored_exact:
            ignored.add(name)
            continue
        if any(name.startswith(prefix) for prefix in ignored_prefixes):
            ignored.add(name)
    return ignored


def write_text(path: Path, text: str) -> None:
    ensure_parent(path)
    path.write_text(text, encoding="utf-8")


def release_config_text() -> str:
    return """{
  "python_command": "python",
  "powershell_command": "powershell",
  "workspace_dir": "output",
  "env_file": ".env",
  "statement": {
    "enabled": true,
    "provider": "openai",
    "model": "gpt-4",
    "api_mode": "chat",
    "base_url": "",
    "timeout": 30,
    "overwrite": false,
    "output_format": "bilingual",
    "export_pdf": false,
    "auth_mode": "browser-cookies",
    "browser_cookies": "auto",
    "session_root": "",
    "session_site": "atcoder",
    "session_env": "prod",
    "session_account": "default",
    "session_browser": "chrome",
    "session_mode": "profile",
    "login_check_selector": ""
  },
  "editorials": {
    "enabled": true,
    "dir_template": "output/{contest}/editorials",
    "require_markdown": false
  }
}
"""


def env_example_text() -> str:
    return """OPENAI_API_KEY=
OPENAI_API_MODE=chat
OPENAI_BASE_URL=
"""


def readme_text() -> str:
    return """AtCoder Delivery Click Package

Quick start
1. Copy `.env.example` to `.env` and fill in `OPENAI_API_KEY`.
2. Ensure you have already logged in to AtCoder in a local browser such as Chrome or Edge.
3. Double-click `run.bat`, then enter a contest id such as `abc457`.

Notes
- This portable package already contains the Python runtime, node.exe and a local md2pdf CLI.
- The default auth mode is `browser-cookies`, so it no longer depends on Codex or browser-session-manager.
- The default package config is optimized for speed and resumability:
  - statement PDF export is disabled by default;
  - existing outputs are reused by default.
- If you want full statement PDFs for a run, use:
  - `run.bat abc457 --with-pdf`
- If you want to force a full rerun from scratch, use:
  - `run.bat abc457 --overwrite`
- If the browser cookies are expired, open AtCoder in your browser and log in again before rerunning.
- Outputs are written to the `output/` directory.
- The editable workflow config is `scripts/atcoder_delivery.release.json`.
"""


def launcher_bat_text() -> str:
    return r"""@echo off
setlocal
set "ROOT=%~dp0"
powershell -NoProfile -ExecutionPolicy Bypass -File "%ROOT%run.ps1" %*
exit /b %ERRORLEVEL%
"""


def launcher_ps1_text() -> str:
    return """param(
    [Parameter(Mandatory = $false, Position = 0)]
    [string]$Contest,
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$ExtraArgs
)

$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent $MyInvocation.MyCommand.Definition
$env:PATH = (Join-Path $root 'runtime\\python') + ';' + (Join-Path $root 'runtime\\node') + ';' + (Join-Path $root 'runtime\\bin') + ';' + $env:PATH
$env:PYTHONUTF8 = '1'

if(-not $Contest){
    $Contest = Read-Host 'Contest ID'
}

if(-not $Contest){
    throw 'Contest ID is required.'
}

$python = Join-Path $root 'runtime\\python\\python.exe'
$script = Join-Path $root 'scripts\\run_atcoder_delivery.py'
$config = Join-Path $root 'scripts\\atcoder_delivery.release.json'

& $python $script $Contest --config $config @ExtraArgs
exit $LASTEXITCODE
"""


def local_md2pdf_cmd_text() -> str:
    return r"""@echo off
setlocal
set "ROOT=%~dp0"
"%ROOT%..\node\node.exe" "%ROOT%node_modules\md2pdf-local-cli\bin\md2pdf.js" %*
exit /b %ERRORLEVEL%
"""


def local_md2pdf_ps1_text() -> str:
    return """#!/usr/bin/env pwsh
$basedir = Split-Path $MyInvocation.MyCommand.Definition -Parent
$node = Join-Path $basedir '..\\node\\node.exe'
$cli = Join-Path $basedir 'node_modules\\md2pdf-local-cli\\bin\\md2pdf.js'
& $node $cli $args
exit $LASTEXITCODE
"""


def build_release(output_dir: Path, include_env: bool) -> None:
    root = repo_root()
    python_src = require_dir(python_home(), "Python home")
    user_site = require_dir(user_site_packages(), "user site-packages")
    node_src = require_file(node_executable(), "node executable")
    md2pdf_src = md2pdf_package_dir()
    statement_src = statement_skill_dir()
    editorial_src = editorial_skill_dir()

    runtime_python_dir = output_dir / "runtime" / "python"
    runtime_node_dir = output_dir / "runtime" / "node"
    runtime_bin_dir = output_dir / "runtime" / "bin"
    release_statement_dir = (
        output_dir / ".codex" / "skills" / "atcoder-statement-bilingual-pdf"
    )
    release_editorial_dir = (
        output_dir / ".codex" / "skills" / "atcoder-editorial-workflow"
    )

    log("copying Python runtime")
    copy_tree(
        python_src,
        runtime_python_dir,
        ignore=shutil.ignore_patterns(
            "__pycache__",
            "test",
            "tests",
            "ensurepip",
            "tcl",
            "Doc",
        ),
    )

    target_site_packages = runtime_python_dir / "Lib" / "site-packages"
    target_site_packages.mkdir(parents=True, exist_ok=True)
    log("copying Python site-packages")
    for item in user_site.iterdir():
        destination = target_site_packages / item.name
        if destination.exists():
            if destination.is_dir():
                shutil.rmtree(destination)
            else:
                destination.unlink()
        if item.is_dir():
            shutil.copytree(item, destination)
        else:
            shutil.copy2(item, destination)

    log("copying node runtime")
    runtime_node_dir.mkdir(parents=True, exist_ok=True)
    copy_file(node_src, runtime_node_dir / "node.exe")

    log("copying local md2pdf cli")
    copy_tree(
        md2pdf_src,
        runtime_bin_dir / "node_modules" / "md2pdf-local-cli",
        ignore=ignore_md2pdf_tree,
    )
    write_text(runtime_bin_dir / "md2pdf.cmd", local_md2pdf_cmd_text())
    write_text(runtime_bin_dir / "md2pdf.ps1", local_md2pdf_ps1_text())

    log("copying statement workflow assets")
    copy_tree(statement_src, release_statement_dir, ignore=ignore_statement_tree)

    log("copying editorial workflow assets")
    (release_editorial_dir / "scripts").mkdir(parents=True, exist_ok=True)
    copy_file(
        editorial_src / "scripts" / "export-editorials.ps1",
        release_editorial_dir / "scripts" / "export-editorials.ps1",
    )

    log("copying release orchestration scripts")
    scripts_dir = output_dir / "scripts"
    scripts_dir.mkdir(parents=True, exist_ok=True)
    copy_file(root / "scripts" / "run_atcoder_delivery.py", scripts_dir / "run_atcoder_delivery.py")
    copy_file(root / "scripts" / "build_click_release.py", scripts_dir / "build_click_release.py")
    write_text(scripts_dir / "atcoder_delivery.release.json", release_config_text())

    write_text(output_dir / ".env.example", env_example_text())
    write_text(output_dir / "README.txt", readme_text())
    write_text(output_dir / "run.bat", launcher_bat_text())
    write_text(output_dir / "run.ps1", launcher_ps1_text())
    (output_dir / "output").mkdir(parents=True, exist_ok=True)

    if include_env and env_file().is_file():
        log("copying current .env for local testing")
        copy_file(env_file(), output_dir / ".env")

    log(f"release package ready: {output_dir}")


def main() -> None:
    args = parse_args()
    target_dir = output_root(args.output_dir)
    if target_dir.exists():
        if args.clean:
            log(f"cleaning existing directory: {target_dir}")
            shutil.rmtree(target_dir)
        elif any(target_dir.iterdir()):
            raise BuildError(
                f"Output directory already exists and is not empty: {target_dir}. "
                "Use --clean to rebuild."
            )
    target_dir.mkdir(parents=True, exist_ok=True)
    build_release(target_dir, args.include_env)


if __name__ == "__main__":
    try:
        main()
    except BuildError as exc:
        print(f"[release-build] error={exc}", file=sys.stderr)
        raise SystemExit(2) from exc
