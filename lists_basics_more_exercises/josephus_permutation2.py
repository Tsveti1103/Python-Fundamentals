people = input().split()
step = int(input())
counter = 0
new_list = []
if not people:
    exit()
while people:
    list_p = people.copy()
    for i, v in enumerate(list_p):
        counter += 1
        if counter % step == 0:
            people.remove(v)
            new_list.append(v)
print(f"[{','.join(new_list)}]")
