# Pode-se definir funções dentro de funções, mas a função dentro da outro so poderá ser acessada quando a principal for

# Pode-se usar variaveis globais dentro da função, mas ela deve ser definida antes da chamada da função

# Caso haja uma variável global e uma variável local (dentro da função) com o mesmo nome, elas não serão afetadas uma pela outra
# Pois há a proteção do escopo local

# Exemplos

x = 1

def funcao():
    # Caso deseje que a variável x que está no escopo global seja modificada dentro da função, o que não é uma boa prática, deve-se colocar o nome "global" antes de definí-la
    # Exemplo:
    global x # agora a variavel x acima será utilizada dentro da função

    x = 10
    print(x) # ira mostrar o valor 10, caso o print seja definido antes do x, retorna um erro pois x estará definido após o print

    def outra_funcao():
        y = 2
        print(x, y) # da pra acessar o valor 10 da funcao principal
    
    outra_funcao()

# outra_funcao(), caso tente iniciar a função que está dentro da outra fora do escopo, será retornado um erro, pois ela não estará definida

funcao()

# Caso tente mostrar o x que está dentro da função, ele mostrará o valor 1 (pois é o x que está no escopo global, fora do escopo da função)
print(x)