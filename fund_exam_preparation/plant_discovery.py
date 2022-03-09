n = int(input())
plants = {}
for _ in range(n):
    information = input().split("<->")
    plant_name = information[0]
    plant_rarity = int(information[1])
    plants[plant_name] = {"plant_rarity": plant_rarity, "rating": []}
command = input().split(": ")
while command[0] != "Exhibition":
    if command[0] == "Rate":
        plant, rating = command[1].split(" - ")
        rating = int(rating)
        if plant in plants:
            plants[plant]["rating"].append(rating)
        else:
            print("error")
    elif command[0] == "Update":
        plant, new_rarity = command[1].split(" - ")
        new_rarity = int(new_rarity)
        if plant in plants:
            plants[plant]["plant_rarity"] = new_rarity
        else:
            print("error")
    elif command[0] == "Reset":
        plant = command[1]
        if plant in plants:
            plants[plant]["rating"] = []
        else:
            print("error")
    command = input().split(": ")
for pl in plants.items():
    name = pl[0]
    if plants[name]["rating"]:
        avg_rating = sum(plants[name]["rating"]) / (len(plants[name]["rating"]))
        plants[name]["rating"] = avg_rating
    else:
        plants[name]["rating"] = 0
plants_final = sorted(plants.items(), key=lambda kvp: (kvp[1]["plant_rarity"], kvp[1]["rating"]), reverse=True)
print("Plants for the exhibition:")
for p in plants_final:
    plant_name = p[0]
    rarity = int(p[1]['plant_rarity'])
    rating = float(p[1]["rating"])
    print(f"- {plant_name}; Rarity: {rarity}; Rating: {rating:.2f}")