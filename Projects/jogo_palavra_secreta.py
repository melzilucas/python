#jogopalavrasecreta

import os

palavra_secreta = 'melzi'
tamanho_palavra_secreta = len(palavra_secreta)
numero_tentativas = 0
letras_acertadas = ''

while True:

    letra_digitada = input('Digite uma letra: ')
    numero_tentativas += 1

    if len(letra_digitada) > 1:
        print('digite apenas uma letra')
        continue
    if letra_digitada != str():
        print('digite uma letra')
        
    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada
    
    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada +=  '*'

    print('palavra formada:', palavra_formada)
    
    if palavra_formada == palavra_secreta:
        os.system('clear') #limpar terminal
        print('VOCÊ ACERTOU!!')
        print('A palavra era:', palavra_secreta)
        print('tentativas:', numero_tentativas)
        numero_tentativas = 0
        letras_acertadas = 0