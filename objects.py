class Animal:
    def __init__(self, birth_type="Unknown", appearance="Unknown", blooded="Unknown"):
        self.birth_type = birth_type
        self.appearance = appearance
        self.blooded = blooded

    @property
    def birth_type(self):
        return self.birth_type

    @birth_type.setter
    def birth_type(self, birth_type):
        self.birth_type = birth_type

    @property
    def appearance(self):
        return self.appearance

    @appearance.setter
    def appearance(self, appearance):
        self.appearance = appearance

    @property
    def blooded(self):
        return self.blooded

    @blooded.setter
    def blooded(self, blood):
        self.blooded = blood

    def __str__(self):
        return "A {} is {} it is {} it is {}".format(type(self).__name__, self.birth_type, self.appearance, self.blooded)

