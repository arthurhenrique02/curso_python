# Caso tente importar um módulo mais de uma vez, isso não será possivel, pois módulos são Singleton

# Singleton quer dizer que eles só serão executados uma vez, ou seja, 1 vez importado o módulo isso não ocorrerá de novo
    # independenmente de quantas vezes o import seja chamado para aquele módulo
    # isso ocorre por questão de eficiência

# Por exemplo:

# importar o modulo "import_modules" uma vez
import import_modules

# tentar importar outras vezes para ver se vai mostrar algo na tela
for i in range(5):
    # pode-se verificar que o loop ta funcionando através do print dos numeros contido em i
    print(i)

    # essa linha de código será "ignorada", e o Python não irá salvar o módulo novamente na memória
    import import_modules


# Não é tão comum, mas pode-se recarregar a importação utilizando um módulo chamado importlib

import importlib
for i in range(5):
    importlib.reload(import_modules)
    print("RECARREGADA")

