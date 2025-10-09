# 知识点：综合使用 if-elif-else 判定票价逻辑，模拟客户分级。

age = 24

if age < 18:
    price = 0
elif age < 60:
    price = 200
else:
    price = 120

print(f"Conference registration fee: ¥{price}")
