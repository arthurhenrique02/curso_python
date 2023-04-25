import json

pessoa = {
    "nome": "Rayssa Aguiar",
    "sobrenome": "Leal",
    "enderecos": [
        {"rua": "R1", "numero": 32},
        {"rua": "R2", "numero": 55},
    ],
    "altura": 1.6,
    "numeros_preferidos": (2, 4, 6, 8, 10),
    "dev": True,
    "nada": None,
}


# criar arquivo e acessar
with open("exemplo_salvar_json.json", "w", encoding="utf-8") as file:
    # fazer dump no arquivo (json possue dump e dumps, dumps é para strings e dump para arquivos)
    json.dump(pessoa, file)  # indent para deixar identado


with open("exemplo_salvar_json.json", "r", encoding="utf-8") as file:
    # pegar a pessoa no arquivo json
    pessoas = json.load(file)
    print(pessoas)
