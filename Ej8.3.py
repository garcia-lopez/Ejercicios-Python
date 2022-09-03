#Leer dos caracteres y deducir si están en orden alfabético.
import os
clear = lambda:os.system('cls')
clear()

conjunto = []

cant = int(input("Escriba la cantidad de letras: "))

cont = 0
aux = 0
caracter = 'a'

while aux < cant:
    letras = input("Letra: ")
    aux += 1
    if letras >= caracter:
        caracter = letras
        cont = cont + 1
      
        
if cont == cant:
    print("Están en orden alfabético")
else:
    print("No estan en orden alfabético")
    



