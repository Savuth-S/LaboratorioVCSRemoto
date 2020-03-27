# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 04:33:09 2020

@author: Savuth S.
"""

#%%Algoritmo con función existente
num = int(1.495) #Función predefinida, se encarga de convertir un numero flotante en numero entero

print(num)

#%%Algoritmo con función personal
def suma(n):
    "Recive un numero, lo suma con 7 y lo convierte en entero"
    sum = round(n+7,0)
    return int(sum)
    
a = float(input("Ingrese un numero: "))
print(suma(a))