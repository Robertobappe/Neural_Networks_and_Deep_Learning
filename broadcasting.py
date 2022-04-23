import numpy as np

#matrix 3 X 4 em que os alimentos estão
#representados na coluna e na linha
#estão carboidrato, proteina e gordura,
#respectivamente.
A = np.array([[56.0, 0.0, 4.4, 68.0],
             [1.2, 104.0, 54.0, 8.0],
             [1.8, 135.0, 99.0, 0.9]])

#a soma das colunas nos fornece
# a quantidade total de calorias.
cal = A.sum(axis=0)

#nova matrix com as porcentagens
#de carboidrato, proteina e gordura.
percentage = 100*A/cal.reshape(1,4)
