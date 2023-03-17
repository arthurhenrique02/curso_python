# solicitar os valores
valor_1 = input('digite um valor: ')
valor_2 = input('digite outro valor: ')

# testar se são números inteiros
try:
    int_valor_1 = int(valor_1)
    int_valor_2 = int(valor_2)
except:
    # printar na tela caso não seja número inteiro
    print("Algum valor digitado é inválido.\nDigite um número inteiro.")

# checar as condições
if int_valor_1 > int_valor_2:
    # mostrar na tela caso valor 1 seja maior que valor 2
    print(f"{valor_1} é maior que {valor_2}")
elif int_valor_1 < int_valor_2:
    # mostrar na tela caso valor 1 seja menor que valor 2
    print(f"{valor_1} é menor que {valor_2}")
else:
    # mostrar na tela caso sejam iguais
    print(f"{valor_1} é igual a {valor_2}")