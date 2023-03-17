# Comando que podem ser utilizados com f-strings
# Pode-se adicionar paddings à string, caso a string não alcance a quantidade determinada de caracteres
# São os comando:
# > - Adiciona caracteres à esquerda
# < - Adiciona caracteres à direita
# ^ - Coloca os caracteres da string ao centro
#
# Pode-se utilizar sinais:
# - para mostrar quando for negativo (por padrao ja mostra)
# + para mostrar quando for positivo  (Ex: f'{10:+})
# = Força o numero a aparecer após alguma coisa (zeros, por exemplo)
# , serve para separar as milhas com a virgula (Ex: f'{1000:,})
# x ou X é para mostrar o Hexadecimal

print(f"{100000:+,}")
print(f"Hexadecimal de 1500: {1500:08X}")