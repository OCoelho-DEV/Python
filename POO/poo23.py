def add_repr(cls):
    def my_repr(self):
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = f'{class_name}({class_dict})'
        return class_repr
    cls.__repr__ = my_repr
    return cls

@add_repr
class Team:
    def __init__(self, name):
        self.name = name

Brazil = Team("Brazil")
print(Brazil)
