import re

demons = sorted(''.join(input().split()).split(','))

for demon in demons:
    health = 0
    damage = 0
    name = demon
    health_symbols = re.findall(r"[^0-9-+*/.]", demon)
    for h in health_symbols:
        health += ord(h)
    damage_numbers = re.finditer(r"([-+]?\d+(\.\d+)?)", demon)
    damage = sum([float(d[0]) for d in damage_numbers])
    for i in range(demon.count('/')): damage /= 2
    for i in range(demon.count('*')): damage *= 2
    print(f"{demon} - {health} health, {damage:.2f} damage")
