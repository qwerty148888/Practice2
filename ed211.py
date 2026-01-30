n, a, b = map(int, input().split())
arr = list(map(int, input().split()))
arr[a - 1:b] = arr[a - 1:b][::-1]
print(*arr)