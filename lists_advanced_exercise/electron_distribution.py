number_of_electrons = int(input())
shells = []
shell_position = 1
current_electrons = 0
while number_of_electrons != 0:
    current_electrons = 2 * (shell_position ** 2)
    if current_electrons > number_of_electrons:
        current_electrons = number_of_electrons
        number_of_electrons = 0
    else:
        number_of_electrons -= current_electrons
    shells.append(current_electrons)
    shell_position += 1
    current_electrons = 0
print(shells)
