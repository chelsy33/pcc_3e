# 知识点：以写模式打开文件，并将多行文本写入其中。

from pathlib import Path

path = Path('project_notes.txt')
path.write_text("Translation sprint notes.\nRemember to verify legal terminology.")
