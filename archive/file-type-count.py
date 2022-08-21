from pathlib import Path
from collections import Counter
import json

p = Path('./docs')

file_types = [i.suffix for i in p.rglob('*')]

c = Counter()

for t in file_types: 
    c[t] += 1

print(c)

with open('filetypes.json','w') as f:
    json.dump(c, f, sort_keys=True, indent=4)