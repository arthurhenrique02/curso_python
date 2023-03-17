# dir mostra todos os métodos disponiveis para aquele tipo de variável

# Por exemplo:
nome = "arthur"
print(dir(nome)) # mostra todos os metodos disponiveis em uma string
# print(dir(21)) # todos os metodos disponiveis em um int

print("========================================")

# hasattr checa dinamicamente se o objeto possui um atributo

# Por exemplo:

# o nome do atributo tem que ser inserido como uma string ("nome do metodo que deseja")
print(hasattr(nome, "strip")) # retornar True ou False caso o objeto tenha ou nao determinado atributo

# dinamicamente pois o atributo pode ser pego de alguma variavel, por exemplo
metodo = "lower"
print(hasattr(nome, metodo))

print("========================================")

# getattr executa o atributo dinamicamente
print(getattr(nome, "strip")) # retorna o end de memoria que o metodo esta alocado

# Para executar esse metodo, é necessário utilizar um () após o getattr
    # Pode ser atribuido à uma variável também (método não indicado para valores imutaveis)
print(getattr(nome, "upper")())
