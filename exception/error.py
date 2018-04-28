# Custom exception
class DogNameError(Exception):

    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)


try:
    dog_name = input("Enter dog name: ")

    if any(char.isdigit() for char in dog_name):
        raise DogNameError

except DogNameError:
    print("Dog name can't contain a number")
else:
    print("No exception raised!")  # else block is executed if no exception is raised!
finally:
    print("Always executed")
