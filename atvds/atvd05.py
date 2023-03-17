# Perguntar a hora ao usuario e mostrar uma saudação de acordo com ela

# solicitar hora
hora = input("Digite a hora: ").strip().replace(':', '') # tirar os dois pontos e os espaços desnecessarios, caso o usuario digite

# checar se digitou um numero inteiro
try:
    int(hora)
except:
    print("O valor digitado é inválido.\nDigite um número inteiro")
    exit(1)


# pegar apenas as horas e desconsiderar os minutos
apenas_hora = int(hora[0:2])

# checar hora para a saudação
if 0 <= apenas_hora <= 11:
    print("Bom dia")
elif 12 <= apenas_hora <= 17:
    print("boa tarde")
elif 18 <= apenas_hora <= 23:
    print("Boa noite")
else:
    print("Digite uma hora válida (de 0 à 23)")