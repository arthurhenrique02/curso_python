# guard clause é 'fazer o refinamento dos ifs', retirando IFs desnecessarios e deixando um de segurança, por exemplo
# deixando o codigo mais limpo e facil de ler

# Mas o que seria fazer o refinamento?

# Segue exemplo:

# Codigo sem guard clause
def printa_oi(string):
    if string == "oi":
        # codigo
        # codigo
        # codigo

        # fazer o print
        print("oi")
    else:
        # apenas retornar algo
        return "oi"
    
# suponha que o codigo acima seja mais complexo e nos comentarios que tenham 'codigo' haja algumas linhas de codigo, e que so seja executado caso a variavel string seja igual a 'oi'
# como apenas uma condição é necessária, podemos fazer o guard clause e evitar o uso do else

# Desta forma
def printa_ola(string):
    # ver se a condição é satisfeita, caso não, retornar logo de cara
    if not string == "ola":
        return
    
    # colocar o codigo sem o uso do else
    # codigo
    # codigo
    # codigo

    print("ola")
    