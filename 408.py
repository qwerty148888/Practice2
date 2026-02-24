def prim(n):
    for i in range(2, n+1):
        pr = True
        for h in range(2, i):
            if i % h == 0:
                pr = False
        if pr:
            yield i
n = int(input())
for q in prim(n):
    print(q, end = " ")