import re

no_mirror = True
pairs = []
text = input()
match = re.findall(r"(@|#)([a-zA-Z]{3,})\1\1([a-zA-Z]{3,})\1", text)
if match:
    print(f"{len(match)} word pairs found!")
    for m in match:
        first = m[1]
        second = m[2]
        if first == second[::-1]:
            pairs.append(f'{first} <=> {second}')
            no_mirror = False
    if no_mirror:
        print("No mirror words!")
    else:
        print("The mirror words are:")
        print(", ".join(pairs))
else:
    print("No word pairs found!")
    print("No mirror words!")
