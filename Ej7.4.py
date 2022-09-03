#7.4. Inicializar una matriz de dos dimensiones con un valor constante dado K.
import os
clear = lambda:os.system('cls')
clear()

m = 4
n = 4

matriz = []

for i in range(m): #para las filas 
    arreglo = []     #para cada fila defino un arreglo
    for j in range(n):  # loop para asignar los valores a cada arreglo
        j = 'k'  #asignar la letra k en la posición j
        arreglo.append(j) #escribir el valor de j en el arreglo
    matriz.append(arreglo) #guardar el arreglo en otra lista
    
for i in range(m):
    for j in range(n):
        print(matriz[i][j], end="  ")
    print()

#[0] * n for i in range(n)
        

