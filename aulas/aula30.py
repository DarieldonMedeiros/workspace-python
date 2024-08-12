'''
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
'''
velocidade = 61 # velociade
localCarro = 100 # local que o carro está na casa

RADAR_1 = 60 # velocidade máxima do radar 1
LOCAL_1 = 100 # local onde o radar
RADAR_RANGE = 1 # A distância que o radar pega

velCarroPassouRadar1 = velocidade > RADAR_1
carroPassouRadar1 = localCarro >= (LOCAL_1 - RADAR_RANGE) and localCarro <= (LOCAL_1 + RADAR_RANGE)

carroMultadoRadar1 = carroPassouRadar1 and velCarroPassouRadar1

if velCarroPassouRadar1:
    print('Velocidade do carro passou do radar ')

if carroPassouRadar1:
    print('Carro passou radar 1')

# barra invertida quebra a linha
if carroMultadoRadar1:
    print('Carro multado em radar 1')