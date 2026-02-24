n = int(input().strip())
arr = [input().strip() for _ in range(n)]
for s in sorted(set(arr)):
    print(s, arr.index(s) + 1)