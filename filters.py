# filter é uma função em Python que tem como objetivo filtrar dados de um objeto

    # a diferença entre filter e map é que geralmente, no map, você terá o mesmo tamanho do objeto original

    # ja no filter, isto pode ser mudado

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# criar nova lista usando a variavel com partial
novos_produtos = [
    p for p in produtos
    # esta linha é um filter (seria o filter a list comprehension)
    if p["preco"] > 100
]

# não diferença entre usar o filter da list comprehension ou a função filter (programação funcional). É criterio do programador

# Utilizando filter:
# a função filter irá retornar um iteravel, para utiliza-lo basta colocar dentro de uma classe
novos_produtos_filter = filter(
    #passa-se uma função como primeiro argumento
    lambda x: x["preco"] > 50,
    produtos
)

print(novos_produtos)
print(list(novos_produtos_filter))