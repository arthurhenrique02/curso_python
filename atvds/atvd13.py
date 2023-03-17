# criar funções que duplicam, triplicam e quadriplicam

# utilizar closure

import sys
# criar a função de multiplicadores
def multiplicador(multiplicador):
    # criar a função para pegar o valor a ser multiplicado
    def multiplicar_valor(valor):
        # retornar o valor multiplicado
        return valor * multiplicador
    # retornar a função
    return multiplicar_valor

# criar função de duplicar
duplicar = multiplicador(2)
# criar função de triplicar
triplicar = multiplicador(3)
# criar função de quadriplicar
quadriplicar = multiplicador(4)

# solicitar valor
valor = input("Digite um valor: ")

# checar se é um valor válido
try:
    float(valor)
except:
    print("Digite um valor valido")
    sys.exit(1)

# mostrar na tela
print(f"valor duplicado: {duplicar(float(valor))}")
print(f"valor triplicado: {triplicar(float(valor))}")
print(f"valor quadriplicado: {quadriplicar(float(valor))}")