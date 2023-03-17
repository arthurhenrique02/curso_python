# No and, todas as condições precisam ser verdadeiras para que seja retornado True
# Caso contrario, alguma condição seja falsa, a expressão inteira será falsy (que são valores não necessariamente falsos, mas que são considerados falsos
# Exemplo: 0, 0.0, '', False (False é considerado falso mesmo))

# Se for digitado:
print(True and True and True) # vai ser retornado True, pois todos os valores são verdadeiros

# Se for digitado:
print(True and False and True) # será retornado False, pois há um valor falso

# Se for digitado:
print(True and 1) # será retornado 1, pois há um número 1

# Isso ocorrerá quando for digitar qualquer número
# Exemplo:
print(True and 5)
print(True and 0)

# Caso seja digitado um número e false, o resultado será false
print(True and 1 and False)

# Caso seja digitado 0 e dois valores True, o resultado será 0
print(True and 0 and True)

# Caso seja digitado qualquer número e dois valores True, o resultado será True
# Ou o ultimo valor digitado, caso o número seja o ultimo, retornará o numero
print(True and -10 and True)
