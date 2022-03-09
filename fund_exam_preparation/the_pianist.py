n = int(input())
pieces = {}
for _ in range(n):
    piece = input().split("|")
    name = piece[0]
    composer = piece[1]
    key = piece[2]
    pieces[name] = [composer, key]
command = input().split("|")
while command[0] != "Stop":
    if command[0] == "Add":
        piece = command[1]
        composer = command[2]
        key = command[3]
        if piece in pieces:
            print(f"{piece} is already in the collection!")
        else:
            pieces[piece] = [composer, key]
            print(f"{piece} by {composer} in {key} added to the collection!")

    elif command[0] == "Remove":
        piece = command[1]
        if piece in pieces:
            pieces.pop(piece)
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    elif command[0] == "ChangeKey":
        piece = command[1]
        new_key = command[2]
        if piece in pieces:
            pieces[piece][1] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    command = input().split("|")

res = sorted(pieces.items(), key=lambda kvp: (kvp[0], kvp[1][0]))
for p in res:
    piece = p[0]
    composer = p[1][0]
    key = p[1][1]
    print(f"{piece} -> Composer: {composer}, Key: {key}")
