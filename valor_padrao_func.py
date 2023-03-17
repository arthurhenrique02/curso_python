# definir um valor padrao como 0 ou "", por exemplo, pode gerar um problema posterior ao checar os valores

# Então devemos optar por atribuir um valor padrao igual a None, isso vai tirar os problemas, mesmo que ele também seja considerado falsy

# Por exemplo:

# função definida com valor padrao 0:

# Nesse caso, se o usuario digitar que z é igual a 0, a função vai entrar na condição else, gerando um de sintaxe pois o usuario digitou q o valor de z é 0
def soma(x, y, z=0):
    if z:
        print(f"{x=}, {y=}, {z=}", x + y + z)
    else:
        print(f"{x=}, {y=}", x + y)

# com valor padrao igual a None

# Nesse caso se o usuario digitar que z é igual a zero, irá entrar na condição do if, pois z tem um valor considerado atribuido e não falsy
def subtracao(x, y, z=None):

    if z is not None:
        print(f"{x=}, {y=}, {z=}", x - y - z)
    else:
        print(f"{x=}, {y=}", x - y)

soma(10, 20, 0)
subtracao(10, 20, 0)