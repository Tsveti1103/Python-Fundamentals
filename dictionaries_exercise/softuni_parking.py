count = int(input())
parking = {}

for _ in range(count):
    split_data = input().split()
    if split_data[0] == "register":
        username = split_data[1]
        license = split_data[2]
        if username in parking:
            print(f"ERROR: already registered with plate number {license}")
        else:
            parking[username] = license
            print(f"{username} registered {license} successfully")
    elif split_data[0] == "unregister":
        username = split_data[1]
        if username not in parking:
            print(f"ERROR: user {username} not found")
        else:
            del parking[username]
            print(f"{username} unregistered successfully")

for username, license in parking.items():
    print(f"{username} => {license}")
