# aula sobre for
"""
texto = 'Python'
i = 0
tamanho_string = len(texto)

while i < tamanho_string:
    print(texto[i])
    i +=1


senha_salva = '123456'
senha_digitada = ''
repeticoes = 0

while senha_salva != senha_digitada: 
    senha_digitada = input(f'Sua senha ({repeticoes}X): ')

    repeticoes +=1

print(repeticoes)
print('Aquele laço acima pode ter repetições infinitas')

"""
texto = 'python'
novo_texto= ''


for letra in texto:
    novo_texto += f'*{letra}'
    print(letra)
print(novo_texto + '*') 