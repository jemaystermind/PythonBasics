# Create a random list filled with the characters H and T
# Output the number of Hs and Ts
# Example output:
# Heads: 46
# Tails: 54

import random

items = []

# Populate list with H and T characters
for i in range(100):
    choice = random.choice(['H', 'T'])
    items.append(choice)

print("Heads:", items.count("H"))
print("Tails:", items.count("T"))
