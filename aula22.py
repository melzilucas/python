"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""
nome = 'lucas'
idade = 19
preço = 19.00

variável_teste = 'o nome é %s e o preço é R$%.2f' % (nome, preço)

print(variável_teste)
print('o hexadecimal de %s e %08X' % (idade, idade))