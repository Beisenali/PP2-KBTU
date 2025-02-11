N = int(input())
a = (q for q in range(1, N+1))
for i in a:
    if i % 2 == 0: print(i, end = ",")
    else: continue