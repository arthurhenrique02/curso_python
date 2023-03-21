# Count é um iterator do modulo "itertools" que é responsavel por contar

# O count é infinito, ou seja, sempre que chamar next, ele vai somar 1 e entregar o numero

# deve-se tomar cuidado com ele, ja que o mesmo é infinito

# Para utilizar, devemos importá-lo do modulo "itertools"

# counter pode pegar um numero como parametro de inicio e outro como parametro de pulo (step)

from itertools import count

counter = count(50, 10) # comeca de 50 e mostra de 10 em 10

print(next(counter))


# aqui irá gerar um loop infinito
for i in counter:
    print(i)

    # para parar o loop deve-se usar o break
    if i == 200:
        break