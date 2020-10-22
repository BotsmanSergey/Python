spam = '%D0%A3%D1%87%D0%B5%D0%BD%D1%8C%D0%B5%20-%20%D1%81%D0%B2%D0%B5%D1%82'
eggs = spam.split('%')
b = '\\x'
new_spam = b.join(eggs)
print(new_spam)
b_spam = b'\xD0\xA3\xD1\x87\xD0\xB5\xD0\xBD\xD1\x8C\xD0\xB5\x20-\x20\xD1\x81\xD0\xB2\xD0\xB5\xD1\x82'
result = b_spam.decode('utf-8')
print(result)

from urllib.parse import unquote_plus
a = unquote_plus('%D0%A3%D1%87%D0%B5%D0%BD%D1%8C%D0%B5%20-%20%D1%81%D0%B2%D0%B5%D1%82')
print(a)