# para acessar outro objetos iteraveis dentro de uma lista (como uma tupla, lista, dicionario) é necessário usar uma lista 2d
# Por exemplo:

my_list = [
    ["arthur", "rayssa", "hill", ("rayssa", "arthur", "hill")],
    {"nome": "arthur", "age": 20, "year": 2002},
    ("rayssa", "arthur", "hill")
]

# para acessar a lista, deve-se digitar

print(my_list[0][2]) # onde 0 é o index da lista principal, e o 2 é o index da lista dentro da lista

# para acessar o dicinário
print(my_list[1]["nome"]) # "nome" é o nome do índice do dicionario

# para acessa a tupla
print(my_list[2][0])

# para acessar uma tupla, ou um iteravel, dentro de outro deve-se aumentar mais uma direção
# Por exemplo:

print(my_list[0][3][1]) # onde o indice um irá entrar dentro da tupla que está dentro da lista de indice 0