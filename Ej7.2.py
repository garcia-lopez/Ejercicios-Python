#Se tienen N temperaturas. Se desea calcular su media y determinar entre todas ellas cuáles son superiores o iguales
#a esa media.
import os
clear = lambda:os.system('cls')
clear()

Temperaturas = []
cont = 0
cant = int(input("Total temperaturas: "))

i = 1
while cont < cant:
    temp = float(input(f"Temperatura #{i}: "))
    Temperaturas.append(temp)
    cont += 1
    i += 1
    
media  = sum(Temperaturas) / cant
    
igualtemp = []
altotemp = []

for temp in Temperaturas:
    if temp == media:
        igualtemp.append(temp)
  
    if temp > media:
        altotemp.append(temp)
        
print("*"*30)
print("Total temperaturas:  ", cant)
print("Temperatura media:  ", media)
print("Temperaturas iguales a la media:  ", len(igualtemp))
print("Temperaturas superiores a la media:  ",len(altotemp))
