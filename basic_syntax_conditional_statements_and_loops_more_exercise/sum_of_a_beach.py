words = input()
lower_words = words.lower()
counter = 0
if "sun" in lower_words:
    counter += lower_words.count("sun")
if "sand" in lower_words:
    counter += lower_words.count("sand")
if "water" in lower_words:
    counter += lower_words.count("water")
if "fish" in lower_words:
    counter += lower_words.count("fish")
print(counter)
