# ini-parser
ini parser

# Usage
### data.ini
```ini
value_outside_section = 1

[section]
value = 2

[section2]
value = 3
value2 = 4
```

### file.py
```py
from ini_parser import Parser

p = Parser()
with open("data.ini") as f:
  p.load(f)

print(p.value_outside_section) # 1
print(p.section.value) # 2
print(p.section2.value) # 3
print(p.section2.value2) # 4
```
