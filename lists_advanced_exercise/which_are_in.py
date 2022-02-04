first_list = input().split(", ")
second_list = input().split(", ")
final_list = []
for word in first_list:
    for words in second_list:
        if word in words and word not in final_list:
            final_list.append(word)
print(final_list)
