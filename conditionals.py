import random

# age = 21
#
# if age > 16:
#     print('You are old enough to drive')
# else:
#     print('You are not old enough to drive')
#
# if age >= 21:
#     print('You are old enough to drive a tractor')
# elif age >= 16:
#     print('You are old enough to drive a car')
# else:
#     print('YOu are not old enough to drive')
#
# if age != 20:
#     print("")
#
# # for-loops
# for x in range(0, 10):  # Exclusive
#     print(x, ' ', end="")
#
# print('\n')
#
# to_dos = ['Read', 'Write', 'Eat', 'Play']
# for todo in to_dos:
#     print(todo)

# random_num = random.randrange(0, 100)
# while random_num != 15:
#     print(random_num)
#     random_num = random.randrange(0, 100)

i = 0
while i <= 20:
    if i % 2 == 0:
        print(i)
    elif i == 9:
        print('You\'re a rockstar!')
    else:
        print(i)

    i += 1
