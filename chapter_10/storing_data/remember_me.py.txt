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
