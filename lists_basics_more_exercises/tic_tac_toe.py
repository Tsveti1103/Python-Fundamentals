line_one = input().split()
line_two = input().split()
line_three = input().split()
final_list = line_one + line_two + line_three
first_player = False
second_player = False
for i in range(len(line_one)):
    if len(line_one) == line_one.count("1") \
            or len(line_two) == line_two.count("1") \
            or len(line_three) == line_three.count("1"):
        first_player = True
        break
    elif len(line_one) == line_one.count("2") \
            or len(line_two) == line_two.count("2") \
            or len(line_three) == line_three.count("2"):
        second_player = True
        break
    elif line_one[0] == line_two[1] == line_three[2] == "1" \
            or line_one[2] == line_two[1] == line_three[0] == "1":
        first_player = True
        break
    elif line_one[0] == line_two[1] == line_three[2] == "2" \
            or line_one[2] == line_two[1] == line_three[0] == "2":
        second_player = True
        break
    elif line_one[i] == line_two[i] == line_three[i] == "1":
        first_player = True
        break
    elif line_one[i] == line_two[i] == line_three[i] == "2":
        second_player = True
        break
if first_player:
    print("First player won")
elif second_player:
    print("Second player won")
else:
    print("Draw!")
