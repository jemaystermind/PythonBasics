import sys


# Defining functions
def add_number(x, y):
    return x + y


# print(add_number(1, 2))
#
# print('What is your name')
#
# name = sys.stdin.readline()
#
# print('Hello', name)

sample_string = "Python Programming Derek Banas"

# Prints the first 6 characters
print(sample_string[0:7])

# Prints the last 5 characters
print(sample_string[-5:])

# Exclude the last 5 characters
print(sample_string[0:-5])

# Wildcards
print('%c is my %s letter and my %d number is %.5f' % ('A', 'favorite', 1, 23))

# String basic functions
print(sample_string.capitalize())

print(sample_string.find("Banas"))

print("Alpha".isalpha())

print("123".isalnum())

print(len(sample_string))

print(sample_string.replace("Python", "Kotlin"))

print(sample_string.strip())

split = sample_string.split(" ")
print(split)