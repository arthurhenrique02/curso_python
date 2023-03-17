# criar um sistema de perguntas e respostas

import random

# criar a lista de perguntas
perguntas = [
    # criar dicionarios com as perguntas, opções e respostas
    {
        "pergunta": "Quanto é  2 + 2?",
        "opcoes": ["1", "2", "3", "4"],
        "correto": "4",
    },
    {
        "pergunta": "Qual o nome de rayssa no wpp?",
        "opcoes": ["minha princesa", "minha deusa", "minha branquinha", "minha obra de arte"],
        "correto": "minha princesa",
    },
    {
        "pergunta": "Quanto é 10 * 10?",
        "opcoes": ["10", "20", "30", "100"],
        "correto": "100", 
    },
]

while True:
    # pegar uma pergunta aleatoriamente
    pergunta_random = random.randint(0, (len(perguntas) - 1))

    # mostrar a pergunta
    print(perguntas[pergunta_random]["pergunta"])

    # mostrar opções
    print(f"Opções: {perguntas[pergunta_random]['opcoes']}")

    # solicitar opção
    opcao_usuario = ''
    while True:
        opcao_usuario = input("Digite a resposta: ")

        if opcao_usuario in perguntas[pergunta_random]["opcoes"]:
            break

    # checar se o usuario acertou
    if opcao_usuario == perguntas[pergunta_random]["correto"]:
        print(
            "Parabéns!!!\n"
            "Você acertou!!"
        )
    else:
        print(
            "Não foi dessa vez!!\n"
            "tente novamente!"
        )