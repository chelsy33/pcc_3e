# 第十一章：正则表达式与翻译文本清洗

> 适配《Python 编程：从入门到实践》第三版翻译技术路线

## 1. 为什么翻译专业学生要学正则表达式？

翻译项目中，经常要处理来自不同客户、不同格式的双语文本：CAT 工具导出的记忆库、PDF 转换的 TXT、字幕脚本等。正则表达式（Regular Expression，简称 **regex**）是一套描述文本模式的“搜索语言”，能帮助你：

- 快速定位批注、标签或术语占位符，减少手动查找的时间。
- 统一数字、空格、标点等格式，为术语提取和记忆库导入做好清洗准备。
- 根据客户风格指南，批量检查译文是否包含禁止词或需要替换的表达。

本章将基于 [菜鸟教程：Python 正则表达式](https://www.runoob.com/python/python-reg-expressions.html) 的核心知识，并结合翻译工作流程进行改写。阅读完成后，你可以写出自己的“Regex Cleaner”工具，清理文本中的噪音，为 CAT 工具交付高质量语料。

## 2. 正则表达式的基础语法

正则表达式通过“元字符”和“量词”描述匹配模式。下表列出常用符号，并附上翻译场景中的例子。

| 元字符 | 含义 | 翻译场景示例 |
| --- | --- | --- |
| `.` | 匹配除换行符以外的任意单个字符 | 找出“CAT”后接任意一个字符的缩写，如 `CAT.` `CAT3` |
| `[]` | 字符集，匹配方括号中的任意一个字符 | `file[0-9]` 捕获 `file1`、`file2` 等文件标签 |
| `[^ ]` | 否定字符集，匹配除括号内字符以外的字符 | `[^A-Za-z]` 用于定位非英文字符，例如多余的空格或中文符号 |
| `^` | 匹配字符串开头 | `^\d+` 检查段落是否以数字编号开始 |
| `$` | 匹配字符串结尾 | `。$` 检查句子是否以全角句号结尾 |
| `*` | 匹配前一个字符 0 次或多次 | `\s*` 捕捉可选的空白符 |
| `+` | 匹配前一个字符 1 次或多次 | `,+` 合并重复的逗号 |
| `?` | 匹配前一个字符 0 次或 1 次（或非贪婪修饰符） | `颜色\s?：` 接受“颜色：”和“颜色 ：” |
| `{m}` | 精确匹配 `m` 次 | `\d{4}` 查找年份 |
| `{m,n}` | 匹配 `m` 到 `n` 次 | `\d{2,3}` 抓取 2~3 位数字，例如页码 |
| `|` | 逻辑或 | `(memo|TM)` 匹配“memo”或“TM” |
| `()` | 分组，并可在替换中引用 | `(?P<term>\b[A-Z]{2,}\b)` 捕获术语并命名为 `term` |

### 2.1 常用转义字符

| 转义符 | 说明 | 翻译场景 |
| --- | --- | --- |
| `\d` | 数字，等价于 `[0-9]` | 检查是否包含数字编号 |
| `\D` | 非数字 | 找出不应出现数字的字段 |
| `\s` | 空白（空格、制表符、换行） | 合并多余空白、清理换行 |
| `\S` | 非空白 | 检查是否存在非空字符 |
| `\w` | 单词字符（字母、数字、下划线） | 匹配英文单词或变量 |
| `\W` | 非单词字符 | 定位特殊符号 |

在 Python 字符串中书写正则表达式时，建议使用原始字符串语法 `r''`，可以避免反斜杠的二次转义。

```python
pattern = r"\bTM\d{3}\b"  # 匹配 TM 后跟三位数字的术语代码
```

## 3. Python `re` 模块概览

Python 内置的 `re` 模块提供了多种方法来执行正则匹配：

| 函数 | 说明 | 翻译场景 |
| --- | --- | --- |
| `re.match(pattern, string)` | 仅在字符串开头尝试匹配 | 检查段落是否以术语标签开头 |
| `re.search(pattern, string)` | 搜索并返回第一处匹配 | 在译文中查找第一处禁止词 |
| `re.findall(pattern, string)` | 返回所有匹配的列表 | 提取术语或标签列表 |
| `re.finditer(pattern, string)` | 返回可迭代的匹配对象 | 逐个遍历匹配位置进行批注 |
| `re.sub(pattern, repl, string)` | 替换匹配内容 | 统一标点、空格等格式 |
| `re.split(pattern, string)` | 按匹配模式拆分字符串 | 拆分混合字段，例如 `key:value` 列表 |

许多翻译项目会重复使用同一套正则，可提前编译以提升性能：

```python
import re

term_pattern = re.compile(r"\b[A-Z]{2,}(?:\s[A-Z]{2,})?\b")
for sentence in sentences:
    matches = term_pattern.findall(sentence)
    # 将结果发送到术语检查流程
```

## 4. 翻译工作中的高频模式

### 4.1 清理多余空格

- 模式：`\s{2,}`
- 用途：将多个空格替换为一个，保持译文整洁。
- 代码：`re.sub(r"\s{2,}", " ", text)`

### 4.2 合并重复标点

- 模式：`([！？?!。，,.])\1+`
- 用途：把连续重复的中英标点合并成一个，避免语料噪音。

### 4.3 提取术语或标签

- 模式：`\[[A-Z_]+\]`
- 用途：捕获类似 `[PLACEHOLDER]` 的标签，提醒译者保持不变。

### 4.4 识别全角与半角混用

- 模式：`[\uff01-\uff5e]`
- 用途：找出全角标点，统一成半角或符合客户要求的形式。

### 4.5 匹配英中混排数字

- 模式：`(?<=\d)(?=\D)|(?<=\D)(?=\d)`
- 用途：在数字与文字之间自动加入空格，例如 `2023年` → `2023 年`，以便 CAT 工具识别数值。

## 5. 处理翻译项目中的文本

下面示例演示如何在 Python 中组合多个正则，完成一次“轻量清洗”。

```python
import re

text = "本项目  包含多个  文件!!! 请在CAT工具中-仔细检查。。"

cleaned = re.sub(r"\s{2,}", " ", text)          # 合并多余空格
cleaned = re.sub(r"([！？?!。，,.])\1+", r"\1", cleaned)  # 合并重复标点
cleaned = re.sub(r"\s?([,.;!?])", r"\1", cleaned)      # 去掉标点前空格
cleaned = re.sub(r"([,.;!?])([^ \n])", r"\1 \2", cleaned)  # 标点后补空格

print(cleaned)
# 输出：本项目 包含多个 文件! 请在CAT工具中-仔细检查。
```

## 6. 练习：翻译场景下的正则应用

1. **术语保护**：编写正则，查找所有形如 `{{TERM}}` 的术语标签，并验证译文中是否完整保留。
2. **日期格式统一**：把 `2023-5-7`、`2023/05/07` 等日期转换成 `2023-05-07`。
3. **中英文空格调整**：为英文单词与中文字符之间自动添加空格，例如 `翻译memory` → `翻译 memory`。
4. **括号内容检查**：找出所有括号内的注释 `(注：...)`，导出单独文件供项目经理审阅。

## 7. Regex Cleaner v1：快速文本洁净器

第一版侧重“所见即所得”，适合初学者手动粘贴文本快速处理。

```python
# tools/regex_cleaner_v1.py
import re

PUNCTUATION_CLASS = "[！？?!。，,.：:；;]"
PUNCT_NEED_SPACE = "[,.;!?。！？]"


def clean_text(text: str) -> str:
    """清理多余空格与重复标点，适合翻译前的简单预处理。"""
    cleaned = re.sub(r"\s+", " ", text)  # 把任意空白缩成一个空格
    cleaned = re.sub(fr"({PUNCTUATION_CLASS})\1+", r"\1", cleaned)  # 合并重复标点
    cleaned = re.sub(fr"\s*({PUNCTUATION_CLASS})", r"\1", cleaned)  # 标点前去空格
    cleaned = re.sub(fr"({PUNCT_NEED_SPACE})(?![\s\n])", r"\1 ", cleaned)  # 标点后补空格
    return cleaned.strip()


if __name__ == "__main__":
    sample = "翻译  记忆库,,, 需要  定期更新!!\n请注意  ：术语一致性。"
    print("原始文本:\n", sample)
    print("\n清理后:\n", clean_text(sample))
```

运行脚本后，你可以把输出复制回 CAT 工具或发给同伴复核。

## 8. Regex Cleaner Tool 完善版：批量清洗助手

完善版在第一版基础上加入以下功能：

- **命令行接口**：支持 `--text` 直接处理一段文本，或 `--input` 指向单个文件。
- **批处理模式**：指定 `--input-dir` 目录，脚本自动读取其中的 `.txt` 文件，输出到 `cleaned/` 子目录。
- **翻译友好日志**：展示处理的文件数量与路径，便于团队追踪。

```python
# tools/regex_cleaner_tool.py
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
    """对翻译文本做常见清洗：空格、重复标点和标点后的空格。"""
    cleaned = WHITESPACE_PATTERN.sub(" ", text)
    cleaned = PUNCT_PATTERN.sub(r"\1", cleaned)
    cleaned = TRAILING_SPACE_PATTERN.sub(r"\1", cleaned)
    cleaned = PUNCT_FOLLOW_PATTERN.sub(r"\1 ", cleaned)
    return cleaned.strip()


def iter_txt_files(folder: pathlib.Path) -> Iterable[pathlib.Path]:
    for path in sorted(folder.glob("*.txt")):
        if path.is_file():
            yield path


def process_file(path: pathlib.Path, output_dir: pathlib.Path) -> pathlib.Path:
    cleaned_text = clean_text(path.read_text(encoding="utf-8"))
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / f"{path.stem}_cleaned.txt"
    output_path.write_text(cleaned_text, encoding="utf-8")
    return output_path


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Regex Cleaner Tool：为翻译项目批量清洗 TXT 文本"
    )
    parser.add_argument("--text", help="直接清洗一段文本", default=None)
    parser.add_argument("--input", type=pathlib.Path, help="单个 TXT 文件路径", default=None)
    parser.add_argument(
        "--input-dir",
        type=pathlib.Path,
        help="包含多个 TXT 文件的文件夹，将在 cleaned/ 子目录生成结果",
        default=None,
    )
    parser.add_argument(
        "--output",
        type=pathlib.Path,
        help="输出文件路径；若不提供，将在原文件旁生成 *_cleaned.txt",
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
```

## 9. 后续扩展建议

- 将清洗规则改写为可配置的 YAML/JSON，便于团队根据客户规范调整。
- 加入术语表对照功能：利用正则捕获术语后与官方译法比对。
- 将脚本封装成 GUI 或 VS Code 扩展，降低非技术译者的使用门槛。

通过本章，你已经学习了正则表达式的核心概念，并基于翻译业务场景构建了两个清洗工具。将它们集成到你的翻译流程中，可以显著提升术语一致性和文本规范性。
