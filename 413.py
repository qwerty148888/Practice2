import json

data = json.loads(input())
q = int(input())

for _ in range(q):
    path = input()
    current = data
    found = True

    parts = path.split('.')

    for part in parts:
        try:
            # сначала получаем ключ до первого [
            while True:
                if '[' in part:
                    key = part[:part.index('[')]
                    
                    if key:
                        current = current[key]

                    # обрабатываем все индексы подряд
                    while '[' in part:
                        start = part.index('[')
                        end = part.index(']')
                        index = int(part[start+1:end])
                        current = current[index]
                        part = part[end+1:]
                else:
                    current = current[part]
                    break

                break

        except (KeyError, IndexError, TypeError, ValueError):
            found = False
            break

    if found:
        print(json.dumps(current, separators=(',', ':')))
    else:
        print("NOT_FOUND")