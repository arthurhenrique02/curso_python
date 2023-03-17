# para desempacotar variaveis de uma lista, tupla ou qualquer outro iteravel, basta fazer isso:

numeros = [1, 2, 3]

num1, num2, num3 = numeros

print(num2)
print(num1)

# Se desejar pegar apenas um valor, ou algun valores, é necessario falar para o python o que ele vai fazer com o resto

# Para isso é necessario usar o * com o nome da variavel, por exemplo:

num4, *numeros_2 = numeros

print(num4)
print(numeros_2)

# Quando não se quer usar a variável, basta usar um _ no lugar, a variável vai continuar existindo, mas no mundo da programação quer dizer que não é para usar ela

num4, *_ = numeros # pode-se printar a variável _
print(num4)


# para desempacotar itens em chamadas de funções basta digitar *item na função
# Por exemplo:

print(*numeros)