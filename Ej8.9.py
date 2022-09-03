#Escribir una función convertida (núm,b) que nos permita transformar un número entero y positivo en base 10 a la
#base que le indiquemos como parámetro. Comprobar el algoritmo para las bases 2 y 16.
import os
clear = lambda:os.system('cls')
clear()

def potencia(num, pot):
    print(f"{num} elevado a la {pot} es >> {pow(num, pot)}")
    
    
def principal():
    num = int(input("Escriba un numero: "))
    pot = int(input("Potencia a elevar: "))
    potencia(num, pot)
    
principal()
    