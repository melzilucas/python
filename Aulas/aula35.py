"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""
# for letra in texto
#texto = 'Luiz'  # iterável

# iteratador = iter(texto)  # iterator

# while True:
#     try:
#         letra = next(iteratador)
#         print(letra)
#     except StopIteration:
#         break

"""
texto = 'luiz'.__iter__()
texto = iter('Luiz')

#print(texto.__next__())#um item por vez
#print(texto.__next__())#um item por vez
#print(texto.__next__())#um item por vez
#print(texto.__next__())#um item por vez

#que é igual

print(next(texto))
print(next(texto))
print(next(texto))
print(next(texto))
"""
#entendendo o for replicando while
texto = 'Lucas' #iterável
iteratator = iter(texto) #iteratator

while True:
    try:
        letra = next(iteratator)
        print(letra)
    except StopIteration:
        break

#for
for letra in texto:
    print(letra)