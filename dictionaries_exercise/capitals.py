country = input().split(", ")
capital = input().split(", ")
couples = dict(zip(country, capital))
for country, capital in couples.items():
    print(f"{country} -> {capital}")
