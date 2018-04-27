
class Time:

    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return "{}:{:02d}:{:02d}".format(self.hour, self.minute, self.second)

    def __add__(self, other):
        pass

    def __sub__(self, other):
        pass

    def __mul__(self, other):
        pass

    def __divmod__(self, other):
        pass

    def __eq__(self, other):
        pass

    def __mod__(self, other):
        pass

    def __eq__(self, other):
        pass

    def __ne__(self, other):
        pass

    def __lt__(self, other):
        pass

    def __gt__(self, other):
        pass

    def __le__(self, other):
        pass

    def __ge__(self, other):
        pass

