x = ("apple", "banana", "cherry")
y = list(x) 
y[1] = "kiwi"
x = tuple(y)

#y = list(thistuple)
#y.append("orange")

#thistuple += y

print(x)