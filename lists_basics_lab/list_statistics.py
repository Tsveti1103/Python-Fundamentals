number_of_lines = int(input())
positive_list = []
negative_list = []
for i in range(number_of_lines):
    num = int(input())
    if num >= 0:
        positive_list.append(num)
    else:
        negative_list.append(num)
print(positive_list)
print(negative_list)
print("Count of positives:", len(positive_list))
print("Sum of negatives:", sum(negative_list))
