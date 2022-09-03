#8.8. Leer cien caracteres de un texto y contar el número de letras “b”.
import os
import time
clear = lambda:os.system('cls')
clear()


caracteres = input("Escriba un texto: ")

b = caracteres.count('b')

print(f"Total de caracteres b: {b}")

time.sleep(30)

#Se desea contar el número de letras “a” y el número de letras “b” de una frase terminada en un punto. Se supone
#que es posible leer los caracteres independientemente.
clear()
caracteres = input("Escriba un texto: ")

b = caracteres.count('b')
a = caracteres.count('a')

print(f"Total de caracteres b: {b}")
print(f"Total de caracteres a: {a}")


