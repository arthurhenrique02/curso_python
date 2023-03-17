# Decoradores são usados para fazer o Python usar as funções decoradas em outras funções

# Decoradores são syntax sugar, ou seja, "grudam" em uma função

# para utilizar o decorador (@), não precisariamos mais da declaração da variável "inverter_string_checando_param = criar_funcao(inverte_string)"
# Seria necessario colocar apenas @criar_funcao em  cima da função inverte_string
# E a função inverte_string também executaria as linhas de codigo da func criar_função.


# os comentários para essas funções estão no módulo "decorador_funcs.py"
def criar_funcao(funcao):
    def func_interna(*args, **kwargs):
        print("EXECUTANDO FUNCAO DECORADORA")
        for arg in args:
            is_string(arg)
        resultado = funcao(*args, **kwargs)
        print("A FUNCAO FOI DECORADA COM SUCESSO")

        return resultado 
    return func_interna

# o decorador (@), que é syntax sugar, fará com que a função inverte string decore a função criar_função sem precisar dar um outro nome para ela
@criar_funcao
def inverte_string(valor):
    return valor[::-1]

def is_string(valor):
    if not isinstance(valor, str):
        raise TypeError("VALOR DIGITADO NÃO É UMA STRING")
    

str_invertida = inverte_string("OLAAABCD")
print(str_invertida)
