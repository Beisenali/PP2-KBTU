data = ["apple", "banana", "orange"]

with open("fruits.txt", "w", encoding="utf-8") as file:
    file.writelines("\n".join(data))
