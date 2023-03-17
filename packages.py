# Um package nada mais é que uma pasta com arquivos python

# pode-se ser importado das seguintes formas:


import teste # não reconhecerá os modulos dentro, não serve pra muita coisa esse tipo de importação

import teste.modulo_teste # importar o modulo inteiro, sendo necessario utilizar esse nome todo como namespace

from teste.modulo_teste import soma # importa sem os namespaces, sendo necessario utilizar apenas o nome da função

from teste import modulo_teste # importa o modulo inteiro, utilizando-o como name space

print(teste) # em relacão ao primeiro import, a função soma não será reconhecida e nem o módulo

print(teste.modulo_teste.soma(1, 2)) # em relação a segunda, a função será reconhecida, mas será necessario utilizar o namespace teste.modulo_teste (ficando muito grande)

print(soma(3, 4)) # para a terceira, so será necessário utilizar o nome da função, pois apenas ela foi importada

print(modulo_teste.soma(5, 6)) # para a quarta, será necessário utilizar o nome do módulo como namespace(modulo_teste.), pois ele foi importado inteiramente