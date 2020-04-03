# -*- coding: utf-8 -*-
"""
Creado el Wed Apr 01 18:12 2020

@author: Carlos "Savuth" Martínez.
"""

###Librerias
import numpy as np

###Funciones
def arr_Me(ar): #Variables en orden: Array. Obtiene la mediana de un array
    #Declaración de variables
    ar_sr = np.sort(ar)
    ar_ln = len(ar)
    med = 0 
    
    if(ar_ln%2==0):
        med = (ar_sr[ar_ln//2]+ar_sr[(ar_ln+2)//2])/2
    else:
        med = ar_sr[(ar_ln+1)/2]
    return med    

def arr_Prom(ar): #Variables en orden: Array. Obtiene la media o promedio de un array
    #Declaración de variables
    sum = 0
    
    for i in range(0,len(ar)-1,1):
        sum += ar[i]
    return sum/len(ar)
    
def obt_Def(n1,n2): #Variables en orden: Numero comparado o maximo (100%), Numero a comparar. Obtienie la deficienco entre dos valores expresado en porcentaje
    defi = (n2*100/n1)
    defi = 100-defi
    return defi
    
###Programa Principal
#Declaración de variables
uoa_kel = np.array([ #Array de la utilidad operacional desde 2008-2017 respectivamente
    27834, 23789, 30189, 30967, 32501,
    32701, 31665, 17155,  4614,   834])
prom16_17 = (uoa_kel[9]+uoa_kel[8])/2
prom08_09 = (uoa_kel[0]+uoa_kel[1])/2
acum_util = 0
a = 0

for i in range(0,9,1):
        acum_util += uoa_kel[i]

print("\nUtilidad operacional acumulada: "+ str(acum_util)+"M$COP")
print("\nMediana: "+ str(arr_Me(uoa_kel))+"M$COP")
print("\nMedia: "+ str(arr_Prom(uoa_kel))+"M$COP")

print("\n\nDeficit 16-17: "+ str(uoa_kel[8]-uoa_kel[9])+str("M$COP"))
print("\nDiferencia de promedios 08-09 con 16-17: "+ str(prom08_09-prom16_17)+"M$COP")
print("\nDiferencia de mayor utilidad (2013) con menor utilidad (2017): "+ str(np.sort(uoa_kel)[9]-np.sort(uoa_kel)[0])+"M$COP")

print("\n\n--Porcentajes de aporte individual--",end="") 
print("\n08: "+ str(round(uoa_kel[0]*100/acum_util,3))+str("%"),end="")
print("\n09: "+ str(round(uoa_kel[1]*100/acum_util,3))+str("%"),end="")
print("\n10: "+ str(round(uoa_kel[2]*100/acum_util,3))+str("%"),end="")
print("\n11: "+ str(round(uoa_kel[3]*100/acum_util,3))+str("%"),end="")
print("\n12: "+ str(round(uoa_kel[4]*100/acum_util,3))+str("%"),end="")
print("\n13: "+ str(round(uoa_kel[5]*100/acum_util,3))+str("%"),end="")
print("\n14: "+ str(round(uoa_kel[6]*100/acum_util,3))+str("%"),end="")
print("\n15: "+ str(round(uoa_kel[7]*100/acum_util,3))+str("%"),end="")
print("\n16: "+ str(round(uoa_kel[8]*100/acum_util,3))+str("%"),end="")
print("\n17: "+ str(round(uoa_kel[9]*100/acum_util,3))+str("%"))

print("\n\n--Deficiencias con año inmediatamente anterior--",end="")
print("\n08-09: "+ str(round(obt_Def(uoa_kel[0],uoa_kel[1]),3))+str("%"),end="")
print("\n09-10: "+ str(round(obt_Def(uoa_kel[1],uoa_kel[2]),3))+str("%"),end="")
print("\n10-11: "+ str(round(obt_Def(uoa_kel[2],uoa_kel[3]),3))+str("%"),end="")
print("\n11-12: "+ str(round(obt_Def(uoa_kel[3],uoa_kel[4]),3))+str("%"),end="")
print("\n12-13: "+ str(round(obt_Def(uoa_kel[4],uoa_kel[5]),3))+str("%"),end="")
print("\n13-14: "+ str(round(obt_Def(uoa_kel[5],uoa_kel[6]),3))+str("%"),end="")
print("\n14-15: "+ str(round(obt_Def(uoa_kel[6],uoa_kel[7]),3))+str("%"),end="")
print("\n15-16: "+ str(round(obt_Def(uoa_kel[7],uoa_kel[8]),3))+str("%"),end="")
print("\n16-17: "+ str(round(obt_Def(uoa_kel[8],uoa_kel[9]),3))+str("%"))
