import os


with open("data.txt", mode="w", encoding="UTF-8") as file:
    file.write('''When do you think people die?
When they are shot through the heart by a bullet of a pistol? NO.
When they are ravaged by an incurable disease? No.
When they drink a soup made from a poisonous mushroom!? NO!
It's when... they are forgotten.''')

with open("data.txt", encoding="UTF-8") as file:
    print(file.read())

# Read one line a time
with open("data.txt") as file:
    line_number = 1

    while True:
        line = file.readline()

        if not line:
            break

        print("Line {} : {}".format(line_number, line), end="")
        line_number += 1

print("")

os.rename("data.txt", "poneglyph.txt")

os.remove("poneglyph.txt")

os.mkdir("Raftel")

os.chdir("Raftel")
print("Current directory: ", os.getcwd())

os.chdir("..")
print("Current directory: ", os.getcwd())

os.removedirs("Raftel")
