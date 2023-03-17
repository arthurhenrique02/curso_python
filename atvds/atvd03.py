# Solicitar o nome e idade
# mostrar o nome, o nome invertido
# ver se o nome possui espaços
# ver quantas letras possui
# primeira letra, ultima letra
# se nada for digitado, mostre "desculpe, existem campos vazios"

# solicitar dados
nome = input("Digite seu nome: ").strip() # strip para tirar os espaços desnecessarios
idade = input("Digite sua idade: ")

nome_sem_espaco = nome.replace(' ', '') # tirar os espaços do nome para contar as letras, apenas

# se não foi digitado nada
if not nome or not idade:
    print("Desculpe, foi deixado algum campo vazio")
    exit(1) # fechar o programa

# verificar se foi digitado um número inteiro
try:
    int(idade)
except:
    print("No campo idade, digite um número inteiro válido")
    exit(2) # fechar o programa

# verificar se a idade digitada é maior que 0
if int(idade) < 0:
    print("No campo idade, digite um número inteiro válido e maior que 0")
    exit(3) # fechar o programa


# mostrar na tela
print(f"Seu nome é: {nome}\n"
      f"Seu nome invertido é: {nome[::-1]}\n"
      f"Seu nome possui {len(nome_sem_espaco)} letras\n"
      f"A primeira letra é: {nome[0]}\n"
      f"A última letra é: {nome[len(nome) - 1]}\n")
