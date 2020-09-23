import sys
import re
pattern = r"\bcat\b"

for line in sys.stdin:
    line = line.rstrip()
    # process line
    match = re.findall(pattern, line)
    if len(match)> 0:
        print(line)
    else: continue