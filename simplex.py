import pandas as pd

with open("./problema_lp/problema.txt", "r") as arq:
    conteudo = arq.read()
linhas = conteudo.split("\n")

# lidando com a maximização
listaSinalTrocado = []
if linhas[0].split(" ")[2] == "1":
    for i in range(len(linhas[1].split(" "))):
        listaSinalTrocado = linhas[1].split(" ")
        for i in range(len(listaSinalTrocado)):
            listaSinalTrocado[i] = str(float(listaSinalTrocado[i]) * -1)
    linhas[1] = " ".join(listaSinalTrocado)

# lidando com termos independentes negativos
for i in range(2, int(linhas[0][0]) + 2):
    if int(linhas[i].split(" ")[int(conteudo[2]) + 1]) < 0:
        linha = [
            float(item) * -1 if index != len(linhas[i].split(" ")) - 2 else item
            for index, item in enumerate(linhas[i].split(" "))
        ]

        sinal = int(linhas[0].split(" ")[1])

        if linha[sinal] == ">=":
            linha[sinal] = "<="
        if linha[sinal] == "<=":
            linha[sinal] = ">="
        linha = [str(elemento) for elemento in linha]
        linha = " ".join(linha)
        linhas[i] = linha

# montando o tableau inicial
listona = []
lista = []
for i in range(1, int(conteudo[0]) + 2):
    j = 0
    for j in range(int(conteudo[2])):
        lista.append(float(linhas[i].split(" ")[j]))
    if i > 1:
        lista.append(linhas[i].split(" ")[j + 2])
    listona.append(lista)
    lista = []

tableauInicial = pd.DataFrame(listona)
listona = []
tableauInicial = tableauInicial.fillna(0)
tableauInicial[int(conteudo[2])] = tableauInicial[int(conteudo[2])].astype(float)

# começando a maldade
if tableauInicial[0][0] <= tableauInicial[1][0]:
    pivo = tableauInicial[0][0]
if tableauInicial[1][0] <= tableauInicial[0][0]:
    pivo = tableauInicial[1][0]
    
