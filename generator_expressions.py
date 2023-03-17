# Generator expressions sao basicamente funções que sabem pausar em uma determinada ocasião

# Um iterator não é um Generator

# Por exemplo:

# Ao usar list comprehension, como por exemplo preencher uma lista com 10 numeros, ficaria algo tranquilo e organizado para o computador. Mas imagina você querer preencher uma lista com 10000 numeros, ficaria algo desorganizado e ocuparia muito espaço

# Então, poderia ser criado um generator que atribuisse um item por vez dentro da lista, por exemplo, a cada vez que for solicitado

# Para criar um generator:
generator = (n for n in range(10000)) # basta mudar as chaves da lista para parenteses 
print(generator) # sera retornado o local na memoria do generator

# para ver a diferença de tamanho entre um generator e uma lista ja criada, basta importar a biblioteca sys

from sys import getsizeof

lista = [n for n in range(10000)]

print(getsizeof(lista))
print(getsizeof(generator))

# A diferença entre generator e lista é que na lista pode-se acessar por indice, saber o tamanho, e no generator isso não ocorre

