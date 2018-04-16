class Base:
    def foo(self):
        return 'foo'


assert hasattr(Base, 'foo'), "You broke it, you fool!"


class Derived(Base):
    def bar(self):
        return self.foo()
