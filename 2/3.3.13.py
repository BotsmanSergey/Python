import re, sys
# pattern = r"\ba+\b"

# for line in sys.stdin:
#     line = re.sub(pattern, "argh", line.rstrip(), count=1, flags=re.IGNORECASE)
#     print(line)
[print(re.sub(r'\b[aA]+\b', 'argh', line.rstrip(), 1)) for line in sys.stdin]