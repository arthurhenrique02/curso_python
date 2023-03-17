# criar um função que encontre o primeiro duplicado a partir da segunda ocorrencia
# caso não tenha nenhum repetido, retornar -1
# exemplo:
# 1, 2, 3, 3, 2, 1 a função deve retornar 3


# criar um lista
nums = [1, 2, 3, 3, 2, 1]
nums2 = [1, 2, 3, 4, 5, 6, 7, 8]

# criar a função
def encontrar_duplicado(lista_itens):
    # criar variavel de repetido
    duplicado = -1
    # criar um set para checar
    nums_checados = set()

    # checar os numeros da lista
    for numero in lista_itens:
        # caso ja tenha jo set, mudar o duplicado e encerrar o loop
        if numero in nums_checados:
            duplicado = numero
            break
        
        # adcionar o duplicado ao set
        nums_checados.add(numero)
    # retornar o duplicado
    return duplicado

# executar a função e mostrar na tela
print(f"O primeiro duplicado foi: {encontrar_duplicado(nums)}")
print(f"O primeiro duplicado foi: {encontrar_duplicado(nums2)}")