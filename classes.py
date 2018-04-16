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
        self.my_var = 1


class Child(Parent):
    def __init__(self):
        Parent.__init__(self)


child = Child()
print(child.my_var)


class Polynomial:
    def __init__(self, *coeffs):
        self.coeffs = coeffs

    def __repr__(self):
        return 'Polynomial(*{!r})'.format(self.coeffs)

p1 = Polynomial(1, 2, 3)
print(p1)
