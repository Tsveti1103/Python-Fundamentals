string = input()
new_list = string.split(", ")
new_list = map(int, new_list)
new_list = list(new_list)
for i, v in enumerate(new_list):
    new_list.append(new_list.pop(new_list.index(0)))
print(new_list)
