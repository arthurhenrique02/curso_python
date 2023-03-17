# Yield é um elemento que é utilizado em funções com generator, ele "substitui" o return para o generator, ou seja, o generator retornará o yield e o return retornará o que o dev deseja

# Por exemplo:

def generator(n=0):
    yield 1 # pausa a execução da função neste ponto

    # O return ainda poderá ser utilizado. Ele funcionará basicamente como uma Raise StopIteration, ou seja, uma exceção caso algo aconteça
    return "Ola"

gen = generator(1)
print(gen) # mostra o local do obejeto generator

# Para mostrar o que está no yield é necessario utilizar o método next
print(next(gen))

print("==================================")
# print(next(gen)) # nesse exemplo, nessa linha será retornado a StopIteration exception


# pode-se utiliar condicionais e loops dentro da função com generator

# Por exemplo:

def func_generator(n=0, max=10):
    while True:
        # coloca o yield para pausar
        yield n

        # para incrementar o yield sem criar um loop infinito e sem precisar declarar, nesse caso, quando definir a função (exemplo: gen = func_generator(0, 10))
        # é necessário incrementar um contador
        n += 1

        # verificar se n é maior que o maximo e retornar caso True
        if n > max:
            return

# defina a variável q carregará a função
teste2 = func_generator(0, 20)

for num in teste2:
    print(num)
    if num >= 5:
        break

print("=========================")
for num in teste2:
    print(num)
print("=========================")


# Yield from

# Em python é possível começar um novo generator a partir de onde outro parou

# Por exemplo

def gen1():
    yield 1
    yield 2
    yield 3

def gen2():
    yield 4
    yield 5
    yield 6

def gen3(gen): # pegar a função com generator
    # Yield from irá entrar na função passada por argumento e pegar tudo o que está no bloco do yield atual, "passando" os valores para a função gen3
    yield from gen() # permite pegar o bloco onde o yield da outra função está, nesse caso, so irá pegar os numeros
    yield 10
    yield 20
    yield 30

g1 = gen3(gen1) # pegar os yields do gen1 e colocar no g3
g2 = gen3(gen2) # pegar os yields do gen2 e colocar no g3

# mostrar na tela
for num in g1:
    print(num)

print("======================================")
for num in g2:
    print(num)
