from pathlib import Path

path = Path('pi_digits.txt')
contents = path.read_text().strip()

print("Translation memory string without line breaks:")
print(contents)
print(len(contents))
