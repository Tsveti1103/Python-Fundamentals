followers = {}
command = input().split(": ")
while command[0] != "Log out":
    if command[0] == "New follower":
        username = command[1]
        if username not in followers:
            followers[username] = 0
    elif command[0] == "Like":
        username = command[1]
        count = int(command[2])
        if username not in followers:
            followers[username] = 0
        followers[username] += count
    elif command[0] == "Comment":
        username = command[1]
        if username not in followers:
            followers[username] = 0
        followers[username] += 1
    elif command[0] == "Blocked":
        username = command[1]
        if username not in followers:
            print(f"{username} doesn't exist.")
        else:
            del followers[username]
    command = input().split(": ")
print(f"{len(followers)} followers")
sorted_followers = sorted(followers.items(), key=lambda kvp: (-kvp[1], kvp[0]))
for name, value in sorted_followers:
    print(f"{name}: {value}")
