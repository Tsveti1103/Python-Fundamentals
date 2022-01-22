data = input()
dwarfs = {}
colors = {}

while data != "Once upon a time":
    not_the_same = True
    name, color, physics = data.split(" <:> ")
    physics = int(physics)
    draft = f"({color}) {name}"
    if draft not in dwarfs:
        dwarfs[draft] = physics
    else:
        if dwarfs[draft] < physics:
            dwarfs[draft] = physics
            not_the_same = False
    if color not in colors:
        colors[color] = {name: physics}
    else:
        if not_the_same:
            colors[color].update({name: physics})
    data = input()
sort = dict(sorted(colors.items(), key=lambda kvp: -len(kvp[1])))

new = {}
for color, dwarf in sort.items():
    for name, value in dwarf.items():
        dr = f"({color}) {name}"
        new[dr] = dwarfs[dr]

final = sorted(new.items(), key=lambda kvp: -kvp[1])
for d, v in final:
    print(f"{d} <-> {v}")
