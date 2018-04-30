
# Find the multiples of 9 from a random 100 value list with
# values between 1 and 1000

import random

# Generate random list
num_list = list(random.randint(1, 1001) for i in range(100))

print("List:", num_list)
print("Size:", len(num_list))

is_multiples_of_9 = lambda x: x % 9 == 0

print(list(filter(is_multiples_of_9, num_list)))  # Creates a new list applying a filter
