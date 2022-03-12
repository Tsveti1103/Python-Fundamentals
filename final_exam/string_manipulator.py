string = input()
command = input().split()
while command[0] != "End":
    if command[0] == "Translate":
        char, replacement = command[1:]
        string = string.replace(char, replacement)
        print(string)
    elif command[0] == "Includes":
        substring = command[1]
        if substring in string:
            print(True)
        else:
            print(False)
    elif command[0] == "Start":
        substring = command[1]
        if substring == string[:len(substring)]:
            print(True)
        else:
            print(False)
    elif command[0] == "Lowercase":
        string = string.lower()
        print(string)
    elif command[0] == "FindIndex":
        char = command[1]
        indexes = []
        for i, v in enumerate(string):
            if char == v:
                indexes.append(i)
        if indexes:
            print(indexes[-1])
        else:
            print(-1)
    elif command[0] == "Remove":
        start_index = int(command[1])
        count = int(command[2])
        end_index = start_index + count
        string = string[:start_index] + string[end_index:]
        print(string)
    command = input().split()
