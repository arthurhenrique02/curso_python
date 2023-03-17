# Enumerator serve para enumerar os itens de uma lista a partir dos indices

lista = [1, 2, 3, 4, 5, 6, 7, 8]

lista_enumerator = enumerate(lista)
print(lista_enumerator) # irá retornar o end de memoria do enumerator

# Para printar isto, basta colocá-lo dentro de uma lista
print(list(lista_enumerator))

# pode-se usar um loop for
for item in lista_enumerator:
    print(item) # caso tente pritar os mesmos elementos novamente, "nada irá acontecer", na verdade o iterador 'para' após o último elemento, ele não volta para o inicio da lista


# com uma tupla:
my_tuple = 1, 2, 3, 4, 5, 6

my_enum_tuple = enumerate(my_tuple)

print(tuple(my_enum_tuple))

for item in my_enum_tuple:
    print(item)

# Para desviar do problema de não conseguir o mesmo valor novamente, basta fazer isso:

# Geralmente, o enumerate não é utilizado dentro de uma variável

# Exemplo:

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(list(enumerate(my_list)))

# ou
for item in enumerate(my_list):
    print(item)

# Pode-se escolher de qual numero voce deseja que o iterador comece, por exemplo:

print(list(enumerate(my_list, start=10)))

# uma estrategia de desenpacotamento pode ser:
for indice, nome in enumerate(my_list):
    print(indice, nome)
