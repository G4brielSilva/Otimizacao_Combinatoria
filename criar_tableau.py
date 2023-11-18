import numpy as np


def criar_tableau(
    coeficientes_funcao_objetivo,
    coeficientes_restricoes,
    termos_independentes,
    otimizacao,
    operations,
):
    num_restricoes = len(coeficientes_restricoes)
    num_variaveis = len(coeficientes_funcao_objetivo)

    tableau = np.zeros((num_restricoes + 1, num_variaveis + num_restricoes + 1))

    # Configurar a função objetivo na primeira linha do tableau
    tableau[0, :num_variaveis] = (
        -coeficientes_funcao_objetivo if otimizacao else coeficientes_funcao_objetivo
    )  # Garantindo que o caso vai cair pra minimização sempre

    for i in range(num_restricoes):
        if termos_independentes[i] < 0:
            tableau[i] = -tableau[i]
            termos_independentes[i] = -termos_independentes[i]
            if operations[i] == "<=":
                operations[i] = ">="
            elif operations[i] == ">=":
                operations[i] = "<="

    for termo in termos_independentes:
        if termo < 0:
            return None

    rows_need_var_art = []
    M = 1000  

    # Configurar as restrições e os termos independentes
    for i in range(num_restricoes):
        tableau[i + 1, :num_variaveis] = coeficientes_restricoes[i]

        # Adicionando variáveis de folga e artificiais com Big M
        if operations[i] == "<=":
            tableau[i + 1, num_variaveis + i] = 1
            tableau[i + 1, -1] = termos_independentes[i]
        elif operations[i] == ">=":
            tableau[i + 1, num_variaveis + i] = -1
            tableau[i + 1, -1] = termos_independentes[i]
        else:  # "=="
            tableau[i + 1, num_variaveis + i] = M  # Variável artificial com penalização M
            tableau[i + 1, -1] = M * termos_independentes[i]

        if rows_need_var_art:
            var_art = np.zeros((len(tableau), len(tableau)))

            for i in range(len(var_art)):
                if i in rows_need_var_art:
                    var_art[0][i] = 1
                    var_art[i][i] = 1
                # array_atualizado = np.insert(array_original, array_original.shape[1], nova_coluna, axis=1)

            b = tableau[:, -1]
            var_art = np.array(var_art)
            # Inserir as colunas de variáveis artificiais antes da última coluna do tableau
            tableau = tableau[:, :-1]
            tableau[0] = 0
            # print(var_art)
            tableau = np.concatenate((tableau, var_art), axis=1)
            tableau = np.concatenate((tableau, b.reshape(-1, 1)), axis=1)

            indices = np.where(tableau[0] == 1)[0]
            for indice in indices:
                row = np.where(tableau[:, indice] == 1)[0][1]
                tableau[0] = tableau[0] - tableau[row]

        return tableau
