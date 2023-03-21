# importando as funções utilizadas
from functools import partial
from types import GeneratorType

# partial é uma função do módulo functools que faz a closure "automaticamente" para você

# Exemplo:

"""partial"""
def aumentar_porcentagem(valor, porcent):
    return round(valor * porcent)


# Utilizando partial para passar 1 argumento
aumentar_dez_porcento = partial(
    aumentar_porcentagem,
    porcent=1.1 # pode-se passar argumentos não nomeados, mas como não está na ordem (porcent, valor), passaremos um argumento nomeado
) 
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# criar nova lista usando a variavel com partial
novos_produtos = [
    {**p,
        'preco': aumentar_dez_porcento(p['preco'])}
    for p in produtos
]

print(novos_produtos)


"""map"""
# map é uma função do Python que tem como objetivo mapear um objeto e aplicar alterações

    # no map passa-se a função que deseja aplicar uma alteração e o objeto que será mapeado


# criando uma função para aumentar o valor do produto
def muda_preco(produto):
    return {
        **produto,
        'preco': aumentar_dez_porcento(produto['preco'])
    }

# utilizar map para mudar o preco
novos_produtos_map = map(
    muda_preco,
    produtos
)

# pode-ser utilizado a função lambda dentro do map. Por exemplo:

print(
    list(
        map(
            lambda x: x*3,
            [1,2,3,4]
        )
    )
)

# ao utilizar map, é retornado um objeto (map object), para iterar sobre ele é necessário um for, ou colocá-lo em uma classe (list, set, tuple, ...)
print(list(novos_produtos_map))

"""GeneratorType"""

# GeneratorType é uma função do módulo types que checa se um determinado objeto é um generator, retornar True ou False

# para verificar melhor vamos utilizar a variavel novos_produtos_map para checar

# verificaremos se o "map" é um generator e depois modificaremos a variavel para um generator
print(f"ANTES DA MODIFICACAO: {isinstance(novos_produtos_map, GeneratorType)}") # retornará False

# criando um generator para a variável
novos_produtos_map = (x for x in produtos)
print(f"DEPOIS DA MODIFICACAO: {isinstance(novos_produtos_map, GeneratorType)}") # retornará True