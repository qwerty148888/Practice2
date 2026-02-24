# словарь для перевода
triplets = {
    "ONE": "1", "TWO": "2", "THR": "3", "FOU": "4", "FIV": "5",
    "SIX": "6", "SEV": "7", "EIG": "8", "NIN": "9", "ZER": "0"
}
# обратный словарь
digits = {v: k for k, v in triplets.items()}

expr = input().strip()

# ищем оператор
for op in ['+', '-', '*']:
    if op in expr:
        left, right = expr.split(op)
        operator = op
        break

# переводим триплеты в число
def decode(s):
    return int("".join(triplets[s[i:i+3]] for i in range(0, len(s), 3)))

# переводим число обратно в триплеты
def encode(num):
    return "".join(digits[d] for d in str(num))

a = decode(left)
b = decode(right)

# считаем результат
if operator == '+':
    res = a + b
elif operator == '-':
    res = a - b
else:  # '*'
    res = a * b

print(encode(res))
