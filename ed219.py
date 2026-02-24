n = int(input().strip())
epizod = {}
for _ in range(n):
    name, coun = input().split()
    coun = int(coun)
    if name in epizod:
        epizod[name] += coun
    else:
        epizod[name] = coun
for dorama in sorted(epizod.keys()):
    print(dorama, epizod[dorama])