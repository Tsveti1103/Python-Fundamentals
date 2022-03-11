import re

text = input()
emoji = []
threshold = 1
count = 0
match = re.finditer(r"(\*\*|::)(\b[A-Z][a-z]{2,})(\1)", text)
threshold_match = re.findall(r"\d", text)
for t in threshold_match:
    threshold *= int(t)
for e in match:
    current_emoji = e.group()
    emoji_coolness = 0
    count += 1
    for letter in current_emoji:
        if letter != ":" and letter != "*":
            emoji_coolness += ord(letter)
    if emoji_coolness >= threshold:
        emoji.append(current_emoji)
print(f"Cool threshold: {threshold}")
print(f"{count} emojis found in the text. The cool ones are:")
for em in emoji:
    print(em)
