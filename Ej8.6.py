#8.6. Contar el número de vocales de una frase terminada en un punto.
import os
clear = lambda:os.system('cls')
clear()

frase = input("Escriba una frase: ")


a = frase.count('a')
e = frase.count('e')
i = frase.count('i')
o = frase.count('o')
u = frase.count('u')

vocales = a + e + i + o + u

print(f"Total de vocales {vocales}")
