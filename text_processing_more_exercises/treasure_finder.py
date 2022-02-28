key = input().split()
command = input()
while command != "find":
    new_string = ""
    index = 0
    for c in command:
        new = ord(c) - int(key[index])
        index += 1
        new_string += chr(new)
        if index == len(key):
            index = 0
    new_string = new_string[new_string.index("&") + 1:]
    item = new_string[:new_string.index("&")]
    coordinates = new_string[new_string.index("<") + 1:new_string.index(">")]
    print(f"Found {item} at {coordinates}")
    command = input()
