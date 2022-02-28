n = int(input())
for i in range(n):
    text = input()
    name = text[text.index("@") + 1:text.index("|")]
    years = text[text.index("#") + 1:text.index("*")]
    print(f"{name} is {years} years old.")
