n = int(input())
numbers = input().split()
total = 0
for i in range(n):
    if int(numbers[i]) > 0:
        total += 1
print(total)print('New line')
