# criar um dicionario com produtos, aumentar o valor em 10%, ordenar por ordem decrescente de nome e por ordem crescente de preço.
# Salvar todos em outros dicionarios (1 para cada) por deep copy


# importar copy
import copy

# criar dicionario
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# aumentar os preços dos produtos em 10% e gerar um deep copy
novos_produtos = [
    # criar um novo dicionario para alterar a chave "preco"
    {**item, "preco": round(item["preco"] * 1.10, 2)} 
    # pegar os itens do deep copy
    for item in copy.deepcopy(produtos)

]
print(*novos_produtos, sep="\n")
print()
# Ordernar por ordem decrescente e salvar em uma outra lista de dicionarios com deep copy

# Ordenar a lista utilizando lambda como parametro para key e reverse=True para ordenar de forma decrescente
produtos.sort(key=lambda x: x["nome"], reverse=True)
produtos_ordenados_por_nome_desc = copy.deepcopy(produtos)
print(*produtos_ordenados_por_nome_desc, sep="\n")
print()

# Ordenar produtos por preço crescente e gerar deep copy
produto_ordenados_por_preco = sorted(produtos, key=lambda x: x["preco"])

print(*produto_ordenados_por_preco, sep="\n")