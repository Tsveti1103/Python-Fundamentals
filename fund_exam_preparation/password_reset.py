password = input()
command = input().split()

while command[0] != "Done":
    if command[0] == "TakeOdd":
        new = ''
        for i, v in enumerate(password):
            if i % 2 != 0:
                new += v
        password = new
        print(password)

    elif command[0] == "Cut":
        start_index = int(command[1])
        length = int(command[2])
        end_index = start_index + length
        to_remove = password[start_index:end_index]
        password = password.replace(to_remove, "", 1)
        print(password)

    elif command[0] == "Substitute":
        substring = command[1]
        new_string = command[2]
        if substring in password:
            password = password.replace(substring, new_string)
            print(password)
        else:
            print("Nothing to replace!")
    command = input().split()
print(f"Your password is: {password}")
