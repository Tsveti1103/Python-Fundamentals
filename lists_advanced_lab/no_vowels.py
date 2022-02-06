text = input()

vowels = ['a', 'o', 'u', 'e', 'i', 'A', 'O', 'U', 'E', 'I']
filtered_text_as_list = [c for c in text if c not in vowels]
filtered_text = "".join(filtered_text_as_list)
print(filtered_text)
