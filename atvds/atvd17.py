# Exercício - Adiando execução de funções
def soma(x, y):
    return x + y


def multiplica(x, y):
    return x * y


def criar_funcao(funcao, x):
    # fazer o closure da funcao
    def executar_funcao(*args):
        return funcao(x , *args)
    # retornar funcao que esta interna
    return executar_funcao


soma_com_cinco = criar_funcao(soma, 5)
multiplica_por_dez = criar_funcao(multiplica, 10)

print(soma_com_cinco(1))