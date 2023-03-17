# criar um programa que valide cpf

import re
import sys

# solicitar o cpf
cpf = input("cpf: ")

cpf = re.sub(r"[^0-9]", "", cpf) # utiliza-se r de regulares para ver as expressoes, ^ é para procurar tudo que não esteja entre 0 e 9, "" vai substituir por nada, e cpf é o argumento a ser substituido

# pegar os nove digitos do cpf
nove_digits_cpf = cpf[:9]

# dois ultimos digitos
ultimos_digits_cpf = cpf[9:11]

# checar se foi digitado apenas numeros
try:
    int(cpf)
except:
    print("Digite um cpf válido")
    sys.exit(1)

# checar se o cpf possui 11 digitos
if len(cpf) != 11:
    print("O CPF deve conter 11 digitos")
    sys.exit(2)

# checar input repetido
repetido = cpf == cpf[0] * len(cpf)
if repetido:
    print("Digitado uma sequencia repetida")
    sys.exit(3)

# criar variaveis para o cpf multiplicado e o multiplicador
cpf_mult = 0
multiplicador = 10

# multiplicar os digitos
for digito in nove_digits_cpf:
    # adicionar o valor multipliado
    cpf_mult += (int(digito) * multiplicador)

    # diminuir o multiplicador
    multiplicador -= 1

# multiplicar o resultado final por 10
result_mult10_cpf = cpf_mult * 10

# calcular resto da conta para o primeiro digito
primeiro_digit = result_mult10_cpf % 11

# checar primeiro digito
primeiro_digit = primeiro_digit if 0 <= primeiro_digit <= 9 else 0

# pegar os digitos contando com o primeiro digito calculado
dez_digits_cpf = nove_digits_cpf + str(primeiro_digit)

# calcular o segundo digito

# reutilizar variaveis do primeiro digito
multiplicador = 11
cpf_mult = 0

# calcular a multiplicação de cada digito
for digito in dez_digits_cpf:
    # adicionar o valor multipliado
    cpf_mult += (int(digito) * multiplicador)

    # diminuir o multiplicador
    multiplicador -= 1

# multiplicar resultado por 10
result_mult10_cpf = cpf_mult * 10

# definir segundo digito e verificar se ele é maior que 9
segundo_digit = result_mult10_cpf % 11
segundo_digit = segundo_digit if 0 <= segundo_digit <= 9 else 0

# checar se os digitos calculados são iguais aos digitados pelo usuário para validar o cpf
cpf_final = dez_digits_cpf + str(segundo_digit)
if cpf_final[9:11] == ultimos_digits_cpf:
    print(f"CPF {cpf} Válido")
else:
    print(f"CPF {cpf} Inválido\n"
          f"Um CPF válido: {cpf_final}")
