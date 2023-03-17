# raise é um modulo do python criado para lançar erros dentro do programa

# Pode-se criar novos erros, mas é necessário saber sobre classe

# Exemplo de como utilizar raise:

print(123)
# o raise irá ativar o erro, necessário colocar os parenteses, e mostrar a mensagem digitada entre os parentes
raise ZeroDivisionError("tentou dividir por 0") 
print(456)

# Um exemplo utilizando try except:

def divide(x, y):
    # essas linhas de códigos estão redundantes (try, except), pois o except tenta tratar o erro e o raise relança o mesmo erro
    try:
        return x / y
    except ZeroDivisionError:
        # o raise irá relançar a exceção, nesse caso, ZeroDivisionError
        raise

print(divide(8, 0))