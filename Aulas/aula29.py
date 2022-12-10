velocidade = 100 #velocidae do carrro
local_carro = 101 #localizao do carro

RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1  # A distância onde o radar pega

vel_carro_pass_radar_1 = velocidade > RADAR_1
carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) # 100 - compara com 99
carro_pasou_radar_2 = local_carro <= (LOCAL_1 + RADAR_RANGE) #100 - compara com 101
carro_multado_radar_1 = carro_passou_radar_1 and carro_pasou_radar_2 and vel_carro_pass_radar_1

# print(carro_passou_radar_1)
# print(carro_pasou_radar_2)

if carro_passou_radar_1 and carro_pasou_radar_2:
    print('Carro passou pelo radar 1')

if vel_carro_pass_radar_1:
    print('Velocidade carro passou do radar 1')


if carro_multado_radar_1:
    print('carro foi  multado em radar 1')