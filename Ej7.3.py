#Calcular la media de las estaturas de una clase. Deducir cuántos son más altos que la media y cuántos son más
#bajos que dicha media
# 
import os
clear = lambda:os.system('cls')
clear()

EstaturaEst = []
cont = 0
cant = int(input("Cantidad de estudiante en la clase: "))

i = 1
while cont < cant:
    est = float(input(f"Estatura del estudiante #{i}: "))
    EstaturaEst.append(est)
    cont += 1
    i += 1
    
media  = sum(EstaturaEst) / len(EstaturaEst)
    
bajomed = []
altomed = []

for est in EstaturaEst:
    if est < media:
        bajomed.append(est)
  
    if est > media:
        altomed.append(est)
        
print("*"*30)
print("Total de estudiantes: ", len(EstaturaEst))
print("Estatura media de los estudiantes: ", media)
print("Cantidad de estudiantes mas bajos que la media: ", len(bajomed))
print("Cantidad de estudianates mas altos que la media: ",len(altomed))
        
    


