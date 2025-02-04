car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items() #item: brand Ford || keys brand || values ford

print(x) #before the change

car["year"] = 2020

print(x) #after the change