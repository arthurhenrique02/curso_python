import os
import json

# func para listar tarefas
def listar(tarefas):
    # pular linha
    print()
    # condicao de seguranca
    if not tarefas:
        print('Nenhuma tarefa para listar')
        return

    # mostrar tarefas, caso existam
    print('Tarefas:')
    for tarefa in tarefas:
        print(f'\t{tarefa}')
    print()

# desfaz a ultima atividade
def desfazer(tarefas, tarefas_refazer):
    # pular linha
    print()
    # if de seguranca
    if not tarefas:
        print('Nenhuma tarefa para desfazer')
        return

    # fazer o pop (retirar a ultima atvd)
    tarefa = tarefas.pop()
    # mostrar
    print(f'{tarefa=} removida da lista de tarefas.')
    # adicionar a lista para refazer
    tarefas_refazer.append(tarefa)
    print()


# refaz a ultima atvd desfeita
def refazer(tarefas, tarefas_refazer):
    print()
    # if de seguranca
    if not tarefas_refazer:
        print('Nenhuma tarefa para refazer')
        return

    # pegar a ultia atvd da lista de refazer
    tarefa = tarefas_refazer.pop()
    print(f'{tarefa=} adicionada na lista de tarefas.')
    # adicionar a lista de tarefas
    tarefas.append(tarefa)
    print()


# adicionar caso nenhuma das outras funcs (listar, desfazer ou refazer) seja chamada
def adicionar(tarefa, tarefas):
    print()
    # tirar espacos desnecessarios no comeco e fim da string
    tarefa = tarefa.strip()
    # if de seguranca
    if not tarefa:
        print('Você não digitou uma tarefa.')
        return
    # mostrar a atvd inserida
    print(f'{tarefa=} adicionada na lista de tarefas.')
    # inserir na lista
    tarefas.append(tarefa)
    print()

# funcs para salvar em um json
def ler(tarefas, caminho_arq):
    # lista para dados
    dados = []

    # tentar abrir arquivo
    try:
        with open(caminho_arq, "r", encoding="utf8") as file:
            # pegar os dados do arquivo
            dados = json.load(file)
    
    # caso o arquivo nao exista, cria-lo e salvar com a func de salvar
    except FileNotFoundError:
        salvar(tarefas, caminho_arq)

    return dados
def salvar(tarefas, caminho_arq):
    dados = None

    with open(caminho_arq, "w", encoding="utf8") as file:
        # fazer dump no json
        dados = json.dump(tarefas, file, indent=2, ensure_ascii=False)

    return dados

# listas utilizadas
ARQUIVO = "atvd20.json"
tarefas = ler([], ARQUIVO)
tarefas_refazer = []


# loop para parar quando o user quiser
while True:
    print('Comandos: listar, desfazer, refazer, digite o que deseja caso queira adicionar')
    tarefa = input('Digite uma tarefa ou comando: ')

    # guard clause com dicts
    comandos = {
        # necessario criar uma lambda para que a func nao seja executada assim que seja chamada
        'listar': lambda: listar(tarefas),
        'desfazer': lambda: desfazer(tarefas, tarefas_refazer),
        'refazer': lambda: refazer(tarefas, tarefas_refazer),
        'clear': lambda: os.system('cls'),
        'adicionar': lambda: adicionar(tarefa, tarefas),
    }

    # pegar a funcao que foi digitada pelo usuario, caso nao tenha sido uma func valida, acionar a func de adicionar valor na lista
    comando = comandos.get(tarefa) if comandos.get(tarefa) is not None else \
        comandos['adicionar']
    
    # executar a funcao
    comando()

    # salvar no json
    salvar(tarefas, ARQUIVO)