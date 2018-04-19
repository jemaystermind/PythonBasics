
string = "    Lorem ipsum dolor set amet    "

print("String: " + string.lstrip())
print(string.rstrip())
print(string.strip())

string = "ludwig van Beethoven".capitalize()
print(string)

print(string.upper())
print(string.lower())

random_words = ["Bunch", "of", "random", "words"]
print(random_words)
print(" ".join(random_words))

list2 = string.split()
for i in list2:
    print(i)

string = "Lorem ipsum dolor set amet"
print("How many: ", string.count("set"))  # Count occurrence
print("Where: ", string.find("Lorem"))
