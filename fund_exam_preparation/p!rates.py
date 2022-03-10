city = input().split("||")
cities = {}
while city[0] != "Sail":
    name = city[0]
    population = int(city[1])
    gold = int(city[2])
    if name not in cities:
        cities[name] = {"population": 0, "gold": 0}
    cities[name]["population"] += population
    cities[name]["gold"] += gold
    city = input().split("||")
command = input().split("=>")
while command[0] != "End":
    if command[0] == "Plunder":
        town_name = command[1]
        people = int(command[2])
        current_gold = int(command[3])
        print(f"{town_name} plundered! {current_gold} gold stolen, {people} citizens killed.")
        cities[town_name]["population"] -= people
        cities[town_name]["gold"] -= current_gold
        if cities[town_name]["population"] == 0 or cities[town_name]["gold"] == 0:
            print(f"{town_name} has been wiped off the map!")
            del cities[town_name]
    elif command[0] == "Prosper":
        town_name = command[1]
        current_gold = int(command[2])
        if current_gold < 0:
            print("Gold added cannot be a negative number!")
        else:
            cities[town_name]["gold"] += current_gold
            total_gold = cities[town_name]["gold"]
            print(f"{current_gold} gold added to the city treasury. {town_name} now has {total_gold} gold.")
    command = input().split("=>")
if cities:
    sorted_cities = sorted(cities.items(), key=lambda kvp: (-kvp[1]["gold"], kvp[0]))
    print(f"Ahoy, Captain! There are {len(sorted_cities)} wealthy settlements to go to:")
    for city in sorted_cities:
        town = city[0]
        people = city[1]["population"]
        gold = city[1]["gold"]
        print(f"{town} -> Population: {people} citizens, Gold: {gold} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
