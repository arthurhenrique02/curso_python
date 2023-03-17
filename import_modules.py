# import (nome do modulo) irá fazer com que o programa importe aquele modulo inteiro
import sys

# sendo necessario utilizar (nome do modulo).(variavel do modulo)
print(sys.platform)

# from (nome do modulo) import (parte do modulo) impotará somente aquela parde do modulo digitada
from sys import platform

# nao será necessário usar o name space, por exemplo:
print(platform)

# as será o apelido que voce dará para aquele módulo ou aquela parte dele. Por exemplo:
import sys as sistema # agora sys será chamado de 'sistema'
from sys import platform as plataforma # agora platform será chamado de 'plataforma'

print(sistema.platform)
print(plataforma)

# * importa tudo do módulo, o que é uma má pratica pois o código não fica nada legível e nada obvio
from sys import *

print(platform) # não é necessário utilizar o namespace, mas também não é bom para o código
#exit()