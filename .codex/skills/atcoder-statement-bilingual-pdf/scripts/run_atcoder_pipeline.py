from __future__ import annotations

import argparse
import time
from pathlib import Path

import fetch_atcoder_tasks
import translate_markdown

MAX_BATCH_BLOCKS = 48
MAX_BATCH_CHARS = 18000


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Fetch English AtCoder statements and translate them into Chinese."
    )
    parser.add_argument("contest", nargs="?", help="Contest ID, for example: arc218")
    parser.add_argument("--contest-id", dest="contest_flag", help="Legacy contest flag.")
    parser.add_argument(
        "--workspace",
        type=Path,
        default=Path.cwd() / "atcoder-output",
        help="Base output directory. Default: ./atcoder-output",
    )
    parser.add_argument(
        "--provider",
        default="openai",
        choices=["rule-based", "openai"],
        help="Translation provider. Default: openai",
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
        default=translate_markdown.default_env_file(),
        help="Path to a .env file. Default: ../.env",
    )
    parser.add_argument(
        "--base-url",
        default="",
        help="API endpoint for the openai provider. Default depends on api mode or OPENAI_BASE_URL.",
    )
    parser.add_argument(
        "--overwrite",
        action=argparse.BooleanOptionalAction,
        default=True,
        help="Overwrite translated files if they already exist. Default: enabled",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=0,
        help="Only translate the first N files. 0 means no limit.",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=30,
        help="HTTP timeout for fetching statements. Default: 30",
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
        help="Load cookies directly from a local browser profile when --auth-mode=browser-cookies. Default: auto. Supported: auto, chrome, edge, brave, chromium, firefox, opera, vivaldi.",
    )
    parser.add_argument(
        "--session-root",
        type=Path,
        default=None,
        help="Override the browser-session-manager store root. Default: %%LOCALAPPDATA%%\\Codex\\browser-sessions",
    )
    parser.add_argument(
        "--session-site",
        default=fetch_atcoder_tasks.DEFAULT_SESSION_SITE,
        help="Session registry site key. Default: atcoder",
    )
    parser.add_argument(
        "--session-env",
        default=fetch_atcoder_tasks.DEFAULT_SESSION_ENV,
        help="Session registry env key. Default: prod",
    )
    parser.add_argument(
        "--session-account",
        default=fetch_atcoder_tasks.DEFAULT_SESSION_ACCOUNT,
        help="Session registry account key. Default: default",
    )
    parser.add_argument(
        "--session-browser",
        default=fetch_atcoder_tasks.DEFAULT_SESSION_BROWSER,
        help="Session registry browser key. Default: chrome",
    )
    parser.add_argument(
        "--session-mode",
        default=fetch_atcoder_tasks.DEFAULT_SESSION_MODE,
        choices=["storageState", "profile", "hybrid"],
        help="Session registry mode. Default: profile",
    )
    parser.add_argument(
        "--login-check-selector",
        default="",
        help="Optional selector that proves the logged-in state. Default: empty",
    )
    parser.add_argument(
        "--output-format",
        default="bilingual",
        choices=["bilingual", "translation-only"],
        help="Output format. Default: bilingual",
    )
    parser.add_argument(
        "--export-pdf",
        action=argparse.BooleanOptionalAction,
        default=True,
        help="Export generated Markdown files to PDF with md2pdf. Default: enabled",
    )
    parser.add_argument(
        "--pdf-output-dir",
        type=Path,
        default=None,
        help="Directory for generated PDFs. Default: same as output workspace zh-CN directory.",
    )
    return parser.parse_args()


def resolve_contest_id(args: argparse.Namespace) -> str:
    contest = (args.contest or "").strip()
    legacy_contest = (args.contest_flag or "").strip()
    resolved = contest or legacy_contest
    if not resolved:
        raise SystemExit("Contest ID is required. Example: run_atcoder_pipeline.py abc456")
    return resolved


def batched_model_entries(
    entries: list[tuple[int, int, str]],
) -> list[list[tuple[int, int, str]]]:
    batches: list[list[tuple[int, int, str]]] = []
    current: list[tuple[int, int, str]] = []
    current_chars = 0

    for entry in entries:
        block_chars = len(entry[2])
        if current and (
            len(current) >= MAX_BATCH_BLOCKS or current_chars + block_chars > MAX_BATCH_CHARS
        ):
            batches.append(current)
            current = []
            current_chars = 0
        current.append(entry)
        current_chars += block_chars

    if current:
        batches.append(current)

    return batches


def main() -> None:
    pipeline_started = time.perf_counter()
    args = parse_args()
    contest_id = resolve_contest_id(args)
    translate_markdown.load_dotenv(args.env_file)

    english_dir = args.workspace / contest_id / "en"
    chinese_dir = args.workspace / contest_id / "zh-CN"
    english_dir.mkdir(parents=True, exist_ok=True)
    chinese_dir.mkdir(parents=True, exist_ok=True)

    print(f"[pipeline] contest={contest_id}")
    print(f"[pipeline] workspace={args.workspace}")
    print(f"[pipeline] provider={args.provider}")
    print(f"[pipeline] env_file={args.env_file}")
    print(f"[pipeline] output_format={args.output_format}")
    print(f"[pipeline] export_pdf={args.export_pdf}")
    if args.provider == "openai":
        api_mode = translate_markdown.resolve_openai_api_mode(args)
        base_url = translate_markdown.resolve_openai_base_url(args, api_mode)
        print(f"[pipeline] api_mode={api_mode}")
        print(f"[pipeline] base_url={base_url}")
        print(f"[pipeline] model={args.model}")
    print(f"[pipeline] auth_mode={args.auth_mode}")
    if args.auth_mode == "session":
        print(
            "[pipeline] session="
            f"{args.session_site}/{args.session_env}/{args.session_account}/{args.session_browser}"
        )
        print(f"[pipeline] session_mode={args.session_mode}")
        if args.session_root is not None:
            print(f"[pipeline] session_root={args.session_root}")
        if args.login_check_selector:
            print(f"[pipeline] login_check_selector={args.login_check_selector}")
    else:
        print(f"[pipeline] browser_cookies={args.browser_cookies}")

    print("[pipeline] fetching english statements")
    fetch_started = time.perf_counter()
    page_html = fetch_atcoder_tasks.fetch_html(
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
    extracted_tasks = list(fetch_atcoder_tasks.extract_tasks(page_html, contest_id))
    fetch_seconds = time.perf_counter() - fetch_started
    for index, (slug, markdown) in enumerate(extracted_tasks, start=1):
        output_path = english_dir / f"{slug}.en.md"
        output_path.write_text(markdown, encoding="utf-8")
        print(f"[pipeline] [fetch {index}/{len(extracted_tasks)}] wrote {output_path}")
    print(f"[pipeline] fetch_seconds={fetch_seconds:.2f}")

    glossary = translate_markdown.load_glossary(
        Path(__file__).resolve().parent.parent / "translation_assets" / "algorithm_glossary.json"
    )
    translator_args = argparse.Namespace(
        provider=args.provider,
        model=args.model,
        api_mode=args.api_mode,
        api_key_env=args.api_key_env,
        base_url=args.base_url,
    )
    translator = translate_markdown.create_translator(translator_args, glossary)

    input_files = translate_markdown.iter_input_files(english_dir)
    if args.limit > 0:
        input_files = input_files[: args.limit]
    print(f"[pipeline] translating {len(input_files)} file(s)")
    pdf_output_dir = args.pdf_output_dir or chinese_dir
    if args.export_pdf:
        print(f"[pipeline] pdf_output_dir={pdf_output_dir}")

    total = len(input_files)
    output_paths: list[Path] = []
    documents: list[dict[str, object]] = []
    model_entries: list[tuple[int, int, str]] = []
    translation_started = time.perf_counter()

    for index, source_path in enumerate(input_files, start=1):
        output_path = chinese_dir / translate_markdown.translated_name(source_path)
        if output_path.exists() and not args.overwrite:
            print(f"[pipeline] [translate {index}/{total}] skip existing {output_path}")
            output_paths.append(output_path)
            continue

        print(f"[pipeline] [translate {index}/{total}] translating {source_path.name}")
        source_text = source_path.read_text(encoding="utf-8")
        source_blocks = translate_markdown.split_markdown_content_blocks(source_text)
        translated_blocks: list[str] = [""] * len(source_blocks)
        doc_index = len(documents)

        if isinstance(translator, translate_markdown.OpenAITranslator):
            for block_index, block in enumerate(source_blocks):
                if translate_markdown.should_translate_with_model(block):
                    model_entries.append((doc_index, block_index, block))
                    continue
                if translate_markdown.is_fenced_code_block(block):
                    translated_blocks[block_index] = block
                else:
                    translated_blocks[block_index] = translate_markdown.translate_block_locally(
                        block,
                        glossary,
                    )
        else:
            translated_blocks = translate_markdown.translate_markdown_blocks(source_text, translator)

        documents.append(
            {
                "index": index,
                "source_path": source_path,
                "output_path": output_path,
                "source_text": source_text,
                "source_blocks": source_blocks,
                "translated_blocks": translated_blocks,
            }
        )

    if isinstance(translator, translate_markdown.OpenAITranslator) and model_entries:
        batches = batched_model_entries(model_entries)
        for batch_index, batch in enumerate(batches, start=1):
            batch_blocks = [entry[2] for entry in batch]
            doc_ids = sorted({entry[0] for entry in batch})
            print(
                "[pipeline] "
                f"[translate batch {batch_index}/{len(batches)}] "
                f"translating {len(batch_blocks)} block(s) across {len(doc_ids)} file(s)"
            )
            translated_batch = translator.translate_blocks(batch_blocks)
            for (doc_index, block_index, _), translated_block in zip(
                batch,
                translated_batch,
                strict=True,
            ):
                documents[doc_index]["translated_blocks"][block_index] = translated_block

    translation_seconds = time.perf_counter() - translation_started
    print(f"[pipeline] translation_seconds={translation_seconds:.2f}")

    pdf_seconds = 0.0
    for document in documents:
        index = int(document["index"])
        output_path = document["output_path"]
        source_text = document["source_text"]
        source_blocks = document["source_blocks"]
        translated_blocks = document["translated_blocks"]

        translated_text = "\n\n".join(block.strip() for block in translated_blocks if block.strip())
        if not translated_text.endswith("\n"):
            translated_text += "\n"
        final_text = translated_text
        if args.output_format == "bilingual":
            final_text = translate_markdown.build_bilingual_markdown_from_blocks(
                source_blocks,
                translated_blocks,
                source_text,
                translated_text,
                glossary,
            )
        output_path.write_text(final_text, encoding="utf-8")
        print(f"[pipeline] [translate {index}/{total}] wrote {output_path}")
        output_paths.append(output_path)
        if args.export_pdf:
            pdf_started = time.perf_counter()
            pdf_path = translate_markdown.export_markdown_to_pdf(output_path, pdf_output_dir)
            pdf_seconds += time.perf_counter() - pdf_started
            print(f"[pipeline] [translate {index}/{total}] wrote {pdf_path}")

    combined_sources = [
        path for path in output_paths if path.exists() and translate_markdown.is_problem_translation_markdown(path)
    ]
    if combined_sources:
        combined_started = time.perf_counter()
        combined_markdown_path = translate_markdown.write_combined_markdown(combined_sources, chinese_dir)
        print(f"[pipeline] wrote combined markdown {combined_markdown_path}")
        if args.export_pdf:
            pdf_started = time.perf_counter()
            combined_pdf_path = translate_markdown.export_markdown_to_pdf(combined_markdown_path, pdf_output_dir)
            pdf_seconds += time.perf_counter() - pdf_started
            print(f"[pipeline] wrote combined pdf {combined_pdf_path}")
        combined_seconds = time.perf_counter() - combined_started
        print(f"[pipeline] combined_seconds={combined_seconds:.2f}")

    if args.export_pdf:
        print(f"[pipeline] pdf_seconds={pdf_seconds:.2f}")
    print(f"[pipeline] total_seconds={time.perf_counter() - pipeline_started:.2f}")


if __name__ == "__main__":
    main()
