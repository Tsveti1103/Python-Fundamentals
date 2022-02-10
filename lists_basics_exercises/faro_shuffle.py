card = input().split()
shuffles_number = int(input())
half_of_card = int(len(card) / 2)
final_list = []
for shuffle in range(shuffles_number):
    final_list = []
    for i in range(half_of_card):
        final_list.append(card[i])
        final_list.append(card[(i+half_of_card)])
    card = final_list
print(final_list)
