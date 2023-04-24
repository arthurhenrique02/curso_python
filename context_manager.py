import os

# Context manager (with) é um método que pode ser utilizado para manipulação de arquivo, ele abre o mesmo e fecha-o automaticamente

# O context manager é muito utilizado para isto.

# r = read (apenas ler)
# w = write (apenas escrever)
# a = append (inserir no fim do arquivo)
# r+ = read and write (pode-se ler e escrever no arquivo)
# w+ = read and write (pode-se ler e escrever no arquivo)

# metodos uteis
# write (escrever e ler)
# writelines (escrever varias linhas) (o write pode escrever varias linhas, mas, as vezes, o writelines é util)
# seek (mover o cursor) (nao muito utilizado)
# readline (ler uma linha por vez)
# realines (ler varias linhas)


# Abrindo um arquivo:
# caso nao exista o arquivo no diretorio, ele sera criado
# o nome do arquivo será "file"
# necessario adicionar o enconding pois o Windows utiliza outro, e para nao gerar erros isso é necessário
with open("exemplo_arquivo.txt", "w+", encoding="utf-8") as file:
    # necessario quebrar linha (se quiser mudar a linha no arquivo)
    file.write("atenção\n")
    file.write("linha 2\n")
    file.writelines(("linha 3\n", "linha 4\n"))

    # mover o cursor para mostrar linhas com readline
    file.seek(0, 0)

    # mostrar linha
    print("LENDO")
    print(file.readline(), end="")  # utilizado end para o print nao pular linha

    # com readlines
    print("LENDO COM READLINES")
    file.seek(0, 0)
    for linha in file.readlines():
        # tirar quebra de linha com strip
        print(linha.strip())


# os.remove ou os.unlink fazem a mesma coisa, os dois metodos servem para apagar um arquivo
# os.remove("exemplo_arquivo.txt")
# os.unlink("exemplo_arquivo.txt")
