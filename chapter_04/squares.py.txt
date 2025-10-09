# 知识点：在循环中逐步 append() 数据，记录翻译练习的里程碑。

word_counts = []
for count in range(100, 1001, 100):
    word_counts.append(count)

print("Milestones for translation practice (word counts):")
print(word_counts)
