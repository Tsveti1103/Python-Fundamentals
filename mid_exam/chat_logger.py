def exist(masage, all_chat):
    return masage in all_chat


chat = []
command = input().split()
while command[0] != "end":
    if command[0] == "Chat":
        chat.append(command[1])
    elif command[0] == "Delete":
        if exist(command[1], chat):
            chat.remove(command[1])
    elif command[0] == "Edit":
        if exist(command[1], chat):
            chat[chat.index(command[1])] = command[2]
    elif command[0] == "Pin":
        if exist(command[1], chat):
            chat.remove(command[1])
            chat.append(command[1])
    elif command[0] == "Spam":
        command = command[1:]
        chat.extend(command)
    command = input().split()
print("\n".join(chat))
