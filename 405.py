def ok(n):
    for i in range(n, -1, -1):
        yield i
n = int(input())
for q in ok(n):
    print(q)
