class Animal:
    __name = ""
    __height = 0
    __weight = 0
    __sound = 0

    def __init__(self, name, height, weight, sound):
        self.__name = name
        self.__height = height
        self.__weight = weight
        self.__sound = sound

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_height(self, height):
        self.__height = height

    def get_height(self):
        return self.__height

    def set_weight(self, weight):
        self.__weight = weight

    def get_weight(self):
        return self.__weight

    def set_sound(self, sound):
        self.__sound = sound

    def get_sound(self):
        return self.__sound

    def to_string(self):
        return "{} is {} cm tall and {} kilograms an say {}".format(self.__name,
                                                                    self.__height,
                                                                    self.__weight,
                                                                    self.__sound)


# Inheritance
class Dog(Animal):
    __owner = ""

    def __init__(self, name, height, weight, sound, owner):
        super().__init__(name, height, weight, sound)
        self.__owner = owner

    def set_owner(self, owner):
        self.__owner = owner

    def to_string(self):
        return "{} is {} cm tall and {} kilograms an say {}. His owner is {}".format(self.get_name(), self.get_height(),
                                                                                     self.get_weight(),
                                                                                     self.get_sound(),
                                                                                     self.__owner)

    def multiple_sounds(self, how_many=None):
        if how_many is None:
            print(self.get_sound())
        else:
            print(self.get_sound() * how_many)


cat = Animal("Whiskers", 33, 10, "Meow")
print(cat.to_string())

dog = Dog("Lucky", 1, 2, "Aww", "Me")
print(dog.get_name())

dog.multiple_sounds(2)

print(dog.to_string())
