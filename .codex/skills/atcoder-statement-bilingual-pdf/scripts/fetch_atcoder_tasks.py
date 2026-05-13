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
DEFAULT_SESSION_BROWSER = "chrome"
DEFAULT_SESSION_MODE = "profile"
DEFAULT_LOGIN_PATTERNS = [
    r"登录",
    r"注册",
    r"\blogin\b",
    r"sign\s*in",
    r"sign\s*up",
]
CLOUDFLARE_TEXT_PATTERNS = [
    "verify you are human",
    "checking your browser",
    "just a moment",
    "cloudflare",
]
DEFAULT_REQUEST_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/136.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
    "Cache-Control": "no-cache",
    "Pragma": "no-cache",
}


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
        help="Session registry browser key. Default: chrome",
    )
    parser.add_argument(
        "--session-mode",
        default=DEFAULT_SESSION_MODE,
        choices=["storageState", "profile", "hybrid"],
        help="Session registry mode. Default: profile",
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
        encoding="utf-8",
        errors="replace",
        capture_output=True,
    )
    if result.returncode != 0:
        raise RuntimeError(
            "PowerShell session helper failed.\n"
            f"command={' '.join(command)}\n"
            f"stdout={result.stdout}\n"
            f"stderr={result.stderr}"
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


def run_powershell_inline_json(command: str) -> dict[str, object]:
    result = subprocess.run(
        [
            "powershell",
            "-ExecutionPolicy",
            "Bypass",
            "-Command",
            command,
        ],
        text=True,
        encoding="utf-8",
        errors="replace",
        capture_output=True,
    )
    if result.returncode != 0:
        raise RuntimeError(
            "PowerShell inline command failed.\n"
            f"stdout={result.stdout}\n"
            f"stderr={result.stderr}"
        )
    return parse_json_tail(result.stdout)


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


def tasks_list_url(contest: str) -> str:
    return f"{ATCODER_BASE}/contests/{contest}/tasks?lang=en"


def safe_session_component(text: str) -> str:
    safe = (text or "default").strip().lower()
    safe = re.sub(r'[\\/:*?"<>|]', "-", safe)
    safe = re.sub(r"\s+", "-", safe)
    safe = re.sub(r"[^a-z0-9._-]", "-", safe)
    safe = re.sub(r"-{2,}", "-", safe)
    safe = safe.strip("-")
    return safe or "default"


def session_safe_stem(
    session_site: str,
    session_env: str,
    session_account: str,
    session_browser: str,
) -> str:
    return "--".join(
        [
            safe_session_component(session_site),
            safe_session_component(session_env),
            safe_session_component(session_account),
            safe_session_component(session_browser),
        ]
    )


def session_mode_path_arguments(
    session_mode: str,
    *,
    session_site: str,
    session_env: str,
    session_account: str,
    session_browser: str,
) -> list[str]:
    safe_stem = session_safe_stem(
        session_site,
        session_env,
        session_account,
        session_browser,
    )
    arguments = ["-Mode", session_mode, "-StatePath", f"states/{safe_stem}.json"]
    if session_mode in {"profile", "hybrid"}:
        arguments.extend(["-ProfilePath", f"profiles/{safe_stem}"])
    return arguments


def upsert_browser_session(
    contest: str,
    *,
    session_root: Path | None,
    session_site: str,
    session_env: str,
    session_account: str,
    session_browser: str,
    session_mode: str,
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
        *session_mode_path_arguments(
            session_mode,
            session_site=session_site,
            session_env=session_env,
            session_account=session_account,
            session_browser=session_browser,
        ),
        "-BaseUrl",
        contest_base_url(contest),
        "-CheckUrl",
        contest_base_url(contest),
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
    session_mode: str,
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
        session_mode,
        "-BaseUrl",
        contest_base_url(contest),
        "-CheckUrl",
        contest_base_url(contest),
        "-Url",
        contest_base_url(contest),
        "-ManualOpen",
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


def playwright_channel_name(name: str) -> str | None:
    value = (name or DEFAULT_SESSION_BROWSER).strip().lower()
    if value == "chrome":
        return "chrome"
    if value in {"edge", "msedge"}:
        return "msedge"
    return None


def is_login_url(url: str) -> bool:
    return urlparse(url).path.rstrip("/") == "/login"


def state_file_cookies(state_path: Path) -> list[dict[str, object]]:
    if not state_path.is_file():
        return []
    raw = json.loads(state_path.read_text(encoding="utf-8"))
    cookies = raw.get("cookies")
    if not isinstance(cookies, list):
        return []
    return [cookie for cookie in cookies if isinstance(cookie, dict)]


def cookie_header_value(cookie_jar: requests.cookies.RequestsCookieJar | None) -> str:
    if cookie_jar is None:
        return ""
    parts: list[str] = []
    for cookie in cookie_jar:
        parts.append(f"{cookie.name}={cookie.value}")
    return "; ".join(parts)


def requests_cookie_jar_from_state_file(state_path: Path) -> requests.cookies.RequestsCookieJar:
    jar = requests.cookies.RequestsCookieJar()
    for cookie in state_file_cookies(state_path):
        name = cookie.get("name")
        value = cookie.get("value")
        if not name or value is None:
            continue
        domain = str(cookie.get("domain") or "")
        path = str(cookie.get("path") or "/")
        if domain:
            jar.set(str(name), str(value), domain=domain, path=path)
        else:
            jar.set(str(name), str(value), path=path)
    return jar


def directory_has_entries(path: Path | None) -> bool:
    if path is None or not path.exists() or not path.is_dir():
        return False
    return any(path.iterdir())


def session_artifact_ready(session_metadata: dict[str, object]) -> bool:
    mode = str(session_metadata.get("mode") or DEFAULT_SESSION_MODE)
    state_path_raw = session_metadata.get("statePath")
    profile_path_raw = session_metadata.get("profilePath")
    state_exists = bool(state_path_raw) and Path(str(state_path_raw)).is_file()
    profile_ready = bool(profile_path_raw) and directory_has_entries(Path(str(profile_path_raw)))
    if mode == "storageState":
        return state_exists
    if mode in {"profile", "hybrid"}:
        return profile_ready or state_exists
    return state_exists or profile_ready


def state_file_ready(session_metadata: dict[str, object]) -> bool:
    state_path_raw = session_metadata.get("statePath")
    return bool(state_path_raw) and Path(str(state_path_raw)).is_file()


def profile_cookie_sources(profile_path: Path) -> tuple[Path, Path] | None:
    candidates = [
        (
            profile_path / "Default" / "Network" / "Cookies",
            profile_path / "Local State",
        ),
        (
            profile_path / "Network" / "Cookies",
            profile_path / "Local State",
        ),
    ]
    for cookie_file, key_file in candidates:
        if cookie_file.is_file() and key_file.is_file():
            return cookie_file, key_file
    return None


def load_profile_cookie_jar(
    browser_name: str,
    profile_path: Path,
    domain_name: str = "atcoder.jp",
):
    sources = profile_cookie_sources(profile_path)
    if sources is None:
        raise RuntimeError(f"Could not find cookie database in profile: {profile_path}")
    cookie_file, key_file = sources
    normalized = (browser_name or DEFAULT_SESSION_BROWSER).strip().lower()
    if normalized.startswith("chrome"):
        loader = browser_cookie3.chrome
    elif normalized in {"edge", "msedge"} or normalized.startswith("msedge"):
        loader = browser_cookie3.edge
    else:
        raise RuntimeError(f"Unsupported browser for profile cookie loading: {browser_name}")
    return loader(cookie_file=str(cookie_file), key_file=str(key_file), domain_name=domain_name)


def storage_state_from_cookie_jar(cookie_jar) -> dict[str, object]:
    cookies: list[dict[str, object]] = []
    for cookie in cookie_jar:
        item: dict[str, object] = {
            "name": cookie.name,
            "value": cookie.value,
            "domain": cookie.domain,
            "path": cookie.path or "/",
            "expires": float(cookie.expires) if cookie.expires else -1,
            "httpOnly": bool(getattr(cookie, "_rest", {}).get("HttpOnly")),
            "secure": bool(cookie.secure),
        }
        same_site = getattr(cookie, "_rest", {}).get("SameSite")
        if same_site in {"Lax", "None", "Strict"}:
            item["sameSite"] = same_site
        cookies.append(item)
    return {"cookies": cookies, "origins": []}


def load_session_cookie_jar(
    session_metadata: dict[str, object],
) -> requests.cookies.RequestsCookieJar | None:
    state_path = Path(str(session_metadata["statePath"]))
    if state_path.is_file():
        cookie_jar = requests_cookie_jar_from_state_file(state_path)
        if len(cookie_jar) > 0:
            return cookie_jar

    profile_path_raw = session_metadata.get("profilePath")
    profile_path = Path(str(profile_path_raw)) if profile_path_raw else None
    if profile_path is not None and profile_path.exists() and browser_cookie3 is not None:
        cookie_jar = load_profile_cookie_jar(
            str(session_metadata.get("browser") or DEFAULT_SESSION_BROWSER),
            profile_path,
        )
        if len(cookie_jar) > 0:
            return cookie_jar

    return None

def html_requires_login(
    page_html: str,
    final_url: str,
    check_selector: str,
) -> tuple[bool, str]:
    if is_login_url(final_url):
        return True, "redirected_to_login"

    root = html.fromstring(page_html)
    text_sample = normalize_text(" ".join(root.xpath("//body//text()"))).lower()
    if "cdn-cgi/challenge-platform" in final_url.lower():
        return True, "cloudflare_challenge_url"
    for pattern in CLOUDFLARE_TEXT_PATTERNS:
        if pattern in text_sample:
            return True, f"cloudflare_challenge:{pattern}"

    if check_selector.strip():
        try:
            if root.cssselect(check_selector.strip()):
                return False, "check_selector_visible"
        except Exception:
            pass

    login_regex = re.compile("|".join(DEFAULT_LOGIN_PATTERNS), re.IGNORECASE)
    clickable_nodes = root.xpath("//a|//button|//*[@role='button']")
    for node in clickable_nodes:
        text = normalize_text("".join(node.itertext()))
        if text and login_regex.search(text):
            return True, f"login_option_detected:{text}"

    return False, "no_login_option_detected"


def fetch_html_via_cookie_jar(
    contest: str,
    timeout: int,
    cookie_jar: requests.cookies.RequestsCookieJar,
    check_selector: str,
) -> tuple[str, bool, str]:
    session = requests.Session()
    session.cookies.update(cookie_jar)
    response = session.get(
        tasks_print_url(contest),
        timeout=timeout,
        headers={
            **DEFAULT_REQUEST_HEADERS,
            "Referer": contest_base_url(contest),
        },
    )
    response.raise_for_status()
    content = response.text
    final_url = response.url
    requires_login, reason = html_requires_login(content, final_url, check_selector)
    if requires_login:
        return "", False, reason
    return content, True, reason


def fetch_html_via_powershell_request(
    contest: str,
    timeout: int,
    check_selector: str,
    cookie_jar: requests.cookies.RequestsCookieJar | None = None,
) -> tuple[str, bool, str]:
    target_url = tasks_print_url(contest)
    referer_url = contest_base_url(contest)
    cookie_header = cookie_header_value(cookie_jar)
    command = f"""
$headers = @{{
    'User-Agent' = {json.dumps(DEFAULT_REQUEST_HEADERS['User-Agent'])}
    'Accept' = {json.dumps(DEFAULT_REQUEST_HEADERS['Accept'])}
    'Accept-Language' = {json.dumps(DEFAULT_REQUEST_HEADERS['Accept-Language'])}
    'Cache-Control' = {json.dumps(DEFAULT_REQUEST_HEADERS['Cache-Control'])}
    'Pragma' = {json.dumps(DEFAULT_REQUEST_HEADERS['Pragma'])}
    'Referer' = {json.dumps(referer_url)}
}}
if ({json.dumps(cookie_header)}) {{
    $headers['Cookie'] = {json.dumps(cookie_header)}
}}
$response = Invoke-WebRequest -Uri {json.dumps(target_url)} -Headers $headers -TimeoutSec {timeout}
[ordered]@{{
    statusCode = [int]$response.StatusCode
    finalUrl = [string]$response.BaseResponse.ResponseUri
    content = $response.Content
}} | ConvertTo-Json -Depth 4 -Compress
"""
    payload = run_powershell_inline_json(command)
    status_code = int(payload.get("statusCode", 0))
    if status_code >= 400:
        raise RuntimeError(f"PowerShell web request returned HTTP {status_code} for {target_url}")
    content = str(payload.get("content") or "")
    final_url = str(payload.get("finalUrl") or target_url)
    requires_login, reason = html_requires_login(content, final_url, check_selector)
    if requires_login:
        return "", False, reason
    return content, True, reason


def fetch_html_via_storage_state(
    contest: str,
    timeout: int,
    session_metadata: dict[str, object],
    check_selector: str,
) -> tuple[str, bool, str]:
    state_path = Path(str(session_metadata["statePath"]))
    profile_path_raw = session_metadata.get("profilePath")
    profile_path = Path(str(profile_path_raw)) if profile_path_raw else None
    goto_url = tasks_print_url(contest)
    browser_name = str(session_metadata.get("browser") or DEFAULT_SESSION_BROWSER)
    playwright_browser = normalize_browser_name(browser_name)
    channel_name = playwright_channel_name(browser_name)
    timeout_ms = timeout * 1000
    launch_kwargs: dict[str, object] = {"headless": True}
    if channel_name:
        launch_kwargs["channel"] = channel_name

    cookie_jar = load_session_cookie_jar(session_metadata)
    if cookie_jar is not None and len(cookie_jar) > 0:
        try:
            return fetch_html_via_cookie_jar(contest, timeout, cookie_jar, check_selector)
        except requests.RequestException as exc:
            print(
                "[fetch] Cookie-based HTTP fetch failed; falling back to Playwright. "
                f"reason={type(exc).__name__}: {exc}",
                file=sys.stderr,
            )
    try:
        return fetch_html_via_powershell_request(contest, timeout, check_selector, cookie_jar)
    except RuntimeError as exc:
        print(
            "[fetch] PowerShell web request failed; falling back to Playwright. "
            f"reason={exc}",
            file=sys.stderr,
        )

    with sync_playwright() as playwright:
        browser_launcher = getattr(playwright, playwright_browser)
        if state_path.is_file():
            browser = browser_launcher.launch(**launch_kwargs)
            context = browser.new_context(storage_state=str(state_path))
        elif profile_path is not None and profile_path.exists() and browser_cookie3 is not None:
            browser = browser_launcher.launch(**launch_kwargs)
            cookie_jar = load_profile_cookie_jar(browser_name, profile_path)
            context = browser.new_context(storage_state=storage_state_from_cookie_jar(cookie_jar))
        else:
            browser = browser_launcher.launch(**launch_kwargs)
            context_kwargs: dict[str, object] = {}
            context = browser.new_context(**context_kwargs)

        try:
            page = context.new_page()
            response = page.goto(goto_url, wait_until="domcontentloaded", timeout=timeout_ms)
            page.wait_for_load_state("networkidle", timeout=timeout_ms)
            final_url = page.url
            content = page.content()
            if response is not None and response.status >= 400:
                raise RuntimeError(f"Failed to fetch {goto_url}: HTTP {response.status}")
            requires_login, reason = html_requires_login(content, final_url, check_selector)
            if requires_login:
                return "", False, reason
            return content, True, reason
        finally:
            context.close()
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
    session_mode: str = DEFAULT_SESSION_MODE,
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
            session_mode=session_mode,
            login_check_selector=login_check_selector,
        )
        if not session_artifact_ready(session_metadata):
            print(
                "[fetch] AtCoder session artifact is missing; opening browser for manual login.",
                file=sys.stderr,
            )
            refresh_browser_session_login(
                contest,
                session_root=session_root,
                session_site=session_site,
                session_env=session_env,
                session_account=session_account,
                session_browser=session_browser,
                session_mode=session_mode,
                login_check_selector=login_check_selector,
            )
            session_metadata = upsert_browser_session(
                contest,
                session_root=session_root,
                session_site=session_site,
                session_env=session_env,
                session_account=session_account,
                session_browser=session_browser,
                session_mode=session_mode,
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
                session_mode=session_mode,
                login_check_selector=login_check_selector,
            )
            session_metadata = upsert_browser_session(
                contest,
                session_root=session_root,
                session_site=session_site,
                session_env=session_env,
                session_account=session_account,
                session_browser=session_browser,
                session_mode=session_mode,
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
        headers={**DEFAULT_REQUEST_HEADERS, "Referer": contest_base_url(contest)},
    )
    response.raise_for_status()
    return response.text


def html_fragment_to_markdown(fragment_html: str) -> str:
    payload = json.dumps({"html": fragment_html}, ensure_ascii=False)
    result = subprocess.run(
        ["node", str(TURNDOWN_SCRIPT)],
        input=payload,
        text=True,
        encoding="utf-8",
        errors="replace",
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
        session_mode=args.session_mode,
        login_check_selector=args.login_check_selector,
    )
    for slug, markdown in extract_tasks(page_html, contest_id):
        output_path = output_dir / f"{slug}.en.md"
        output_path.write_text(markdown, encoding="utf-8")
        print(f"Wrote {output_path}")


if __name__ == "__main__":
    main()
