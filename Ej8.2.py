#Leer un carácter y deducir si está situado antes o después de la letra “m” en orden alfabético.

import os
clear = lambda:os.system('cls')
clear()

caracter = input("Escriba una letra: ")

if caracter.lower() < 'm':
    print("Alfabeticamente esta antes de << m >>")
    
if caracter.lower() > 'm':
    print("Alfabeticamente esta despues de << m >>")
    
if caracter.lower() == 'm':
    print("Escribio << m >>")
    
