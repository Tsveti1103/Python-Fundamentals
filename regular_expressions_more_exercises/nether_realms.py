import re

demons = input().split(",")
all_demons = {}

for demon in demons:
    demon = demon.strip()
    if " " not in demon and "," not in demon and len(demon) > 0:
        health = 0
        damage = 0
        name = demon
        health_symbols = re.findall(r"[^\+\-\*\/\d,\.]", demon)
        damage_numbers = re.finditer(r"([-+]?\d+(\.\d+)?)", demon)
        damage = sum([float(d[0]) for d in damage_numbers])
        if health_symbols:
            for s in health_symbols:
                health += ord(s)
        if damage_numbers:
            for n in damage_numbers:
                damage += float(n)
        for i in range(demon.count('/')): damage /= 2
        for i in range(demon.count('*')): damage *= 2
        all_demons[name] = {'health': health, 'damage': damage}
all_demons = dict(sorted(all_demons.items(), key=lambda kvp: kvp[0]))

for demon, values in all_demons.items():
    print(f"{demon} - {values.get('health')} health, {values.get('damage'):.2f} damage")
