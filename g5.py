def countdown(n):
    for i in range(n, -1, -1):
        yield i

# Ввод числа
n = int(input("Enter n: "))

# Использование генератора
for num in countdown(n):
    print(num, end=' ')