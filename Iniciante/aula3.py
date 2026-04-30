#Conversão de tipos
#Coercion, typecasting

#print('1' + 1) ->Impossível (str + int)

print(type(int('1')))
print(1 + int('1'))
print(int(1.4) + 3)
print(float('1') + 1)

print(bool(''))
print(bool('a'))

print(str(101) + 'n')