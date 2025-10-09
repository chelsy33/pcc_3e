# 知识点：结合条件判断与布尔值，决定译员是否能参与评审。

preferred_tool = 'memoq'

if preferred_tool == 'trados':
    print("Assign the project in Trados Studio.")
elif preferred_tool == 'memoq':
    print("Set up the project in memoQ.")
else:
    print("Confirm the tool setup with the translator.")
