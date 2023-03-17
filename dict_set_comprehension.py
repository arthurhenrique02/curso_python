# Dict comprehension

my_dict = {
    "nome": "arthur",
    "sobrenome": "henrique",
    "idade": 20,
}

# chave:valor é para mapear o que sera salvo
# o if apos o for permite pegar apenas a chave "nome", ou qualquer outra condição que deseje
my_dict2 = {
    chave: valor.upper() 
    # checar se o valor é string e mudar para upper case
    if isinstance(valor, str) else valor
    for chave, valor in my_dict.items()
    # checar se há alguma chave "nome" e add apenas ela
    if chave == "nome"
}
print(my_dict2)