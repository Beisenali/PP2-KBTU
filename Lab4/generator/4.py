a = int(input())
b = int(input())
squares = (i ** 2 for i in range(a, b+1))
for square in squares:
    print(square)