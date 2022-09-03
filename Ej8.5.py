#8.5. Contar el número de letras “i” de una frase terminada en un punto. Se supone que las letras pueden leerse indepen-
#dientemente.

import os
clear = lambda:os.system('cls')
clear()

frase = input("Escriba una frase con punto final: ")

i = frase.count('i')

print(f"i's encontradas: {i}")