""" 
for in com listas
mostrando os indices para cada item da lista
""" 

lista = ['lucas', 'joão', 'pedro', 10, 10.2, True]
indice = 0
tamanho_lista = len(lista)

for nomes in lista:
    print(f'O nome é: {nomes} e o indice é: {indice}')
    indice +=1
    
print(tamanho_lista)