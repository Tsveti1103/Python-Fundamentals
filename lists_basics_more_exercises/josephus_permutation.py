people = input().split()
step = int(input())
counter = 0
new_list = []
if not people:
    exit()
while people:
    x = len(people)
    counter = (counter + step - 1) % len(people)
    new_list.append(people.pop(counter))
print(f"[{','.join(new_list)}]")
