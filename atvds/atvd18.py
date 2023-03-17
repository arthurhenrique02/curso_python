# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]


# definir as listas
cities = ['Salvador', 'Ubatuba', 'Belo Horizonte']
siglas = ['BA', 'SP', 'MG', 'RJ']

def ver_maior(lista1, lista2):
    #retornar len da lista2 caso seja maior
    if len(lista2) < len(lista1):
        return len(lista2)
    
    # retornar len lista1 por padrao
    return len(lista1)

# definir funcao zipper
def zipper(lista1, lista2, length):\
    # pode ser resolvido dessa forma:
    # # criar lista temporaria
    # tempList = []
    # # criar um loop para percorrer as duas listas
    # for i in range(length):
    #     tempList.append((lista1[i], lista2[i]))
    #     print(tempList)
    # # retornar lista
    # return tempList

    # ou desta forma:
    max_index = min(len(lista1), len(lista2))
    return [
        (lista1[i], lista2[i]) for i in range(max_index)
    ]

# declarar variavel e atribuir funcao
cidades_e_estados = zipper(cities, siglas, ver_maior(cities, siglas))
# mostrar na tela
print(cidades_e_estados)

# o Python ja tem essa funcao pronta e ela se chama "zip"

# O zip pega valores e "zipa" ele, junta-os, e retorna um local na memoria onde esta localizado este objeto
# para consumir esse objeto, basta coloca-lo numa classe (tupla, lista, set, dict) ou utilizar um for

print("local na memoria ", zip(cities, siglas)) # sera retornado um objeto
print("set ", set(zip(cities, siglas)))
print("dict ", dict(zip(cities, siglas)))
print("lista ", list(zip(cities, siglas)))
print("tuple ", tuple(zip(cities, siglas)))

# python tem um modulo chamado itertool que possui uma funcao que utiliza o valor da lista maior para "zipar"
from itertools import zip_longest
print("tuple ", tuple(zip_longest(cities, siglas, fillvalue="NAO TEM A CIDADE"))) # fillvalue é o valor que vai substituir o valor nulo (None)


