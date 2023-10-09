import numpy as np
import sys

def criar_tableau(coeficientes_funcao_objetivo, coeficientes_restricoes, termos_independentes):
    num_restricoes = len(coeficientes_restricoes)
    num_variaveis = len(coeficientes_funcao_objetivo)

    tableau = np.zeros((num_restricoes + 1, num_variaveis + num_restricoes + 1))

    # Configurar a função objetivo na primeira linha do tableau
    tableau[0, :num_variaveis] = -coeficientes_funcao_objetivo

    # Configurar as restrições e os termos independentes
    for i in range(num_restricoes):
        tableau[i + 1, :num_variaveis] = coeficientes_restricoes[i]
        tableau[i + 1, num_variaveis + i] = 1  # Adicionando variáveis de folga
        tableau[i + 1, -1] = termos_independentes[i]

    return tableau

def arrayToFloat(array):
    return list( map( lambda val: float(val), array ) )

def arrayToInt(array):
    return list( map( lambda val: int(val), array ) )

if __name__ == '__main__':
    if sys.argv[1]:
        path = sys.argv[1]
    else:
        path = str(input("Digite o path do arquivo do problema"))


    with open(path, "r") as arq:
        content = arq.read()
    lines = content.split('\n')
    
    num_restricoes, num_variaveis, otimizacao = arrayToInt(lines[0].split(' '))
    coeficientes_funcao_objetivo = arrayToFloat(lines[1].split(' '))
    coeficientes_funcao_objetivo = np.array(coeficientes_funcao_objetivo)

    coeficientes_restricoes = []
    operations = []
    termos_independentes = []

    for i in range(num_restricoes):
        *coeficientes_restricao, operation, termo_independente = lines[2+i].split(' ')
        
        coeficientes_restricoes.append(arrayToFloat(coeficientes_restricao))
        operations.append(operation)
        termos_independentes.append(float(termo_independente))
    
    coeficientes_restricoes = np.array(coeficientes_restricoes)
    operations = np.array(operations)
    termos_independentes = np.array(termos_independentes)

    tableu = criar_tableau(coeficientes_funcao_objetivo, coeficientes_restricoes, termos_independentes)
    print(tableu)
