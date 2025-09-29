deadlines = (2, 5)
print("Original turnaround windows:")
for days in deadlines:
    print(f"- {days} day(s) for standard translation")

print("\nUpdated turnaround windows:")
deadlines = (2, 3)
for days in deadlines:
    print(f"- {days} day(s) for urgent projects")
