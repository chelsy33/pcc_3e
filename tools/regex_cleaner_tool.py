"""Regex Cleaner Tool：面向翻译项目的批量文本清洗脚本。"""

import argparse
import pathlib
import re
from typing import Iterable

PUNCTUATION_CLASS = "[！？?!。，,.：:；;]"
PUNCT_NEED_SPACE = "[,.;!?。！？]"
PUNCT_PATTERN = re.compile(fr"({PUNCTUATION_CLASS})\1+")
WHITESPACE_PATTERN = re.compile(r"\s+")
TRAILING_SPACE_PATTERN = re.compile(fr"\s*({PUNCTUATION_CLASS})")
PUNCT_FOLLOW_PATTERN = re.compile(fr"({PUNCT_NEED_SPACE})(?![\s\n])")


def clean_text(text: str) -> str:
    """将翻译稿中的多余空格、重复标点统一成规范格式。"""
    cleaned = WHITESPACE_PATTERN.sub(" ", text)
    cleaned = PUNCT_PATTERN.sub(r"\1", cleaned)
    cleaned = TRAILING_SPACE_PATTERN.sub(r"\1", cleaned)
    cleaned = PUNCT_FOLLOW_PATTERN.sub(r"\1 ", cleaned)
    return cleaned.strip()


def iter_txt_files(folder: pathlib.Path) -> Iterable[pathlib.Path]:
    """遍历文件夹中的 TXT 文件，以字母序返回。"""
    for path in sorted(folder.glob("*.txt")):
        if path.is_file():
            yield path


def process_file(path: pathlib.Path, output_dir: pathlib.Path) -> pathlib.Path:
    """清洗单个 TXT 文件并写入输出目录。"""
    cleaned_text = clean_text(path.read_text(encoding="utf-8"))
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / f"{path.stem}_cleaned.txt"
    output_path.write_text(cleaned_text, encoding="utf-8")
    return output_path


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Regex Cleaner Tool：清理翻译语料的多余空格与重复标点"
    )
    parser.add_argument("--text", help="直接清理一段文本", default=None)
    parser.add_argument(
        "--input",
        type=pathlib.Path,
        help="单个 TXT 文件路径",
        default=None,
    )
    parser.add_argument(
        "--input-dir",
        type=pathlib.Path,
        help="包含多个 TXT 的文件夹，将在 cleaned/ 子目录输出",
        default=None,
    )
    parser.add_argument(
        "--output",
        type=pathlib.Path,
        help="输出文件路径；未提供时将写入 *_cleaned.txt",
        default=None,
    )

    args = parser.parse_args()

    executed = False

    if args.text:
        print(clean_text(args.text))
        executed = True

    if args.input:
        output_path = args.output or args.input.with_name(f"{args.input.stem}_cleaned.txt")
        cleaned_text = clean_text(args.input.read_text(encoding="utf-8"))
        output_path.write_text(cleaned_text, encoding="utf-8")
        print(f"已清理文件：{args.input} → {output_path}")
        executed = True

    if args.input_dir:
        output_dir = args.input_dir / "cleaned"
        outputs = [process_file(path, output_dir) for path in iter_txt_files(args.input_dir)]
        if outputs:
            print("批量清洗完成：")
            for out_path in outputs:
                print(f"  - {out_path}")
        else:
            print("未在指定文件夹中找到 TXT 文件。")
        executed = True

    if not executed:
        parser.error("请至少提供 --text、--input 或 --input-dir 其中之一。")


if __name__ == "__main__":
    main()
