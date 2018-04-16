pi_tuple = (3, 1, 4, 5, 5)
print(pi_tuple)

list_tuple = list(pi_tuple)
print(list_tuple)
print(tuple(list_tuple))

print(len(list_tuple))
print(min(list_tuple))
print(max(list_tuple))

# Dictionaries

# Create dictionaries with parenthesis '{}'
villains = {'Fiddler': 'Isaaic Bowin'}
print(villains['Fiddler'])

# Use del for deleting an item from dictionary, tuple, list
del villains['Fiddler']
print("Villains=", villains)

# Add item to a dictionary
villains['Foo'] = "Bar"
print("Add villain=", villains)

# Modify/update dictionary
villains['Foo'] = "Baz"
print("Modify villain=", villains)

print(villains.keys())

print(villains.values())
