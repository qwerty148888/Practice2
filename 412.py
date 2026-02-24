import json

a = json.loads(input())
b = json.loads(input())

def deepdi(a, b, path=""):
    diffs = []
    keys = set(a.keys()) | set(b.keys())

    for key in keys:
        curpath = f"{path}.{key}" if path else key

        va = a.get(key, "<missing>")
        vb = b.get(key, "<missing>")

        if isinstance(va, dict) and isinstance(vb, dict):
            diffs.extend(deepdi(va, vb, curpath))
        else:
            if va != vb:

                # Если значение <missing>, печатаем без json.dumps
                if va == "<missing>":
                    old_value = "<missing>"
                else:
                    old_value = json.dumps(va, separators=(',', ':'))

                if vb == "<missing>":
                    new_value = "<missing>"
                else:
                    new_value = json.dumps(vb, separators=(',', ':'))

                diffs.append(f"{curpath} : {old_value} -> {new_value}")

    return diffs


result = deepdi(a, b)

if result:
    for line in sorted(result):
        print(line)
else:
    print("No differences")