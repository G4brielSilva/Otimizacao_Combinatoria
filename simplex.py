import numpy as np
import sys

def criar_tableau(coeficientes_funcao_objetivo, coeficientes_restricoes, termos_independentes, otimizacao, operations):
    num_restricoes = len(coeficientes_restricoes)
    num_variaveis = len(coeficientes_funcao_objetivo)

    tableau = np.zeros((num_restricoes + 1, num_variaveis + num_restricoes + 1))

    # Configurar a função objetivo na primeira linha do tableau
    tableau[0, :num_variaveis] = coeficientes_funcao_objetivo

    for i in range(num_restricoes):
        if termos_independentes[i] < 0:
            tableau[0] = -tableau[0]
            termos_independentes[i] = -termos_independentes
            if operations[i] == "<=":
                operations[i] = ">="
            elif operations[i] == ">=":
                operations[i] = "<="

    # Configurar as restrições e os termos independentes
    for i in range(num_restricoes):
        tableau[i + 1, :num_variaveis] = coeficientes_restricoes[i]
        tableau[i + 1, num_variaveis + i] = 1 if operations[i] == '<=' or operations[i] == '==' else -1  # Adicionando variáveis de folga
        tableau[i + 1, -1] = termos_independentes[i]

    return tableau

def arrayToFloat(array):
    return list( map( lambda val: float(val), array ) )

def arrayToInt(array):
    return list( map( lambda val: int(val), array ) )

def solve(tableau, otimizacao):
    best_i = -1
    exit_val_i = -1
    while True:
        fo = np.delete(tableau[0], np.where(tableau[0] == 0))
        
        # TODO Considere verificar se tem que fazer tratativa pra max e min ou se tem como só jogar todo problema de max pra mim ou vice versa
        if otimizacao: best = np.amax(fo)
        else: best = np.amin(fo)

        
        # Interrompendo se não houverem valores negativos na minimização
        if not otimizacao and best > 0: break
        # Interrompendo se não houverem valores positivos na maximização
        if otimizacao and best < 0: break

        # Selecionando a Variável de Entrada
        best_i = np.where(fo == best)[0][0]

        # Interrompendo se o valor de melhora for o mesmo que foi removido anteriormente
        if best_i == exit_val_i: break

        #Selecionando a Coluna Pivô
        pivot_column = tableau[:,best_i]
        
        b = tableau[:,-1]
        b_results = b/pivot_column
        b_results = np.delete(b_results, np.where(b_results <= 0))

        if len(b_results) == 0: break

        # Selecionando a Variável de Saída
        exit_val = np.amin(b_results)
        exit_val_i = np.where(b_results == exit_val)[0][0] + 1
        
        # Transformando em Identidade
        # Dividindo a linha da variável de Entrada para
        tableau[exit_val_i] = tableau[exit_val_i]/tableau[exit_val_i][best_i]

        # Transformações lineares
        for row_i in range(len(tableau)):
            if (row_i != exit_val_i):
                pivot = tableau[row_i][best_i]
                row = -pivot * tableau[exit_val_i]
                tableau[row_i] = tableau[row_i] + row
        
        tableau = np.around(tableau, 2)

    return tableau[:,-1]

if __name__ == '__main__':
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