# esse tipo de importação gerará erros quando o módulo "ponto_de_vista_package.py" for executado
#from teste2 import fala_oi

# o modo correto de importação é:
from teste.teste2 import fala_oi

# ou, from .teste2 import fala_oi

# caso tente executar este módulo como main, a importação não funcionará e será retornado um erro. Pois a importação muda


fala_oi()

def soma(x, y):
    return x + y