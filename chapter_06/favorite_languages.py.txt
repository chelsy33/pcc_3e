# 知识点：遍历键与值，统计团队常用的编程语言。

favorite_specializations = {
    'li': 'medical',
    'chen': 'legal',
    'maria': 'marketing',
    'david': 'software localization',
}

for translator, focus in favorite_specializations.items():
    print(f"{translator.title()} enjoys {focus} projects.")
