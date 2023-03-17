# Strings são textos
# Para criar uma string é necessário colocar o conteúdo entre aspas (simples ou duplas)
# exemplo:
nome = "Arthur"
# ou
nome_2 = 'Rayssa'

# para colocar uma aspas duplas dentro de um print tendo iniciado o print também com aspas duplas
# é necessário usar um caracter de escape chamado barra invertida (\)
print("Olá \"arthur\"")

# Se quiser que o caracter de escape apareça no print, basta digitar um R antes da string:
# o R, segundo o desenvolvedor, é apenas para expressões regulares, mas pode ser utilizado desta forma
print(r"Olá \"arthur\"")


# Mas para deixar seu código mais limpo e bonito, basta inverter as aspas
print(r"Olá 'arthur'")

# ou inverter as aspas do print
print('Olá "arthur"')