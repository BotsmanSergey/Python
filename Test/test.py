import re
line = re.sub(r'<a href=\"(.*)\".*>1</a>', r'\1', "<a href=\"https://stepic.org/media/attachments/lesson/24472/sample1.html\">1</a>")
print(line)