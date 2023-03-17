# Pode-se fatiar strings usando a seguinte forma:

# string[i:f:p]
#   Sendo 
#       i = inicio (de onde deve-se começar a fatiar)
#       F = final (até onde deve-se fatiar)
#       p = passo (Como deve seguir, passo 1 = pular de um em um)

nome = "arthur"
# começa do 0 e vai até o final pulando de 2 em 2 caracteres
print(nome[::2])

# começa do 1 e vai até o 3 pulando de 1 em 1
print(nome[1:3]) # mas não mostra o caracter na posição 3

print(len(nome)) # retorna o tamanho da str