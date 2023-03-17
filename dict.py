# Dicinarios são objetos mutáveis dentro do python, assim como listas. Eles podem receber indices imutaveis, como str, integers, floats, etc.
# No dicinario os indices sao chamados de chave

my_dict = {
    "nome": "arthur",
    "sobrenome": "henrique",
    "idade": 20,
}
# pode-se criar um dicionario da seguinte forma:
# my_dict = dict(nome="arthur", sobrenome="henrique", idade=18)

# Para tentar pegar uma chave no dicinario, que possa existir ou não, é utilizado o metodo get
my_dict.get("endereco", None) # por padrao o get retorna None caso nao seja encontrado a chave, nao é necessario escreve-lo dessa forma

# len ve quantas chaves o dicinario possui
# print(my_dict.__len__()) # __len__ não é exclusivamente do dict
# Len é escrito mais comumente da seguinte forma:
print(len(my_dict))

# keys retorna as chaves que o dict possui:
print(my_dict.keys())

# values retorna os valores que o dict possui:
print(my_dict.values())

# items retorna as chaves e valores do dict:
print(my_dict.items())

# setdefault seta um valor padrao caso uma variavel nao exista
my_dict.setdefault("endereco", "abc") # caso o valor exista no dict, esse trecho não é executado
print(my_dict["endereco"])

# copy copia o dict
my_dict2 = my_dict.copy() # é necessario usar o copy pois o = apenas vai direcionar para o mesmo end de memoria no caso de valores mutaveis

    # mas o .copy faz uma copia rasa (shallow copy) dos dados
    # isso quer dizer que se houver um outro item mutavel dentro do dict, ele não vai copiar, apenas apontar pro mesmo end de memoria

# para poder copiar todos os dados do dict ou de outro objeto mutavel, é necessario importar um modulo chamado copy

import copy
my_dict2 = copy.deepcopy(my_dict) # ha tambem o copy.copy que é uma copia rasa também

# pop apaga um item a partir da chave digitada
pop_item = my_dict.pop("nome")
print(my_dict) # caso a chave não exista, retorna um KeyError


# popitem apaga o ultimo item do dict
popped = my_dict.popitem()
print(my_dict)

# pop e popitem apagam os valores mas retornam ele, caso deseje guardar em uma variavel por exemplo, é possivel
print(pop_item)
print(popped)

# update atualiza o dict, podendo agregar outros dicts
my_dict2 = {
    "endereco": "abcd",
    "rayssa": "amor da minha vida",
}

# Atualizando dados do dict e adcionando alguns outros
my_dict.update({
    "nome": "arthur henrique",
    "sobrenome": "lima nascimento de oliveira",
})

print(my_dict)

# incrementando outros dicts
my_dict.update(my_dict2)

print(my_dict)

# da para passar tuplas ou de outras formas tambem
tupla = ("endereco", "aaaaaaaaaaaaaaaaaa"), # caso passe apenas um valor, deverá colocar uma "," sobrando
lista = ["rayssa", "mulher da minha vida"],
my_dict.update(tupla)
print(my_dict)
my_dict.update(lista)
print(my_dict)
