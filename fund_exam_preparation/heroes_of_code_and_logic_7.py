number_of_heroes = int(input())
heroes = {}
for n in range(number_of_heroes):
    hero_info = input().split()
    hero = hero_info[0]
    hp = int(hero_info[1])
    mp = int(hero_info[2])
    heroes[hero] = {"hp": hp, "mp": mp}
command = input().split(" - ")
while command[0] != "End":
    if command[0] == "CastSpell":
        hero_name = command[1]
        needed_mp = int(command[2])
        spell_name = command[3]
        if needed_mp <= heroes[hero_name]["mp"]:
            heroes[hero_name]["mp"] -= needed_mp
            print(f"{hero_name} has successfully cast {spell_name} and now has {heroes[hero_name]['mp']} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")
    elif command[0] == "TakeDamage":
        hero_name = command[1]
        damage = int(command[2])
        attacker = command[3]
        heroes[hero_name]["hp"] -= damage
        if heroes[hero_name]["hp"] > 0:
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {heroes[hero_name]['hp']} HP left!")
        else:
            del heroes[hero_name]
            print(f"{hero_name} has been killed by {attacker}!")
    elif command[0] == "Recharge":
        hero_name = command[1]
        amount = int(command[2])
        if amount + heroes[hero_name]["mp"] > 200:
            amount_recovered = 200 - heroes[hero_name]["mp"]
        else:
            amount_recovered = amount
        heroes[hero_name]["mp"] += amount_recovered
        print(f"{hero_name} recharged for {amount_recovered} MP!")
    elif command[0] == "Heal":
        hero_name = command[1]
        amount = int(command[2])
        if amount + heroes[hero_name]["hp"] > 100:
            amount_recovered = 100 - heroes[hero_name]["hp"]
        else:
            amount_recovered = amount
        heroes[hero_name]["hp"] += amount_recovered
        print(f"{hero_name} healed for {amount_recovered} HP!")
    command = input().split(" - ")
sorted_heroes = sorted(heroes.items(), key=lambda kvp: (-kvp[1]["hp"], kvp[0]))
for hero in sorted_heroes:
    print(hero[0])
    print(f"  HP: {heroes[hero[0]]['hp']}")
    print(f"  MP: {heroes[hero[0]]['mp']}")
