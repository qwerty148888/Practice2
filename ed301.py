s = input()
valid = True
for word in s:
    if int(word) % 2 != 0:
        valid = False
        break
if valid:
    print("Valid")
else:
    print("Not valid")