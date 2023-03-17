# List comprehension, em Python, é uma forma rápida de criar listas

# Por exemplo:

# pode-se colocar um iteravel dentro da lista colocando um valor a esquerda dele para que seja inserido dentro da lista
my_list = [numero for numero in range(10)]

print(my_list)

# pode-se colocar qualquer valor:
# nesse caso será inserido o numero 1 dez vezes na lista
my_list2 = [1 for numero in range(10)]
print(my_list2)

# Mapeamento é ver os items que estão sendo colocados dentro da lista e também poder modicá-los

# Exemplo:
produtos = [
    {"nome": "p3", "preco": 10,},
    {"nome": "p3", "preco": 20,},
    {"nome": "p3", "preco": 30,},
]

novos_produtos = [
    # desempacota os dicts da outra lista para mapeamento
    {**produto, "preco": produto["preco"] *  1.05} # aumento de 5%
    # operação ternaria para aumentar o preço caso o valor seja maior que 20
    if produto["preco"] > 20 else {**produto} # retorna o produto caso não seja
    # iterar a outra lista
    for produto in produtos
]

# mostrar na tela a lista desempacotada
print(*novos_produtos)

# Filter é toda a logica a direita do for, e filtra o que deve ser incluido dentro da lista a partir da condição
novos_produtos = [
    # desempacota os dicts da outra lista para mapeamento
    {**produto, "preco": produto["preco"] *  1.05} # aumento de 5%
    # operação ternaria para aumentar o preço caso o valor seja maior que 20
    if produto["preco"] > 20 else {**produto} # retorna o produto caso não seja
    # iterar a outra lista
    for produto in produtos
    # incluir itens com preço maior ou igual a 20
    if produto["preco"] >= 20
]

print(*novos_produtos)

# um for dentro do outro pode ser feito de maneira simples:

my_list4 = [
    # adciona uma tupla com os valores
    (x, y)
    for x in range(3) for y in range(3)
]

print(my_list4)