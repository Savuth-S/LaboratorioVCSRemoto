# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 18:01:05 2020

@author: Savuth S.
"""

#%%Producto de dos numeros
a = float(input("Ingrese el primer numero de entrada: "))
b = float(input("Ingrese el segundo numero de entrada: "))

print("El producto de "+ str(a) +" y "+ str(c) +" es: "+ str(a*c))
print("El doble de "+ str(a) +" es: "+ str(a*2))
        
#%%Cuadrado de un numero
c = int(input("Ingrese un numero entero de entrada: "))
print("El cuadrado de "+ str(b))

#%%Raiz cuadrada de un numero
d = float(input("Ingrese un numero de entrada: "))

#%%Solución simple a ecuación cuadrada
print("Teniendo en cuenta la formula aX^2+bX+c=0")

a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
c = float(input("Ingrese el valor de c: "))
d = b**2-4*a*c

if d>0:
    x1 = (-b+d**(1/2))/2*a
    x2 = (-b-d**(1/2))/2*a
    print("El valor de x1 es:", x1)
    print("El valor de x2 es:", x2)
elif d==0:
    print("El valor de x1 y x2 son iguales "+ str(-b/2*a))
elif d<0:
    print("No existe solucion a la ecuacion cuadratica dentro del dominio de los numeros reales")