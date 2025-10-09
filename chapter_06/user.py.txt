# 知识点：在字典中嵌套字典，记录多名用户的详细信息。

translator = {
    'username': 'mtran',
    'first': 'mei',
    'last': 'tran',
    'specialization': 'financial reports',
}

for key, value in translator.items():
    print(f"{key.title()}: {value}")
