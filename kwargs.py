# No dict pode-se extrair outro dicts utilizando **, quando isso é feito, o dict extrairá os dados de outro e guardará nele

# Por exemplo:

pessoa = {
    "nome": "arthur",
    "sobrenome": "henrique",
}

dados_pessoa = {
    "idade": 20,
    "altura": 1.70,
}

# pode-se extrair quantos dicts quiser
dados_completos_pessoa = {
    **pessoa,
}

# Em funções, quando vamos usar dicts, utilizamos os kwargs para seus argumentosexecutar

def mostro_kwargs(**kwargs):
    print(kwargs)

mostro_kwargs(nome="arthur", idade=20)

# pode-se desempacotar dicts para mostrar na função
mostro_kwargs(**pessoa)