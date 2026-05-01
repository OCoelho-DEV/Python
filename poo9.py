# Encapsulamento (modificadores de acesso: public, protected, private)
# Python NÃO TEM modificadores de acesso
# Mas podemos seguir as seguintes convenções
#   (sem underline) = public
#       pode ser usado em qualquer lugar
# _ (um underline) = protected
#       não DEVE ser usado fora da classe
#       ou suas subclasses.
# __ (dois underlines) = private
#       "name mangling" (desfiguração de nomes) em Python
#       _NomeClasse__nome_attr_ou_method
#       só DEVE ser usado na classe em que foi
#       declarado.

class Test:
    def __init__(self,):
        self.__private = 'Private'
        self.public = 'Public'
        self._protected = 'Protected'

    def __private_method(self):
        return self.__private
    
    def public_method(self):
        return self.public
        
    def _protected_method(self):
        return self._protected
    

t1 = Test()
print(t1.public_method())
print(t1._protected_method())
print(t1._Test__private_method())
        