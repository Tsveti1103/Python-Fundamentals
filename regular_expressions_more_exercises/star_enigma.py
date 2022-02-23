import re

attacked_planet = []
destroyed_planet = []

messages_count = int(input())
for i in range(messages_count):
    message = input()
    decrypt = ""
    keys_count = int(len(re.findall(r"[starSTAR]", message)))
    for letter in message:
        new_letter = ord(letter) - keys_count
        decrypt += chr(new_letter)
    pattern = r".*@([A-Z][a-z]+)[^\@\-\!\:\>]*:(\d+)[^\@\-\!\:\>]*\!(A|D)\![^\@\-\!\:\>]*\->(\d+).*"
    matches = re.findall(pattern, decrypt)
    if matches:
        for match in matches:
            name = match[0]
            population = match[1]
            type = match[2]
            soldier = match[3]
            if type == "A":
                attacked_planet.append(name)
            elif type == "D":
                destroyed_planet.append(name)

print(f"Attacked planets: {len(attacked_planet)}")
attacked_planet = sorted(attacked_planet)
for planet in attacked_planet:
    print(f"-> {planet}")
print(f"Destroyed planets: {len(destroyed_planet)}")
destroyed_planet = sorted(destroyed_planet)
for planet in destroyed_planet:
    print(f"-> {planet}")
