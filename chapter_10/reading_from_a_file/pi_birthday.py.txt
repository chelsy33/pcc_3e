from pathlib import Path

path = Path('pi_digits.txt')
contents = path.read_text().strip().replace('\n', '')

phrase = input("Enter a sequence to search in the translation memory snippet: ")

if phrase in contents:
    print("Your sequence appears in the snippet!")
else:
    print("Sequence not found.")
