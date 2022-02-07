population = input().split(", ")
new_population = []
minimum_wealth = int(input())
is_equal = True
for i in population:
    i = int(i)
    new_population.append(i)
for i, v in enumerate(new_population):
    if sum(new_population) / len(new_population) < minimum_wealth:
        print("No equal distribution possible")
        is_equal = False
        break
    wealthiest = int(max(new_population))
    current_wealth = int(v)
    difference = minimum_wealth - current_wealth
    if wealthiest - difference >= minimum_wealth:
        if current_wealth < minimum_wealth:
            new_wealth = current_wealth + difference
            new_wealthiest = wealthiest - difference
            new_population[i] = new_wealth
            new_population[new_population.index(wealthiest)] = new_wealthiest
if is_equal:
    print(new_population)
