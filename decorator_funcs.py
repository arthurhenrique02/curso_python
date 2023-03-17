# Funções decoradoras são funções que decoram outras funções, salvam ela e não executam no momento (como o closure)

# Decorar = adicionar / remover / restringir / alterar


# Criando uma função decoradora:
    # criar_funcao é a func decoradora
def criar_funcao(funcao):
    # criar uma função interna que será executada após
    def func_interna(*args, **kwargs):
        # pode-se fazer coisas antes de checar a validade da outra função, por exemplo, printar alguma coisa:
        print("EXECUTANDO FUNCAO DECORADORA")
        for arg in args:
            is_string(arg)

        # variavel criada apenas para demonstrar que pode ser feito coisas após a execução da outra fun (is_string), assim como qualquer outra func
        resultado = funcao(*args, **kwargs)
        # como também pode-se fazer coisas após a execução da outra funcao (is_string)
        print("A FUNCAO FOI DECORADA COM SUCESSO")
        
        # retornar o resultado da func decoradora
        return resultado # poderia ser retornado apenas o func(*args, **kwargs)
    
    # retornar a função interna para que a mesma possa ser executada
    return func_interna

# criar func que inverte string como exemplo
def inverte_string(valor):
    return valor[::-1]

# func para checar se é string
def is_string(valor):
    if not isinstance(valor, str):
        raise TypeError("VALOR DIGITADO NÃO É UMA STRING")
    

inverter_string_checando_param = criar_funcao(inverte_string)
str_invertida = inverter_string_checando_param("OLAAABCD")
print(str_invertida)
