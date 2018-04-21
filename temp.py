import random
import math

print(random.randrange(1, 10))

numbers = [i * 2 for i in range(10)]

numbers_2 = [math.pow(i, 2) for i in range(20)]

print(numbers)
print(numbers_2)
