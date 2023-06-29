# No python, ha como limitar uma func para receber apenas parametros nomeados ou posicionais

# Sao os chamados Positional-Only (/) e Keyword-Only (*)

# podem ser utilizados da seguinte forma:

# Positional-Only (para apenas params posicionais)

# a barra diz que pode-se passar apenas argumentos posicionais
# o que vem antes da barra, tem que ser posicional
# o que vem depois, pode ser posicional ou nomeado
def soma(x, y, /, a): 
    print(x + y + a)

# funcionará
soma(1, 2, 3)

# mas, se tentar passar:

# tentando passar no try, para nao quebrar o programa
try:
    soma(1, y=2, a=3) # nao funciona, retorna um erro "TypeError"
except:
    print("nao possivel passar argumento y nomeado")


# Funcionará, pois o a está após a barra
soma(1, 2, a=3)

# Keyword-Only (para apenas argumentos nomeados)
# tudo que estiver antes do * é argumento posicional ou nomeado (pode ser qualquer um dos dois, a obrigatoriedade é apenaspara argumentos após o *)
# e tudo que vier depois do * é argumento nomeado, e deve ser chamado dessa forma (por exemplo a=10)
def soma2(x, y, *, a):
    print(x + y + a)

# funcionará  
soma2(2, 2, a=10)


# mas, se tentar passar:
# tentando passar no try, para nao quebrar o programa
try:
    soma2(2, 2, 10) # nao funciona, retorna um erro "TypeError"
except:
    print("nao possivel passar 'a' como argumento posicional")