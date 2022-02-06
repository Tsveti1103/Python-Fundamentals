string = input().split(", ")
nums = list(map(int, string))
result = []
for i, v in enumerate(nums):
    if v % 2 == 0:
        result.append(i)
print(result)
