velocidade = 61 #Velocidade do carro
local_carro = 100 #Local onde está o carro

RADAR_1 = 60 #Velocidade máxima permitida
LOCAL_1 = 100 #Local onde está o radar
RADAR_RANGE = 1 #Distância onde o radar pega


velocidade_maior_radar_1 = velocidade > RADAR_1
carro_no_range_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado_radar_1 = velocidade_maior_radar_1 and\
    carro_no_range_radar_1

if velocidade_maior_radar_1:
    print("Velocidade do carro é maior que o radar")
   
if carro_multado_radar_1:
    print('Multado no radar 1')