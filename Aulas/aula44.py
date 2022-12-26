#introducao ao desempacotamento

#nomes = ['lucas', 'joao', 'maria']

nome1, nome2, nome3 = ['lucas', 'joao', 'maria']

print(nome1)

nome1, *restante= ['lucas', 'joao', 'maria']

print(restante)

nome1, *_ = ['lucas', 'joao', 'maria'] # underline significa que a variável não será utilizada, por convenção

print(_)