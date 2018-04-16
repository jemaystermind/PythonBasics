class Robot:
    def introduce_self(self):
        print("My name is " + self.name)


r1 = Robot()
r1.name = "Tom"
r1.color = "red"
r1.weight = 30

r1.introduce_self()


class Parent:
    def __init__(self):
        self.__my_var = 1


class Child(Parent):
    def __init__(self):
        Parent.__init__(self)


child = Child()
print(child._my_var)

