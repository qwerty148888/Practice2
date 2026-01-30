n = int(input())
numbers = list(map(int, input().split()))
maxv = numbers[0]
minv = numbers[0]
for ch in numbers[1:]:
    if maxv < ch:
        maxv = ch
for ch in numbers[1:]:
    if minv > ch:
        minv = ch
for i in range(n):
    if numbers[i] == maxv:
        numbers[i] = minv
print(*numbers)
