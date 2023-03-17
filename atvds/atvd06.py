# Fazer um programa que solicite um nome e de acordo com o cumprimento falar se é curto, normal ou longo

# solicitar nome
nome = input("Digite um nome: ").strip().replace(' ', '') # tirar os espaços desnecessarios para contar as letras, caso o usuario digite

# pegar o len
length = len(nome)

if length <= 4:
    print("Seu nome é curto")
elif 5 <= length <= 6:
    print("Seu nome é normal")
else:
    print("Seu nome é muito grande")
