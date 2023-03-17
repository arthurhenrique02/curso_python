# O for é um loop no python, o mais utilizado entre eles.

# alguns elemtentos da iteracação:
#
# Iterável - str, range, etc. É o elemento que pode ser iterável, e que pode entregar um valor por vez
#   um iterável possui um método dentro dele chamado __iter__ (método é tudo aquilo que voce pode chamar após o .. Ex: str.upper())
# 
# Iterador - quem sabe entregar um valor por vez
# next - entrega o proximo valor
# iter - entregue seu iterador

# Exemplo:
# texto = "Arthur".__iter__() # Quando printar esse texto, será retornado o local onde está o iterador pra esse texto
# print(texto)

# No python há uma função que tem a mesma funcionalidade do __iter__
# É essa:

# texto = iter("Arthur")
# 
# O next serve apenas para pedir o proximo valor, ou seja, quando for executado, ele vai mostrar o proximo e depois o proximo... ate o final da str
# print(texto.__next__())
# print(texto.__next__())
# print(texto.__next__())
# print(texto.__next__())
# print(texto.__next__())
# print(texto.__next__())
# print(texto.__next__()) # quando acabar a string, ele retorna um erro, pois não há mais caracteres
# 
# # Também há uma função com a mesma funcionalidade
# print(next(texto))


# Usando um exemplo de iteração
texto_2 = "Arthur"
iterador = iter(texto_2)

# dentro do While loop

while True:
    try:
        print(next(iterador))
    except StopIteration: # agora, quando der algum erro após a iteração, ele irá retornar o StopIteration e fechar o programa (exit(0))
        exit(0)
