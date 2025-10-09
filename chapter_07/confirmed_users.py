# 知识点：通过 while 循环与列表操作跟踪待确认与已确认用户。

unconfirmed_translators = ['li wen', 'chen yu', 'maria gonzalez']
confirmed_translators = []

while unconfirmed_translators:
    translator = unconfirmed_translators.pop()
    print(f"Verifying CAT tool setup for {translator.title()}...")
    confirmed_translators.append(translator)

print("\nConfirmed translators:")
for translator in confirmed_translators:
    print(f"- {translator.title()}")
