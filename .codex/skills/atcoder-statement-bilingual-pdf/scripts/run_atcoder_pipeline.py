from __future__ import annotations

import argparse
from pathlib import Path

import fetch_atcoder_tasks
import translate_markdown


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
        "--browser-cookies",
        default="auto",
        help="Load cookies directly from a local browser profile. Default: auto. Supported: auto, chrome, edge, brave, chromium, firefox, opera, vivaldi.",
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


def main() -> None:
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
    print(f"[pipeline] browser_cookies={args.browser_cookies}")

    print("[pipeline] fetching english statements")
    page_html = fetch_atcoder_tasks.fetch_html(
        contest_id,
        args.timeout,
        browser_cookies=args.browser_cookies,
    )
    extracted_tasks = list(fetch_atcoder_tasks.extract_tasks(page_html, contest_id))
    for index, (slug, markdown) in enumerate(extracted_tasks, start=1):
        output_path = english_dir / f"{slug}.en.md"
        output_path.write_text(markdown, encoding="utf-8")
        print(f"[pipeline] [fetch {index}/{len(extracted_tasks)}] wrote {output_path}")

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
    for index, source_path in enumerate(input_files, start=1):
        output_path = chinese_dir / translate_markdown.translated_name(source_path)
        if output_path.exists() and not args.overwrite:
            print(f"[pipeline] [translate {index}/{total}] skip existing {output_path}")
            output_paths.append(output_path)
            continue

        print(f"[pipeline] [translate {index}/{total}] translating {source_path.name}")
        source_text = source_path.read_text(encoding="utf-8")
        translated_text = translate_markdown.translate_markdown(source_text, translator)
        final_text = translated_text
        if args.output_format == "bilingual":
            final_text = translate_markdown.build_bilingual_markdown_with_glossary(
                source_text,
                translated_text,
                glossary,
            )
        output_path.write_text(final_text, encoding="utf-8")
        print(f"[pipeline] [translate {index}/{total}] wrote {output_path}")
        output_paths.append(output_path)
        if args.export_pdf:
            pdf_path = translate_markdown.export_markdown_to_pdf(output_path, pdf_output_dir)
            print(f"[pipeline] [translate {index}/{total}] wrote {pdf_path}")

    combined_sources = [
        path for path in output_paths if path.exists() and translate_markdown.is_problem_translation_markdown(path)
    ]
    if combined_sources:
        combined_markdown_path = translate_markdown.write_combined_markdown(combined_sources, chinese_dir)
        print(f"[pipeline] wrote combined markdown {combined_markdown_path}")
        if args.export_pdf:
            combined_pdf_path = translate_markdown.export_markdown_to_pdf(combined_markdown_path, pdf_output_dir)
            print(f"[pipeline] wrote combined pdf {combined_pdf_path}")


if __name__ == "__main__":
    main()
