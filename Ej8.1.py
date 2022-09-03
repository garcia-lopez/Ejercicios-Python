#8.1. Se desea eliminar los blancos de una frase dada terminada en un punto. Se supone que es posible leer los caracteres
#de la frase de uno en uno.

import os
clear = lambda:os.system('cls')
clear()

frase = str(input("Escriba una frase: "))

for i in frase:
    if i != " ":
        print(i, end="")

