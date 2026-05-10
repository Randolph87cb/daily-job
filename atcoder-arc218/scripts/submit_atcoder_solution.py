from __future__ import annotations

import argparse
import getpass
import re
import sys
import time
from pathlib import Path
from typing import Any
from urllib.parse import urljoin, urlparse

import requests
from lxml import html

try:
    import browser_cookie3
except ImportError:
    browser_cookie3 = None


ATCODER_BASE = "https://atcoder.jp"
BROWSER_COOKIE_ORDER = ["chrome", "edge", "brave", "chromium", "firefox", "opera", "vivaldi"]
PENDING_VERDICT_KEYWORDS = (
    "judg",
    "wait",
    "queue",
    "pend",
    "running",
    "compile",
    "progress",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Submit local source code to AtCoder and poll until the verdict reaches a terminal state."
    )
    parser.add_argument("--contest-id", required=True, help="Contest ID, for example: arc218")
    parser.add_argument(
        "--task",
        required=True,
        help="Task screen name or slug, for example: arc218_a or A",
    )
    parser.add_argument(
        "--source-file",
        required=True,
        type=Path,
        help="Path to the source code file that will be submitted.",
    )
    parser.add_argument(
        "--language",
        required=True,
        help="Language id, exact name, or case-insensitive substring match from the submit page.",
    )
    parser.add_argument(
        "--auth-mode",
        choices=["auto", "browser", "password"],
        default="auto",
        help="Authentication mode. Default: auto",
    )
    parser.add_argument(
        "--browser-cookies",
        default="auto",
        help="Browser cookies to load. Supported: auto, off, chrome, edge, brave, chromium, firefox, opera, vivaldi.",
    )
    parser.add_argument("--username", default=None, help="AtCoder username for password login.")
    parser.add_argument("--password", default=None, help="AtCoder password for password login.")
    parser.add_argument("--timeout", type=int, default=30, help="HTTP timeout in seconds. Default: 30")
    parser.add_argument(
        "--poll-interval",
        type=float,
        default=2.0,
        help="Seconds between verdict polls. Default: 2.0",
    )
    parser.add_argument(
        "--poll-timeout",
        type=int,
        default=300,
        help="Maximum polling time in seconds. Default: 300",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Resolve authentication, task, and language without sending the final submit POST.",
    )
    parser.add_argument(
        "--print-languages",
        action="store_true",
        help="Print language ids and names available on the submit page, then exit.",
    )
    return parser.parse_args()


def browser_cookie_loader_names(browser_name: str) -> list[str]:
    normalized = (browser_name or "").strip().lower()
    if not normalized or normalized == "off":
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


def build_session() -> requests.Session:
    session = requests.Session()
    session.headers.update(
        {
            "User-Agent": "Mozilla/5.0 (compatible; AtCoderSolutionSubmitter/1.0)",
        }
    )
    return session


def normalize_text(value: str) -> str:
    return " ".join((value or "").split()).strip()


def normalize_token(value: str) -> str:
    return normalize_text(value).casefold()


def is_login_url(url: str) -> bool:
    return urlparse(url).path.rstrip("/") == "/login"


def submit_page_url(contest_id: str) -> str:
    return f"{ATCODER_BASE}/contests/{contest_id}/submit"


def login_url(continue_url: str) -> str:
    return f"{ATCODER_BASE}/login?continue={requests.utils.quote(continue_url, safe='')}"


def resolve_action_url(page_url: str, form: html.HtmlElement) -> str:
    action = (form.get("action") or "").strip()
    return urljoin(page_url, action or page_url)


def collect_form_defaults(form: html.HtmlElement) -> dict[str, str]:
    payload: dict[str, str] = {}
    for input_node in form.xpath(".//input[@name]"):
        if input_node.get("disabled") is not None:
            continue
        input_type = (input_node.get("type") or "text").lower()
        name = input_node.get("name")
        if not name or input_type in {"submit", "button", "image", "file"}:
            continue
        if input_type in {"checkbox", "radio"} and input_node.get("checked") is None:
            continue
        payload[name] = input_node.get("value") or ""

    for textarea_node in form.xpath(".//textarea[@name]"):
        if textarea_node.get("disabled") is not None:
            continue
        name = textarea_node.get("name")
        if name:
            payload[name] = textarea_node.text or ""

    for select_node in form.xpath(".//select[@name]"):
        if select_node.get("disabled") is not None:
            continue
        name = select_node.get("name")
        if not name:
            continue
        selected = select_node.xpath(".//option[@selected]")
        option = selected[0] if selected else next(iter(select_node.xpath(".//option")), None)
        if option is not None:
            payload[name] = option.get("value") or normalize_text(option.text_content())
    return payload


def choose_submit_form(page_url: str, tree: html.HtmlElement) -> html.HtmlElement:
    forms = tree.xpath("//form")
    textarea_forms = [form for form in forms if form.xpath(".//textarea[@name]")]
    if textarea_forms:
        return textarea_forms[0]
    post_forms = [
        form
        for form in forms
        if (form.get("method") or "get").lower() == "post"
        and "submit" in resolve_action_url(page_url, form)
    ]
    if post_forms:
        return post_forms[0]
    raise RuntimeError("Could not find the submit form on the page.")


def task_candidates(value: str) -> set[str]:
    token = normalize_token(value)
    candidates = {token}
    if "_" in token:
        candidates.add(token.split("_", 1)[1])
    return {candidate for candidate in candidates if candidate}


def task_option_matches(option: html.HtmlElement, requested_task: str) -> bool:
    requested = task_candidates(requested_task)
    option_value = normalize_token(option.get("value") or "")
    option_text = normalize_token(option.text_content())
    if option_value in requested or option_text in requested:
        return True
    if "_" in option_value and option_value.split("_", 1)[1] in requested:
        return True
    if " - " in option_text and option_text.split(" - ", 1)[0] in requested:
        return True
    return False


def resolve_task_select(form: html.HtmlElement, requested_task: str) -> tuple[html.HtmlElement, html.HtmlElement]:
    matches: list[tuple[html.HtmlElement, html.HtmlElement]] = []
    for select_node in form.xpath(".//select[@name]"):
        options = select_node.xpath(".//option")
        for option_node in options:
            if task_option_matches(option_node, requested_task):
                matches.append((select_node, option_node))
    if not matches:
        raise RuntimeError(f"Task `{requested_task}` was not found in the submit form.")
    if len(matches) > 1:
        unique_values = {option.get('value') or normalize_text(option.text_content()) for _, option in matches}
        if len(unique_values) > 1:
            raise RuntimeError(f"Task `{requested_task}` matched multiple form options: {sorted(unique_values)}")
    return matches[0]


def resolve_language_select(
    form: html.HtmlElement,
    requested_language: str,
) -> tuple[html.HtmlElement, html.HtmlElement]:
    request = normalize_text(requested_language)
    request_token = normalize_token(requested_language)
    request_is_id = request.isdigit()
    exact_matches: list[tuple[html.HtmlElement, html.HtmlElement]] = []
    partial_matches: list[tuple[html.HtmlElement, html.HtmlElement]] = []

    for select_node in form.xpath(".//select[@name]"):
        for option_node in select_node.xpath(".//option"):
            option_value = normalize_text(option_node.get("value") or "")
            option_text = normalize_text(option_node.text_content())
            option_token = normalize_token(option_text)
            if request_is_id and option_value == request:
                exact_matches.append((select_node, option_node))
                continue
            if option_token == request_token:
                exact_matches.append((select_node, option_node))
                continue
            if request_token and request_token in option_token:
                partial_matches.append((select_node, option_node))

    matches = exact_matches or partial_matches
    if not matches:
        raise RuntimeError(f"Language `{requested_language}` was not found in the submit form.")
    unique_values = {
        f"{option.get('value') or ''}\t{normalize_text(option.text_content())}"
        for _, option in matches
    }
    if len(unique_values) > 1:
        preview = "\n".join(sorted(unique_values)[:10])
        raise RuntimeError(
            "Language match is ambiguous. Use a more specific name or the numeric language id.\n"
            f"{preview}"
        )
    return matches[0]


def resolve_source_field(form: html.HtmlElement) -> html.HtmlElement:
    textareas = form.xpath(".//textarea[@name]")
    if not textareas:
        raise RuntimeError("Could not find the source code textarea in the submit form.")
    preferred = [
        node
        for node in textareas
        if any(keyword in normalize_token(node.get("name") or "") for keyword in ("source", "code"))
    ]
    return preferred[0] if preferred else textareas[0]


def parse_flash_messages(tree: html.HtmlElement) -> list[str]:
    messages: list[str] = []
    for node in tree.xpath("//*[contains(@class,'alert') or contains(@class,'error') or contains(@class,'warning')]"):
        text = normalize_text(node.text_content())
        if text and text not in messages:
            messages.append(text)
    return messages


def password_login(
    session: requests.Session,
    continue_url: str,
    username: str,
    password: str,
    timeout: int,
) -> None:
    page = session.get(login_url(continue_url), timeout=timeout)
    page.raise_for_status()
    tree = html.fromstring(page.text)
    form = next(
        (
            node
            for node in tree.xpath("//form")
            if node.xpath(".//input[@name='username']") and node.xpath(".//input[@name='password']")
        ),
        None,
    )
    if form is None:
        raise RuntimeError("Could not find the AtCoder login form.")

    payload = collect_form_defaults(form)
    payload["username"] = username
    payload["password"] = password
    response = session.post(
        resolve_action_url(page.url, form),
        data=payload,
        timeout=timeout,
        headers={"Referer": page.url},
    )
    response.raise_for_status()
    if is_login_url(response.url):
        messages = parse_flash_messages(html.fromstring(response.text))
        reason = "; ".join(messages) if messages else "AtCoder kept the session on the login page."
        raise RuntimeError(f"Password login failed: {reason}")


def ensure_authenticated(
    session: requests.Session,
    contest_id: str,
    auth_mode: str,
    browser_cookies: str,
    username: str | None,
    password: str | None,
    timeout: int,
) -> tuple[str, str]:
    page_url = submit_page_url(contest_id)
    errors: list[str] = []

    if auth_mode in {"auto", "browser"} and browser_cookie_loader_names(browser_cookies):
        try:
            session.cookies.update(load_browser_cookie_jar(browser_cookies))
            response = session.get(page_url, timeout=timeout)
            response.raise_for_status()
            if not is_login_url(response.url):
                return response.url, response.text
            errors.append("browser cookie login reached the login page")
        except Exception as exc:
            errors.append(f"browser cookie login failed: {exc}")

    if auth_mode in {"auto", "password"}:
        if not username:
            if auth_mode == "password":
                raise RuntimeError("`--username` is required when auth mode is `password`.")
        else:
            try:
                actual_password = password if password is not None else getpass.getpass("AtCoder password: ")
                password_login(session, page_url, username, actual_password, timeout)
                response = session.get(page_url, timeout=timeout)
                response.raise_for_status()
                if is_login_url(response.url):
                    raise RuntimeError("Password login succeeded but the submit page still redirected to login.")
                return response.url, response.text
            except Exception as exc:
                errors.append(f"password login failed: {exc}")

    raise RuntimeError("Authentication failed. " + " | ".join(errors))


def submissions_me_url(contest_id: str, task_value: str) -> str:
    return f"{ATCODER_BASE}/contests/{contest_id}/submissions/me?f.Task={requests.utils.quote(task_value)}"


def extract_first_submission(
    page_html: str,
    contest_id: str,
) -> dict[str, Any] | None:
    tree = html.fromstring(page_html)
    rows = tree.xpath("//table//tr[td]")
    for row in rows:
        row_html = html.tostring(row, encoding="unicode")
        match = re.search(rf"/contests/{re.escape(contest_id)}/submissions/(\d+)", row_html)
        if not match:
            continue
        row_text = normalize_text(" ".join(row.xpath(".//td//text()")))
        verdict = extract_verdict_from_row(row)
        return {
            "id": int(match.group(1)),
            "verdict": verdict,
            "url": f"{ATCODER_BASE}/contests/{contest_id}/submissions/{match.group(1)}",
            "text": row_text,
        }
    return None


def extract_verdict_from_row(row: html.HtmlElement) -> str:
    verdict_nodes = row.xpath(".//*[contains(@class,'label') or contains(@class,'status') or contains(@title,'Judg')]")
    for node in verdict_nodes:
        text = normalize_text(node.text_content())
        if text:
            return text
    cells = [normalize_text(cell.text_content()) for cell in row.xpath(".//td")]
    for text in cells:
        if not text:
            continue
        lowered = text.casefold()
        if any(keyword in lowered for keyword in PENDING_VERDICT_KEYWORDS):
            return text
        if re.fullmatch(r"[A-Z][A-Z0-9 +()-]{1,20}", text):
            return text
    return cells[0] if cells else ""


def verdict_is_terminal(verdict: str) -> bool:
    lowered = normalize_token(verdict)
    if not lowered:
        return False
    return not any(keyword in lowered for keyword in PENDING_VERDICT_KEYWORDS)


def load_source_code(source_file: Path) -> str:
    if not source_file.is_file():
        raise RuntimeError(f"Source file does not exist: {source_file}")
    return source_file.read_text(encoding="utf-8")


def print_languages(form: html.HtmlElement) -> None:
    printed: set[str] = set()
    for select_node in form.xpath(".//select[@name]"):
        for option_node in select_node.xpath(".//option"):
            value = normalize_text(option_node.get("value") or "")
            text = normalize_text(option_node.text_content())
            if not value or not text:
                continue
            key = f"{value}\t{text}"
            if key in printed:
                continue
            printed.add(key)
            print(f"{value}\t{text}")


def submit_solution(
    session: requests.Session,
    page_url: str,
    page_html: str,
    contest_id: str,
    requested_task: str,
    requested_language: str,
    source_code: str,
    dry_run: bool,
    print_languages_only: bool,
    timeout: int,
    poll_interval: float,
    poll_timeout: int,
) -> dict[str, Any]:
    tree = html.fromstring(page_html)
    form = choose_submit_form(page_url, tree)
    task_select, task_option = resolve_task_select(form, requested_task)
    language_select, language_option = resolve_language_select(form, requested_language)
    source_field = resolve_source_field(form)

    if print_languages_only:
        print_languages(form)
        return {"mode": "print-languages"}

    if dry_run:
        result = {
            "mode": "dry-run",
            "submit_url": resolve_action_url(page_url, form),
            "task_value": task_option.get("value") or "",
            "task_label": normalize_text(task_option.text_content()),
            "language_value": language_option.get("value") or "",
            "language_label": normalize_text(language_option.text_content()),
            "source_field": source_field.get("name") or "",
        }
        for key, value in result.items():
            print(f"{key}: {value}")
        return result

    task_value = task_option.get("value") or ""
    previous_submission = fetch_latest_submission(session, contest_id, task_value, timeout)
    previous_id = previous_submission["id"] if previous_submission else None

    payload = collect_form_defaults(form)
    payload[task_select.get("name")] = task_value
    payload[language_select.get("name")] = language_option.get("value") or ""
    payload[source_field.get("name")] = source_code

    response = session.post(
        resolve_action_url(page_url, form),
        data=payload,
        timeout=timeout,
        headers={"Referer": page_url},
    )
    response.raise_for_status()

    if is_login_url(response.url):
        raise RuntimeError("Submit POST redirected to the login page. Authentication likely expired.")

    if response.url.rstrip("/") == page_url.rstrip("/"):
        messages = parse_flash_messages(html.fromstring(response.text))
        if messages:
            raise RuntimeError("Submit was rejected: " + "; ".join(messages))

    submission = wait_for_new_submission(
        session=session,
        contest_id=contest_id,
        task_value=task_value,
        previous_id=previous_id,
        timeout=timeout,
        poll_interval=poll_interval,
        poll_timeout=poll_timeout,
    )
    print(f"submission_id: {submission['id']}")
    print(f"verdict: {submission['verdict']}")
    print(f"url: {submission['url']}")
    return submission


def fetch_latest_submission(
    session: requests.Session,
    contest_id: str,
    task_value: str,
    timeout: int,
) -> dict[str, Any] | None:
    response = session.get(submissions_me_url(contest_id, task_value), timeout=timeout)
    response.raise_for_status()
    if is_login_url(response.url):
        raise RuntimeError("The submissions page redirected to login. Authentication likely expired.")
    return extract_first_submission(response.text, contest_id)


def wait_for_new_submission(
    session: requests.Session,
    contest_id: str,
    task_value: str,
    previous_id: int | None,
    timeout: int,
    poll_interval: float,
    poll_timeout: int,
) -> dict[str, Any]:
    deadline = time.monotonic() + poll_timeout
    latest: dict[str, Any] | None = None

    while time.monotonic() <= deadline:
        latest = fetch_latest_submission(session, contest_id, task_value, timeout)
        if latest and (previous_id is None or latest["id"] > previous_id):
            if verdict_is_terminal(latest["verdict"]):
                return latest
        time.sleep(poll_interval)

    if latest and (previous_id is None or latest["id"] > previous_id):
        raise RuntimeError(
            "Polling timed out before a terminal verdict was reached. "
            f"Latest status: {latest['verdict']} ({latest['url']})"
        )
    raise RuntimeError("Polling timed out before the new submission appeared on the submissions page.")


def main() -> None:
    args = parse_args()
    session = build_session()
    source_code = load_source_code(args.source_file)
    page_url, page_html = ensure_authenticated(
        session=session,
        contest_id=args.contest_id,
        auth_mode=args.auth_mode,
        browser_cookies=args.browser_cookies,
        username=args.username,
        password=args.password,
        timeout=args.timeout,
    )
    submit_solution(
        session=session,
        page_url=page_url,
        page_html=page_html,
        contest_id=args.contest_id,
        requested_task=args.task,
        requested_language=args.language,
        source_code=source_code,
        dry_run=args.dry_run,
        print_languages_only=args.print_languages,
        timeout=args.timeout,
        poll_interval=args.poll_interval,
        poll_timeout=args.poll_timeout,
    )


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted.", file=sys.stderr)
        raise SystemExit(130)
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        raise SystemExit(1)
