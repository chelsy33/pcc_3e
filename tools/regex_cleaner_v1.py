"""轻量版 Regex Cleaner：帮助翻译学生快速清理文本。"""

import re

PUNCTUATION_CLASS = "[！？?!。，,.：:；;]"
PUNCT_NEED_SPACE = "[,.;!?。！？]"


def clean_text(text: str) -> str:
    """清理多余空格和重复标点，并保持标点后的可读空格。"""
    cleaned = re.sub(r"\s+", " ", text)
    cleaned = re.sub(fr"({PUNCTUATION_CLASS})\1+", r"\1", cleaned)
    cleaned = re.sub(fr"\s*({PUNCTUATION_CLASS})", r"\1", cleaned)
    cleaned = re.sub(fr"({PUNCT_NEED_SPACE})(?![\s\n])", r"\1 ", cleaned)
    return cleaned.strip()


def main() -> None:
    sample = "翻译  记忆库,,, 需要  定期更新!!\n请注意  ：术语一致性。"
    print("原始文本:\n", sample)
    print("\n清理后:\n", clean_text(sample))


if __name__ == "__main__":
    main()
