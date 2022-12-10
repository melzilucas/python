"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""
numero_str = input(
    'Vou dobrar o número que vc digitar: '
)

print(numero_str)
try:
    numero_float = float(numero_str)
    print(f'numero float é: {numero_float:.2f}')
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
except:
    print('Isso não é um número')


# try:
#     numero_float = float(numero_str)
#     if numero_str.isdigit():
#      print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
#     else:
#      print('Isso não é um número')

# except:
#     print('alo')