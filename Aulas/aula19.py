#exercicios if e comparação

primeiro_valor = input('Digite um valor:  ')
segundo_valor = input('Digite outro valor:  ')

primeiro_valor_maior = primeiro_valor > segundo_valor
valores_iguais = primeiro_valor == segundo_valor

if primeiro_valor_maior:
    print(f'primeiro_valor = {primeiro_valor} '
     f'é maior que o segundo valor = {segundo_valor}'
    )

elif valores_iguais:
    print('os valores são iguais')

else:
    print(f'segundo valor = {segundo_valor} '  
    f'é maior que o primeiro valor = {primeiro_valor}'
    )