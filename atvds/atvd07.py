# Criar um programa pra iterar strings com while

# criar uma string
nome = "Arthur Henrique"

novo_nome = ''  # iniciar nova string
counter = 0    # iniciar counter

# iniciar o while
while counter < len(nome):
    letra = nome[counter]
    novo_nome += f'{letra:->2}'
    counter += 1

print(novo_nome)