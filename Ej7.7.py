#Realizar la búsqueda de un determinado nombre en una lista de nombres, de modo que el algoritmo imprima los
#siguientes mensajes según el resultado:
#'Nombre encontrado' si el nombre está en la lista
#'Nombre no existe' si el nombre no está en la lista

import os
clear = lambda:os.system('cls')
clear()

listanombres = ['Marcela', 'Sofia', 'Ligia', 'Andrea', 'Juliana', 'Alicia', 'Isi']

nombre= str(input("Escriba un nombre: "))


aux = 0
for i in range(len(listanombres)):
    if nombre.capitalize() == listanombres[i]:
        aux  = 1
        
if aux == 1:
    print("El nombre existe en la lista")
else:
    print("El nombre no existe en la lista")