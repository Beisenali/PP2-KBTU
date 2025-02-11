N = int(input())
a = (q for q in range(1, N+1))
for i in a:
    if i % 3 == 0 and i % 4 == 0: print(i)
    else: continue