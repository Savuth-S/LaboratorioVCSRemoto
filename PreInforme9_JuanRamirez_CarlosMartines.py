# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 17:51:09 2020

@author: Juan Camilo Ramirez
"""


#%% (Punto 1)Ejercicio 19

x1 = float(input("Ingresar el valor de x1: "))
y1 = float(input("Ingresar el valor de y1: "))
x2 = float(input("Ingresar el valor de x2: "))
y2 = float(input("Ingresar el valor de y2: "))

a = x2 - x1
b = y2 - y1 

c = (a**(1/2))+(b**(1/2))

print("La distancia euclidiana es:", c)

#%% (Punto 2) Ejercicio 23 
n = int(input("Ingresar numero de 4 cifras: "))

c4 = n%10
c3 = (n%100)//10
c2 = (n%1000)//100
c1 = (n-(n%1000))//1000

print(str(c4) + str(c3) + str(c2) + str(c1))

#%% (Punto 3) Ejercicio 30
n1 = float(input("Ingrese el valor de la nota 1: "))
n2 = float(input("Ingrese el valor de la nota 2: "))
n3 = float(input("Ingrese el valor de la nota 3: "))
n4 = float(input("Ingrese el valor de la nota 4: "))
n5 = float(input("Ingrese el valor de la nota 5: "))

nf = n1*0.15+n2*0.20+n3*0.15+n4*0.30+n5*0.20

if nf<2.0:
    print("No puede habilitar")
    print("Su nota es:", nf)
elif 2.0<=nf<3.0:
    print("Reprobo")
    print("Su nota es:", nf)
elif 3.0<=nf<=4.5:
    print("Aprobo")
    print("Su nota es:", nf)
elif nf>4.5:
    print("Felicitacion")
    print("Su nota es:", nf)
    
#%% (Punto 4) Ejercicio 60
n = int(input("Ingrese la cantidad de filas: "))
if n>0:
    for i in range(1,n+1):
        print("")
        for j in range(1,i+1):
            print(j,end=" ")
else:
    print("El numero ingresado es invalido, intentelo con otro numero")

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