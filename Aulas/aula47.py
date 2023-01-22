"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""

def soma (a, b, c):
    print(f'{a=} {b=} {c=}' , '|' , 'a + b + c=' , a + b + c)


soma(10,20,30 )

soma(a=10, b=20, c=30)