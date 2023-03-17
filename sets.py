# Sets sao uma classe bastante utilizadas para retirar valores repetidos

# não possuem indices
# não garantem ordem

# para criar um set:
my_set = set() # criar um set vazio

# para criar um set com valores dentros:
# my_set = {1, 2, 3, 4}

# Métodos uteis nos sets

my_set.add(1) # add so adciona um valor por vez
my_set.update(("ola mundo", 1, 2, 3 ,4)) # para um texto não ser separado letra por letra é necessario coloca em uma tupla ou em um outro iteravel

# my_set.clear() #limpa o set
my_set.remove("ola mundo") # remove um item

print(my_set)

# Operadores/ metodos com set
my_set2 = {1, 2, 5, 6, 7, 8}

# union
my_set3 = my_set.union(my_set2) # retornara um novo set com os itens dos outros 2

# intersection
my_set4 = my_set.intersection(my_set2) # retorna as intersecções de 2 sets

# difference
my_set5 = my_set.difference(my_set2) # retorna a diferença do primeiro set pro segundo

# symetric_difference
my_set6 = my_set.symmetric_difference(my_set2) # retorna a diferença entre os 2 sets

# difference update
my_set7 = my_set.difference_update(my_set2) # remove elementos do 1 set que o segundo set tbm possui

# symetric difference update
my_set8 = my_set.symmetric_difference_update(my_set2) # remove todos os elementos iguai que os 2 sets possuem

# is super set
my_set9 = my_set.issuperset(my_set2) # verifica se o primeiro set possui todos os elementos do 2

# is sub set
my_set10 = my_set.issubset(my_set2) # verifica se o segundo set possui todos os elementos do 1

print(my_set3)
print(my_set4)
print(my_set5)
print(my_set6)
print(my_set7)
print(my_set8)
print(my_set9)
print(my_set10)
