import re

text = input()
matches = re.finditer(r"(@+#*|@*#+)(?P<color>[a-z]{3,})(@+#*|@*#+)([^a-zA-Z0-9]*)(\/+(?P<amount>[0-9]+)\/+)", text)
for egg in matches:
    amount = egg.group("amount")
    color = egg.group("color")
    print(f"You found {amount} {color} eggs!")
