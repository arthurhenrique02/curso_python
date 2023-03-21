# Itertools é um módulo em python que tem diversos iteráveis

# combinations - metodos matematico para fazer combinações
    # Não importa a ordem

    # Deve-se passar o iteravel e o tamanho do grupo como parametro

# Permutations - metodo matematico que faz combinações

    # Nesse caso, a ordem importa (arthur e raysa é diferente de rayssa e arthur, por exemplo)s

    # passa-se o iteravel e tamanho

# Product

    # ordem importa

    # faz a iteração e a combinação de 2 iteraveis juntos, por exemplo, 2 listas juntando-as, ficaria ("arthur", "preta")

# Exemplos:

# deve-se importar de itertools
from itertools import combinations, permutations, product, groupby # importado todas as funcoes que serao utilizadas

# da para importar combinações com preenchimento, basta importar combinations_with_replacement

pessoas = [
    "arthur", "rayssa", "pedro", "rayane"
]

camisas = [
    ["pretas", "brancas", "laranjas"],
    ["p", "m", "g", "gg"]
]

# fazendo combinações de nomes
"""combinations"""
print(list(combinations(pessoas, 2))) # combinations retorna um objeto, por isso ele está sendo colocado dentro de uma lista
print()

"""permutation"""
print(list(permutations(pessoas, 2))) # também retorna um objeto
print()
"""product"""
print(list(product(pessoas, camisas)))
print()
# Com product, da para utilizar listas de listas, apenas é necessário desempacotá-las, por exemplo *lista1
# print(list(product(*camisas)))

# pode-se utilizar o parametro "repeat" para repetir quantas vezes quiser
# print(list(product(*camisas, repeat=2))) # criará uma tupla, a cada iteração, que contem elementos 2 vezes (exemplo: ('pretas', 'p', 'pretas', 'p'), ('pretas', 'p', 'pretas', 'm'))


"""groupby"""
# Groupby é uma funcionalidade do itertools que agrupa items por alguma coisa

    # para o groupby funcionar, os itens devem estar ordenados

    # a função gera um objeto iteravel onde pode-se pegar chave e valores

# pode-se utilizar groupby para agrupar uma lista, mas ele seria mais usual em listas/elementos mais complexos (por exemplo, uma lista de dicionarios)

# Utilizando o exemplo de lista:

myList = ["a", "a", "a", "a", "a", "b", "c"] 
grupos = groupby(myList) # criará um objeto iteravel e dará "a" como chave e valor, "b" como chave e valor e "c" como chave e valor

for chave, valores in grupos:
    # o resultado do print mostrará grupos de letras salvos em uma lista e a chave deles (a propria letra, neste caso)
    print(chave, list(valores)) # necessario colcocar os valores em uma classe (list, tuple, set, etc)


# no caso de listas mais complexas, é necessario ordenar antes
alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
]


# criar função para pegar nota
def pegaNota (aluno):
    return aluno["nota"]

# para ordernar basta fazer
alunos.sort(key=lambda x: pegaNota(x))

# pode-se passar outro parametros na funcao groupby
grupos_de_alunos = groupby(alunos, key=lambda x: pegaNota(x)) # irá agrupar por nota dos alunos

for chave, grupo in grupos_de_alunos:
    print(chave, list(grupo)) # necessario colcocar os valores em uma classe (list, tuple, set, etc)
    

# print(alunos)