command = input()

while command != "end":
    rev = ""
    for chr in reversed(command):
        rev += chr
    print(f"{command} = {rev}")
    command = input()
