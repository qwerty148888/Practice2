nums = list(map(int, input().split()))
s = []
for some in nums:
    if some > 1:
        for i in range(2, some):
            if some % i == 0:
                break
        else:
            s.append(some)
if s:
    print(*s)
else:
    print("No primes")