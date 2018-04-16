# Writing into a file
import os

test_file = open("test.txt", "wb")

print(test_file.mode)
print(test_file.name)

test_file.write(bytes("Write me the file\nOh yes!", "UTF-8"))

test_file.close()

# Reading into a file
test_file = open("test.txt", "r+")
print(test_file.read())

test_file.close()

# Remove file
os.remove("test.txt")
