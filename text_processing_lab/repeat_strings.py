string = input().split()
result = ""
for i in string:
    result += i * len(i)
print(result)
