#Escribir el algoritmo que permita sumar el número de elementos positivos y el de negativos de una tabla T.
import os
clear = lambda:os.system('cls')
clear()

numeros = []
cont = 0

total = int(input("Cantidad de numeros: "))

while cont < total:
  num = int(input("Digite un numero: "))
  numeros.append(num)
  cont += 1

negativos = []
positivos = []


for num in numeros:
    if num < 0:
        negativos.append(num)
        
    if num >= 0:
        positivos.append(num)
        
print("Suma numeros positivos: ", sum(positivos))
print("Suma numeros negativos: ", sum(negativos))
