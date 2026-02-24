# Генератор квадратов
def square_generator(N):
    for i in range(1, N+1):
        yield i ** 2

# Пример использования
N = int(input("Enter N: "))
for square in square_generator(N):
    print(square)