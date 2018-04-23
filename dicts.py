
heroes = {"All Might": "Toshinori Yagi", "Endeavor": "Enji Todoroki", "Eraserhead": "Shota Aizawa"}

print(heroes)

# Printing dictionaries
for k, v in heroes.items():
    print("Hero name={} , Real name={}".format(k, v))

# Retrieve item
print(heroes["All Might"])
print(heroes.get("Endeavor"))

# Remove item in a dictionary
del heroes["Eraserhead"]
print(heroes)

# Iterate dictionary keys
for key in heroes:
    print(key)

# Remove all items
heroes.clear()
print(heroes)
