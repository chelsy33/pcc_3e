from pathlib import Path
import json

path = Path('username.json')
username = json.loads(path.read_text())

print(f"Welcome back, Translator {username}! Ready for your next project?")
