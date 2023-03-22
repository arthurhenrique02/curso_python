# funções recursivas são funções que se chamam novamente

# isso faz com que chamadas sejam mais rápidas 

# elas são uteis para dividir problemas maiores em menores 

# os problemas devem ser uniformes e que possam ser divididos em problemas menores

# caso esqueça de colocar o código de segurança (caso base), o Python retornará um erro (RecursionError) e o código irá parar
    # isso acontece por segurança do python, para evitar danos à maquina

# definindo uma função recursiva
def recursive_func(num):
    # a função precisa ter um item de segurança para que não gere erros(stack overflow). Nesse caso, deve parar quando o numero for menor que 1
    if num <= 1:
        return 1
    
    #retornar funcao com o novo valor
    return num * recursive_func(num - 1)


total = recursive_func(5)
print(total)


# Pode-se alterar o limite de recursoes no programa, por padrão o Python colocou 1000

# para alterar basta importar do modulo sys a função "setrecursionlimit"
import sys

sys.setrecursionlimit(1004) # agora o limite de recursoes vao ate 1000

# total = recursive_func(1050)
# print(total)