from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from pathlib import Path
from typing import Iterable
from urllib.parse import urlparse

import requests
from lxml import html
from playwright.sync_api import sync_playwright

try:
    import browser_cookie3
except ImportError:
    browser_cookie3 = None


ATCODER_BASE = "https://atcoder.jp"
SCRIPT_DIR = Path(__file__).resolve().parent
TURNDOWN_SCRIPT = SCRIPT_DIR / "atcoder_better_turndown.cjs"
BROWSER_COOKIE_ORDER = ["chrome", "edge", "brave", "chromium", "firefox", "opera", "vivaldi"]
DEFAULT_SESSION_SITE = "atcoder"
DEFAULT_SESSION_ENV = "prod"
DEFAULT_SESSION_ACCOUNT = "default"
DEFAULT_SESSION_BROWSER = "chromium"
DEFAULT_LOGIN_PATTERNS = [
    r"登录",
    r"注册",
    r"\blogin\b",
    r"sign\s*in",
    r"sign\s*up",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Fetch English task statements from AtCoder tasks_print with browser login state and save them as Markdown."
    )
    parser.add_argument("contest", nargs="?", help="Contest ID, for example: arc218")
    parser.add_argument("--contest-id", dest="contest_flag", help="Legacy contest flag.")
    parser.add_argument(
        "--output-dir",
        default=None,
        type=Path,
        help="Directory where Markdown files will be written. Default: ./atcoder-output/<contest>/en",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=30,
        help="HTTP timeout in seconds. Default: 30",
    )
    parser.add_argument(
        "--auth-mode",
        default="session",
        choices=["session", "browser-cookies"],
        help="Authentication mode. Default: session",
    )
    parser.add_argument(
        "--browser-cookies",
        default="auto",
        help="Load cookies from a local browser profile when --auth-mode=browser-cookies. Default: auto. Supported: auto, chrome, edge, brave, chromium, firefox, opera, vivaldi.",
    )
    parser.add_argument(
        "--session-root",
        default=None,
        type=Path,
        help="Override the browser-session-manager store root. Default: %%LOCALAPPDATA%%\\Codex\\browser-sessions",
    )
    parser.add_argument(
        "--session-site",
        default=DEFAULT_SESSION_SITE,
        help="Session registry site key. Default: atcoder",
    )
    parser.add_argument(
        "--session-env",
        default=DEFAULT_SESSION_ENV,
        help="Session registry env key. Default: prod",
    )
    parser.add_argument(
        "--session-account",
        default=DEFAULT_SESSION_ACCOUNT,
        help="Session registry account key. Default: default",
    )
    parser.add_argument(
        "--session-browser",
        default=DEFAULT_SESSION_BROWSER,
        help="Session registry browser key. Default: chromium",
    )
    parser.add_argument(
        "--login-check-selector",
        default="",
        help="Optional selector that proves the logged-in state. Default: empty",
    )
    return parser.parse_args()


def resolve_contest_id(args: argparse.Namespace) -> str:
    contest = (args.contest or "").strip()
    legacy_contest = (args.contest_flag or "").strip()
    resolved = contest or legacy_contest
    if not resolved:
        raise SystemExit("Contest ID is required. Example: fetch_atcoder_tasks.py abc456")
    return resolved


def normalize_text(text: str) -> str:
    return " ".join(text.split()).strip()


def remove_thematic_break_blocks(markdown: str) -> str:
    parts = re.split(r"(\n\s*\n+)", markdown)
    filtered: list[str] = []
    for part in parts:
        stripped = part.strip()
        if stripped in {"***", "* * *", "---", "- - -", "___", "_ _ _"}:
            continue
        filtered.append(part)
    cleaned = "".join(filtered)
    cleaned = re.sub(r"\n{3,}", "\n\n", cleaned)
    return cleaned.strip()


def task_slug(contest: str, short_code: str) -> str:
    return f"{contest}_{short_code.lower()}"


def browser_cookie_loader_names(browser_name: str) -> list[str]:
    normalized = browser_name.strip().lower()
    if not normalized:
        return []
    if normalized == "auto":
        return BROWSER_COOKIE_ORDER
    return [normalized]


def load_browser_cookie_jar(
    browser_name: str,
    domain_name: str = "atcoder.jp",
) -> requests.cookies.RequestsCookieJar:
    cookie_jar = requests.cookies.RequestsCookieJar()
    loader_names = browser_cookie_loader_names(browser_name)
    if not loader_names:
        return cookie_jar

    if browser_cookie3 is None:
        raise RuntimeError(
            "browser-cookie3 is not installed. Run `python -m pip install browser-cookie3` first."
        )

    errors: list[str] = []
    for loader_name in loader_names:
        loader = getattr(browser_cookie3, loader_name, None)
        if loader is None:
            errors.append(f"{loader_name}: unsupported browser name")
            continue
        try:
            loaded = loader(domain_name=domain_name)
            cookie_jar.update(loaded)
            if len(cookie_jar) > 0:
                return cookie_jar
            errors.append(f"{loader_name}: no matching cookies found for {domain_name}")
        except Exception as exc:
            errors.append(f"{loader_name}: {type(exc).__name__}: {exc}")

    raise RuntimeError("Failed to load browser cookies. " + " | ".join(errors))


def codex_home() -> Path:
    configured = os.environ.get("CODEX_HOME")
    if configured:
        return Path(configured).expanduser().resolve()
    return (Path.home() / ".codex").resolve()


def session_manager_script(name: str) -> Path:
    script_path = codex_home() / "skills" / "browser-session-manager" / "scripts" / name
    if not script_path.is_file():
        raise RuntimeError(f"Missing browser-session-manager script: {script_path}")
    return script_path


def run_powershell_json(script_path: Path, arguments: list[str]) -> dict[str, object]:
    command = [
        "powershell",
        "-ExecutionPolicy",
        "Bypass",
        "-File",
        str(script_path),
        *arguments,
    ]
    result = subprocess.run(
        command,
        text=True,
        capture_output=True,
        check=True,
    )
    return parse_json_tail(result.stdout)


def parse_json_tail(raw_text: str) -> dict[str, object]:
    stripped = raw_text.strip()
    if not stripped:
        raise RuntimeError("PowerShell script returned no JSON output.")

    lines = stripped.splitlines()
    start_index = None
    for index in range(len(lines) - 1, -1, -1):
        if lines[index].lstrip().startswith("{"):
            start_index = index
            break

    if start_index is None:
        raise RuntimeError(f"Could not locate JSON output in: {stripped}")

    json_text = "\n".join(lines[start_index:])
    try:
        parsed = json.loads(json_text)
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"Failed to decode JSON output: {json_text}") from exc
    if not isinstance(parsed, dict):
        raise RuntimeError(f"Expected a JSON object, got: {type(parsed).__name__}")
    return parsed


def build_session_arguments(
    *,
    session_root: Path | None,
    session_site: str,
    session_env: str,
    session_account: str,
    session_browser: str,
) -> list[str]:
    arguments = [
        "-Site",
        session_site,
        "-Env",
        session_env,
        "-Account",
        session_account,
        "-Browser",
        session_browser,
    ]
    if session_root is not None:
        arguments.extend(["-Root", str(session_root)])
    return arguments


def tasks_print_url(contest: str) -> str:
    return f"{ATCODER_BASE}/contests/{contest}/tasks_print?lang=en"


def contest_base_url(contest: str) -> str:
    return f"{ATCODER_BASE}/contests/{contest}"


def upsert_browser_session(
    contest: str,
    *,
    session_root: Path | None,
    session_site: str,
    session_env: str,
    session_account: str,
    session_browser: str,
    login_check_selector: str,
) -> dict[str, object]:
    script_path = session_manager_script("session_registry.ps1")
    arguments = [
        "upsert",
        *build_session_arguments(
            session_root=session_root,
            session_site=session_site,
            session_env=session_env,
            session_account=session_account,
            session_browser=session_browser,
        ),
        "-Mode",
        "storageState",
        "-BaseUrl",
        contest_base_url(contest),
        "-CheckUrl",
        tasks_print_url(contest),
    ]
    if login_check_selector.strip():
        arguments.extend(["-CheckSelector", login_check_selector.strip()])
    return run_powershell_json(script_path, arguments)


def mark_browser_session_verified(
    *,
    session_root: Path | None,
    session_site: str,
    session_env: str,
    session_account: str,
    session_browser: str,
) -> None:
    script_path = session_manager_script("session_registry.ps1")
    arguments = [
        "mark-verified",
        *build_session_arguments(
            session_root=session_root,
            session_site=session_site,
            session_env=session_env,
            session_account=session_account,
            session_browser=session_browser,
        ),
    ]
    run_powershell_json(script_path, arguments)


def refresh_browser_session_login(
    contest: str,
    *,
    session_root: Path | None,
    session_site: str,
    session_env: str,
    session_account: str,
    session_browser: str,
    login_check_selector: str,
) -> dict[str, object]:
    script_path = session_manager_script("refresh_login.ps1")
    arguments = [
        *build_session_arguments(
            session_root=session_root,
            session_site=session_site,
            session_env=session_env,
            session_account=session_account,
            session_browser=session_browser,
        ),
        "-Mode",
        "storageState",
        "-BaseUrl",
        contest_base_url(contest),
        "-CheckUrl",
        tasks_print_url(contest),
        "-Url",
        tasks_print_url(contest),
    ]
    if login_check_selector.strip():
        arguments.extend(["-CheckSelector", login_check_selector.strip()])
    return run_powershell_json(script_path, arguments)


def normalize_browser_name(name: str) -> str:
    value = (name or DEFAULT_SESSION_BROWSER).strip().lower()
    if value in {"cr", "chrome", "chromium"}:
        return "chromium"
    if value in {"ff", "firefox"}:
        return "firefox"
    if value in {"wk", "webkit"}:
        return "webkit"
    return value


def is_login_url(url: str) -> bool:
    return urlparse(url).path.rstrip("/") == "/login"


def page_requires_login(page, check_selector: str) -> tuple[bool, str]:
    if is_login_url(page.url):
        return True, "redirected_to_login"

    if check_selector.strip():
        locator = page.locator(check_selector.strip()).first
        if locator.count() > 0 and locator.is_visible():
            return False, "check_selector_visible"

    login_regex = re.compile("|".join(DEFAULT_LOGIN_PATTERNS), re.IGNORECASE)
    clickable_items = page.locator("a,button,[role='button']").evaluate_all(
        """
        els => els
          .map(el => ({
            text: (el.innerText || '').trim(),
            href: el.href || null
          }))
          .filter(item => item.text)
        """
    )
    for item in clickable_items:
        if login_regex.search(item["text"]):
            return True, f"login_option_detected:{item['text']}"

    return False, "no_login_option_detected"


def fetch_html_via_storage_state(
    contest: str,
    timeout: int,
    session_metadata: dict[str, object],
    check_selector: str,
) -> tuple[str, bool, str]:
    state_path = Path(str(session_metadata["statePath"]))
    browser_name = normalize_browser_name(str(session_metadata.get("browser") or DEFAULT_SESSION_BROWSER))
    goto_url = str(session_metadata.get("checkUrl") or tasks_print_url(contest))

    with sync_playwright() as playwright:
        browser_launcher = getattr(playwright, browser_name)
        browser = browser_launcher.launch(headless=True)
        try:
            context_kwargs: dict[str, object] = {}
            if state_path.is_file():
                context_kwargs["storage_state"] = str(state_path)
            context = browser.new_context(**context_kwargs)
            page = context.new_page()
            response = page.goto(goto_url, wait_until="networkidle", timeout=timeout * 1000)
            requires_login, reason = page_requires_login(page, check_selector)
            if requires_login:
                return "", False, reason
            if response is not None and response.status >= 400:
                raise RuntimeError(f"Failed to fetch {goto_url}: HTTP {response.status}")
            return page.content(), True, reason
        finally:
            browser.close()


def fetch_html(
    contest: str,
    timeout: int,
    auth_mode: str = "session",
    browser_cookies: str = "auto",
    session_root: Path | None = None,
    session_site: str = DEFAULT_SESSION_SITE,
    session_env: str = DEFAULT_SESSION_ENV,
    session_account: str = DEFAULT_SESSION_ACCOUNT,
    session_browser: str = DEFAULT_SESSION_BROWSER,
    login_check_selector: str = "",
) -> str:
    url = tasks_print_url(contest)
    if auth_mode == "session":
        session_metadata = upsert_browser_session(
            contest,
            session_root=session_root,
            session_site=session_site,
            session_env=session_env,
            session_account=session_account,
            session_browser=session_browser,
            login_check_selector=login_check_selector,
        )
        page_html, logged_in, reason = fetch_html_via_storage_state(
            contest,
            timeout,
            session_metadata,
            login_check_selector,
        )
        if not logged_in:
            print(
                f"[fetch] AtCoder session missing or expired ({reason}); opening browser for manual login.",
                file=sys.stderr,
            )
            refresh_browser_session_login(
                contest,
                session_root=session_root,
                session_site=session_site,
                session_env=session_env,
                session_account=session_account,
                session_browser=session_browser,
                login_check_selector=login_check_selector,
            )
            session_metadata = upsert_browser_session(
                contest,
                session_root=session_root,
                session_site=session_site,
                session_env=session_env,
                session_account=session_account,
                session_browser=session_browser,
                login_check_selector=login_check_selector,
            )
            page_html, logged_in, reason = fetch_html_via_storage_state(
                contest,
                timeout,
                session_metadata,
                login_check_selector,
            )
            if not logged_in:
                raise RuntimeError(
                    "AtCoder session is still not logged in after the browser login flow. "
                    f"Last check result: {reason}"
                )

        mark_browser_session_verified(
            session_root=session_root,
            session_site=session_site,
            session_env=session_env,
            session_account=session_account,
            session_browser=session_browser,
        )
        return page_html

    session = requests.Session()
    session.cookies.update(load_browser_cookie_jar(browser_cookies))
    response = session.get(
        url,
        timeout=timeout,
        headers={
            "User-Agent": "Mozilla/5.0 (compatible; AtCoderStatementFetcher/1.0)",
            "Referer": contest_base_url(contest),
        },
    )
    response.raise_for_status()
    return response.text


def html_fragment_to_markdown(fragment_html: str) -> str:
    payload = json.dumps({"html": fragment_html}, ensure_ascii=False)
    result = subprocess.run(
        ["node", str(TURNDOWN_SCRIPT)],
        input=payload,
        text=True,
        capture_output=True,
        check=True,
        cwd=SCRIPT_DIR.parent,
    )
    return remove_thematic_break_blocks(result.stdout.strip())


def extract_tasks(page_html: str, contest: str) -> Iterable[tuple[str, str]]:
    root = html.fromstring(page_html)
    titles = root.xpath("//span[contains(@class,'h2')]")
    statements = root.xpath("//div[@id='task-statement']")

    if len(titles) != len(statements):
        raise RuntimeError(
            f"Title count ({len(titles)}) does not match statement count ({len(statements)})."
        )

    for title_node, statement_node in zip(titles, statements, strict=True):
        title = normalize_text("".join(title_node.itertext()))
        short_code = title.split(" - ", 1)[0]
        slug = task_slug(contest, short_code)
        source_url = f"{ATCODER_BASE}/contests/{contest}/tasks/{slug}?lang=en"

        english_nodes = statement_node.xpath(".//span[contains(@class,'lang-en')]")
        if not english_nodes:
            raise RuntimeError(f"Missing English statement for task {title}.")

        english_html = html.tostring(english_nodes[0], encoding="unicode")
        statement_markdown = html_fragment_to_markdown(english_html)
        parts = [f"# {title}", f"Source: {source_url}", statement_markdown]
        markdown = "\n\n".join(part for part in parts if part).strip() + "\n"
        yield slug, markdown


def main() -> None:
    args = parse_args()
    contest_id = resolve_contest_id(args)
    output_dir = args.output_dir or (Path.cwd() / "atcoder-output" / contest_id / "en")
    output_dir.mkdir(parents=True, exist_ok=True)

    page_html = fetch_html(
        contest_id,
        args.timeout,
        auth_mode=args.auth_mode,
        browser_cookies=args.browser_cookies,
        session_root=args.session_root,
        session_site=args.session_site,
        session_env=args.session_env,
        session_account=args.session_account,
        session_browser=args.session_browser,
        login_check_selector=args.login_check_selector,
    )
    for slug, markdown in extract_tasks(page_html, contest_id):
        output_path = output_dir / f"{slug}.en.md"
        output_path.write_text(markdown, encoding="utf-8")
        print(f"Wrote {output_path}")


if __name__ == "__main__":
    main()
