import numpy as np
import sys

def arrayToFloat(array):
    print(array)
    arr = list( map( lambda val: float(val), array ) )
    print(arr)
    return arr

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
        termos_independentes.append(arrayToFloat(termo_independente))

    coeficientes_restricoes = np.array(coeficientes_restricoes)
    operations = np.array(operations)
    termos_independentes = np.array(termos_independentes)

    # print(coeficientes_funcao_objetivo, coeficientes_restricoes, termos_independentes)

    tableu_simplex = np.column_stack((coeficientes_restricoes, termos_independentes))
    tableu_simplex = np.vstack((coeficientes_funcao_objetivo, tableu_simplex))

    # print(tableu_simplex)
