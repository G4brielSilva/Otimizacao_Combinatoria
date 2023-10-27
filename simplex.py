import numpy as np
import sys
from solve import solve
from criar_tableau import criar_tableau

def arrayToFloat(array):
    return list( map( lambda val: float(val), array ) )

def arrayToInt(array):
    return list( map( lambda val: int(val), array ) )

if __name__ == '__main__':
    cmd = 0
    file = ''
    while (cmd != 3):
        cmd = int(input("Escolha:\n1 - Executar o Simplex, mostrando resultados intermediários\n2 - Executar o Simples mostrando apenas o resultado final\n3 - Sair do programa\n"))
        if (cmd == 1):
            path = input("Digite o nome do arquivo a ser lido: ")
            # ler o arquivo e mostrar na tela o tableau inicial
        if (cmd == 2):
            path = input("Digite o nome do arquivo a ser lido: ")
            # executar o simplex imediatamente
        if (cmd == 3):
            pass

        with open(path, "r") as arq:
          content = arq.read()
        lines = content.split('\n')
        
        num_restricoes, num_variaveis, otimizacao = arrayToInt(lines[0].split(' '))
        coeficientes_funcao_objetivo = arrayToFloat(lines[1].split(' '))
        # FO
        coeficientes_funcao_objetivo = np.array(coeficientes_funcao_objetivo)
        print(coeficientes_funcao_objetivo)

        # coeficientes_restricoes = []
        # operations = []
        # termos_independentes = []

        # # Capturando valores
        # for i in range(num_restricoes):
        #     *coeficientes_restricao, operation, termo_independente = lines[2+i].split(' ')
        
        #     coeficientes_restricoes.append(arrayToFloat(coeficientes_restricao))
        #     operations.append(operation)
        #     termos_independentes.append(float(termo_independente))
    
        # # A
        # coeficientes_restricoes = np.array(coeficientes_restricoes)
        # operations = np.array(operations)
        # # b
        # termos_independentes = np.array(termos_independentes)

        # tableau = criar_tableau(coeficientes_funcao_objetivo, coeficientes_restricoes, termos_independentes, otimizacao, operations)
        # solved = solve(np.copy(tableau), otimizacao)

        # print(solved)
        # print(tableau)    