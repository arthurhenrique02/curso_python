# Try, except, else, finally

# O try tentará executar um bloco de código, caso retorne algum erro, será ativado o execept ou o finally

# O finally pode ser utilizado sozinho com o try ou também pode ser utilizado em grupo (try, except e finally)

    # Ele sempre será executado, independente se algum erro ocorrer

    # um exemplo de utilização seria fechar algum arquivo que foi aberto no try

# O else é acionado após o bloco try ser executado

    # Somente da para usar o bloco else caso seja utilizado try e except, caso tente utilizar try finally, não será possivel
    # Ou seja, após bloco try ser executado, o bloco else também será


try:
    # 10 / 0
    print("hello world")

except ValueError: # ValueError trata todos os erros de uma maneira geral
    print(ValueError)

finally:
    print("aaa")


# Pode-se utilizar diversos except para tratar diversos erros
try:
    a = 10
    b = 1
    a / b
    frase = "ola mundo"

    frase[1000]
    c = a / "b"
    print("hello world")

# pode-se resolver mais de um erro por except, basta adcionar uma tupla. Por exemplo:
except (ZeroDivisionError, TypeError): # ZeroDivisionError trata o erro de divisao por 0
    print("impossivel dividir por 0 ou impossivel dividir um numero por uma letra")

except NameError: # ZeroDivisionError trata o erro de divisao por 0
    print("variavel nao definida")

# Para pegar a mensagem do error, é so atribuí-lo à uma variável quando declarar o except, para isso deve-se utilizar o as
except IndexError as error:
    print(f"msg: {error}")