# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

# shallow copy, não copia os subniveis, por exemplo a lista l1, apenas no primeiro nível. Ou seja, L1 será apenas apontado para o dicionário de origem. É copiado apenas valores mutaveis e os imutaveis sao apenas "linkados".

import copy

d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0, 1, 2],
}
d2 = d1.copy()

d2['c1'] = 10
d2['l1'][1] = 999999

print('d1:', d1)
print('d2:', d2)
print('#############')

#deepcopy é uma copia profunda, e um dict não afeta mais o outro dict.

d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0, 1, 2],
}
d2 = copy.deepcopy(d1)

d2['c1'] = 10
d2['l1'][1] = 999999

print('d1:', d1)
print('d2:', d2)