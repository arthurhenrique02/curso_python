# continue é uma estrutura para loops em python
# Consiste em pular uma determinada etapa do loop, que você deseja
# Após o interpretador ver a palavra 'continue' ele irá voltar para o inicio do loop a partir daquele código
# Por exemplo:

# Um loop que mostre 10 numeros na tela, vocâ não deseja que apareça o numero 5
# Então:

contador = 0

while contador <= 10:
    # O contador pode ser incrementado no inicio ou no final, depende da estratégia
    contador += 1

    # pular o 5
    if contador == 5:
        continue

    # No print, será visto que o numero 5 não foi mostrado
    print(contador)
