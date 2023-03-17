# criar uma função que multiplica todos os números, salvar em uma variavel e mostrar o valor

# Depois criar uma função para ver se é impar ou par e mostrar

import re

# definir função de multiplicação
def mult(*args):
    # checar se ha algum numero na tupla
    if len(args) < 1:
        return 0

    # definir total
    total = 1
    for num in args:
        total *= int(num)

    # retornar total
    return total

# definir função de par ou impar
def par_impar(num):
    # usar operação ternaria para retornar
    return "par" if num % 2 == 0 else "impar"

# definir função main
def main():
    # definir lista para numero digitados pelo usuario
    numeros = []

    # pegar quantos numeros o usuário deseja
    while True:
        num = input("Digite um número ou [s]air: ")

        # caso digite s, encerrar o loop
        if num.lower().startswith("s"):
            break

        # checar se tem letra e substituir
        num = re.sub(r"[^0-9]", "", num)

        # se o num for vazio, pular o loop
        if num == "":
            continue

        # adicionar o numero digitado a lista
        numeros.append(num)
    
    # multiplicar numeros e mostrar na tela o valor
    total = mult(*numeros)
    print(f"A multiplicação deu: {total}")

    # ver se é par ou impar e mostrar na tela
    odd_even = par_impar(total)
    print(f"O número {total} é {odd_even}")

# executar o bloco main
main()
