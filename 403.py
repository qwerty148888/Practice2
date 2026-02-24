def ok(n):
    for i in range(0, n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i
n = int(input())
for q in ok(n):
    print(q, end = " ")