import pandas as pd

with open("./problema_lp/problema1.txt", "r") as arq:
    content = arq.read()
lines = content.split("\n")

# lidando com a maximização
listaSinalTrocado = []
if lines[0].split(" ")[2] == "1":
    for i in range(len(lines[1].split(" "))):
        listaSinalTrocado = lines[1].split(" ")
        for i in range(len(listaSinalTrocado)):
            listaSinalTrocado[i] = str(float(listaSinalTrocado[i]) * -1)
    lines[1] = " ".join(listaSinalTrocado)

#montando o tableau inicial
listona = []
lista = []
for i in range(1, int(content[0]) + 2):
    j = 0
    for j in range(int(content[2])):
        lista.append(float(lines[i].split(" ")[j]))
    if i > 1:
            lista.append(lines[i].split(" ")[j + 2])
    listona.append(lista)
    lista = []

df = pd.DataFrame(listona)
listona = []
df = df.fillna(0)
df[int(content[2])] = df[int(content[2])].astype(int)
print(df)
