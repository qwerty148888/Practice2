n_commands = int(input())
g = 0
n = 0

for _ in range(n_commands):
    scope, value = input().split()
    value = int(value)
    if scope == "global":
        g += value
    elif scope == "nonlocal":
        n += value
    # local просто игнорируем, так как не влияет на g или n

print(g, n)