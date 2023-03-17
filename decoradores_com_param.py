# Funções decoradoras e decorades podem conter parametros

# Por exemplo:

# def decorator(func):
#     print("decorator 1")

#     # definir funcao interna
#     def inner_func(*args, **kwargs):
#         print("INNER")
#         res = func(*args, **kwargs)
#         return res
#     return inner_func

# Quando executar sem os ()
# O decorador executará apenas o primeiro bloco de código (o bloco decorator)
    # sem entrar no codigo mais interno (inner_func)
    # como por exemplo
        # ao rodar o programa vc só verá o primeiro print "decorator 1"
# @decorator
# def soma(x, y):
#     return x + y


# ao executar a funcao soma, e utilizar os (), o bloco mais interno (inner_func) será executado também

    # isso ocorre pois quando o código roda e passa pelo @decorator, a func soma é 'trocada' pela inner_func, então ele decora a func soma e joga dentro do bloco interno

# executando a função soma
# dez_mais_cinco = soma(10, 5) # ao executar essa linha de código, vemos o segundo print "INNER", isso ocorre pq a funcao mais interna foi executada tambem

# ao utilizar o print para mostrar o valor da variavel acima, veremos o valor normal resultante da soma
# print(dez_mais_cinco)


# Os decoradores podem ter parametros, sendo adcionados de outro escopo
# Mas os decoradores em python sao obrigados a terem uma funcao como parametro

# Para adcionar parametros ao decorador, é necessário criar uma outra função aninhada que criará o decorador

# por exemplo:

# funcao criada para pegar os parametros do decorador e criar um decorador
def decorator_factory(a=None, b=None, c=None): # os parametros passados aqui podem ser acessados em qualquer escopo interno da funcao
    #print("DECORATOR FACTORY")
    # Por exemplo
    #print(a) # mostrando parametro a

    # funcao que irá criar a funcao interna
    def func_factory(func):
        #print("FUNC FACTORY")
        #print(b)# mostrando parametro c
        print(f"DECORADOR: {a}") # mostrar qual decorador foi criado
        # definir funcao interna
        def inner_func(*args, **kwargs):
            #print("INNER")
            #print(c)# mostrando parametro c

            res = func(*args, **kwargs)
            valor_final = f" {a}"
            return valor_final

        # retornar a funcao interna
        return inner_func
    
    # primeiro retornar a fabrica de funcoes
    return func_factory

# @decorator_factory(1, 2, 3) # passando parametros para o decorador
# def multiplicacao(x, y): # passando funcao para o decorador
#     return x * y

# dez_vezes_cinco = multiplicacao(10, 5) # executando funcao "multiplicacao"
# print(dez_vezes_cinco) # mostrando na tela


# Pode-se atribuir diversos decoradores à uma função, sendo a ordem de precedencia do mais proximo para o mais distante, ou seja, seria em "ordem decrescente"

# Exemplo:

@decorator_factory("QUINTO", 2, 3) # quinto...
@decorator_factory("QUARTO", 2, 3) # quarto
@decorator_factory("TERCEIRO", 4, 5) # terceiro
@decorator_factory("SEGUNDO", 3, 4) # segundo
@decorator_factory("PRIMEIRO", 2, 3) # executado primeiro
def divide(x, y):
    return x / y

dez_por_cinco = divide(10, 5)
print(dez_por_cinco)
