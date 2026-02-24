def tt(n):
    for i in range(0, n + 1):
        yield 2**i
n = int(input())
for q in tt(n):
    print(q, end = " ")