n = int(input().strip())

surnames = set()

for i in range(n):
    surname = input().strip()
    surnames.add(surname)
print(len(surnames))