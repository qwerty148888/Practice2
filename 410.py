def wf(arr, k):
    for i in range(k):
        for ok in arr:
            yield ok
arr = input().split()
k = int(input())
for q in wf(arr, k):
    print(q, end = " ")