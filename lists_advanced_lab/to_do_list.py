notes = [''] * 11
command_input = input()
while command_input != "End":
    command_args = command_input.split("-")
    priority = int(command_args[0])
    note = command_args[1]

    notes.pop(priority)
    notes.insert(priority, note)
    command_input = input()

filtered_notes = [n for n in notes if n != '']
print(filtered_notes)
