message = input()
command = input().split("|")
while command[0] != "Decode":
    if command[0] == "Move":
        n = int(command[1])
        message = message[n:] + message[:n]
    elif command[0] == "Insert":
        index = int(command[1])
        value = command[2]
        message = message[:index] + value + message[index:]
    elif command[0] == "ChangeAll":
        old = command[1]
        new = command[2]
        while old in message:
            message = message.replace(old, new)
    command = input().split("|")
print(f"The decrypted message is: {message}")
