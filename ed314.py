n = int(input())
doc = {}
for _ in range(n):
    parts = input().split()
    cmd = parts[0]
    if cmd == "set":
        key, value = parts[1], parts[2]
        doc[key] = value
    elif cmd == "get":
        key = parts[1]
        if key in doc:
            print(doc[key])
        else:
            print("poshel nahui")