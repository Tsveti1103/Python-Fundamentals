dragons_count = int(input())
dragons_type = {}
for i in range(dragons_count):
    dragons_info = input().split()
    d_type = dragons_info[0]
    name = dragons_info[1]
    damage = dragons_info[2]
    health = dragons_info[3]
    armor = dragons_info[4]
    if damage == "null":
        damage = 45
    else:
        damage = int(damage)
    if health == "null":
        health = 250
    else:
        health = int(health)
    if armor == "null":
        armor = 10
    else:
        armor = int(armor)
    if d_type not in dragons_type:
        dragons_type[d_type] = {name: [damage, health, armor]}
    if name not in dragons_type[d_type].keys():
        dragons_type[d_type].update({name: [damage, health, armor]})
    else:
        dragons_type[d_type][name] = [damage, health, armor]
new = {}
for type, d in dragons_type.items():
    total_damage = 0
    total_health = 0
    total_armor = 0
    for dragon, values in d.items():
        total_damage += values[0]
        total_health += values[1]
        total_armor += values[2]
    total_damage = f"{total_damage / len(d):.2f}"
    total_health = f"{total_health / len(d):.2f}"
    total_armor = f"{total_armor / len(d):.2f}"
    new[type] = [total_damage, total_health, total_armor]
dragons = {}
for key, value in dragons_type.items():
    sort = dict(sorted(value.items(), key=lambda kvp: kvp[0]))
    if key not in dragons:
        dragons[key] = sort
    else:
        dragons[key].append(sort)
for k, v in new.items():
    print(f"{k}::({v[0]}/{v[1]}/{v[2]})")
    for name, stat in dragons[k].items():
        print(f"-{name} -> damage: {stat[0]}, health: {stat[1]}, armor: {stat[2]}")
