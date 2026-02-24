nums = list(map(int, input().split()))
evensum = 0
oddsum = 0
for i in range(len(nums)):
    if i % 2 == 0:
        oddsum += nums[i]
    else:
        evensum += nums[i]
print(f"Result: {oddsum} {evensum}")
