"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd 
de caracteres da str
"""
variavel = 'Olá mundo'
print(variavel[3:])

espaço = ' '
print(len(variavel)) #conta qtde)

print(len(variavel[3]))
print(variavel[3])

variavel_passo  = 'teste_passo'

print(variavel_passo[::-1])