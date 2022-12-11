#else no while

nome = 'Lucas Eduardo Melzi'
i = 0

while i < len(nome):
    letra = nome[i]
    #break finaliza o while e cai no print dora do while
    
    if letra == ' ':
        break

    print(letra)
    i += 1
else:
    print('Não encontrei espaço')

print('Sempre executado')

"""
recurso particular do python
roda o while até achar o espaço na nome
achando o espaço, cai no if e no break e morre o while
"""