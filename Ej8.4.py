#8.4. Leer una letra de un texto. Deducir si está o no comprendida entre las letras mayúsculas I-M inclusive.

import os
clear = lambda:os.system('cls')
clear()

char = input("Escriba una letra: ")

if char.isupper() == True:
    print("Mayuscula")
    
else:
    print("Minuscula")