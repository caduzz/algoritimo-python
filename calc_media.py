import json

#input area, toda entrada de dados
nome_aluno = input('Digite o nome do aluno: ')

nota_1 = int(input('Digite o primeira nota: '))
nota_2 = int(input('Digite o segunda nota: '))
nota_3 = int(input('Digite o terceira nota: '))
nota_4 = int(input('Digite o quarta nota: '))

#calcular a media
soma = nota_1 + nota_2 + nota_3 + nota_4
divisao = soma / 4

#escreve na tela a media
print(divisao)

#verifica se o aluno foi aprovado ou não
if divisao >= 7 :
    print('Passou com nota: ' + str(divisao))
    aprovado = True
else:
    print('Passou com nota: ' + str(divisao))
    aprovado = False

#define o nome do arquivo que quero abrir
nome_arquivo = "alunos.json"

with open(nome_arquivo, "r") as file:
    alunos = json.load(file)['alunos']

#salva as informações em uma variavel
informacoes = {
    "nome": nome_aluno,
    "notas": {
        "nota_1": nota_1,
        "nota_2": nota_2,
        "nota_3": nota_3,
        "nota_4": nota_4
    },
    "soma": soma,
    "media": divisao,
    "aprovado": aprovado
}


alunos.append(informacoes)
print(alunos)

dados = {
    "alunos": alunos
}

objeto_json = json.dumps(dados, indent = 4)

with open(nome_arquivo, "w") as outfile: 
    outfile.write(objeto_json)