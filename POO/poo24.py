def add_repr(cls):
    def my_repr(self):
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = f'{class_name}({class_dict})'
        return class_repr
    cls.__repr__ = my_repr
    return cls

def my_team(method):
    def intern(self, *args, **kwargs):
        result = method(self, *args, **kwargs)
        if 'Brazil' in result:
            return "You're on Brazil"
        return result
    return intern

@add_repr
class Team:
    def __init__(self, name):
        self.name = name

    @my_team
    def say_team(self):
        return f'The team is {self.name}'

Brazil = Team("Brazil")
print(Brazil)
print(Brazil.say_team())
