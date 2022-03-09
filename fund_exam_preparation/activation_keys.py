key = input()
command = input().split(">>>")
while command[0] != "Generate":
    if command[0] == "Contains":
        substring = command[1]
        if substring in key:
            print(f"{key} contains {substring}")
        else:
            print("Substring not found!")
    elif command[0] == "Flip":
        start_index = int(command[2])
        end_index = int(command[3])
        if command[1] == "Upper":
            key = key[:start_index] + key[start_index:end_index].upper() + key[end_index:]
        elif command[1] == "Lower":
            key = key[:start_index] + key[start_index:end_index].lower() + key[end_index:]
        print(key)
    elif command[0] == "Slice":
        start_index = int(command[1])
        end_index = int(command[2])
        key = key[:start_index] + key[end_index:]
        print(key)
    command = input().split(">>>")
print(f"Your activation key is: {key}")
