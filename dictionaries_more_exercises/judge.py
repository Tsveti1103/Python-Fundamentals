command = input().split(" -> ")
contests = {}
individual_points = {}
while command[0] != "no more time":
    username = command[0]
    contest = command[1]
    points = int(command[2])
    if contest not in contests:
        contests[contest] = {}
    if username not in contests[contest]:
        contests[contest][username] = points
    else:
        if points > contests[contest][username]:
            contests[contest][username] = points
    command = input().split(" -> ")
for key, value in contests.items():
    print(f"{key}: {len(value)} participants")
    counter = 0
    sort_value = sorted(value.items(), key=lambda kvp: (-kvp[1], kvp[0]))
    for k, v in sort_value:
        counter += 1
        print(f"{counter}. {k} <::> {v}")
        if k not in individual_points:
            individual_points[k] = 0
        individual_points[k] += v
print("Individual standings:")
sort_individual = sorted(individual_points.items(), key=lambda kvp: (-kvp[1], kvp[0]))
user_counter = 0
for user, points in sort_individual:
    user_counter += 1
    print(f"{user_counter}. {user} -> {points}")
