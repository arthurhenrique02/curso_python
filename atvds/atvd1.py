# criar variáveis nome, sobrenome, idade, ano de nascimento, maior idade, altura

nome = "Arthur"
sobrenome = "Henrique"
idade = 20
ano_nascimento = 2002
if idade >= 18:
    maior_idade = True
else:
    maior_idade = False
altura = 1.70

print(f"Nome: {nome}")
print(f"Sobrenome: {sobrenome}")
print(f"Idade: {idade}")
print(f"Maior de idade?: {maior_idade}")
print(f"Altura: {altura:.2f}")