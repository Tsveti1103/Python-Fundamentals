contacts = input().split("-")
phonebook = {}
while len(contacts) > 1:
    name = contacts[0]
    phone_number = contacts[1]
    phonebook[name] = phone_number
    contacts = input().split("-")
n = int(contacts[0])
for _ in range(n):
    name = input()
    if name in phonebook:
        print(f"{name} -> {phonebook[name]}")
    else:
        print(f"Contact {name} does not exist.")
