# ini-parser
ini parser

# Usage
### data.ini
```ini
[section]
value = 42
```

### file.py
```py
from ini_parser import Parser

p = Parser()
with open("data.ini") as f:
  p.load(f)

print(p.section.value) # 42
```
