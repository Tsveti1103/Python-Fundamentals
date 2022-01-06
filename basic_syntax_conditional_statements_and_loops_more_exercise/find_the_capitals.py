word = input()
final_list = []
for index in range(len(word)):
    if word[index].isupper():
        final_list.append(index)
print(final_list)
