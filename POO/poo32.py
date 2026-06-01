# dataclasses - O que são dataclasses?
# O módulo dataclasses fornece um decorador e funções para criar métodos como
# __init__(), __repr__(), __eq__() (entre outros) em classes definidas pelo
# usuário.
# Em resumo: dataclasses são syntax sugar para criar classes normais.
# Foi descrito na PEP 557 e adicionado na versão 3.7 do Python.
# doc: https://docs.python.org/3/library/dataclasses.html
from dataclasses import dataclass, asdict, astuple


@dataclass() # init=False or init=True 
# Order = bool
class Person:
    name: str
    surname: str
    age_: int

    def __post_init__(self):
        self.complete_name = f'{self.name} {self.surname}'

    @property
    def age(self):
        return self.age_
    
    @age.setter
    def age(self, age):
        self.age_ = age


if __name__ == '__main__':

    p1 = Person('Rafael', 'Coelho', 30)
    # print(p1.age)
    # p1.age = 100
    # print(p1.age)
    print(asdict(p1).items())
    print(asdict(p1).keys())
    print(asdict(p1).values())
    print(astuple(p1))

    
