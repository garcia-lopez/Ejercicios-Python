#Escribir un algoritmo que permita calcular el cuadrado de los cien primeros números enteros y a continuación es-
#cribir una tabla que contenga dichos cien números cuadrados.
import os
clear = lambda:os.system('cls')
clear()

arreglo = [] 
num = 1
cant = 101
while num < cant:
    arreglo.append(num)
    num  += 1

for num in arreglo:
    doble = num * num
    print(f"T({num}) = {num} * {num} = {doble}")
    