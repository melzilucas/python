"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""

nome_usuario = input('Digite seu nome:  ')
nome_usuario_len = len(nome_usuario)
idade_usuario = input('Digite sua idade:  ')
nome_usuario_com_espaço = ' ' in nome_usuario #retorna true ou false

if nome_usuario_com_espaço == True:
   tem_espaço = 'contem'
else: tem_espaço = 'nao contem'

if nome_usuario and idade_usuario:
    print(f'Seu nome é {nome_usuario}')
    print(f'Seu nome invertido é {nome_usuario[::-1]}')
    print(f'Seu nome {tem_espaço} espaço')
    print(f'Seu nome tem {nome_usuario_len} letras')
    print(f'A primeira letra do seu nome é {nome_usuario[0]}')
    print(f'A última letra do seu nome é {nome_usuario[-1]}')
    if ' ' in nome_usuario:
            print('Seu nome contem espaço - outra forma de fazer')
    else: 
            print('seu nome não contém espaço - outra forma de fazer')
        
else: print('Desculpe, você deixou campos vazios')