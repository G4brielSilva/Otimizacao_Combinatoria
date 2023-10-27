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
    while (cmd != 3):
        cmd = int(input("Escolha:\n1 - Executar o Simplex, mostrando resultados intermediários\n2 - Executar o Simples mostrando apenas o resultado final\n3 - Sair do programa"))
        if len(sys.argv) >= 2:
            path = sys.argv[1]
        else:
            path = str(input("Digite o path do arquivo do PPL: "))


        with open(path, "r") as arq:
          content = arq.read()
        lines = content.split('\n')

        num_restricoes, num_variaveis, otimizacao = arrayToInt(lines[0].split(' '))
        coeficientes_funcao_objetivo = arrayToFloat(lines[1].split(' '))

        # FO
        coeficientes_funcao_objetivo = np.array(coeficientes_funcao_objetivo)

        coeficientes_restricoes = []
        operations = []
        termos_independentes = []

        # Capturando valores
        for i in range(num_restricoes):
            *coeficientes_restricao, operation, termo_independente = lines[2+i].split(' ')
        
            coeficientes_restricoes.append(arrayToFloat(coeficientes_restricao))
            operations.append(operation)
            termos_independentes.append(float(termo_independente))
    
        # A
        coeficientes_restricoes = np.array(coeficientes_restricoes)
        operations = np.array(operations)
        # b
        termos_independentes = np.array(termos_independentes)

        tableau = criar_tableau(coeficientes_funcao_objetivo, coeficientes_restricoes, termos_independentes, otimizacao, operations)
        solved = solve(np.copy(tableau), otimizacao)

        print(solved)
        print(tableau)    