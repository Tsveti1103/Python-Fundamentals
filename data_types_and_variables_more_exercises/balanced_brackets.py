n = int(input())
open_counter = 0
close_counter = 0
is_balanced = bool
command = ""

for i in range(n):
    current_command = input()
    if current_command == command:
        print("UNBALANCED")
        is_balanced = False
        break
    if current_command == command:
        is_balanced = False
        print("UNBALANCED")
        break
    if current_command == "(":
        open_counter += 1
        command = current_command
        continue
    elif current_command == ")":
        close_counter += 1
        command = current_command
        continue
    if open_counter == close_counter:
        is_balanced = True
if is_balanced:
    print("BALANCED")