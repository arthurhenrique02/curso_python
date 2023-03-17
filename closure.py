# Closure é basicamente criar uma função dentro da outra, e com a funcao principal poder criar outras funcoes
# É bastante comum fazer isso, e em códigos eficientes o closure é usado

# Por exemplo:

def principal(saudacao):
    def segundaria(nome):
        return f"{saudacao}, {nome}"
    return segundaria

# Pode-se definir uma variavel de greeting
retornar_bom_dia = principal("bom dia")
retornar_boa_noite = principal("boa noite")

# O nome sera passado ao usar a função pois a execução da função segundária foi adiada e será executada neste momento
print(retornar_boa_noite("arthur"))
print(retornar_bom_dia("arthur"))