#continue, break, else no for

for i in range(10):
    if i == 2:
        print('i é 2, estou pulando...')
        continue

    if i == 8:
        print('i é 8, o else não sera executado')
        break #quando cair nessa condicação, i==8 o break finaliza o laço.

    for j in range (1,3):
        print(i,j)
else:
    print('For completo com sucesso')#só executa após finalizar o laço do for, caso não tenha o braeak
    