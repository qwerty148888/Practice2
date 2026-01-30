n = int(input())
arr = list(map(int, input().split()))
common = arr[0]
comc = arr.count(common)

for num in arr:
    c = arr.count(num)
    if (c > comc) or (c == comc and num < common):
        common = num
        comc = c
print(common)