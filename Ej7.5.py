#7.5. Realizar la suma de dos matrices bidimensionales.

"""algoritmo suma_matrices
inicio
desde I ← 1 hasta N hacer
desde J ← 1 hasta M hacer
S[I, J] ← A[I, J] + B[I, J]
fin_desde
fin_desde
fin"""

matriz1 = [[1, 2, 3, 4],
           [2, 2, 2, 2],
           [2, 2, 2, 2],
           [2, 2, 2, 2]]

matriz2 = [[1, 2, 3, 4],
           [3, 3, 3, 3],
           [3, 3, 3, 3],
           [3, 3, 3, 3]]

matriz3 = []

for i in range(len(matriz1)):
    matriz3.append([])
    for j in range(len(matriz1)):
        matriz3[i].append(matriz1[i][j] + matriz2[i][j])
        
for i in range(len(matriz3)):
    for j in range(len(matriz3)):
        print(matriz3[i][j], end="  ")
    print()
        
        

 

