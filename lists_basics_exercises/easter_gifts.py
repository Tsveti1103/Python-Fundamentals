gifts = input().split()
command = input()
if command == "No Money":
    gifts = []
while command != "No Money":
    command = command.split()
    if command[0] == "OutOfStock":
        for i, v in enumerate(gifts):
            if command[1] == v:
                gifts[i] = None
    elif command[0] == "Required":
        c = len(gifts)
        if len(gifts) > int(command[2]) > 0:
            gifts[int(command[2])] = command[1]
    elif command[0] == "JustInCase":
        gifts[-1] = command[1]
    command = input()
gifts = filter(None, gifts)

print(" ".join(gifts))
