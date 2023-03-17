# No or, todas as condições precisam ser verdadeiras para que seja retornado False
# Caso contrario, alguma condição seja verdadeira, a expressão inteira será verdadeira

# falsy (que são valores não necessariamente falsos, mas que são considerados falsos
# Exemplo: 0, 0.0, '', False (False é considerado falso mesmo))

# Avaliação de curto circuito
print(True or False or 0)

# Caso tenha algum outro valor
print(True or False or 0 or 'abc') # será retornado True

# Caso todas as operações sejam falsas e exista algum outro valor, será retornado o ultimo valor verdadeiro
print(False or False or 0 or 'abc') # será retornado 'abc'

# Pode usar esses operadores (and, or, not, not in, in) em variáveis
# exemplo:
# or
senha = input("senha: ") or "Senha padrao"
print(senha)

# and
senha_2 = "1234" and "567"
print(senha_2) # será retornado '567'

