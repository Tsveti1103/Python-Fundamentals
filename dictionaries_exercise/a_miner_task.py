command = input()
count = 1
resources = []
quantities = []
collection = {}
while command != "stop":
    if count % 2 != 0:
        resources.append(command)
    else:
        quantities.append(int(command))
    command = input()
    count += 1

for index, res in enumerate(resources):
    if res not in collection:
        collection[res] = 0
    collection[res] += quantities[index]
for resource, quantity in collection.items():
    print(f"{resource} -> {quantity}")
