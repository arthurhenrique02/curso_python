# reduce é uma função do módulo functools que reduz o iteravel à um valor

from functools import reduce

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]


# a função passada para o reduce deverá ter 2 parametros o acumulador (prev ou acumulator) e o produto
    # caso não seja passado o valor inicial, ele será o primeiro valor
def reduce_func(prev, value):
    return prev + value["preco"]

total = reduce(
    # primeiro argumento é uma função
    reduce_func,
    # segundo é o iteravel
    produtos,
    # terceiro é o valor inicial (pode-se não passar o valor inicial, mas gera transtornos posteriormente)
    0
)

# com lambda
total2 = reduce(
    lambda x, y: x + y["preco"],
    produtos,
    0
)

print(total)
print(total2)