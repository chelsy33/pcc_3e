# 翻译方向 Python 练习题（章节 01-10）

## Chapter 01
（本章示例过短，无需额外练习。）

## Chapter 02
### `chapter_02/full_name.py`

**练习**
1. 基于原脚本，加入额外的状态输出或日志，用于追踪翻译项目的进度。
2. 将扩展后的程序运行结果整理成文字说明，与同学分享。

**参考答案**
```python
first_name = "li"
last_name = "wen"
full_name = f"{first_name} {last_name}"
print(full_name.title())

print("\n练习扩展：记录至少一条你在翻译项目中学到的新经验。")
```
### `chapter_02/full_name_2.py`

**练习**
1. 基于原脚本，加入额外的状态输出或日志，用于追踪翻译项目的进度。
2. 将扩展后的程序运行结果整理成文字说明，与同学分享。

**参考答案**
```python
first_name = "li"
last_name = "wen"
full_name = f"{first_name} {last_name}"
print(f"Hello, Translator {full_name.title()}!")

print("\n练习扩展：记录至少一条你在翻译项目中学到的新经验。")
```
### `chapter_02/full_name_3.py`

**练习**
1. 基于原脚本，加入额外的状态输出或日志，用于追踪翻译项目的进度。
2. 将扩展后的程序运行结果整理成文字说明，与同学分享。

**参考答案**
```python
first_name = "li"
last_name = "wen"
full_name = f"{first_name} {last_name}"
message = f"Translator {full_name.title()}, your CAT tool is ready."
print(message)

print("\n练习扩展：记录至少一条你在翻译项目中学到的新经验。")
```
### `chapter_02/hello_world_variables_2.py`

**练习**
1. 基于原脚本，加入额外的状态输出或日志，用于追踪翻译项目的进度。
2. 将扩展后的程序运行结果整理成文字说明，与同学分享。

**参考答案**
```python
message = "Python 能帮助我们管理翻译项目。"
print(message)

message = "让我们一起构建翻译自动化工具！"
print(message)

print("\n练习扩展：记录至少一条你在翻译项目中学到的新经验。")
```

## Chapter 03
### `chapter_03/cars.py`

**练习**
1. 在 `glossaries` 列表中补充两项新的语言服务资源。
2. 遍历扩展后的列表，为每个条目写一句使用计划。

**参考答案**
```python
glossaries = ['legal glossary', 'medical glossary', 'technical glossary', 'marketing glossary']

extra_resources = ['术语云平台', '翻译记忆体检查']
extended_glossaries = list(glossaries) + extra_resources
for item in extended_glossaries:
    print(f"准备评估 {item} 在翻译项目中的应用。")
```
### `chapter_03/motorcycles.py`

**练习**
1. 在 `translation_requests` 列表中补充两项新的语言服务资源。
2. 遍历扩展后的列表，为每个条目写一句使用计划。

**参考答案**
```python
translation_requests = ['software manual', 'tourism brochure', 'research abstract', 'overnight legal brief']

extra_resources = ['术语云平台', '翻译记忆体检查']
extended_translation_requests = list(translation_requests) + extra_resources
for item in extended_translation_requests:
    print(f"准备评估 {item} 在翻译项目中的应用。")
```
### `chapter_03/partial_programs/cars_2_sorted.py`

**练习**
1. 在 `cars` 列表中补充两项新的语言服务资源。
2. 遍历扩展后的列表，为每个条目写一句使用计划。

**参考答案**
```python
cars = ['bmw', 'audi', 'toyota', 'subaru']

extra_resources = ['术语云平台', '翻译记忆体检查']
extended_cars = list(cars) + extra_resources
for item in extended_cars:
    print(f"准备评估 {item} 在翻译项目中的应用。")
```
### `chapter_03/partial_programs/cars_3_reverse_order.py`

**练习**
1. 在 `cars` 列表中补充两项新的语言服务资源。
2. 遍历扩展后的列表，为每个条目写一句使用计划。

**参考答案**
```python
cars = ['bmw', 'audi', 'toyota', 'subaru']

extra_resources = ['术语云平台', '翻译记忆体检查']
extended_cars = list(cars) + extra_resources
for item in extended_cars:
    print(f"准备评估 {item} 在翻译项目中的应用。")
```
### `chapter_03/partial_programs/motorcycles_0_first_version.py`

**练习**
1. 在 `motorcycles` 列表中补充两项新的语言服务资源。
2. 遍历扩展后的列表，为每个条目写一句使用计划。

**参考答案**
```python
motorcycles = ['honda', 'yamaha', 'suzuki']

extra_resources = ['术语云平台', '翻译记忆体检查']
extended_motorcycles = list(motorcycles) + extra_resources
for item in extended_motorcycles:
    print(f"准备评估 {item} 在翻译项目中的应用。")
```
### `chapter_03/partial_programs/motorcycles_10_use_value.py`

**练习**
1. 在 `motorcycles` 列表中补充两项新的语言服务资源。
2. 遍历扩展后的列表，为每个条目写一句使用计划。

**参考答案**
```python
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']

extra_resources = ['术语云平台', '翻译记忆体检查']
extended_motorcycles = list(motorcycles) + extra_resources
for item in extended_motorcycles:
    print(f"准备评估 {item} 在翻译项目中的应用。")
```
### `chapter_03/partial_programs/motorcycles_1_appending.py`

**练习**
1. 在 `motorcycles` 列表中补充两项新的语言服务资源。
2. 遍历扩展后的列表，为每个条目写一句使用计划。

**参考答案**
```python
motorcycles = ['honda', 'yamaha', 'suzuki']

extra_resources = ['术语云平台', '翻译记忆体检查']
extended_motorcycles = list(motorcycles) + extra_resources
for item in extended_motorcycles:
    print(f"准备评估 {item} 在翻译项目中的应用。")
```
### `chapter_03/partial_programs/motorcycles_2_starting_empty.py`

**练习**
1. 在 `motorcycles` 列表中补充两项新的语言服务资源。
2. 遍历扩展后的列表，为每个条目写一句使用计划。

**参考答案**
```python
motorcycles = []

extra_resources = ['术语云平台', '翻译记忆体检查']
extended_motorcycles = list(motorcycles) + extra_resources
for item in extended_motorcycles:
    print(f"准备评估 {item} 在翻译项目中的应用。")
```
### `chapter_03/partial_programs/motorcycles_4_removing_elements.py`

**练习**
1. 在 `motorcycles` 列表中补充两项新的语言服务资源。
2. 遍历扩展后的列表，为每个条目写一句使用计划。

**参考答案**
```python
motorcycles = ['honda', 'yamaha', 'suzuki']

extra_resources = ['术语云平台', '翻译记忆体检查']
extended_motorcycles = list(motorcycles) + extra_resources
for item in extended_motorcycles:
    print(f"准备评估 {item} 在翻译项目中的应用。")
```
### `chapter_03/partial_programs/motorcycles_5_remove_second_item.py`

**练习**
1. 在 `motorcycles` 列表中补充两项新的语言服务资源。
2. 遍历扩展后的列表，为每个条目写一句使用计划。

**参考答案**
```python
motorcycles = ['honda', 'yamaha', 'suzuki']

extra_resources = ['术语云平台', '翻译记忆体检查']
extended_motorcycles = list(motorcycles) + extra_resources
for item in extended_motorcycles:
    print(f"准备评估 {item} 在翻译项目中的应用。")
```
### `chapter_03/partial_programs/motorcycles_6_pop.py`

**练习**
1. 在 `motorcycles` 列表中补充两项新的语言服务资源。
2. 遍历扩展后的列表，为每个条目写一句使用计划。

**参考答案**
```python
motorcycles = ['honda', 'yamaha', 'suzuki']

extra_resources = ['术语云平台', '翻译记忆体检查']
extended_motorcycles = list(motorcycles) + extra_resources
for item in extended_motorcycles:
    print(f"准备评估 {item} 在翻译项目中的应用。")
```
### `chapter_03/partial_programs/motorcycles_9_removing_item_by_value.py`

**练习**
1. 在 `motorcycles` 列表中补充两项新的语言服务资源。
2. 遍历扩展后的列表，为每个条目写一句使用计划。

**参考答案**
```python
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']

extra_resources = ['术语云平台', '翻译记忆体检查']
extended_motorcycles = list(motorcycles) + extra_resources
for item in extended_motorcycles:
    print(f"准备评估 {item} 在翻译项目中的应用。")
```

## Chapter 04
### `chapter_04/dimensions.py`

**练习**
1. 基于原脚本，加入额外的状态输出或日志，用于追踪翻译项目的进度。
2. 将扩展后的程序运行结果整理成文字说明，与同学分享。

**参考答案**
```python
deadlines = (2, 5)
print("Original turnaround windows:")
for days in deadlines:
    print(f"- {days} day(s) for standard translation")

print("\nUpdated turnaround windows:")
deadlines = (2, 3)
for days in deadlines:
    print(f"- {days} day(s) for urgent projects")

print("\n练习扩展：记录至少一条你在翻译项目中学到的新经验。")
```
### `chapter_04/foods.py`

**练习**
1. 在 `cat_glossaries` 列表中补充两项新的语言服务资源。
2. 遍历扩展后的列表，为每个条目写一句使用计划。

**参考答案**
```python
cat_glossaries = ['legal terms', 'medical terminology', 'software UI strings', 'marketing slogans']

extra_resources = ['术语云平台', '翻译记忆体检查']
extended_cat_glossaries = list(cat_glossaries) + extra_resources
for item in extended_cat_glossaries:
    print(f"准备评估 {item} 在翻译项目中的应用。")
```
### `chapter_04/magicians.py`

**练习**
1. 在 `translators` 列表中补充两项新的语言服务资源。
2. 遍历扩展后的列表，为每个条目写一句使用计划。

**参考答案**
```python
translators = ['li wen', 'chen yu', 'maria gonzalez']

extra_resources = ['术语云平台', '翻译记忆体检查']
extended_translators = list(translators) + extra_resources
for item in extended_translators:
    print(f"准备评估 {item} 在翻译项目中的应用。")
```
### `chapter_04/partial_programs/dimensions_3_writing_over_tuple.py`

**练习**
1. 基于原脚本，加入额外的状态输出或日志，用于追踪翻译项目的进度。
2. 将扩展后的程序运行结果整理成文字说明，与同学分享。

**参考答案**
```python
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

print("\n练习扩展：记录至少一条你在翻译项目中学到的新经验。")
```
### `chapter_04/partial_programs/foods_0_first_version.py`

**练习**
1. 在 `my_foods` 列表中补充两项新的语言服务资源。
2. 遍历扩展后的列表，为每个条目写一句使用计划。

**参考答案**
```python
my_foods = ['pizza', 'falafel', 'carrot cake']

extra_resources = ['术语云平台', '翻译记忆体检查']
extended_my_foods = list(my_foods) + extra_resources
for item in extended_my_foods:
    print(f"准备评估 {item} 在翻译项目中的应用。")
```
### `chapter_04/partial_programs/foods_1_new_foods.py`

**练习**
1. 在 `my_foods` 列表中补充两项新的语言服务资源。
2. 遍历扩展后的列表，为每个条目写一句使用计划。

**参考答案**
```python
my_foods = ['pizza', 'falafel', 'carrot cake']

extra_resources = ['术语云平台', '翻译记忆体检查']
extended_my_foods = list(my_foods) + extra_resources
for item in extended_my_foods:
    print(f"准备评估 {item} 在翻译项目中的应用。")
```
### `chapter_04/partial_programs/foods_2_incorrect_approach.py`

**练习**
1. 在 `my_foods` 列表中补充两项新的语言服务资源。
2. 遍历扩展后的列表，为每个条目写一句使用计划。

**参考答案**
```python
my_foods = ['pizza', 'falafel', 'carrot cake']

extra_resources = ['术语云平台', '翻译记忆体检查']
extended_my_foods = list(my_foods) + extra_resources
for item in extended_my_foods:
    print(f"准备评估 {item} 在翻译项目中的应用。")
```
### `chapter_04/partial_programs/magicians_2_next_trick.py`

**练习**
1. 在 `magicians` 列表中补充两项新的语言服务资源。
2. 遍历扩展后的列表，为每个条目写一句使用计划。

**参考答案**
```python
magicians = ['alice', 'david', 'carolina']

extra_resources = ['术语云平台', '翻译记忆体检查']
extended_magicians = list(magicians) + extra_resources
for item in extended_magicians:
    print(f"准备评估 {item} 在翻译项目中的应用。")
```
### `chapter_04/partial_programs/magicians_3_great_show.py`

**练习**
1. 在 `magicians` 列表中补充两项新的语言服务资源。
2. 遍历扩展后的列表，为每个条目写一句使用计划。

**参考答案**
```python
magicians = ['alice', 'david', 'carolina']

extra_resources = ['术语云平台', '翻译记忆体检查']
extended_magicians = list(magicians) + extra_resources
for item in extended_magicians:
    print(f"准备评估 {item} 在翻译项目中的应用。")
```
### `chapter_04/partial_programs/magicians_5_errors_forgetting_to_indent_additional_lines.py`

**练习**
1. 在 `magicians` 列表中补充两项新的语言服务资源。
2. 遍历扩展后的列表，为每个条目写一句使用计划。

**参考答案**
```python
magicians = ['alice', 'david', 'carolina']

extra_resources = ['术语云平台', '翻译记忆体检查']
extended_magicians = list(magicians) + extra_resources
for item in extended_magicians:
    print(f"准备评估 {item} 在翻译项目中的应用。")
```
### `chapter_04/partial_programs/magicians_6_errors_indenting_unnecessarily_after_loop.py`

**练习**
1. 在 `magicians` 列表中补充两项新的语言服务资源。
2. 遍历扩展后的列表，为每个条目写一句使用计划。

**参考答案**
```python
magicians = ['alice', 'david', 'carolina']

extra_resources = ['术语云平台', '翻译记忆体检查']
extended_magicians = list(magicians) + extra_resources
for item in extended_magicians:
    print(f"准备评估 {item} 在翻译项目中的应用。")
```
### `chapter_04/partial_programs/players_5_looping_through_slice.py`

**练习**
1. 在 `players` 列表中补充两项新的语言服务资源。
2. 遍历扩展后的列表，为每个条目写一句使用计划。

**参考答案**
```python
players = ['charles', 'martina', 'michael', 'florence', 'eli']

extra_resources = ['术语云平台', '翻译记忆体检查']
extended_players = list(players) + extra_resources
for item in extended_players:
    print(f"准备评估 {item} 在翻译项目中的应用。")
```
### `chapter_04/partial_programs/square_numbers_0_first_version.py`

**练习**
1. 在 `squares` 列表中补充两项新的语言服务资源。
2. 遍历扩展后的列表，为每个条目写一句使用计划。

**参考答案**
```python
squares = []

extra_resources = ['术语云平台', '翻译记忆体检查']
extended_squares = list(squares) + extra_resources
for item in extended_squares:
    print(f"准备评估 {item} 在翻译项目中的应用。")
```
### `chapter_04/partial_programs/square_numbers_1_shorter_loop.py`

**练习**
1. 在 `squares` 列表中补充两项新的语言服务资源。
2. 遍历扩展后的列表，为每个条目写一句使用计划。

**参考答案**
```python
squares = []

extra_resources = ['术语云平台', '翻译记忆体检查']
extended_squares = list(squares) + extra_resources
for item in extended_squares:
    print(f"准备评估 {item} 在翻译项目中的应用。")
```
### `chapter_04/players.py`

**练习**
1. 在 `team_members` 列表中补充两项新的语言服务资源。
2. 遍历扩展后的列表，为每个条目写一句使用计划。

**参考答案**
```python
team_members = ['project manager', 'lead translator', 'proofreader', 'terminologist']

extra_resources = ['术语云平台', '翻译记忆体检查']
extended_team_members = list(team_members) + extra_resources
for item in extended_team_members:
    print(f"准备评估 {item} 在翻译项目中的应用。")
```
### `chapter_04/squares.py`

**练习**
1. 在 `word_counts` 列表中补充两项新的语言服务资源。
2. 遍历扩展后的列表，为每个条目写一句使用计划。

**参考答案**
```python
word_counts = []

extra_resources = ['术语云平台', '翻译记忆体检查']
extended_word_counts = list(word_counts) + extra_resources
for item in extended_word_counts:
    print(f"准备评估 {item} 在翻译项目中的应用。")
```

## Chapter 05
### `chapter_05/amusement_park.py`

**练习**
1. 基于原脚本，加入额外的状态输出或日志，用于追踪翻译项目的进度。
2. 将扩展后的程序运行结果整理成文字说明，与同学分享。

**参考答案**
```python
age = 24

if age < 18:
    price = 0
elif age < 60:
    price = 200
else:
    price = 120

print(f"Conference registration fee: ¥{price}")

print("\n练习扩展：记录至少一条你在翻译项目中学到的新经验。")
```
### `chapter_05/banned_users.py`

**练习**
1. 在 `banned_clients` 列表中补充两项新的语言服务资源。
2. 遍历扩展后的列表，为每个条目写一句使用计划。

**参考答案**
```python
banned_clients = ['late payer', 'unrealistic deadline']

extra_resources = ['术语云平台', '翻译记忆体检查']
extended_banned_clients = list(banned_clients) + extra_resources
for item in extended_banned_clients:
    print(f"准备评估 {item} 在翻译项目中的应用。")
```
### `chapter_05/cars.py`

**练习**
1. 基于原脚本，加入额外的状态输出或日志，用于追踪翻译项目的进度。
2. 将扩展后的程序运行结果整理成文字说明，与同学分享。

**参考答案**
```python
assignment = 'medical manual'

if assignment == 'medical manual':
    print("Assign to translator with medical background.")
elif assignment == 'legal contract':
    print("Assign to translator with legal expertise.")
else:
    print("Assign to general translation team.")

print("\n练习扩展：记录至少一条你在翻译项目中学到的新经验。")
```
### `chapter_05/partial_programs/amusement_park_0_first_version.py`

**练习**
1. 基于原脚本，加入额外的状态输出或日志，用于追踪翻译项目的进度。
2. 将扩展后的程序运行结果整理成文字说明，与同学分享。

**参考答案**
```python
age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")

print("\n练习扩展：记录至少一条你在翻译项目中学到的新经验。")
```
### `chapter_05/partial_programs/amusement_park_1_price_only.py`

**练习**
1. 基于原脚本，加入额外的状态输出或日志，用于追踪翻译项目的进度。
2. 将扩展后的程序运行结果整理成文字说明，与同学分享。

**参考答案**
```python
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40

print(f"Your admission cost is ${price}.")

print("\n练习扩展：记录至少一条你在翻译项目中学到的新经验。")
```
### `chapter_05/partial_programs/amusement_park_2_multiple_elif.py`

**练习**
1. 基于原脚本，加入额外的状态输出或日志，用于追踪翻译项目的进度。
2. 将扩展后的程序运行结果整理成文字说明，与同学分享。

**参考答案**
```python
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20

print(f"Your admission cost is ${price}.")

print("\n练习扩展：记录至少一条你在翻译项目中学到的新经验。")
```
### `chapter_05/partial_programs/amusement_park_3_omitting_else.py`

**练习**
1. 基于原脚本，加入额外的状态输出或日志，用于追踪翻译项目的进度。
2. 将扩展后的程序运行结果整理成文字说明，与同学分享。

**参考答案**
```python
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20

print(f"Your admission cost is ${price}.")

print("\n练习扩展：记录至少一条你在翻译项目中学到的新经验。")
```
### `chapter_05/partial_programs/banned_users.py`

**练习**
1. 在 `banned_users` 列表中补充两项新的语言服务资源。
2. 遍历扩展后的列表，为每个条目写一句使用计划。

**参考答案**
```python
banned_users = ['andrew', 'carolina', 'david']

extra_resources = ['术语云平台', '翻译记忆体检查']
extended_banned_users = list(banned_users) + extra_resources
for item in extended_banned_users:
    print(f"准备评估 {item} 在翻译项目中的应用。")
```
### `chapter_05/partial_programs/cars.py`

**练习**
1. 在 `cars` 列表中补充两项新的语言服务资源。
2. 遍历扩展后的列表，为每个条目写一句使用计划。

**参考答案**
```python
cars = ['audi', 'bmw', 'subaru', 'toyota']

extra_resources = ['术语云平台', '翻译记忆体检查']
extended_cars = list(cars) + extra_resources
for item in extended_cars:
    print(f"准备评估 {item} 在翻译项目中的应用。")
```
### `chapter_05/partial_programs/toppings_1_multiple_conditions.py`

**练习**
1. 在 `requested_toppings` 列表中补充两项新的语言服务资源。
2. 遍历扩展后的列表，为每个条目写一句使用计划。

**参考答案**
```python
requested_toppings = ['mushrooms', 'extra cheese']

extra_resources = ['术语云平台', '翻译记忆体检查']
extended_requested_toppings = list(requested_toppings) + extra_resources
for item in extended_requested_toppings:
    print(f"准备评估 {item} 在翻译项目中的应用。")
```
### `chapter_05/partial_programs/toppings_2_checking_special_items.py`

**练习**
1. 在 `requested_toppings` 列表中补充两项新的语言服务资源。
2. 遍历扩展后的列表，为每个条目写一句使用计划。

**参考答案**
```python
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

extra_resources = ['术语云平台', '翻译记忆体检查']
extended_requested_toppings = list(requested_toppings) + extra_resources
for item in extended_requested_toppings:
    print(f"准备评估 {item} 在翻译项目中的应用。")
```
### `chapter_05/partial_programs/toppings_3_no_green_peppers.py`

**练习**
1. 在 `requested_toppings` 列表中补充两项新的语言服务资源。
2. 遍历扩展后的列表，为每个条目写一句使用计划。

**参考答案**
```python
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

extra_resources = ['术语云平台', '翻译记忆体检查']
extended_requested_toppings = list(requested_toppings) + extra_resources
for item in extended_requested_toppings:
    print(f"准备评估 {item} 在翻译项目中的应用。")
```
### `chapter_05/partial_programs/toppings_4_checking_list_not_empty.py`

**练习**
1. 在 `requested_toppings` 列表中补充两项新的语言服务资源。
2. 遍历扩展后的列表，为每个条目写一句使用计划。

**参考答案**
```python
requested_toppings = []

extra_resources = ['术语云平台', '翻译记忆体检查']
extended_requested_toppings = list(requested_toppings) + extra_resources
for item in extended_requested_toppings:
    print(f"准备评估 {item} 在翻译项目中的应用。")
```
### `chapter_05/partial_programs/toppings_5_multiple_lists.py`

**练习**
1. 在 `available_toppings` 列表中补充两项新的语言服务资源。
2. 遍历扩展后的列表，为每个条目写一句使用计划。

**参考答案**
```python
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']

extra_resources = ['术语云平台', '翻译记忆体检查']
extended_available_toppings = list(available_toppings) + extra_resources
for item in extended_available_toppings:
    print(f"准备评估 {item} 在翻译项目中的应用。")
```
### `chapter_05/partial_programs/voting_1_two_lines.py`

**练习**
1. 基于原脚本，加入额外的状态输出或日志，用于追踪翻译项目的进度。
2. 将扩展后的程序运行结果整理成文字说明，与同学分享。

**参考答案**
```python
age = 19
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")

print("\n练习扩展：记录至少一条你在翻译项目中学到的新经验。")
```
### `chapter_05/partial_programs/voting_2_if_else.py`

**练习**
1. 基于原脚本，加入额外的状态输出或日志，用于追踪翻译项目的进度。
2. 将扩展后的程序运行结果整理成文字说明，与同学分享。

**参考答案**
```python
age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")

print("\n练习扩展：记录至少一条你在翻译项目中学到的新经验。")
```
### `chapter_05/toppings.py`

**练习**
1. 在 `requested_keywords` 列表中补充两项新的语言服务资源。
2. 遍历扩展后的列表，为每个条目写一句使用计划。

**参考答案**
```python
requested_keywords = ['brand name consistency', 'legal disclaimer']

extra_resources = ['术语云平台', '翻译记忆体检查']
extended_requested_keywords = list(requested_keywords) + extra_resources
for item in extended_requested_keywords:
    print(f"准备评估 {item} 在翻译项目中的应用。")
```
### `chapter_05/voting.py`

**练习**
1. 基于原脚本，加入额外的状态输出或日志，用于追踪翻译项目的进度。
2. 将扩展后的程序运行结果整理成文字说明，与同学分享。

**参考答案**
```python
preferred_tool = 'memoq'

if preferred_tool == 'trados':
    print("Assign the project in Trados Studio.")
elif preferred_tool == 'memoq':
    print("Set up the project in memoQ.")
else:
    print("Confirm the tool setup with the translator.")

print("\n练习扩展：记录至少一条你在翻译项目中学到的新经验。")
```

## Chapter 06
### `chapter_06/alien.py`

**练习**
1. 复制 `project_brief` 字典，并新增与翻译项目协作相关的键值对。
2. 循环输出最终字典，说明每条信息如何帮助项目推进。

**参考答案**
```python
project_brief = {'language_pair': 'EN->ZH', 'word_count': 2500}

extended_project_brief = project_brief.copy()
extended_project_brief['术语库'] = '集中维护客户批准的关键词'
extended_project_brief['审校说明'] = '与审校团队共享 QA 要点'
for key, value in extended_project_brief.items():
    print(f"{key} -> {value}")
```
### `chapter_06/aliens.py`

**练习**
1. 在 `projects` 列表中补充两项新的语言服务资源。
2. 遍历扩展后的列表，为每个条目写一句使用计划。

**参考答案**
```python
projects = []

extra_resources = ['术语云平台', '翻译记忆体检查']
extended_projects = list(projects) + extra_resources
for item in extended_projects:
    print(f"准备评估 {item} 在翻译项目中的应用。")
```
### `chapter_06/favorite_languages.py`

**练习**
1. 复制 `favorite_specializations` 字典，并新增与翻译项目协作相关的键值对。
2. 循环输出最终字典，说明每条信息如何帮助项目推进。

**参考答案**
```python
favorite_specializations = {'li': 'medical', 'chen': 'legal', 'maria': 'marketing', 'david': 'software localization'}

extended_favorite_specializations = favorite_specializations.copy()
extended_favorite_specializations['术语库'] = '集中维护客户批准的关键词'
extended_favorite_specializations['审校说明'] = '与审校团队共享 QA 要点'
for key, value in extended_favorite_specializations.items():
    print(f"{key} -> {value}")
```
### `chapter_06/many_users.py`

**练习**
1. 复制 `translator_profiles` 字典，并新增与翻译项目协作相关的键值对。
2. 循环输出最终字典，说明每条信息如何帮助项目推进。

**参考答案**
```python
translator_profiles = {'lwen': {'first': 'li', 'last': 'wen', 'languages': ['English', 'Chinese']}, 'cchen': {'first': 'chen', 'last': 'yu', 'languages': ['English', 'Japanese']}}

extended_translator_profiles = translator_profiles.copy()
extended_translator_profiles['术语库'] = '集中维护客户批准的关键词'
extended_translator_profiles['审校说明'] = '与审校团队共享 QA 要点'
for key, value in extended_translator_profiles.items():
    print(f"{key} -> {value}")
```
### `chapter_06/partial_programs/alien_3_new_key_value_pairs.py`

**练习**
1. 复制 `alien_0` 字典，并新增与翻译项目协作相关的键值对。
2. 循环输出最终字典，说明每条信息如何帮助项目推进。

**参考答案**
```python
alien_0 = {'color': 'green', 'points': 5}

extended_alien_0 = alien_0.copy()
extended_alien_0['术语库'] = '集中维护客户批准的关键词'
extended_alien_0['审校说明'] = '与审校团队共享 QA 要点'
for key, value in extended_alien_0.items():
    print(f"{key} -> {value}")
```
### `chapter_06/partial_programs/alien_4_starting_empty.py`

**练习**
1. 复制 `alien_0` 字典，并新增与翻译项目协作相关的键值对。
2. 循环输出最终字典，说明每条信息如何帮助项目推进。

**参考答案**
```python
alien_0 = {}

extended_alien_0 = alien_0.copy()
extended_alien_0['术语库'] = '集中维护客户批准的关键词'
extended_alien_0['审校说明'] = '与审校团队共享 QA 要点'
for key, value in extended_alien_0.items():
    print(f"{key} -> {value}")
```
### `chapter_06/partial_programs/alien_5_modifying_values.py`

**练习**
1. 复制 `alien_0` 字典，并新增与翻译项目协作相关的键值对。
2. 循环输出最终字典，说明每条信息如何帮助项目推进。

**参考答案**
```python
alien_0 = {'color': 'green'}

extended_alien_0 = alien_0.copy()
extended_alien_0['术语库'] = '集中维护客户批准的关键词'
extended_alien_0['审校说明'] = '与审校团队共享 QA 要点'
for key, value in extended_alien_0.items():
    print(f"{key} -> {value}")
```
### `chapter_06/partial_programs/alien_6_track_position.py`

**练习**
1. 复制 `alien_0` 字典，并新增与翻译项目协作相关的键值对。
2. 循环输出最终字典，说明每条信息如何帮助项目推进。

**参考答案**
```python
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}

extended_alien_0 = alien_0.copy()
extended_alien_0['术语库'] = '集中维护客户批准的关键词'
extended_alien_0['审校说明'] = '与审校团队共享 QA 要点'
for key, value in extended_alien_0.items():
    print(f"{key} -> {value}")
```
### `chapter_06/partial_programs/alien_7_removing_key_value_pairs.py`

**练习**
1. 复制 `alien_0` 字典，并新增与翻译项目协作相关的键值对。
2. 循环输出最终字典，说明每条信息如何帮助项目推进。

**参考答案**
```python
alien_0 = {'color': 'green', 'points': 5}

extended_alien_0 = alien_0.copy()
extended_alien_0['术语库'] = '集中维护客户批准的关键词'
extended_alien_0['审校说明'] = '与审校团队共享 QA 要点'
for key, value in extended_alien_0.items():
    print(f"{key} -> {value}")
```
### `chapter_06/partial_programs/aliens_0_first_listing.py`

**练习**
1. 复制 `alien_0` 字典，并新增与翻译项目协作相关的键值对。
2. 循环输出最终字典，说明每条信息如何帮助项目推进。

**参考答案**
```python
alien_0 = {'color': 'green', 'points': 5}

extended_alien_0 = alien_0.copy()
extended_alien_0['术语库'] = '集中维护客户批准的关键词'
extended_alien_0['审校说明'] = '与审校团队共享 QA 要点'
for key, value in extended_alien_0.items():
    print(f"{key} -> {value}")
```
### `chapter_06/partial_programs/aliens_1_thirty_aliens.py`

**练习**
1. 在 `aliens` 列表中补充两项新的语言服务资源。
2. 遍历扩展后的列表，为每个条目写一句使用计划。

**参考答案**
```python
aliens = []

extra_resources = ['术语云平台', '翻译记忆体检查']
extended_aliens = list(aliens) + extra_resources
for item in extended_aliens:
    print(f"准备评估 {item} 在翻译项目中的应用。")
```
### `chapter_06/partial_programs/aliens_2_change_colors.py`

**练习**
1. 在 `aliens` 列表中补充两项新的语言服务资源。
2. 遍历扩展后的列表，为每个条目写一句使用计划。

**参考答案**
```python
aliens = []

extra_resources = ['术语云平台', '翻译记忆体检查']
extended_aliens = list(aliens) + extra_resources
for item in extended_aliens:
    print(f"准备评估 {item} 在翻译项目中的应用。")
```
### `chapter_06/partial_programs/favorite_languages_0_first_version.py`

**练习**
1. 复制 `favorite_languages` 字典，并新增与翻译项目协作相关的键值对。
2. 循环输出最终字典，说明每条信息如何帮助项目推进。

**参考答案**
```python
favorite_languages = {'jen': 'python', 'sarah': 'c', 'edward': 'rust', 'phil': 'python'}

extended_favorite_languages = favorite_languages.copy()
extended_favorite_languages['术语库'] = '集中维护客户批准的关键词'
extended_favorite_languages['审校说明'] = '与审校团队共享 QA 要点'
for key, value in extended_favorite_languages.items():
    print(f"{key} -> {value}")
```
### `chapter_06/partial_programs/favorite_languages_1_look_up_language.py`

**练习**
1. 复制 `favorite_languages` 字典，并新增与翻译项目协作相关的键值对。
2. 循环输出最终字典，说明每条信息如何帮助项目推进。

**参考答案**
```python
favorite_languages = {'jen': 'python', 'sarah': 'c', 'edward': 'rust', 'phil': 'python'}

extended_favorite_languages = favorite_languages.copy()
extended_favorite_languages['术语库'] = '集中维护客户批准的关键词'
extended_favorite_languages['审校说明'] = '与审校团队共享 QA 要点'
for key, value in extended_favorite_languages.items():
    print(f"{key} -> {value}")
```
### `chapter_06/partial_programs/favorite_languages_2_loop_items.py`

**练习**
1. 复制 `favorite_languages` 字典，并新增与翻译项目协作相关的键值对。
2. 循环输出最终字典，说明每条信息如何帮助项目推进。

**参考答案**
```python
favorite_languages = {'jen': 'python', 'sarah': 'c', 'edward': 'rust', 'phil': 'python'}

extended_favorite_languages = favorite_languages.copy()
extended_favorite_languages['术语库'] = '集中维护客户批准的关键词'
extended_favorite_languages['审校说明'] = '与审校团队共享 QA 要点'
for key, value in extended_favorite_languages.items():
    print(f"{key} -> {value}")
```
### `chapter_06/partial_programs/favorite_languages_3_loop_keys.py`

**练习**
1. 复制 `favorite_languages` 字典，并新增与翻译项目协作相关的键值对。
2. 循环输出最终字典，说明每条信息如何帮助项目推进。

**参考答案**
```python
favorite_languages = {'jen': 'python', 'sarah': 'c', 'edward': 'rust', 'phil': 'python'}

extended_favorite_languages = favorite_languages.copy()
extended_favorite_languages['术语库'] = '集中维护客户批准的关键词'
extended_favorite_languages['审校说明'] = '与审校团队共享 QA 要点'
for key, value in extended_favorite_languages.items():
    print(f"{key} -> {value}")
```
### `chapter_06/partial_programs/favorite_languages_4_work_inside_loop.py`

**练习**
1. 复制 `favorite_languages` 字典，并新增与翻译项目协作相关的键值对。
2. 循环输出最终字典，说明每条信息如何帮助项目推进。

**参考答案**
```python
favorite_languages = {'jen': 'python', 'sarah': 'c', 'edward': 'rust', 'phil': 'python'}

extended_favorite_languages = favorite_languages.copy()
extended_favorite_languages['术语库'] = '集中维护客户批准的关键词'
extended_favorite_languages['审校说明'] = '与审校团队共享 QA 要点'
for key, value in extended_favorite_languages.items():
    print(f"{key} -> {value}")
```
### `chapter_06/partial_programs/favorite_languages_5_check_polled.py`

**练习**
1. 复制 `favorite_languages` 字典，并新增与翻译项目协作相关的键值对。
2. 循环输出最终字典，说明每条信息如何帮助项目推进。

**参考答案**
```python
favorite_languages = {'jen': 'python', 'sarah': 'c', 'edward': 'rust', 'phil': 'python'}

extended_favorite_languages = favorite_languages.copy()
extended_favorite_languages['术语库'] = '集中维护客户批准的关键词'
extended_favorite_languages['审校说明'] = '与审校团队共享 QA 要点'
for key, value in extended_favorite_languages.items():
    print(f"{key} -> {value}")
```
### `chapter_06/partial_programs/favorite_languages_6_loop_sorted.py`

**练习**
1. 复制 `favorite_languages` 字典，并新增与翻译项目协作相关的键值对。
2. 循环输出最终字典，说明每条信息如何帮助项目推进。

**参考答案**
```python
favorite_languages = {'jen': 'python', 'sarah': 'c', 'edward': 'rust', 'phil': 'python'}

extended_favorite_languages = favorite_languages.copy()
extended_favorite_languages['术语库'] = '集中维护客户批准的关键词'
extended_favorite_languages['审校说明'] = '与审校团队共享 QA 要点'
for key, value in extended_favorite_languages.items():
    print(f"{key} -> {value}")
```
### `chapter_06/partial_programs/favorite_languages_7_loop_values.py`

**练习**
1. 复制 `favorite_languages` 字典，并新增与翻译项目协作相关的键值对。
2. 循环输出最终字典，说明每条信息如何帮助项目推进。

**参考答案**
```python
favorite_languages = {'jen': 'python', 'sarah': 'c', 'edward': 'rust', 'phil': 'python'}

extended_favorite_languages = favorite_languages.copy()
extended_favorite_languages['术语库'] = '集中维护客户批准的关键词'
extended_favorite_languages['审校说明'] = '与审校团队共享 QA 要点'
for key, value in extended_favorite_languages.items():
    print(f"{key} -> {value}")
```
### `chapter_06/partial_programs/favorite_languages_8_loop_set.py`

**练习**
1. 复制 `favorite_languages` 字典，并新增与翻译项目协作相关的键值对。
2. 循环输出最终字典，说明每条信息如何帮助项目推进。

**参考答案**
```python
favorite_languages = {'jen': 'python', 'sarah': 'c', 'edward': 'rust', 'phil': 'python'}

extended_favorite_languages = favorite_languages.copy()
extended_favorite_languages['术语库'] = '集中维护客户批准的关键词'
extended_favorite_languages['审校说明'] = '与审校团队共享 QA 要点'
for key, value in extended_favorite_languages.items():
    print(f"{key} -> {value}")
```
### `chapter_06/partial_programs/favorite_languages_9_nested_lists.py`

**练习**
1. 复制 `favorite_languages` 字典，并新增与翻译项目协作相关的键值对。
2. 循环输出最终字典，说明每条信息如何帮助项目推进。

**参考答案**
```python
favorite_languages = {'jen': ['python', 'rust'], 'sarah': ['c'], 'edward': ['rust', 'go'], 'phil': ['python', 'haskell']}

extended_favorite_languages = favorite_languages.copy()
extended_favorite_languages['术语库'] = '集中维护客户批准的关键词'
extended_favorite_languages['审校说明'] = '与审校团队共享 QA 要点'
for key, value in extended_favorite_languages.items():
    print(f"{key} -> {value}")
```
### `chapter_06/partial_programs/many_users.py`

**练习**
1. 复制 `users` 字典，并新增与翻译项目协作相关的键值对。
2. 循环输出最终字典，说明每条信息如何帮助项目推进。

**参考答案**
```python
users = {'aeinstein': {'first': 'albert', 'last': 'einstein', 'location': 'princeton'}, 'mcurie': {'first': 'marie', 'last': 'curie', 'location': 'paris'}}

extended_users = users.copy()
extended_users['术语库'] = '集中维护客户批准的关键词'
extended_users['审校说明'] = '与审校团队共享 QA 要点'
for key, value in extended_users.items():
    print(f"{key} -> {value}")
```
### `chapter_06/partial_programs/pizza.py`

**练习**
1. 复制 `pizza` 字典，并新增与翻译项目协作相关的键值对。
2. 循环输出最终字典，说明每条信息如何帮助项目推进。

**参考答案**
```python
pizza = {'crust': 'thick', 'toppings': ['mushrooms', 'extra cheese']}

extended_pizza = pizza.copy()
extended_pizza['术语库'] = '集中维护客户批准的关键词'
extended_pizza['审校说明'] = '与审校团队共享 QA 要点'
for key, value in extended_pizza.items():
    print(f"{key} -> {value}")
```
### `chapter_06/partial_programs/user_0_first_listing.py`

**练习**
1. 复制 `user_0` 字典，并新增与翻译项目协作相关的键值对。
2. 循环输出最终字典，说明每条信息如何帮助项目推进。

**参考答案**
```python
user_0 = {'username': 'efermi', 'first': 'enrico', 'last': 'fermi'}

extended_user_0 = user_0.copy()
extended_user_0['术语库'] = '集中维护客户批准的关键词'
extended_user_0['审校说明'] = '与审校团队共享 QA 要点'
for key, value in extended_user_0.items():
    print(f"{key} -> {value}")
```
### `chapter_06/partial_programs/user_1_loop_items.py`

**练习**
1. 复制 `user_0` 字典，并新增与翻译项目协作相关的键值对。
2. 循环输出最终字典，说明每条信息如何帮助项目推进。

**参考答案**
```python
user_0 = {'username': 'efermi', 'first': 'enrico', 'last': 'fermi'}

extended_user_0 = user_0.copy()
extended_user_0['术语库'] = '集中维护客户批准的关键词'
extended_user_0['审校说明'] = '与审校团队共享 QA 要点'
for key, value in extended_user_0.items():
    print(f"{key} -> {value}")
```
### `chapter_06/pizza.py`

**练习**
1. 复制 `term_list` 字典，并新增与翻译项目协作相关的键值对。
2. 循环输出最终字典，说明每条信息如何帮助项目推进。

**参考答案**
```python
term_list = {'base_language': 'English', 'target_language': 'Spanish', 'keywords': ['compliance', 'sustainability', 'stakeholder']}

extended_term_list = term_list.copy()
extended_term_list['术语库'] = '集中维护客户批准的关键词'
extended_term_list['审校说明'] = '与审校团队共享 QA 要点'
for key, value in extended_term_list.items():
    print(f"{key} -> {value}")
```
### `chapter_06/user.py`

**练习**
1. 复制 `translator` 字典，并新增与翻译项目协作相关的键值对。
2. 循环输出最终字典，说明每条信息如何帮助项目推进。

**参考答案**
```python
translator = {'username': 'mtran', 'first': 'mei', 'last': 'tran', 'specialization': 'financial reports'}

extended_translator = translator.copy()
extended_translator['术语库'] = '集中维护客户批准的关键词'
extended_translator['审校说明'] = '与审校团队共享 QA 要点'
for key, value in extended_translator.items():
    print(f"{key} -> {value}")
```

## Chapter 07
### `chapter_07/cities.py`

**练习**
1. 复制 `cities` 字典，并新增与翻译项目协作相关的键值对。
2. 循环输出最终字典，说明每条信息如何帮助项目推进。

**参考答案**
```python
cities = {'beijing': {'country': 'china', 'language_pair': 'EN->ZH', 'notable_project': 'tech conference materials'}, 'montreal': {'country': 'canada', 'language_pair': 'FR->EN', 'notable_project': 'immigration handbook'}}

extended_cities = cities.copy()
extended_cities['术语库'] = '集中维护客户批准的关键词'
extended_cities['审校说明'] = '与审校团队共享 QA 要点'
for key, value in extended_cities.items():
    print(f"{key} -> {value}")
```
### `chapter_07/confirmed_users.py`

**练习**
1. 在 `unconfirmed_translators` 列表中补充两项新的语言服务资源。
2. 遍历扩展后的列表，为每个条目写一句使用计划。

**参考答案**
```python
unconfirmed_translators = ['li wen', 'chen yu', 'maria gonzalez']

extra_resources = ['术语云平台', '翻译记忆体检查']
extended_unconfirmed_translators = list(unconfirmed_translators) + extra_resources
for item in extended_unconfirmed_translators:
    print(f"准备评估 {item} 在翻译项目中的应用。")
```
### `chapter_07/counting.py`

**练习**
1. 基于原脚本，加入额外的状态输出或日志，用于追踪翻译项目的进度。
2. 将扩展后的程序运行结果整理成文字说明，与同学分享。

**参考答案**
```python
number = 1
while number <= 5:
    print(f"Processing segment {number}")
    number += 1

print("\n练习扩展：记录至少一条你在翻译项目中学到的新经验。")
```
### `chapter_07/even_or_odd.py`

**练习**
1. 基于原脚本，加入额外的状态输出或日志，用于追踪翻译项目的进度。
2. 将扩展后的程序运行结果整理成文字说明，与同学分享。

**参考答案**
```python
segment = 13

if segment % 2 == 0:
    print("Send this segment to the reviewer queue.")
else:
    print("Translator continues working on this segment.")

print("\n练习扩展：记录至少一条你在翻译项目中学到的新经验。")
```
### `chapter_07/mountain_poll.py`

**练习**
1. 复制 `responses` 字典，并新增与翻译项目协作相关的键值对。
2. 循环输出最终字典，说明每条信息如何帮助项目推进。

**参考答案**
```python
responses = {}

extended_responses = responses.copy()
extended_responses['术语库'] = '集中维护客户批准的关键词'
extended_responses['审校说明'] = '与审校团队共享 QA 要点'
for key, value in extended_responses.items():
    print(f"{key} -> {value}")
```
### `chapter_07/partial_programs/cities.py`

**练习**
1. 基于原脚本，加入额外的状态输出或日志，用于追踪翻译项目的进度。
2. 将扩展后的程序运行结果整理成文字说明，与同学分享。

**参考答案**
```python
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")

print("\n练习扩展：记录至少一条你在翻译项目中学到的新经验。")
```
### `chapter_07/partial_programs/confirmed_users.py`

**练习**
1. 在 `unconfirmed_users` 列表中补充两项新的语言服务资源。
2. 遍历扩展后的列表，为每个条目写一句使用计划。

**参考答案**
```python
unconfirmed_users = ['alice', 'brian', 'candace']

extra_resources = ['术语云平台', '翻译记忆体检查']
extended_unconfirmed_users = list(unconfirmed_users) + extra_resources
for item in extended_unconfirmed_users:
    print(f"准备评估 {item} 在翻译项目中的应用。")
```
### `chapter_07/partial_programs/counting_0_first_version.py`

**练习**
1. 基于原脚本，加入额外的状态输出或日志，用于追踪翻译项目的进度。
2. 将扩展后的程序运行结果整理成文字说明，与同学分享。

**参考答案**
```python
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

print("\n练习扩展：记录至少一条你在翻译项目中学到的新经验。")
```
### `chapter_07/partial_programs/counting_1_using_continue.py`

**练习**
1. 基于原脚本，加入额外的状态输出或日志，用于追踪翻译项目的进度。
2. 将扩展后的程序运行结果整理成文字说明，与同学分享。

**参考答案**
```python
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number)

print("\n练习扩展：记录至少一条你在翻译项目中学到的新经验。")
```
### `chapter_07/partial_programs/even_or_odd.py`

**练习**
1. 基于原脚本，加入额外的状态输出或日志，用于追踪翻译项目的进度。
2. 将扩展后的程序运行结果整理成文字说明，与同学分享。

**参考答案**
```python
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")

print("\n练习扩展：记录至少一条你在翻译项目中学到的新经验。")
```
### `chapter_07/partial_programs/greeter_1_longer_prompt.py`

**练习**
1. 基于原脚本，加入额外的状态输出或日志，用于追踪翻译项目的进度。
2. 将扩展后的程序运行结果整理成文字说明，与同学分享。

**参考答案**
```python
prompt = "If you share your name, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print(f"\nHello, {name}!")

print("\n练习扩展：记录至少一条你在翻译项目中学到的新经验。")
```
### `chapter_07/partial_programs/mountain_poll.py`

**练习**
1. 复制 `responses` 字典，并新增与翻译项目协作相关的键值对。
2. 循环输出最终字典，说明每条信息如何帮助项目推进。

**参考答案**
```python
responses = {}

extended_responses = responses.copy()
extended_responses['术语库'] = '集中维护客户批准的关键词'
extended_responses['审校说明'] = '与审校团队共享 QA 要点'
for key, value in extended_responses.items():
    print(f"{key} -> {value}")
```
### `chapter_07/partial_programs/parrot_1_while_loop.py`

**练习**
1. 基于原脚本，加入额外的状态输出或日志，用于追踪翻译项目的进度。
2. 将扩展后的程序运行结果整理成文字说明，与同学分享。

**参考答案**
```python
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != 'quit':
    message = input(prompt)
    print(message)

print("\n练习扩展：记录至少一条你在翻译项目中学到的新经验。")
```
### `chapter_07/partial_programs/parrot_2_while_loop_if_test.py`

**练习**
1. 基于原脚本，加入额外的状态输出或日志，用于追踪翻译项目的进度。
2. 将扩展后的程序运行结果整理成文字说明，与同学分享。

**参考答案**
```python
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        print(message)

print("\n练习扩展：记录至少一条你在翻译项目中学到的新经验。")
```
### `chapter_07/partial_programs/parrot_3_while_loop_flag.py`

**练习**
1. 基于原脚本，加入额外的状态输出或日志，用于追踪翻译项目的进度。
2. 将扩展后的程序运行结果整理成文字说明，与同学分享。

**参考答案**
```python
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)

print("\n练习扩展：记录至少一条你在翻译项目中学到的新经验。")
```
### `chapter_07/partial_programs/pets.py`

**练习**
1. 在 `pets` 列表中补充两项新的语言服务资源。
2. 遍历扩展后的列表，为每个条目写一句使用计划。

**参考答案**
```python
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']

extra_resources = ['术语云平台', '翻译记忆体检查']
extended_pets = list(pets) + extra_resources
for item in extended_pets:
    print(f"准备评估 {item} 在翻译项目中的应用。")
```
### `chapter_07/partial_programs/rollercoaster.py`

**练习**
1. 基于原脚本，加入额外的状态输出或日志，用于追踪翻译项目的进度。
2. 将扩展后的程序运行结果整理成文字说明，与同学分享。

**参考答案**
```python
height = input("How tall are you, in inches? ")
height = int(height)

if height >= 48:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")

print("\n练习扩展：记录至少一条你在翻译项目中学到的新经验。")
```
### `chapter_07/pets.py`

**练习**
1. 在 `active_assignments` 列表中补充两项新的语言服务资源。
2. 遍历扩展后的列表，为每个条目写一句使用计划。

**参考答案**
```python
active_assignments = ['legal contract', 'software release notes', 'marketing campaign']

extra_resources = ['术语云平台', '翻译记忆体检查']
extended_active_assignments = list(active_assignments) + extra_resources
for item in extended_active_assignments:
    print(f"准备评估 {item} 在翻译项目中的应用。")
```
### `chapter_07/rollercoaster.py`

**练习**
1. 基于原脚本，加入额外的状态输出或日志，用于追踪翻译项目的进度。
2. 将扩展后的程序运行结果整理成文字说明，与同学分享。

**参考答案**
```python
word_count = 2200

if word_count >= 2000:
    print("Apply premium proofreading workflow.")
else:
    print("Standard proofreading is sufficient.")

print("\n练习扩展：记录至少一条你在翻译项目中学到的新经验。")
```

## Chapter 08
### `chapter_08/formatted_name.py`

**练习**
1. 使用 `build_translator_name` 函数模拟新的翻译场景输入。
2. 观察返回结果或输出，并记录参数（例如：first_name、last_name）。

**参考答案**
```python
from chapter_08.formatted_name import build_translator_name

result = build_translator_name('示例信息', '示例信息')
print(result)
print(build_translator_name('示例信息', '示例信息', middle_name='示例信息'))
```
### `chapter_08/importing_functions/importing_0_entire_module/pizza.py`

**练习**
1. 使用 `make_pizza` 函数模拟新的翻译场景输入。
2. 观察返回结果或输出，并记录参数（例如：size）。

**参考答案**
```python
from chapter_08.importing_functions.importing_0_entire_module.pizza import make_pizza

result = make_pizza('示例信息')
print(result)
```
### `chapter_08/importing_functions/importing_1_specific_functions/pizza.py`

**练习**
1. 使用 `make_pizza` 函数模拟新的翻译场景输入。
2. 观察返回结果或输出，并记录参数（例如：size）。

**参考答案**
```python
from chapter_08.importing_functions.importing_1_specific_functions.pizza import make_pizza

result = make_pizza('示例信息')
print(result)
```
### `chapter_08/importing_functions/importing_2_function_alias/pizza.py`

**练习**
1. 使用 `make_pizza` 函数模拟新的翻译场景输入。
2. 观察返回结果或输出，并记录参数（例如：size）。

**参考答案**
```python
from chapter_08.importing_functions.importing_2_function_alias.pizza import make_pizza

result = make_pizza('示例信息')
print(result)
```
### `chapter_08/importing_functions/importing_3_module_alias/pizza.py`

**练习**
1. 使用 `make_pizza` 函数模拟新的翻译场景输入。
2. 观察返回结果或输出，并记录参数（例如：size）。

**参考答案**
```python
from chapter_08.importing_functions.importing_3_module_alias.pizza import make_pizza

result = make_pizza('示例信息')
print(result)
```
### `chapter_08/importing_functions/importing_4_all_functions/pizza.py`

**练习**
1. 使用 `make_pizza` 函数模拟新的翻译场景输入。
2. 观察返回结果或输出，并记录参数（例如：size）。

**参考答案**
```python
from chapter_08.importing_functions.importing_4_all_functions.pizza import make_pizza

result = make_pizza('示例信息')
print(result)
```
### `chapter_08/partial_programs/formatted_name_0_first_version.py`

**练习**
1. 使用 `get_formatted_name` 函数模拟新的翻译场景输入。
2. 观察返回结果或输出，并记录参数（例如：first_name、last_name）。

**参考答案**
```python
from chapter_08.partial_programs.formatted_name_0_first_version import get_formatted_name

result = get_formatted_name('示例信息', '示例信息')
print(result)
```
### `chapter_08/partial_programs/formatted_name_1_making_argument_optional.py`

**练习**
1. 使用 `get_formatted_name` 函数模拟新的翻译场景输入。
2. 观察返回结果或输出，并记录参数（例如：first_name、middle_name、last_name）。

**参考答案**
```python
from chapter_08.partial_programs.formatted_name_1_making_argument_optional import get_formatted_name

result = get_formatted_name('示例信息', '示例信息', '示例信息')
print(result)
```
### `chapter_08/partial_programs/formatted_name_2_argument_optional.py`

**练习**
1. 使用 `get_formatted_name` 函数模拟新的翻译场景输入。
2. 观察返回结果或输出，并记录参数（例如：first_name、last_name）。

**参考答案**
```python
from chapter_08.partial_programs.formatted_name_2_argument_optional import get_formatted_name

result = get_formatted_name('示例信息', '示例信息')
print(result)
print(get_formatted_name('示例信息', '示例信息', middle_name='示例信息'))
```
### `chapter_08/partial_programs/greet_users.py`

**练习**
1. 使用 `greet_users` 函数模拟新的翻译场景输入。
2. 观察返回结果或输出，并记录参数（例如：names）。

**参考答案**
```python
from chapter_08.partial_programs.greet_users import greet_users

result = greet_users('示例信息')
print(result)
```
### `chapter_08/partial_programs/greeter_0_first_version.py`

**练习**
1. 使用 `greet_user` 函数模拟新的翻译场景输入。
2. 观察返回结果或输出，并记录参数（例如：默认参数）。

**参考答案**
```python
from chapter_08.partial_programs.greeter_0_first_version import greet_user

result = greet_user()
print(result)
```
### `chapter_08/partial_programs/greeter_1_passing_information.py`

**练习**
1. 使用 `greet_user` 函数模拟新的翻译场景输入。
2. 观察返回结果或输出，并记录参数（例如：username）。

**参考答案**
```python
from chapter_08.partial_programs.greeter_1_passing_information import greet_user

result = greet_user(True)
print(result)
```
### `chapter_08/partial_programs/greeter_2_infinite_loop.py`

**练习**
1. 使用 `get_formatted_name` 函数模拟新的翻译场景输入。
2. 观察返回结果或输出，并记录参数（例如：first_name、last_name）。

**参考答案**
```python
from chapter_08.partial_programs.greeter_2_infinite_loop import get_formatted_name

result = get_formatted_name('示例信息', '示例信息')
print(result)
```
### `chapter_08/partial_programs/greeter_3_quit_conditions.py`

**练习**
1. 使用 `get_formatted_name` 函数模拟新的翻译场景输入。
2. 观察返回结果或输出，并记录参数（例如：first_name、last_name）。

**参考答案**
```python
from chapter_08.partial_programs.greeter_3_quit_conditions import get_formatted_name

result = get_formatted_name('示例信息', '示例信息')
print(result)
```
### `chapter_08/partial_programs/importing_0_entire_module/pizza.py`

**练习**
1. 使用 `make_pizza` 函数模拟新的翻译场景输入。
2. 观察返回结果或输出，并记录参数（例如：size）。

**参考答案**
```python
from chapter_08.partial_programs.importing_0_entire_module.pizza import make_pizza

result = make_pizza('示例信息')
print(result)
```
### `chapter_08/partial_programs/importing_1_specific_functions/pizza.py`

**练习**
1. 使用 `make_pizza` 函数模拟新的翻译场景输入。
2. 观察返回结果或输出，并记录参数（例如：size）。

**参考答案**
```python
from chapter_08.partial_programs.importing_1_specific_functions.pizza import make_pizza

result = make_pizza('示例信息')
print(result)
```
### `chapter_08/partial_programs/importing_2_function_alias/pizza.py`

**练习**
1. 使用 `make_pizza` 函数模拟新的翻译场景输入。
2. 观察返回结果或输出，并记录参数（例如：size）。

**参考答案**
```python
from chapter_08.partial_programs.importing_2_function_alias.pizza import make_pizza

result = make_pizza('示例信息')
print(result)
```
### `chapter_08/partial_programs/importing_3_module_alias/pizza.py`

**练习**
1. 使用 `make_pizza` 函数模拟新的翻译场景输入。
2. 观察返回结果或输出，并记录参数（例如：size）。

**参考答案**
```python
from chapter_08.partial_programs.importing_3_module_alias.pizza import make_pizza

result = make_pizza('示例信息')
print(result)
```
### `chapter_08/partial_programs/importing_4_all_functions/pizza.py`

**练习**
1. 使用 `make_pizza` 函数模拟新的翻译场景输入。
2. 观察返回结果或输出，并记录参数（例如：size）。

**参考答案**
```python
from chapter_08.partial_programs.importing_4_all_functions.pizza import make_pizza

result = make_pizza('示例信息')
print(result)
```
### `chapter_08/partial_programs/person_0_first_version.py`

**练习**
1. 使用 `build_person` 函数模拟新的翻译场景输入。
2. 观察返回结果或输出，并记录参数（例如：first_name、last_name）。

**参考答案**
```python
from chapter_08.partial_programs.person_0_first_version import build_person

result = build_person('示例信息', '示例信息')
print(result)
```
### `chapter_08/partial_programs/person_1_with_age.py`

**练习**
1. 使用 `build_person` 函数模拟新的翻译场景输入。
2. 观察返回结果或输出，并记录参数（例如：first_name、last_name）。

**参考答案**
```python
from chapter_08.partial_programs.person_1_with_age import build_person

result = build_person('示例信息', '示例信息')
print(result)
print(build_person('示例信息', '示例信息', age=28))
```
### `chapter_08/partial_programs/pets_0_first_version.py`

**练习**
1. 使用 `describe_pet` 函数模拟新的翻译场景输入。
2. 观察返回结果或输出，并记录参数（例如：animal_type、pet_name）。

**参考答案**
```python
from chapter_08.partial_programs.pets_0_first_version import describe_pet

result = describe_pet('示例信息', '示例信息')
print(result)
```
### `chapter_08/partial_programs/pets_1_multiple_calls.py`

**练习**
1. 使用 `describe_pet` 函数模拟新的翻译场景输入。
2. 观察返回结果或输出，并记录参数（例如：animal_type、pet_name）。

**参考答案**
```python
from chapter_08.partial_programs.pets_1_multiple_calls import describe_pet

result = describe_pet('示例信息', '示例信息')
print(result)
```
### `chapter_08/partial_programs/pets_2_order_matters.py`

**练习**
1. 使用 `describe_pet` 函数模拟新的翻译场景输入。
2. 观察返回结果或输出，并记录参数（例如：animal_type、pet_name）。

**参考答案**
```python
from chapter_08.partial_programs.pets_2_order_matters import describe_pet

result = describe_pet('示例信息', '示例信息')
print(result)
```
### `chapter_08/partial_programs/pets_3_keyword_arguments.py`

**练习**
1. 使用 `describe_pet` 函数模拟新的翻译场景输入。
2. 观察返回结果或输出，并记录参数（例如：animal_type、pet_name）。

**参考答案**
```python
from chapter_08.partial_programs.pets_3_keyword_arguments import describe_pet

result = describe_pet('示例信息', '示例信息')
print(result)
```
### `chapter_08/partial_programs/pets_4_default_values.py`

**练习**
1. 使用 `describe_pet` 函数模拟新的翻译场景输入。
2. 观察返回结果或输出，并记录参数（例如：pet_name）。

**参考答案**
```python
from chapter_08.partial_programs.pets_4_default_values import describe_pet

result = describe_pet('示例信息')
print(result)
print(describe_pet('示例信息', animal_type='示例信息'))
```
### `chapter_08/partial_programs/pizza_0_first_version.py`

**练习**
1. 使用 `make_pizza` 函数模拟新的翻译场景输入。
2. 观察返回结果或输出，并记录参数（例如：默认参数）。

**参考答案**
```python
from chapter_08.partial_programs.pizza_0_first_version import make_pizza

result = make_pizza()
print(result)
```
### `chapter_08/partial_programs/pizza_1_loop.py`

**练习**
1. 使用 `make_pizza` 函数模拟新的翻译场景输入。
2. 观察返回结果或输出，并记录参数（例如：默认参数）。

**参考答案**
```python
from chapter_08.partial_programs.pizza_1_loop import make_pizza

result = make_pizza()
print(result)
```
### `chapter_08/partial_programs/pizza_2_mixing_positional_arbitrary_args.py`

**练习**
1. 使用 `make_pizza` 函数模拟新的翻译场景输入。
2. 观察返回结果或输出，并记录参数（例如：size）。

**参考答案**
```python
from chapter_08.partial_programs.pizza_2_mixing_positional_arbitrary_args import make_pizza

result = make_pizza('示例信息')
print(result)
```
### `chapter_08/partial_programs/printing_models_0_first_version.py`

**练习**
1. 在 `unprinted_designs` 列表中补充两项新的语言服务资源。
2. 遍历扩展后的列表，为每个条目写一句使用计划。

**参考答案**
```python
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']

extra_resources = ['术语云平台', '翻译记忆体检查']
extended_unprinted_designs = list(unprinted_designs) + extra_resources
for item in extended_unprinted_designs:
    print(f"准备评估 {item} 在翻译项目中的应用。")
```
### `chapter_08/partial_programs/printing_models_1_two_functions.py`

**练习**
1. 使用 `print_models` 函数模拟新的翻译场景输入。
2. 观察返回结果或输出，并记录参数（例如：unprinted_designs、completed_models）。

**参考答案**
```python
from chapter_08.partial_programs.printing_models_1_two_functions import print_models

result = print_models('示例信息', '示例信息')
print(result)
```
### `chapter_08/partial_programs/user_profile.py`

**练习**
1. 使用 `build_profile` 函数模拟新的翻译场景输入。
2. 观察返回结果或输出，并记录参数（例如：first、last）。

**参考答案**
```python
from chapter_08.partial_programs.user_profile import build_profile

result = build_profile('示例信息', '示例信息')
print(result)
```
### `chapter_08/person.py`

**练习**
1. 使用 `build_translator` 函数模拟新的翻译场景输入。
2. 观察返回结果或输出，并记录参数（例如：first_name、last_name）。

**参考答案**
```python
from chapter_08.person import build_translator

result = build_translator('示例信息', '示例信息')
print(result)
print(build_translator('示例信息', '示例信息', specialization='示例信息'))
```
### `chapter_08/pets.py`

**练习**
1. 使用 `describe_assignment` 函数模拟新的翻译场景输入。
2. 观察返回结果或输出，并记录参数（例如：project_type、language_pair）。

**参考答案**
```python
from chapter_08.pets import describe_assignment

result = describe_assignment('marketing localization', 'EN->ZH')
print(result)
```
### `chapter_08/pizza.py`

**练习**
1. 使用 `build_keyword_list` 函数模拟新的翻译场景输入。
2. 观察返回结果或输出，并记录参数（例如：base_language、target_language）。

**参考答案**
```python
from chapter_08.pizza import build_keyword_list

result = build_keyword_list(28, 28)
print(result)
```
### `chapter_08/printing_models.py`

**练习**
1. 使用 `prepare_projects` 函数模拟新的翻译场景输入。
2. 观察返回结果或输出，并记录参数（例如：pending_projects、completed_projects）。

**参考答案**
```python
from chapter_08.printing_models import prepare_projects

result = prepare_projects('marketing localization', 'marketing localization')
print(result)
```
### `chapter_08/user_profile.py`

**练习**
1. 使用 `build_translator_profile` 函数模拟新的翻译场景输入。
2. 观察返回结果或输出，并记录参数（例如：first、last）。

**参考答案**
```python
from chapter_08.user_profile import build_translator_profile

result = build_translator_profile('示例信息', '示例信息')
print(result)
```

## Chapter 09
### `chapter_09/car.py`

**练习**
1. 参考 `TranslationProject` 类，创建一个属于你自己的翻译案例实例。
2. 输出实例的主要属性，并尝试调用至少一个不需要额外参数的方法。

**参考答案**
```python
from chapter_09.car import TranslationProject

example = TranslationProject('TransGlobe', 'EN->ZH')
print(vars(example))
example.describe_project()
```
### `chapter_09/dog.py`

**练习**
1. 参考 `Reviewer` 类，创建一个属于你自己的翻译案例实例。
2. 输出实例的主要属性，并尝试调用至少一个不需要额外参数的方法。

**参考答案**
```python
from chapter_09.dog import Reviewer

example = Reviewer('示例信息', True)
print(vars(example))
example.describe_reviewer()
```
### `chapter_09/electric_car.py`

**练习**
1. 参考 `TranslationProject` 类，创建一个属于你自己的翻译案例实例。
2. 输出实例的主要属性，并尝试调用至少一个不需要额外参数的方法。

**参考答案**
```python
from chapter_09.electric_car import TranslationProject

example = TranslationProject('TransGlobe', 'EN->ZH')
print(vars(example))
example.describe_project()
```
### `chapter_09/importing_classes/importing_0_importing_single_class/car.py`

**练习**
1. 参考 `TranslationProject` 类，创建一个属于你自己的翻译案例实例。
2. 输出实例的主要属性，并尝试调用至少一个不需要额外参数的方法。

**参考答案**
```python
from chapter_09.importing_classes.importing_0_importing_single_class.car import TranslationProject

example = TranslationProject('TransGlobe', 'EN->ZH')
print(vars(example))
example.describe_project()
```
### `chapter_09/importing_classes/importing_0_importing_single_class/my_car.py`

**练习**
1. 基于原脚本，加入额外的状态输出或日志，用于追踪翻译项目的进度。
2. 将扩展后的程序运行结果整理成文字说明，与同学分享。

**参考答案**
```python
from car import TranslationProject

project = TranslationProject('GlobalTech', 'EN->ZH')
print(project.describe_project())
project.advance_status('translation')
print(f"Status: {project.status}")

print("\n练习扩展：记录至少一条你在翻译项目中学到的新经验。")
```
### `chapter_09/importing_classes/importing_1_storing_multiple_classes_in_a_module/car.py`

**练习**
1. 参考 `TranslationProject` 类，创建一个属于你自己的翻译案例实例。
2. 输出实例的主要属性，并尝试调用至少一个不需要额外参数的方法。

**参考答案**
```python
from chapter_09.importing_classes.importing_1_storing_multiple_classes_in_a_module.car import TranslationProject

example = TranslationProject('TransGlobe', 'EN->ZH')
print(vars(example))
example.describe_project()
```
### `chapter_09/importing_classes/importing_1_storing_multiple_classes_in_a_module/my_electric_car.py`

**练习**
1. 基于原脚本，加入额外的状态输出或日志，用于追踪翻译项目的进度。
2. 将扩展后的程序运行结果整理成文字说明，与同学分享。

**参考答案**
```python
from car import MultimediaProject

project = MultimediaProject('CreativeMedia', 'EN->ES')
project.add_subtitle_track()
print(project.describe_project())
print(f"Subtitle tracks: {project.subtitle_tracks}")

print("\n练习扩展：记录至少一条你在翻译项目中学到的新经验。")
```
### `chapter_09/importing_classes/importing_2_importing_multiple_classes_from_a_module/car.py`

**练习**
1. 参考 `TranslationProject` 类，创建一个属于你自己的翻译案例实例。
2. 输出实例的主要属性，并尝试调用至少一个不需要额外参数的方法。

**参考答案**
```python
from chapter_09.importing_classes.importing_2_importing_multiple_classes_from_a_module.car import TranslationProject

example = TranslationProject('TransGlobe', 'EN->ZH')
print(vars(example))
example.describe_project()
```
### `chapter_09/importing_classes/importing_2_importing_multiple_classes_from_a_module/my_cars.py`

**练习**
1. 基于原脚本，加入额外的状态输出或日志，用于追踪翻译项目的进度。
2. 将扩展后的程序运行结果整理成文字说明，与同学分享。

**参考答案**
```python
from car import TranslationProject, MultimediaProject

standard_project = TranslationProject('GlobalTech', 'EN->ZH')
multimedia_project = MultimediaProject('CreativeMedia', 'EN->ES')
multimedia_project.add_subtitle_track()

print(standard_project.describe_project())
print(multimedia_project.describe_project())
print(f"Subtitle tracks: {multimedia_project.subtitle_tracks}")

print("\n练习扩展：记录至少一条你在翻译项目中学到的新经验。")
```
### `chapter_09/importing_classes/importing_3_importing_entire_module/car.py`

**练习**
1. 参考 `TranslationProject` 类，创建一个属于你自己的翻译案例实例。
2. 输出实例的主要属性，并尝试调用至少一个不需要额外参数的方法。

**参考答案**
```python
from chapter_09.importing_classes.importing_3_importing_entire_module.car import TranslationProject

example = TranslationProject('TransGlobe', 'EN->ZH')
print(vars(example))
example.describe_project()
```
### `chapter_09/importing_classes/importing_3_importing_entire_module/my_cars.py`

**练习**
1. 基于原脚本，加入额外的状态输出或日志，用于追踪翻译项目的进度。
2. 将扩展后的程序运行结果整理成文字说明，与同学分享。

**参考答案**
```python
import car

project = car.TranslationProject('GlobalTech', 'EN->ZH')
print(project.describe_project())
project.advance_status('translation')
print(f"Status: {project.status}")

print("\n练习扩展：记录至少一条你在翻译项目中学到的新经验。")
```
### `chapter_09/importing_classes/importing_4_importing_module_into_module/car.py`

**练习**
1. 参考 `TranslationProject` 类，创建一个属于你自己的翻译案例实例。
2. 输出实例的主要属性，并尝试调用至少一个不需要额外参数的方法。

**参考答案**
```python
from chapter_09.importing_classes.importing_4_importing_module_into_module.car import TranslationProject

example = TranslationProject('TransGlobe', 'EN->ZH')
print(vars(example))
example.describe_project()
```
### `chapter_09/importing_classes/importing_4_importing_module_into_module/electric_car.py`

**练习**
1. 参考 `MultimediaProject` 类，创建一个属于你自己的翻译案例实例。
2. 输出实例的主要属性，并尝试调用至少一个不需要额外参数的方法。

**参考答案**
```python
from chapter_09.importing_classes.importing_4_importing_module_into_module.electric_car import MultimediaProject

example = MultimediaProject('TransGlobe', 'EN->ZH')
print(vars(example))
example.add_subtitle_track()
```
### `chapter_09/importing_classes/importing_4_importing_module_into_module/my_cars.py`

**练习**
1. 基于原脚本，加入额外的状态输出或日志，用于追踪翻译项目的进度。
2. 将扩展后的程序运行结果整理成文字说明，与同学分享。

**参考答案**
```python
from car import TranslationProject
from electric_car import MultimediaProject

standard_project = TranslationProject('GlobalTech', 'EN->ZH')
multimedia_project = MultimediaProject('CreativeMedia', 'EN->ES')
multimedia_project.add_subtitle_track()

print(standard_project.describe_project())
print(multimedia_project.describe_project())
print(f"Subtitle tracks: {multimedia_project.subtitle_tracks}")

print("\n练习扩展：记录至少一条你在翻译项目中学到的新经验。")
```
### `chapter_09/partial_programs/creating_and_using_a_class/dog_0_first_version.py`

**练习**
1. 参考 `Reviewer` 类，创建一个属于你自己的翻译案例实例。
2. 输出实例的主要属性，并尝试调用至少一个不需要额外参数的方法。

**参考答案**
```python
from chapter_09.partial_programs.creating_and_using_a_class.dog_0_first_version import Reviewer

example = Reviewer('示例信息', True)
print(vars(example))
example.describe_reviewer()
```
### `chapter_09/partial_programs/creating_and_using_a_class/dog_1_calling_methods.py`

**练习**
1. 参考 `Reviewer` 类，创建一个属于你自己的翻译案例实例。
2. 输出实例的主要属性，并尝试调用至少一个不需要额外参数的方法。

**参考答案**
```python
from chapter_09.partial_programs.creating_and_using_a_class.dog_1_calling_methods import Reviewer

example = Reviewer('示例信息', True)
print(vars(example))
example.describe_reviewer()
```
### `chapter_09/partial_programs/creating_and_using_a_class/dog_2_multiple_instances.py`

**练习**
1. 参考 `Reviewer` 类，创建一个属于你自己的翻译案例实例。
2. 输出实例的主要属性，并尝试调用至少一个不需要额外参数的方法。

**参考答案**
```python
from chapter_09.partial_programs.creating_and_using_a_class.dog_2_multiple_instances import Reviewer

example = Reviewer('示例信息', True)
print(vars(example))
example.describe_reviewer()
```
### `chapter_09/partial_programs/importing_classes/importing_0_importing_single_class/car.py`

**练习**
1. 参考 `TranslationProject` 类，创建一个属于你自己的翻译案例实例。
2. 输出实例的主要属性，并尝试调用至少一个不需要额外参数的方法。

**参考答案**
```python
from chapter_09.partial_programs.importing_classes.importing_0_importing_single_class.car import TranslationProject

example = TranslationProject('TransGlobe', 'EN->ZH')
print(vars(example))
example.describe_project()
```
### `chapter_09/partial_programs/importing_classes/importing_1_storing_multiple_classes_in_a_module/car.py`

**练习**
1. 参考 `TranslationProject` 类，创建一个属于你自己的翻译案例实例。
2. 输出实例的主要属性，并尝试调用至少一个不需要额外参数的方法。

**参考答案**
```python
from chapter_09.partial_programs.importing_classes.importing_1_storing_multiple_classes_in_a_module.car import TranslationProject

example = TranslationProject('TransGlobe', 'EN->ZH')
print(vars(example))
example.describe_project()
```
### `chapter_09/partial_programs/importing_classes/importing_1_storing_multiple_classes_in_a_module/my_electric_car.py`

**练习**
1. 基于原脚本，加入额外的状态输出或日志，用于追踪翻译项目的进度。
2. 将扩展后的程序运行结果整理成文字说明，与同学分享。

**参考答案**
```python
from car import MultimediaProject

project = MultimediaProject('CreativeMedia', 'EN->ES')
project.add_subtitle_track()
print(project.describe_project())
print(f"Subtitle tracks: {project.subtitle_tracks}")

print("\n练习扩展：记录至少一条你在翻译项目中学到的新经验。")
```
### `chapter_09/partial_programs/importing_classes/importing_2_importing_multiple_classes_from_a_module/car.py`

**练习**
1. 参考 `TranslationProject` 类，创建一个属于你自己的翻译案例实例。
2. 输出实例的主要属性，并尝试调用至少一个不需要额外参数的方法。

**参考答案**
```python
from chapter_09.partial_programs.importing_classes.importing_2_importing_multiple_classes_from_a_module.car import TranslationProject

example = TranslationProject('TransGlobe', 'EN->ZH')
print(vars(example))
example.describe_project()
```
### `chapter_09/partial_programs/importing_classes/importing_2_importing_multiple_classes_from_a_module/my_cars.py`

**练习**
1. 基于原脚本，加入额外的状态输出或日志，用于追踪翻译项目的进度。
2. 将扩展后的程序运行结果整理成文字说明，与同学分享。

**参考答案**
```python
from car import TranslationProject, MultimediaProject

project = TranslationProject('GlobalTech', 'EN->ZH')
video_project = MultimediaProject('CreativeMedia', 'EN->ES')
video_project.add_subtitle_track()

print(project.describe_project())
print(video_project.describe_project())
print(f"Subtitle tracks: {video_project.subtitle_tracks}")

print("\n练习扩展：记录至少一条你在翻译项目中学到的新经验。")
```
### `chapter_09/partial_programs/importing_classes/importing_3_importing_entire_module/car.py`

**练习**
1. 参考 `TranslationProject` 类，创建一个属于你自己的翻译案例实例。
2. 输出实例的主要属性，并尝试调用至少一个不需要额外参数的方法。

**参考答案**
```python
from chapter_09.partial_programs.importing_classes.importing_3_importing_entire_module.car import TranslationProject

example = TranslationProject('TransGlobe', 'EN->ZH')
print(vars(example))
example.describe_project()
```
### `chapter_09/partial_programs/importing_classes/importing_3_importing_entire_module/my_cars.py`

**练习**
1. 基于原脚本，加入额外的状态输出或日志，用于追踪翻译项目的进度。
2. 将扩展后的程序运行结果整理成文字说明，与同学分享。

**参考答案**
```python
import car

project = car.TranslationProject('GlobalTech', 'EN->ZH')
video_project = car.MultimediaProject('CreativeMedia', 'EN->ES')
video_project.add_subtitle_track()

print(project.describe_project())
print(video_project.describe_project())
print(f"Subtitle tracks: {video_project.subtitle_tracks}")

print("\n练习扩展：记录至少一条你在翻译项目中学到的新经验。")
```
### `chapter_09/partial_programs/importing_classes/importing_4_importing_module_into_module/car.py`

**练习**
1. 参考 `TranslationProject` 类，创建一个属于你自己的翻译案例实例。
2. 输出实例的主要属性，并尝试调用至少一个不需要额外参数的方法。

**参考答案**
```python
from chapter_09.partial_programs.importing_classes.importing_4_importing_module_into_module.car import TranslationProject

example = TranslationProject('TransGlobe', 'EN->ZH')
print(vars(example))
example.describe_project()
```
### `chapter_09/partial_programs/importing_classes/importing_4_importing_module_into_module/electric_car.py`

**练习**
1. 参考 `MultimediaProject` 类，创建一个属于你自己的翻译案例实例。
2. 输出实例的主要属性，并尝试调用至少一个不需要额外参数的方法。

**参考答案**
```python
from chapter_09.partial_programs.importing_classes.importing_4_importing_module_into_module.electric_car import MultimediaProject

example = MultimediaProject('TransGlobe', 'EN->ZH')
print(vars(example))
example.add_subtitle_track()
```
### `chapter_09/partial_programs/importing_classes/importing_4_importing_module_into_module/my_cars.py`

**练习**
1. 基于原脚本，加入额外的状态输出或日志，用于追踪翻译项目的进度。
2. 将扩展后的程序运行结果整理成文字说明，与同学分享。

**参考答案**
```python
from car import TranslationProject
from electric_car import MultimediaProject

project = TranslationProject('GlobalTech', 'EN->ZH')
video_project = MultimediaProject('CreativeMedia', 'EN->ES')
video_project.add_subtitle_track()

print(project.describe_project())
print(video_project.describe_project())
print(f"Subtitle tracks: {video_project.subtitle_tracks}")

print("\n练习扩展：记录至少一条你在翻译项目中学到的新经验。")
```
### `chapter_09/partial_programs/inheritance/electric_car_0_first_version.py`

**练习**
1. 参考 `TranslationProject` 类，创建一个属于你自己的翻译案例实例。
2. 输出实例的主要属性，并尝试调用至少一个不需要额外参数的方法。

**参考答案**
```python
from chapter_09.partial_programs.inheritance.electric_car_0_first_version import TranslationProject

example = TranslationProject('TransGlobe', 'EN->ZH')
print(vars(example))
```
### `chapter_09/partial_programs/inheritance/electric_car_1_child_attributes_methods.py`

**练习**
1. 参考 `TranslationProject` 类，创建一个属于你自己的翻译案例实例。
2. 输出实例的主要属性，并尝试调用至少一个不需要额外参数的方法。

**参考答案**
```python
from chapter_09.partial_programs.inheritance.electric_car_1_child_attributes_methods import TranslationProject

example = TranslationProject('TransGlobe', 'EN->ZH')
print(vars(example))
example.describe_project()
```
### `chapter_09/partial_programs/inheritance/electric_car_2_instances_as_attributes.py`

**练习**
1. 参考 `SubtitlePackage` 类，创建一个属于你自己的翻译案例实例。
2. 输出实例的主要属性，并尝试调用至少一个不需要额外参数的方法。

**参考答案**
```python
from chapter_09.partial_programs.inheritance.electric_car_2_instances_as_attributes import SubtitlePackage

example = SubtitlePackage()
print(vars(example))
example.describe_package()
```
### `chapter_09/partial_programs/inheritance/electric_car_3_battery_get_range.py`

**练习**
1. 参考 `SubtitlePackage` 类，创建一个属于你自己的翻译案例实例。
2. 输出实例的主要属性，并尝试调用至少一个不需要额外参数的方法。

**参考答案**
```python
from chapter_09.partial_programs.inheritance.electric_car_3_battery_get_range import SubtitlePackage

example = SubtitlePackage(subtitle_tracks='示例信息')
print(vars(example))
example.describe_package()
```
### `chapter_09/partial_programs/working_with_classes_instances/car_0_first_version.py`

**练习**
1. 参考 `TranslationProject` 类，创建一个属于你自己的翻译案例实例。
2. 输出实例的主要属性，并尝试调用至少一个不需要额外参数的方法。

**参考答案**
```python
from chapter_09.partial_programs.working_with_classes_instances.car_0_first_version import TranslationProject

example = TranslationProject('TransGlobe', 'EN->ZH')
print(vars(example))
```
### `chapter_09/partial_programs/working_with_classes_instances/car_1_default_value.py`

**练习**
1. 参考 `TranslationProject` 类，创建一个属于你自己的翻译案例实例。
2. 输出实例的主要属性，并尝试调用至少一个不需要额外参数的方法。

**参考答案**
```python
from chapter_09.partial_programs.working_with_classes_instances.car_1_default_value import TranslationProject

example = TranslationProject('TransGlobe', 'EN->ZH')
print(vars(example))
example.describe_project()
```
### `chapter_09/partial_programs/working_with_classes_instances/car_2_modifying_attributes_directly.py`

**练习**
1. 参考 `TranslationProject` 类，创建一个属于你自己的翻译案例实例。
2. 输出实例的主要属性，并尝试调用至少一个不需要额外参数的方法。

**参考答案**
```python
from chapter_09.partial_programs.working_with_classes_instances.car_2_modifying_attributes_directly import TranslationProject

example = TranslationProject('TransGlobe', 'EN->ZH')
print(vars(example))
```
### `chapter_09/partial_programs/working_with_classes_instances/car_3_modifying_through_method.py`

**练习**
1. 参考 `TranslationProject` 类，创建一个属于你自己的翻译案例实例。
2. 输出实例的主要属性，并尝试调用至少一个不需要额外参数的方法。

**参考答案**
```python
from chapter_09.partial_programs.working_with_classes_instances.car_3_modifying_through_method import TranslationProject

example = TranslationProject('TransGlobe', 'EN->ZH')
print(vars(example))
```
### `chapter_09/partial_programs/working_with_classes_instances/car_4_reject_rollbacks.py`

**练习**
1. 参考 `TranslationProject` 类，创建一个属于你自己的翻译案例实例。
2. 输出实例的主要属性，并尝试调用至少一个不需要额外参数的方法。

**参考答案**
```python
from chapter_09.partial_programs.working_with_classes_instances.car_4_reject_rollbacks import TranslationProject

example = TranslationProject('TransGlobe', 'EN->ZH')
print(vars(example))
```
### `chapter_09/partial_programs/working_with_classes_instances/car_5_incrementing_attribute.py`

**练习**
1. 参考 `TranslationProject` 类，创建一个属于你自己的翻译案例实例。
2. 输出实例的主要属性，并尝试调用至少一个不需要额外参数的方法。

**参考答案**
```python
from chapter_09.partial_programs.working_with_classes_instances.car_5_incrementing_attribute import TranslationProject

example = TranslationProject('TransGlobe', 'EN->ZH')
print(vars(example))
```

## Chapter 10
### `chapter_10/exceptions/alice.py`

**练习**
1. 基于原脚本，加入额外的状态输出或日志，用于追踪翻译项目的进度。
2. 将扩展后的程序运行结果整理成文字说明，与同学分享。

**参考答案**
```python
from pathlib import Path

path = Path('alice.txt')
try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f"Sorry, the reference file {path} is missing.")
else:
    words = contents.split()
    num_words = len(words)
    print(f"The file {path} contains about {num_words} words to translate.")

print("\n练习扩展：记录至少一条你在翻译项目中学到的新经验。")
```
### `chapter_10/exceptions/division_calculator.py`

**练习**
1. 基于原脚本，加入额外的状态输出或日志，用于追踪翻译项目的进度。
2. 将扩展后的程序运行结果整理成文字说明，与同学分享。

**参考答案**
```python
print("Enter two numbers to calculate average words per day.")
print("Enter 'q' to quit.")

while True:
    total_words = input("Total words: ")
    if total_words == 'q':
        break
    days = input("Days available: ")
    if days == 'q':
        break
    try:
        words_per_day = int(total_words) / int(days)
    except ZeroDivisionError:
        print("You can't schedule zero days!")
    else:
        print(f"You need to translate {words_per_day:.0f} words per day.")

print("\n练习扩展：记录至少一条你在翻译项目中学到的新经验。")
```
### `chapter_10/exceptions/word_count.py`

**练习**
1. 使用 `count_words` 函数模拟新的翻译场景输入。
2. 观察返回结果或输出，并记录参数（例如：path）。

**参考答案**
```python
from chapter_10.exceptions.word_count import count_words

result = count_words('示例信息')
print(result)
```
### `chapter_10/partial_programs/exceptions/alice_1_handline_filenotfounderror.py`

**练习**
1. 基于原脚本，加入额外的状态输出或日志，用于追踪翻译项目的进度。
2. 将扩展后的程序运行结果整理成文字说明，与同学分享。

**参考答案**
```python
from pathlib import Path


path = Path('alice.txt')
try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f"Sorry, the file {path} does not exist.")

print("\n练习扩展：记录至少一条你在翻译项目中学到的新经验。")
```
### `chapter_10/partial_programs/exceptions/alice_2_analyzing_text.py`

**练习**
1. 基于原脚本，加入额外的状态输出或日志，用于追踪翻译项目的进度。
2. 将扩展后的程序运行结果整理成文字说明，与同学分享。

**参考答案**
```python
from pathlib import Path


path = Path('alice.txt')
try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f"Sorry, the file {path} does not exist.")
else:
    # Count the approximate number of words in the file:
    words = contents.split()
    num_words = len(words)
    print(f"The file {path} has about {num_words} words.")

print("\n练习扩展：记录至少一条你在翻译项目中学到的新经验。")
```
### `chapter_10/partial_programs/exceptions/division_calculator_1_try_except.py`

**练习**
1. 基于原脚本，加入额外的状态输出或日志，用于追踪翻译项目的进度。
2. 将扩展后的程序运行结果整理成文字说明，与同学分享。

**参考答案**
```python
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")

print("\n练习扩展：记录至少一条你在翻译项目中学到的新经验。")
```
### `chapter_10/partial_programs/exceptions/division_calculator_2_prevent_crashes.py`

**练习**
1. 基于原脚本，加入额外的状态输出或日志，用于追踪翻译项目的进度。
2. 将扩展后的程序运行结果整理成文字说明，与同学分享。

**参考答案**
```python
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    answer = int(first_number) / int(second_number)
    print(answer)

print("\n练习扩展：记录至少一条你在翻译项目中学到的新经验。")
```
### `chapter_10/partial_programs/exceptions/division_calculator_3_else_block.py`

**练习**
1. 基于原脚本，加入额外的状态输出或日志，用于追踪翻译项目的进度。
2. 将扩展后的程序运行结果整理成文字说明，与同学分享。

**参考答案**
```python
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)

print("\n练习扩展：记录至少一条你在翻译项目中学到的新经验。")
```
### `chapter_10/partial_programs/exceptions/word_count_0_first_version.py`

**练习**
1. 使用 `count_words` 函数模拟新的翻译场景输入。
2. 观察返回结果或输出，并记录参数（例如：path）。

**参考答案**
```python
from chapter_10.partial_programs.exceptions.word_count_0_first_version import count_words

result = count_words('示例信息')
print(result)
```
### `chapter_10/partial_programs/exceptions/word_count_1_multiple_texts.py`

**练习**
1. 使用 `count_words` 函数模拟新的翻译场景输入。
2. 观察返回结果或输出，并记录参数（例如：path）。

**参考答案**
```python
from chapter_10.partial_programs.exceptions.word_count_1_multiple_texts import count_words

result = count_words('示例信息')
print(result)
```
### `chapter_10/partial_programs/exceptions/word_count_2_failing_silently.py`

**练习**
1. 使用 `count_words` 函数模拟新的翻译场景输入。
2. 观察返回结果或输出，并记录参数（例如：path）。

**参考答案**
```python
from chapter_10.partial_programs.exceptions.word_count_2_failing_silently import count_words

result = count_words('示例信息')
print(result)
```
### `chapter_10/partial_programs/reading_from_a_file/file_reader_0_first_version.py`

**练习**
1. 基于原脚本，加入额外的状态输出或日志，用于追踪翻译项目的进度。
2. 将扩展后的程序运行结果整理成文字说明，与同学分享。

**参考答案**
```python
from pathlib import Path


path = Path('pi_digits.txt')
contents = path.read_text()
print(contents)

print("\n练习扩展：记录至少一条你在翻译项目中学到的新经验。")
```
### `chapter_10/partial_programs/reading_from_a_file/file_reader_1_remove_blank_line.py`

**练习**
1. 基于原脚本，加入额外的状态输出或日志，用于追踪翻译项目的进度。
2. 将扩展后的程序运行结果整理成文字说明，与同学分享。

**参考答案**
```python
from pathlib import Path


path = Path('pi_digits.txt')
contents = path.read_text()
contents = contents.rstrip()
print(contents)

print("\n练习扩展：记录至少一条你在翻译项目中学到的新经验。")
```
### `chapter_10/partial_programs/reading_from_a_file/file_reader_2_chained_methods.py`

**练习**
1. 基于原脚本，加入额外的状态输出或日志，用于追踪翻译项目的进度。
2. 将扩展后的程序运行结果整理成文字说明，与同学分享。

**参考答案**
```python
from pathlib import Path


path = Path('pi_digits.txt')
contents = path.read_text().rstrip()
print(contents)

print("\n练习扩展：记录至少一条你在翻译项目中学到的新经验。")
```
### `chapter_10/partial_programs/reading_from_a_file/file_reader_3_accessing_lines.py`

**练习**
1. 基于原脚本，加入额外的状态输出或日志，用于追踪翻译项目的进度。
2. 将扩展后的程序运行结果整理成文字说明，与同学分享。

**参考答案**
```python
from pathlib import Path


path = Path('pi_digits.txt')
contents = path.read_text()

lines = contents.splitlines()
for line in lines:
  print(line)

print("\n练习扩展：记录至少一条你在翻译项目中学到的新经验。")
```
### `chapter_10/partial_programs/reading_from_a_file/pi_birthday.py`

**练习**
1. 基于原脚本，加入额外的状态输出或日志，用于追踪翻译项目的进度。
2. 将扩展后的程序运行结果整理成文字说明，与同学分享。

**参考答案**
```python
from pathlib import Path


path = Path('pi_million_digits.txt')
contents = path.read_text()

lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.lstrip()

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")

print("\n练习扩展：记录至少一条你在翻译项目中学到的新经验。")
```
### `chapter_10/partial_programs/reading_from_a_file/pi_string_0_first_version.py`

**练习**
1. 基于原脚本，加入额外的状态输出或日志，用于追踪翻译项目的进度。
2. 将扩展后的程序运行结果整理成文字说明，与同学分享。

**参考答案**
```python
from pathlib import Path


path = Path('pi_digits.txt')
contents = path.read_text()

lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line
    
print(pi_string)
print(len(pi_string))

print("\n练习扩展：记录至少一条你在翻译项目中学到的新经验。")
```
### `chapter_10/partial_programs/reading_from_a_file/pi_string_1_lstrip.py`

**练习**
1. 基于原脚本，加入额外的状态输出或日志，用于追踪翻译项目的进度。
2. 将扩展后的程序运行结果整理成文字说明，与同学分享。

**参考答案**
```python
from pathlib import Path


path = Path('pi_digits.txt')
contents = path.read_text()

lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.lstrip()
    
print(pi_string)
print(len(pi_string))

print("\n练习扩展：记录至少一条你在翻译项目中学到的新经验。")
```
### `chapter_10/partial_programs/reading_from_a_file/pi_string_2_million_digits.py`

**练习**
1. 基于原脚本，加入额外的状态输出或日志，用于追踪翻译项目的进度。
2. 将扩展后的程序运行结果整理成文字说明，与同学分享。

**参考答案**
```python
from pathlib import Path


path = Path('pi_million_digits.txt')
contents = path.read_text()

lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.lstrip()

print(f"{pi_string[:52]}...")
print(len(pi_string))

print("\n练习扩展：记录至少一条你在翻译项目中学到的新经验。")
```
### `chapter_10/partial_programs/storing_data/greet_user.py`

**练习**
1. 基于原脚本，加入额外的状态输出或日志，用于追踪翻译项目的进度。
2. 将扩展后的程序运行结果整理成文字说明，与同学分享。

**参考答案**
```python
from pathlib import Path
import json


path = Path('username.json')
contents = path.read_text()
username = json.loads(contents)

print(f"Welcome back, {username}!")

print("\n练习扩展：记录至少一条你在翻译项目中学到的新经验。")
```
### `chapter_10/partial_programs/storing_data/number_reader.py`

**练习**
1. 基于原脚本，加入额外的状态输出或日志，用于追踪翻译项目的进度。
2. 将扩展后的程序运行结果整理成文字说明，与同学分享。

**参考答案**
```python
from pathlib import Path
import json

path = Path('numbers.json')
contents = path.read_text()
numbers = json.loads(contents)

print(numbers)

print("\n练习扩展：记录至少一条你在翻译项目中学到的新经验。")
```
### `chapter_10/partial_programs/storing_data/number_writer.py`

**练习**
1. 在 `numbers` 列表中补充两项新的语言服务资源。
2. 遍历扩展后的列表，为每个条目写一句使用计划。

**参考答案**
```python
numbers = [2, 3, 5, 7, 11, 13]

extra_resources = ['术语云平台', '翻译记忆体检查']
extended_numbers = list(numbers) + extra_resources
for item in extended_numbers:
    print(f"准备评估 {item} 在翻译项目中的应用。")
```
### `chapter_10/partial_programs/storing_data/remember_me_0_first_version.py`

**练习**
1. 基于原脚本，加入额外的状态输出或日志，用于追踪翻译项目的进度。
2. 将扩展后的程序运行结果整理成文字说明，与同学分享。

**参考答案**
```python
from pathlib import Path
import json


username = input("What is your name? ")

path = Path('username.json')
contents = json.dumps(username)
path.write_text(contents)

print(f"We'll remember you when you come back, {username}!")

print("\n练习扩展：记录至少一条你在翻译项目中学到的新经验。")
```
### `chapter_10/partial_programs/storing_data/remember_me_1_combined.py`

**练习**
1. 基于原脚本，加入额外的状态输出或日志，用于追踪翻译项目的进度。
2. 将扩展后的程序运行结果整理成文字说明，与同学分享。

**参考答案**
```python
from pathlib import Path
import json


path = Path('username.json')
if path.exists():
    contents = path.read_text()
    username = json.loads(contents)
    print(f"Welcome back, {username}!")
else:
    username = input("What is your name? ")
    contents = json.dumps(username)
    path.write_text(contents)
    print(f"We'll remember you when you come back, {username}!")

print("\n练习扩展：记录至少一条你在翻译项目中学到的新经验。")
```
### `chapter_10/partial_programs/storing_data/remember_me_2_refactoring.py`

**练习**
1. 使用 `greet_user` 函数模拟新的翻译场景输入。
2. 观察返回结果或输出，并记录参数（例如：默认参数）。

**参考答案**
```python
from chapter_10.partial_programs.storing_data.remember_me_2_refactoring import greet_user

result = greet_user()
print(result)
```
### `chapter_10/partial_programs/storing_data/remember_me_3_refactoring_two_functions.py`

**练习**
1. 使用 `get_stored_username` 函数模拟新的翻译场景输入。
2. 观察返回结果或输出，并记录参数（例如：path）。

**参考答案**
```python
from chapter_10.partial_programs.storing_data.remember_me_3_refactoring_two_functions import get_stored_username

result = get_stored_username('示例信息')
print(result)
```
### `chapter_10/partial_programs/storing_data/remember_me_4_refactoring_three_functions.py`

**练习**
1. 使用 `get_stored_username` 函数模拟新的翻译场景输入。
2. 观察返回结果或输出，并记录参数（例如：path）。

**参考答案**
```python
from chapter_10.partial_programs.storing_data.remember_me_4_refactoring_three_functions import get_stored_username

result = get_stored_username('示例信息')
print(result)
```
### `chapter_10/partial_programs/writing_to_a_file/write_message_1_multiple_lines.py`

**练习**
1. 基于原脚本，加入额外的状态输出或日志，用于追踪翻译项目的进度。
2. 将扩展后的程序运行结果整理成文字说明，与同学分享。

**参考答案**
```python
from pathlib import Path


contents = "I love programming.\n"
contents += "I love creating new games.\n"
contents += "I also love working with data.\n"

path = Path('programming.txt')
path.write_text(contents)

print("\n练习扩展：记录至少一条你在翻译项目中学到的新经验。")
```
### `chapter_10/reading_from_a_file/file_reader.py`

**练习**
1. 基于原脚本，加入额外的状态输出或日志，用于追踪翻译项目的进度。
2. 将扩展后的程序运行结果整理成文字说明，与同学分享。

**参考答案**
```python
from pathlib import Path

path = Path('pi_digits.txt')
contents = path.read_text()

print("Sample translation memory snippet:")
for line in contents.splitlines():
    print(line)

print("\n练习扩展：记录至少一条你在翻译项目中学到的新经验。")
```
### `chapter_10/reading_from_a_file/pi_birthday.py`

**练习**
1. 基于原脚本，加入额外的状态输出或日志，用于追踪翻译项目的进度。
2. 将扩展后的程序运行结果整理成文字说明，与同学分享。

**参考答案**
```python
from pathlib import Path

path = Path('pi_digits.txt')
contents = path.read_text().strip().replace('\n', '')

phrase = input("Enter a sequence to search in the translation memory snippet: ")

if phrase in contents:
    print("Your sequence appears in the snippet!")
else:
    print("Sequence not found.")

print("\n练习扩展：记录至少一条你在翻译项目中学到的新经验。")
```
### `chapter_10/reading_from_a_file/pi_string.py`

**练习**
1. 基于原脚本，加入额外的状态输出或日志，用于追踪翻译项目的进度。
2. 将扩展后的程序运行结果整理成文字说明，与同学分享。

**参考答案**
```python
from pathlib import Path

path = Path('pi_digits.txt')
contents = path.read_text().strip()

print("Translation memory string without line breaks:")
print(contents)
print(len(contents))

print("\n练习扩展：记录至少一条你在翻译项目中学到的新经验。")
```
### `chapter_10/storing_data/greet_user.py`

**练习**
1. 基于原脚本，加入额外的状态输出或日志，用于追踪翻译项目的进度。
2. 将扩展后的程序运行结果整理成文字说明，与同学分享。

**参考答案**
```python
from pathlib import Path
import json

path = Path('username.json')
username = json.loads(path.read_text())

print(f"Welcome back, Translator {username}! Ready for your next project?")

print("\n练习扩展：记录至少一条你在翻译项目中学到的新经验。")
```
### `chapter_10/storing_data/number_reader.py`

**练习**
1. 基于原脚本，加入额外的状态输出或日志，用于追踪翻译项目的进度。
2. 将扩展后的程序运行结果整理成文字说明，与同学分享。

**参考答案**
```python
from pathlib import Path
import json

path = Path('numbers.json')
numbers = json.loads(path.read_text())

print("Previously analyzed word counts:")
for number in numbers:
    print(number)

print("\n练习扩展：记录至少一条你在翻译项目中学到的新经验。")
```
### `chapter_10/storing_data/number_writer.py`

**练习**
1. 在 `numbers` 列表中补充两项新的语言服务资源。
2. 遍历扩展后的列表，为每个条目写一句使用计划。

**参考答案**
```python
numbers = [1500, 2750, 3200, 4800]

extra_resources = ['术语云平台', '翻译记忆体检查']
extended_numbers = list(numbers) + extra_resources
for item in extended_numbers:
    print(f"准备评估 {item} 在翻译项目中的应用。")
```
### `chapter_10/storing_data/remember_me.py`

**练习**
1. 基于原脚本，加入额外的状态输出或日志，用于追踪翻译项目的进度。
2. 将扩展后的程序运行结果整理成文字说明，与同学分享。

**参考答案**
```python
from pathlib import Path
import json

path = Path('username.json')
if path.exists():
    username = json.loads(path.read_text())
    print(f"Welcome back, Translator {username}!")
else:
    username = input("What is your translator name? ")
    path.write_text(json.dumps(username))
    print("We'll remember your preferences next time.")

print("\n练习扩展：记录至少一条你在翻译项目中学到的新经验。")
```
