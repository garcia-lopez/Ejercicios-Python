#Se dispone de una tabla T de dos dimensiones. Calcular la suma de sus elementos.

arreglouno = [[1, 2],
              [1, 2]]

arreglodos = [[1, 2],
              [1, 2]]

suma = []

for i in range(len(arreglouno)):
    suma.append([])
    for j in range(len(arreglouno)):
        suma[i].append(arreglouno[i][j] + arreglodos[i][j])
        
for i in range(len(suma)):
    for j in range(len(suma)):
        print(suma[i][j], end=" ")
    print()
    
