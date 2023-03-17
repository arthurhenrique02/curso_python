# Modularização é basicamente dividir os programas em módulos (arquivos)

# O comum é dividir em módulos proximos ao arquivo main, ou seja, não é comum sair caçando os modulos em diferentes pastas
# geralmente tudo é feito em uma mesma pasta, mesmo que existam outras pastas dentro dela

# Para pegar um módulo de uma pasta totalmente diferente, pode-se dar um .append no path

# Por exemplo:
try:
    import sys
    sys.path.append("C:/Users/FLY-PC/Documents/projetos/python/fabrica/aula01")
except ModuleNotFoundError:
    print("module error")

# o mais comum é fazer da seguinte forma: import (nome do modulo que deseja e que está na mesma pasta deste)
import import_modules

# modulo importado do path que foi inserido (append) ao path
import modulos_calc

# o modulo iniciado primeiro sempre será o main
print(f"Modulo {__name__}")

# pode-se olhar o path para este modulo e os paths incluidos atraves do append
print(*sys.path, sep="\n")
