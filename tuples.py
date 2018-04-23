# Tuples are immutable list
numbers = (1, 2, 3, 4, 5)
print(numbers)

# Operations available to tuples are almost the same with list
print(numbers[0:3])

print("Length: ", len(numbers))

numbers = numbers + (6, 7)
print(numbers)

print("7 in tuple?", 7 in numbers)

for num in numbers:
    print(num, end=", ")

print("")

# Convert list to tuple
strawhat_crew = ["Luffy", "Zorro", "Nami", "Sanji", "Usopp", "Chopper", "Robin", "Franky", "Brook", "Jimbei"]
strawhat_crew = tuple(strawhat_crew)
print(strawhat_crew)

# Convert tuple to list
print(list(strawhat_crew))

print(min(strawhat_crew))
print(max(strawhat_crew))

