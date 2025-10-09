# 知识点：捕获 ZeroDivisionError，确保除法计算器安全运行。

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
