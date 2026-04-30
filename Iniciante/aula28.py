contador = 0

while contador < 100:
    contador += 1

    if contador == 10:
        print('Você não vai ver esse')
        continue 

    if contador >= 30 and contador <= 60:
        print('Você não vai ver esse tbm')
        continue

    print(contador)

    if contador == 75:
        break
    
print('Acabou')