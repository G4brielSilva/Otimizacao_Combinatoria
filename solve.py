import numpy as np


def solve(tableau):
    best_i = -1
    exit_val_i = -1
    while True:
        print()
        print(tableau)
        fo = np.delete(tableau[0], np.where(tableau[0] == 0))
        
        best = np.amin(fo)
        print(best)
        
        # Interrompendo se não houverem valores negativos na minimização
        if best > 0: break

        # Selecionando a Variável de Entrada
        best_i = np.where(fo == best)[0][0]

        # Interrompendo se o valor de melhora for o mesmo que foi removido anteriormente
        if best_i == exit_val_i: break

        #Selecionando a Coluna Pivô
        pivot_column = tableau[:,best_i]
        
        b = tableau[:,-1]
        b_results = [bi/pivot if pivot != 0 else bi for bi, pivot in zip(b, pivot_column)]
        b_results = np.array(b_results)
        b_results_without0 = np.delete(b_results, np.where(b_results <= 0))
        if len(b_results_without0) == 0: break

        # Selecionando a Variável de Saída
        exit_val = np.amin(b_results_without0)
        exit_val_i = np.where(b_results == exit_val)[0][0]
        
        # Transformando em Identidade
        # Dividindo a linha da variável de Entrada para
        if tableau[exit_val_i][best_i] != 0:
            # tableau[exit_val_i] = np.where(tableau[exit_val_i] != 0, tableau[exit_val_i] / tableau[exit_val_i][best_i], tableau[exit_val_i])
            tableau[exit_val_i] = tableau[exit_val_i] / tableau[exit_val_i][best_i]

        # Problema é que na segunda iteração ele ta pegando a mesma linha, no caso eu to usando menor, se for maior acho que muda

        # Transformações lineares
        for row_i in range(len(tableau)):
            if (row_i != exit_val_i):
                pivot = tableau[row_i][best_i]
                row = -pivot * tableau[exit_val_i]
                tableau[row_i] = tableau[row_i] + row
        
        tableau = np.around(tableau, 2)

    return tableau[:,-1]