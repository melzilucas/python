#operadores in e not in
#strings sao interáveis

# 0 1 2 3 4
# l u c a s

# nome = 'lucas'
# print(nome[2])

# print('s' and 'a' in nome)
# print(10 * '-')
# print('a' not in  nome)

nome = input('Digite o seu nome:'  )
encontrar = input('Digite o que deseja encontrar:'  )


if encontrar == nome and '' in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')

# variavel_a = 1 or 0
# variavel_b = 0 or 1
# print(variavel_a, variavel_a)

# nome = 'Maria Carmo'
 
# if ' ' in nome:
#     print(f'O nome {nome} tem espaços.')
# else:
#     print(f'O nome {nome} NÃO tem espaços.')