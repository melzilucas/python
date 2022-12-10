nome = "Lucas"
idade = 23
de_idade = 'de idade'
formato = '{a} tem {b:.2f} anos {c}'
print(formato.format(
    a=nome, b=idade, c=de_idade))