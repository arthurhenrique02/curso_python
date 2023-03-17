# importar algumas coisas para o main pode ser  confuso as vezes

# Caso tente importar um módulo de um pacote main, as vezes pode dar erro, pois não se está olhando de dentro do main

# Então, caso eu tenha um módulo (modulo_teste) dentro de um pacote com a seguinte linha de código

# from teste2 import fala_oi

# essa linha de código pode gerar erro quando o módulo (modulo_teste) for importado para esse modulo aqui

# para evitar esse erro, devemos importar o módulo teste2 com o ponto de vista deste, ou seja, importar desta forma:

# from teste.teste2 import fala_oi

# dessa maneira o codigo irá funcionar sem erros

from teste.modulo_teste import soma


