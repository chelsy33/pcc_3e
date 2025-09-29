from pathlib import Path
import json

numbers = [1500, 2750, 3200, 4800]
path = Path('numbers.json')
path.write_text(json.dumps(numbers))
