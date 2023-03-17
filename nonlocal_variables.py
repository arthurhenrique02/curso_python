# variaveis não locais são utilizadas quando fazemos closure, por exemplo, e você pega a variável do escopo mais externo para o mais interno

# dentro de funções mais internas, pode-se pegar o valor da variável, mas apenas para visualização, ou seja, não podem ser modificadas

# Para que possam ser modificadas, utilizamos o método nonlocal

# Por exemplo:

# vamos criar uma função para concatenar strings, inicalmente so receberá um valor e depois outro
def externa(string_inicial):

    # caso queira passar o valor dessa string e poder editar ela para a função interna, é necessário utilizar o nonlocal
    valor_final = string_inicial

    def interna(valor_concat):
        # pode-se retornar o valor final da função com escopo mas externo, mas não se pode modificá-la
        # por exemplo:
        # valor_final += valor_concat # essa linha de código não irá funcionar, pois valor_final não está definida no escopo local
        # return valor_final
    
        # para que se possa modificar, é necessário:
        nonlocal valor_final # agora o python irá reconhecer que não é uma variável local e irá buscar no escopo mais acima
        valor_final += valor_concat
        return valor_final 
    
    # retornar função interna
    return interna


concat_str = externa("bom dia, ")

print(concat_str("arthur"))