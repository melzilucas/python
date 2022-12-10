#calculo imc
#IMC = Peso ÷ (Altura × Altura)

nome =  'Lucas Eduardo'
altura = 1.80
peso = 72
imc = peso / (altura ** 2)

#print(nome, 'tem', altura, 'de altura,')
#print('pesa', peso, 'quilos e seu IMC é:')
#print(imc)

#renderizando variaveis, F strings
#f-strings -> f de formatacao
linha_1 = f'{nome} tem {altura:.2f} de altura' #2f = 2 casas decimais
linha_2 = f'pesa {peso} quilos e seu IMC é,'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)
