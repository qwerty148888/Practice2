def squares(a, b):
    for i in range(a, b+1):
        yield i**2

# Ввод диапазона
a = int(input("Enter start (a): "))
b = int(input("Enter end (b): "))

# Использование через цикл
for sq in squares(a, b):
    print(sq)