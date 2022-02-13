numbers = input().split()
for i in range(len(numbers)):
    print(max(numbers), end="")
    numbers.remove(max(numbers))