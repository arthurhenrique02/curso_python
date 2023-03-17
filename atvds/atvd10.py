# Fazer uma lista de compras

# O usuário poderá inserir, apagar e ver a lista

import os

# declarar carrinho
carrinho = []

while True:
    # solicitar opção
    opcao = input("Selecione uma opção\n"
                  "[i]nserir [a]pagar [l]istar: ")
    
    # checar se foi digitado uma opção válida
    if not opcao.lower().startswith("i") and not opcao.lower().startswith("a") and not opcao.lower().startswith("l"):
        os.system("cls")
        print("digite uma opção válida!!")
        continue

    # condições para mostrar cada opção
    # inserir item
    if opcao.lower().startswith("i"):
        os.system("cls") # limpar terminal
        print(f"{'INSERIR ITEM':=^30}") # detalhe visual
        # solicitar item
        item = input("Digite o item que deseja: ").lower()

        # inserir item na lista
        carrinho.append(item) 

    # apagar item
    elif opcao.lower().startswith("a"):
        os.system("cls") # limpar terminal
        print(f"{'APAGAR ITEM':=^30}") # detalhe visual

        # mostrar itens e ID
        print("ID      Item")
        for indice, item in enumerate(carrinho):
            print(indice, "    ",item)
        
        # solicitaro iD do item que o usuario deseja apagar
        del_item = input("Digite o ID do item que deseja excluir: ")

        # tentar apagar o item correspondente ao ID
        try:
            del carrinho[int(del_item)]
        except:
            # Mostrar algo na tela caso não consiga
            print("Digite um ID de item válido")

    # listar itens
    else:
        os.system("cls") # limpar terminal
        print(f"{'LISTAR ITENS':=^30}") # detalhe visual

        # checar se ha algum item
        if len(carrinho) < 1:
            print("O carrinho está vazio!")
            continue

        # listar os itens da lista
        print("ID      Item")
        for indice, item in enumerate(carrinho):
            print(indice, "    ",item)