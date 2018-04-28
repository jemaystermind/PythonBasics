class Dog:

    num_of_dogs = 0

    def __init__(self, name="Unknown"):
        self.name = name

        Dog.num_of_dogs += 1

    @staticmethod
    def get_number_of_dogs():
        print("There are currently {} dogs".format(Dog.num_of_dogs))


def main():

    spot = Dog("Spot")
    doug = Dog("Doug")

    spot.get_number_of_dogs()
    doug.get_number_of_dogs()


main()
