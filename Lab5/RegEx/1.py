import re
file_path = "/Users/mtqcty/programming/TSIS Labs/Lab5/RegEx/row.txt"
with open(file_path, "r", encoding="utf-8") as file:
    txt = file.read()
pt1 = re.findall(r'ab*', txt)
pt2 = re.findall(r'ab{2.3}', txt)
pt3 = re.findall(r'\b[a-z]+_[a-z]+\b', txt)
pt4 = re.findall(r'[A-ZА-ЯЁ][a-zа-яё]+', txt)
pt5 = re.findall(r'a.*b', txt)
pt6 = re.sub(r'[ ,.]', ':', txt)
def snake_to_camel(snake_str):
    return ''.join(word.capitalize() for word in snake_str.split('_'))
pt7 = [snake_to_camel(match) for match in re.findall(r'\b[a-z]+_[a-z]+\b', txt)]
pt8 = re.split(r'(?=[A-ZА-ЯЁ])', txt)
pt9 = re.sub(r'([A-ZА-ЯЁ])', r' \1', txt)
pt10 = re.sub(r'(?<!^)(?=[A-ZА-ЯЁ])', '_', txt).lower()

print("1.", pt1)
print("2.", pt2)
print("3.", pt3)
print("4.", pt4)
print("5.", pt5)
print("6.", pt6[:300])
print("7.", pt7)
print("8.", pt8[:10])
print("9.", pt9[:300])
print("10.", pt10[:300])