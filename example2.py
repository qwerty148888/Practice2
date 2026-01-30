n = int(input())
numbers = list(map(int, input().split()))
maxval = max(numbers)
pos = numbers.index(maxval) + 1
print(pos)
