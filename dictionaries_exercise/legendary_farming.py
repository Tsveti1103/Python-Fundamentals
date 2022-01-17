key_materials = {"shards": "Shadowmourne", "fragments": "Valanyr", "motes": "Dragonwrath"}
items = {"shards": 0, "fragments": 0, "motes": 0}
junk_items = {}
is_obtained = False
while not is_obtained:
    data = input()
    split_data = data.split()
    for index in range(0, len(split_data), 2):
        quantity = int(split_data[index])
        material = split_data[index + 1].lower()
        if material in items:
            items[material] += quantity
        else:
            if material not in junk_items:
                junk_items[material] = 0
            junk_items[material] += quantity
        for material, quantity in items.items():
            if quantity >= 250:
                is_obtained = True
                items[material] -= 250
                print(f"{key_materials[material]} obtained!")
                break
        if is_obtained:
            break

sorted_items = sorted(items.items(), key=lambda kvpt: (-kvpt[1], kvpt[0]))
for material, quantity in sorted_items:
    print(f"{material}: {quantity}")
sorted_junk = sorted(junk_items.items(), key=lambda kvpt: kvpt[0])
for material, quantity in sorted_junk:
    print(f"{material}: {quantity}")
