#!/usr/bin/env python3
"""Generate translation-focused practice prompts and answers for chapters 01-10."""
from __future__ import annotations

import ast
import itertools
from pathlib import Path
from textwrap import dedent

CHAPTERS = [f"chapter_{i:02d}" for i in range(1, 11)]
OUTPUT_PATH = Path("learning_resources") / "chapters_01-10_practice.md"

STRING_KEYWORDS = {
    "client": "TransGlobe",
    "project": "marketing localization",
    "language_pair": "EN->ZH",
    "translator": "Chen Yu",
    "reviewer": "Li Na",
    "deadline": "2024-09-30",
    "tool": "SmartCAT",
    "workflow": "QA review",
    "team": "Asia Delivery Squad",
}

INT_KEYWORDS = {
    "count": 2500,
    "number": 3,
    "years": 5,
    "age": 28,
    "hours": 6,
    "rate": 0.12,
    "score": 95,
    "words": 3200,
    "pages": 12,
}

BOOL_KEYWORDS = {
    "include": True,
    "allow": True,
    "is": True,
    "has": True,
    "use": True,
}

DEFAULT_STRING = "示例信息"
DEFAULT_NUMBER = 2
DEFAULT_BOOL = True

def count_non_empty_lines(text: str) -> int:
    return sum(1 for line in text.splitlines() if line.strip() and not line.lstrip().startswith("#"))


def safe_unparse(node: ast.AST) -> str:
    try:
        return ast.unparse(node)
    except Exception:  # pragma: no cover - defensive
        return "..."


def sample_value(name: str) -> str:
    lower = name.lower()
    for key, value in STRING_KEYWORDS.items():
        if key in lower:
            return repr(value)
    for key, value in INT_KEYWORDS.items():
        if key in lower:
            return repr(value)
    for key, value in BOOL_KEYWORDS.items():
        if key in lower:
            return repr(value)
    if any(token in lower for token in ("count", "number", "total", "words", "pages", "hours", "years", "age")):
        return repr(DEFAULT_NUMBER)
    if any(token in lower for token in ("rate", "ratio", "score", "percent")):
        return repr(DEFAULT_NUMBER)
    if lower.startswith("is_") or lower.startswith("has_"):
        return repr(DEFAULT_BOOL)
    return repr(DEFAULT_STRING)


def build_markdown_section(relative_path: str, tasks: list[str], solution_code: str) -> str:
    cleaned_solution = solution_code.strip("\n")
    lines: list[str] = [f"### `{relative_path}`", "", "**练习**"]
    for index, task in enumerate(tasks, 1):
        lines.append(f"{index}. {task}")
    lines.extend(["", "**参考答案**", "```python"])
    if cleaned_solution:
        lines.extend(cleaned_solution.splitlines())
    lines.append("```")
    return "\n".join(lines)


def build_list_solution(code: str, var_name: str) -> str:
    extension = dedent(
        f"""
        extra_resources = ['术语云平台', '翻译记忆体检查']
        extended_{var_name} = list({var_name}) + extra_resources
        for item in extended_{var_name}:
            print(f"准备评估 {{item}} 在翻译项目中的应用。")
        """
    ).strip()
    return f"{code.strip()}\n\n{extension}"


def build_dict_solution(code: str, var_name: str) -> str:
    extension = dedent(
        f"""
        extended_{var_name} = {var_name}.copy()
        extended_{var_name}['术语库'] = '集中维护客户批准的关键词'
        extended_{var_name}['审校说明'] = '与审校团队共享 QA 要点'
        for key, value in extended_{var_name}.items():
            print(f"{{key}} -> {{value}}")
        """
    ).strip()
    return f"{code.strip()}\n\n{extension}"


def build_function_solution(module_path: str, func: ast.FunctionDef) -> tuple[str, str]:
    args = [arg.arg for arg in func.args.args]
    defaults_count = len(func.args.defaults)
    required_args = args[: len(args) - defaults_count] if defaults_count else list(args)
    optional_args = args[len(args) - defaults_count :] if defaults_count else []

    call_args = []
    for name in required_args:
        if name == "self":
            continue
        call_args.append(sample_value(name))

    call_lines = []
    call_repr = f"{func.name}({', '.join(call_args)})" if call_args else f"{func.name}()"
    call_lines.append(f"result = {call_repr}")
    for name in optional_args:
        if name == "self":
            continue
        call_lines.append(
            f"print({func.name}({', '.join(call_args + [f'{name}={sample_value(name)}'])}))"
        )

    solution = dedent(
        f"""
        from {module_path} import {func.name}

        {call_lines[0]}
        print(result)
        """
    ).strip()
    if len(call_lines) > 1:
        solution += "\n" + "\n".join(call_lines[1:])
    return solution, required_args


def build_class_solution(module_path: str, cls: ast.ClassDef, code: str) -> str:
    init_func = None
    for node in cls.body:
        if isinstance(node, ast.FunctionDef) and node.name == "__init__":
            init_func = node
            break

    call_args: list[str] = []
    call_kwargs: list[str] = []
    if init_func:
        args = [arg.arg for arg in init_func.args.args][1:]  # skip self
        defaults_count = len(init_func.args.defaults)
        required_args = args[: len(args) - defaults_count] if defaults_count else list(args)
        optional_args = args[len(args) - defaults_count :] if defaults_count else []

        for name in required_args:
            call_args.append(sample_value(name))
        for name in optional_args:
            call_kwargs.append(f"{name}={sample_value(name)}")

    joined_args = ", ".join(itertools.chain(call_args, call_kwargs))
    instantiation = f"{cls.name}({joined_args})" if joined_args else f"{cls.name}()"

    methods = [
        node for node in cls.body if isinstance(node, ast.FunctionDef) and node.name not in {"__init__"}
    ]
    method_calls = []
    for method in methods:
        method_args = [arg.arg for arg in method.args.args][1:]  # skip self
        required_count = len(method_args) - len(method.args.defaults)
        if required_count <= 0 and not method.args.vararg and not method.args.kwonlyargs:
            method_calls.append(f"example.{method.name}()")
            break

    extension = dedent(
        f"""
        from {module_path} import {cls.name}

        example = {instantiation}
        print(vars(example))
        """
    ).strip()
    if method_calls:
        extension += "\n" + "\n".join(method_calls)
    return extension


def build_error_solution(code: str) -> str:
    return dedent(
        """
        # 这段代码原本用来演示语法错误。以下示例提供了一个正确的结构供对照：
        magicians = ['术语负责人', '审校专家', '语言技术顾问']
        for magician in magicians:
            print(f"确认 {magician} 的任务已准备好。")

        print("根据报错信息调整原脚本的缩进或标点，让它恢复如上所示的结构。")
        """
    ).strip()


def render_entry(relative_path: str, code: str) -> str | None:
    if count_non_empty_lines(code) <= 3:
        return None

    try:
        tree = ast.parse(code)
    except SyntaxError:
        return build_markdown_section(
            relative_path,
            ["识别并修复示例中的语法问题，让脚本能够正常运行。", "用注释记录你修复错误时总结的经验。"],
            build_error_solution(code),
        )

    first_list = None
    first_dict = None
    first_function = None
    first_class = None

    for node in tree.body:
        if isinstance(node, ast.Assign):
            target = node.targets[0]
            if isinstance(target, ast.Name):
                if isinstance(node.value, ast.List) and first_list is None:
                    first_list = target.id, node.value
                elif isinstance(node.value, ast.Dict) and first_dict is None:
                    first_dict = target.id, node.value
        elif isinstance(node, ast.FunctionDef) and first_function is None:
            first_function = node
        elif isinstance(node, ast.ClassDef) and first_class is None:
            first_class = node

    module_path = relative_path[:-3].replace("/", ".")

    if first_class is not None:
        extension_code = build_class_solution(module_path, first_class, code)
        return build_markdown_section(
            relative_path,
            [
                f"参考 `{first_class.name}` 类，创建一个属于你自己的翻译案例实例。",
                "输出实例的主要属性，并尝试调用至少一个不需要额外参数的方法。",
            ],
            extension_code,
        )

    if first_function is not None:
        solution_code, required_args = build_function_solution(module_path, first_function)
        argument_note = "、".join(required_args) if required_args else "默认参数"
        return build_markdown_section(
            relative_path,
            [
                f"使用 `{first_function.name}` 函数模拟新的翻译场景输入。",
                f"观察返回结果或输出，并记录参数（例如：{argument_note}）。",
            ],
            solution_code,
        )

    if first_dict is not None:
        var_name, value = first_dict
        base_repr = safe_unparse(value)
        source_stub = f"{var_name} = {base_repr}\n"
        solution_code = build_dict_solution(source_stub, var_name)
        return build_markdown_section(
            relative_path,
            [
                f"复制 `{var_name}` 字典，并新增与翻译项目协作相关的键值对。",
                "循环输出最终字典，说明每条信息如何帮助项目推进。",
            ],
            solution_code,
        )

    if first_list is not None:
        var_name, value = first_list
        base_repr = safe_unparse(value)
        source_stub = f"{var_name} = {base_repr}\n"
        solution_code = build_list_solution(source_stub, var_name)
        return build_markdown_section(
            relative_path,
            [
                f"在 `{var_name}` 列表中补充两项新的语言服务资源。",
                "遍历扩展后的列表，为每个条目写一句使用计划。",
            ],
            solution_code,
        )

    generic_solution = f"{code.strip()}\n\nprint(\"\\n练习扩展：记录至少一条你在翻译项目中学到的新经验。\")"
    return build_markdown_section(
        relative_path,
        [
            "基于原脚本，加入额外的状态输出或日志，用于追踪翻译项目的进度。",
            "将扩展后的程序运行结果整理成文字说明，与同学分享。",
        ],
        generic_solution,
    )


def main() -> None:
    sections: list[str] = ["# 翻译方向 Python 练习题（章节 01-10）", ""]
    for chapter in CHAPTERS:
        sections.append(f"## {chapter.replace('_', ' ').title()}")
        chapter_entries = []
        for path in sorted(Path(chapter).rglob("*.py")):
            relative = path.as_posix()
            code = path.read_text(encoding="utf-8")
            entry = render_entry(relative, code)
            if entry:
                chapter_entries.append(entry)
        if chapter_entries:
            sections.extend(chapter_entries)
        else:
            sections.append("（本章示例过短，无需额外练习。）")
        sections.append("")

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text("\n".join(sections), encoding="utf-8")


if __name__ == "__main__":
    main()
