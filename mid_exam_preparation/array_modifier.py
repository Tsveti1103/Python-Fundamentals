numbers = [int(n) for n in input().split()]
command = input().split()
while command[0] != "end":
    if len(command) > 1:
        index_one = int(command[1])
        index_two = int(command[2])
    if command[0] == "swap":
        numbers[index_one], numbers[index_two] = numbers[index_two], numbers[index_one]
    elif command[0] == "multiply":
        numbers[index_one] = numbers[index_one] * numbers[index_two]
    elif command[0] == "decrease":
        for num in range(len(numbers)):
            numbers[num] -= 1
    command = input().split()
numbers = [str(e) for e in numbers]
print(", ".join(numbers))
