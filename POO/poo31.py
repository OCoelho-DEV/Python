"""
Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tem clientes, contas e
um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
possa sacar/depositar nessa conta. Contas corrente tem um limite extra.

Conta (ABC)
    ContaCorrente
    ContaPoupanca

Pessoa (ABC)
    Cliente
        Clente -> Conta

Banco
    Banco -> Cliente
    Banco -> Conta

Dicas:
Criar classe Cliente que herda da classe Pessoa (Herança)
    Pessoa tem nome e idade (com getters)
    Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)
Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
    ContaCorrente deve ter um limite extra
    Contas têm agência, número da conta e saldo
    Contas devem ter método para depósito
    Conta (super classe) deve ter o método sacar abstrato (Abstração e
    polimorfismo - as subclasses que implementam o método sacar)
Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
Banco será responsável autenticar o cliente e as contas da seguinte maneira:
    Banco tem contas e clentes (Agregação)
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco
Só será possível sacar se passar na autenticação do banco (descrita acima)
Banco autentica por um método.
"""
from abc import ABC, abstractmethod
import random

def gen_acc_number():
    return random.randint(11111, 99999)

def gen_agency_number():
    return random.randint(1111, 9999)

class Person(ABC):
    def __init__(self, name, age):
        self._name = name
        self._age = age
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, age):
        self._age = age

    @abstractmethod
    def __str__(self):
        pass

class Client(Person):
    def __init__(self, name, age, accounts=None):
        self._accounts = accounts if accounts else []
        super().__init__(name, age)
    
    @property
    def accounts(self):
        return self._accounts
    
    def add_account(self, account):
        self._accounts.append(account)
    
    def __str__(self):
        return f'Client {self.name} {self.age}y'
    
    def __repr__(self):
        return self.__str__()


class Account(ABC):
    acc_type = 'Unknow'
    def __init__(self, bank, client, balance=0):
        self._balance = balance
        self._bank = bank
        self._client = client 
        self._agency = bank.agency

    
    @abstractmethod
    def withdraw(self, amount):
        pass

    def __str__(self):
        return f'{self.acc_type} - B:{self._bank} | \
N:{self._number} | Balance: {self._balance}'

    def __repr__(self):
        return self.__str__()
    
    def deposit(self, amount):
        self._balance += amount

class CheckingAccount(Account):
    acc_type = 'Checking Account'
    def __init__(self, bank, client, balance=0, limit=500):
        self._number = gen_acc_number()
        self._limit = limit
        super().__init__(bank, client, balance)

    def withdraw(self, amount):
        auth = self._bank.authenticate(self._client, self)
        if auth:
            result = (self._balance - amount) + self._limit
            if result >= 0:
                self._balance -= amount
                print('>>> Withdraw realized with success')
                print(f'>>> Account have {self._balance}$')
            else:
                print(f'>>> Account reached the maximum limit')
        else:
            print('>>> Not authorized by bank')

class SavingAccount(Account):
    acc_type = 'Saving Account'
    def __init__(self, bank, client, balance=0):
        self._number = gen_acc_number()
        super().__init__(bank, client, balance)

    def withdraw(self, amount):
        auth = self._bank.authenticate(self._client, self)
        if auth:
            if self._balance >= amount:
                self._balance -= amount
                print('>>> Withdraw realized with success')
                print(f'>>> Account have {self._balance}$')
            else:
                print(f'>>> Account reached the maximum limit')
        else:
            print('>>> Not authorized by bank')
    

class Bank:
    def __init__(self, name):
        self.name = name
        self.agency = gen_agency_number()
        self.accounts = []
        self.clients = []
    
    def add_account_and_client(self, account):
        self.accounts.append(account)
        self.clients.append(account._client)
    
    def create_checking_acc(self, client, balance):
        acc = CheckingAccount(self, client, balance)
        self.add_account_and_client(acc)
        return acc
    
    def create_saving_acc(self, client, balance):
        acc = SavingAccount(self, client, balance)
        self.add_account_and_client(acc)
        return acc
    
    def authenticate(self, client, account):
        return (
            account._agency == self.agency and
            account in self.accounts and
            client in self.clients
        )
    
    def __str__(self):
        return f'{self.name} | Agency {self.agency}'

# Testing
bank = Bank('Bradesco')
bank2 = Bank('Bank')
c1 = Client('Rafael', 18)
c2 = Client('Giovana', 18)
acc1 = bank.create_checking_acc(c1, 1000)
acc2 = bank.create_saving_acc(c1, 1000)
acc1.deposit(500)
acc1.withdraw(500)
acc1.withdraw(1000)
acc1.withdraw(1000) # Limit
acc2.withdraw(1000)
acc2.withdraw(1) # Limit
print(bank)    
print(c1)    
print(acc1)    
print(acc2)

# Not authorized
acc1._bank = bank2 # bank 2 don't know who is acc1
acc1.deposit(50)
acc1.withdraw(1)
# bank.accounts.remove(acc1) is the same

# fake_acc = CheckingAccount(bank, c1, 999999)
# fake_acc.withdraw(100) 
# Is the same