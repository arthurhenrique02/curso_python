# Criar um programa para ver se o numero digitado pelo usuario é par ou impar, no caso de nenhum numero digitado, retorar umas mensagem

# solicitar numero
num =input("Digite um número inteiro: ")

# checar se digitou um numero inteiro
try:
    int(num)
except:
    print("O valor digitado é inválido.\nDigite um número inteiro")
    exit(1)

if int(num) % 2 == 0:
    print("O numero digitado é par.")
else:
    print("O numero digitado é ímpar.")
