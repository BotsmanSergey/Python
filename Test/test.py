import re
pattern = r"(abc)|(test|text)*"
string = "testtext"
match = re.match(pattern, string)
print(match) #--> span = (0, 3) , match = "abc"
print(match.groups()) #--> ('testtext', None, 'text')  #сперва показана группа в скобках (abc|(test|text)*, потом abc, затем test|text (показан text т.к. это последнее вхождение)
print(match.group(0))
print(match.group(1))
print(match.group(2))
print(match.group(3))
