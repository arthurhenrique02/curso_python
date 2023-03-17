# criar um programa que cotenha uma palavra secreta e o usuario tenha que advinhar, 
# mostrar as palavras em *
# aceitar so uma letra por vez
# Se a palavra secreta possuir a letra digitada, mostrar na tela. Exemplo: A*****

# importar os para limpar o terminal
import os

# Solicitar a palavra
palavra = "arthur"
letras_acertadas = '' # string vazia para salvar as letras acertadas
tentativas = 0

# Criar o loop
while True:
    # solicitar letra
    letra_digitada = input("Digite uma letra: ")

    # contabilizar tentativas
    tentativas += 1

    # checar se foi digitado apenas uma letra
    if len(letra_digitada) > 1:
        print("Digite apenas uma letra!")
        continue

    # checar se a letra digitada está na palavra
    if letra_digitada in palavra:
        letras_acertadas += letra_digitada
    
    # loop para mostrar a palavra escondida
    palavra_escondida = ''
    for letra in palavra:
        if letra in letras_acertadas:
            palavra_escondida += letra
        else:
            palavra_escondida += "*"
    
    print(palavra_escondida)

    if not "*" in palavra_escondida:
        os.system("cls")
        print("Parabéns!!!\n"
              "Você ganhou!!\n"
              f"A palavra é: {palavra}\n"
              f"Tentativas: {tentativas}")
        palavra_escondida = ''
        