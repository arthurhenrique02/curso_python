# A função print pode pegar vários argumentos como parâmetro sem necessariamente precisar digitar infinitos parametros na hora de escrevê-la:

# Exemplo: 
print(1, 2, 3, 4, 5, 6, 7, 8, 9, 10) # Na função, o criador não escreveu 10 parametros, ele usou *args

# Args é apenas uma convensão para argumentos, mas poderia ser escrito qualquer coisa, como *abc por exemplo

# Para pegar diversos argumentos como parametro é necessário mudar a logica da função e os parametros

# Exemplo

def soma(x, y): # essa função só poderá pegar 2 argumentos como parametro
    return x + y

# ja se for definido com *args como parametro, poderemos pegar infinitos parametros
def subtracao(*args): # todos os argumentos serão salvos em uma tupla

    # a logica dentro do código terá que ser mudada
    total = 0
    for num in args:
        total -= num
    return total
