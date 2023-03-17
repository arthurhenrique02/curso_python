"""
Isso é uma DocString

DocStrings não são comentários. São conteúdos digitados pelo programador que serão utilizados quando alguem digitar a função help.

Por exemplo:
"""
def exemplo(x, y):
    """ Soma o valor de x e y e retorna o valor total """
    return x + y

    # Quando a função help(exemplo) for executada, ela vai retornar a DocString
    # Explicando para o usuário como funciona tal função
    # O interpretador de python lê a DocString e armazena na memória
    # Diferentemente destes comentários, o interpretador ignora-os e pula para a proxima linha