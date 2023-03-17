# Criar uma calculadora

# Entrar no while loop infinito
while True:
    # solicitar o primeiro valor
    valor_1 = input("Digite o primeiro número: ")
    # solicitar o tipo de operação que o usuário deseja
    operacao = input("Digite a operação que deseja: \n"
                     "(soma: +, subtração: -, multiplicação: *, "
                     "divisão: /, potência: **)\n")
    # solicitar segundo valor
    valor_2 = input("Digite o segundo número: ")

    # testar os valores digitados
    try:
        float(valor_1)
        float(valor_2)
    except:
        print("\nDigite um valor válido\n")
        continue

    # Ver se a operação escolhida está entre as possíveis no programa
    if operacao not in ["+", "-", "*", "/", "**"]:
        print("\nDigite uma operação válida\n") # \n apenas para pular uma linha a mais
        continue

    # checar a operação e usar o case de acordo
    match operacao:
        # soma
        case '+':
            print(f"A soma de {valor_1} e {valor_2} é: {float(valor_1) + float(valor_2):.2f}")
        # subtração
        case '-':
            print(f"A subtração de {valor_1} por {valor_2} é: {float(valor_1) - float(valor_2):.2f}")
        # multiplicação
        case '*':
            print(f"A multiplicação de {valor_1} por {valor_2} é: {float(valor_1) * float(valor_2):.2f}")
        # divisão
        case '/':
            print(f"A divisão de {valor_1} por {valor_2} é: {float(valor_1) / float(valor_2):.2f}")
        # potênciação
        case '**':
            print(f"A potenciação de {valor_1} por {valor_2} é: {float(valor_1) ** float(valor_2):.2f}")


    # ver se o usuario deseja sair do programa
    sair = input("Deseja sair? [s]im ou [n]ão: ")
    if sair.lower().startswith("s"):
        print("Saindo da calculadora.")
        exit(0)