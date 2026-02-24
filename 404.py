def ok(a, b):
    for i in range(a, b+1):
        yield i**2
a, b = map(int, input().split())
for q in ok(a,b):
    print(q)