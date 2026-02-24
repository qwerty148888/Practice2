n = int(input().strip())
arr = [input().strip() for _ in range(n)]

result = sum(1 for num in set(arr) if arr.count(num) == 3)
print(result)
