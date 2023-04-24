import re


# procurar uma determinada palavra utilizando expressões regulares

texto = "Este é uma texto de exemplo de utilização de expressões regulares. texto texto texto"

# utilizar o search:
# retorna um objeto com um span da localizacao e a palavra
# o search verificar apenas a primeira ocorrencia da esquerda para a direita
# o search pode-se ser utilizado com o if, por exemplo, caso queira fazer algo com essa ocorrencia
# caso nao encontre nenhuma expressao, retorna None

print(re.search(r"texto", texto))
print(re.search(r"texto2", texto))

# findall:
# retorna uma lista com todas as ocorrencias da expressao
# caso nao encontre, retorna uma lista vazia
print(re.findall(r"texto", texto))

# sub:
# substitue uma palavra que deseja
# necessario passar a palavra que deseja substituir como primeiro parametro
# a palavra de substituicao de segundo parametro
# e o texto em que deseja fazer essa substituicao
# pode-se passar um quarto parametro (nao obrigatorio) com a quantidade de palavras que deseja substituir
# retorna o texto modificado
modifica_uma_palavra_texto = re.sub(r"texto", "AAAAAA", texto, count=1)
print(modifica_uma_palavra_texto)

modifica_duas_palavras_texto = re.sub(r"texto", "BBBBBB", texto, count=2)
print(modifica_duas_palavras_texto)

modifica_todas_palavras_texto = re.sub(r"texto", "CCCCCCC", texto)
print(modifica_todas_palavras_texto)


# compile:
# compile é utilizado quando voce quer reutilizar uma mesma expressao regular
# DEVE ser utilizado sempre neste caso, pois é uma questão de desempenho, já que o Python não terá que compilar novamente a mesma expressao
palavra_texto_compilada = re.compile(r"texto")

# para utilizar a palavra compilada basta fazer:
print("UTILIZANDO O COMPILE")
# procurar a palavra texto na variavel texto
print(palavra_texto_compilada.search(texto))
# procurar todas as palavra texto na variavel texto
print(palavra_texto_compilada.findall(texto))
# substituir
print(palavra_texto_compilada.sub("AAAA", texto))


# metacaracteres

# . ^ $ * + ? { } [ ] \ | ( )
# | (significa ou)
# . (qualquer caractere, menos quebra de linha)

# [] utilizado para especificar classes de caracteres (sequencias de caracteres)

# pode ser utilizado como range [a-c], ou digitando todos [abc]

# [a-c] ira dar matchem todos os caracteres de a ate c, a mesma coisa para [abc]

# Adicionar caracteres especiais, nao os torna especiais, pois eles estao dentro da classe

# por exemplo: [abc!$]

# $ é um metacaracter, mas nesse caso, ele será lido em sua forma normal

# pode-se utilizar ^ para limitar os caracteres

# deve-se colocar no inicio da expressao

# [^5] ira dar match em qualquer caracter, menos o 5

# [5^] nao significa nada, ira dar match em qualquer caracter igual 5 ou igual a ^


# Exemplo utilizando ou . e []
print(re.findall(r"texto|Texto|Este", texto))
print(re.findall(r"texto|Texto", texto))
print(re.findall(r"[Tt]exto", texto))
print(re.findall(r"[a-z]exto", texto))
print(re.findall(r"[a-zA-Z]exto", texto))
# utilizando flag para case insensitive
print(re.findall(r"TeXTo", texto, flags=re.I))
