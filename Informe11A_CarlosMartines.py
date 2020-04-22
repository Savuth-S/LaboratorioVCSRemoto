# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 2020

@author: Savuth S.
"""
###Librerias
import numpy as np
import random as rn

###Clases
class suc_Dict(dict):
    def __missing__(self, key):
        return "Indefenido"

class mes_Dict(dict):
    def __missing__(self, key):
        return "Indefinido"

###Funciones
def generador(rango=(0,0), tamaño=(2,2)): 
    "Crea un array bidimensional lleno de numeros enteros pseudoaleatorios de un rango ingresado."
    "Parametros: generador(rango=(rango minino, rango maximo), tamaño=(filas, columnas))"
    
    #Declaración de variables
    ran_array = np.zeros(tamaño)
    
    for f in range(0,tamaño[0],1): #Asignación de valores pseudoaleatorios al array, Filas
        for c in range(0,tamaño[1],1): #Columnas
            ran_array[f,c] = int(rn.uniform(rango[0], rango[1]))
    return ran_array
    
def imprimir(ar_2d):
    "Impresion de un array bidimensional 4x12 de manera legible con nombres especificos"
    
    #Declaración de variables
    ar_fil, ar_col = np.shape(ar_2d)
    nm_fil = suc_Dict({0: "Buracamanga", 1: "Floridablanca", 2: "Girón", 3: "Piedecuesta"})
    nm_col = mes_Dict({0: "Enero", 1: "Febrero", 2: "Marzo", 3: "Abril", 4: "Mayo", 5: "Junio", 6: "Julio", 7: "Agosto", 8: "Septiembre", 9: "Octubre", 10: "Noviembre", 11: "Diciembre"})
    
    for f in range(0,ar_fil,1): #Impresión legible, Filas con nombre asignado
        print("\n--"+str(nm_fil[f])+"--")
        for c in range(0,ar_col,1): #Columnas con nombre asignado
            print("    "+str(nm_col[c])+": "+str(int(ar_2d[f,c]))+"M $COP")
    
def restador(br_mn,br_st): 
    "Resta dos arrays bidimensionales del mismo tamaño en la forma minuendo-sustraendo"
    
    #Check
    if np.shape(br_mn) != np.shape(br_st): #Simetria
        return 
    
    #Declaración de variables
    ar_fil, ar_col = np.shape(br_mn)
    ar_resul = np.zeros((ar_fil,ar_col))
    
    for f in range(0,ar_fil,1): #Asignación de la resta de arrays ingresados al array de resultado, Filas
        for c in range(0,ar_col,1): #Columnas
            ar_resul[f,c] = int(br_mn[f,c]-br_st[f,c])            
    return ar_resul
    
def mejor_Ciudad(ar_2d, cl = -1, prnt = False): 
    "Encuentra la fila de mayor valor en un array bidimensional y devuelve un nombre especifico"
    
    #Declaración de variables
    ar_fil, ar_col = ar_2d.shape
    pos = 0
    sl_max = 0
    
    if cl > -1 and ar_col-1 >= cl: #Bloque para la selección de columna por el usuario
        for f in range(0,ar_fil,1): #Comparación de valores en una columna
            if sl_max < ar_2d[f,cl]:
                sl_max = ar_2d[f,cl]
                pos = f
        if prnt == True:
            nm_fil = suc_Dict({0: "Buracamanga", 1: "Floridablanca", 2: "Girón", 3: "Piedecuesta"})
            print(nm_fil[pos])
        return sl_max
    elif cl > -1:
        print("ERROR: Tamaño de columnas invalido")
        return
    
    for f in range(0,ar_fil,1):
        sum = 0
        
        for c in range(0,ar_col,1): #Suma de valores en un fila
            sum += ar_2d[f,c]
            
        if sl_max < sum:
            sl_max = sum
            pos = f
            
    if prnt == True:
        nm_fil = suc_Dict({0: "Buracamanga", 1: "Floridablanca", 2: "Girón", 3: "Piedecuesta"})
        print(nm_fil[pos])
    return sl_max
    
def peor_Ciudad(ar_2d, cl = -1, prnt = False): 
    "Encuentra la fila de menor valor en un array bidimensional y devuelve un nombre especifico"
    
    #Declaración de variables
    ar_fil, ar_col = ar_2d.shape
    pos = 0
    sl_min = 9999
    
    if cl > -1 and ar_col-1 >= cl: #Bloque para la selección de columna por el usuario
        for f in range(0,ar_fil,1): #Comparación de valores en una columna
            if sl_min > ar_2d[f,cl]:
                sl_min = ar_2d[f,cl]
                pos = f
        if prnt == True:
            nm_fil = suc_Dict({0: "Buracamanga", 1: "Floridablanca", 2: "Girón", 3: "Piedecuesta"})
            print(nm_fil[pos])
        return sl_min
    elif cl > -1:
        print("ERROR: Tamaño de columnas invalido")
        return
    
    for f in range(0,ar_fil,1):
        sum = 0
        
        for c in range(0,ar_col,1): #Suma de valores en un fila
            sum += ar_2d[f,c]
            
        if sl_min > sum:
            sl_min = sum
            pos = f
            
    if prnt == True:
        nm_fil = suc_Dict({0: "Buracamanga", 1: "Floridablanca", 2: "Girón", 3: "Piedecuesta"})
        print(nm_fil[pos])
    return sl_min
    
def mejor_Mes(ar_2d, fl = -1, prnt = False):
    "Encuentra la columna de mayor valor en un array bidimensional y devuelve un nombre especifico"
    
    #Declaración de variables
    ar_fil, ar_col = ar_2d.shape
    sl_col = 0
    sl_max = 0
    
    if fl > -1 and ar_fil-1 >= fl: #Bloque para la selección de fila por el usuario
        for c in range(0,ar_col,1): #Comparación de valores en una fila
            if sl_max < ar_2d[fl,c]:
                sl_max = ar_2d[fl,c]
                sl_col = c
                
        if prnt == True:
            nm_col = mes_Dict({0: "Enero", 1: "Febrero", 2: "Marzo", 3: "Abril", 4: "Mayo", 5: "Junio", 6: "Julio", 7: "Agosto", 8: "Septiembre", 9: "Octubre", 10: "Noviembre", 11: "Diciembre"})
            print(nm_col[sl_col])
        return sl_max
    elif fl > -1:
        print("ERROR: Tamaño de fila invalido")
        return
    
    for f in range(0,ar_fil,1):
        for c in range(0,ar_col,1): #Comparación de valores en una fila
            if sl_max < ar_2d[f,c]:
                sl_max = ar_2d[f,c]
                sl_col = c
                
        if prnt == True:
            nm_fil = suc_Dict({0: "Buracamanga", 1: "Floridablanca", 2: "Girón", 3: "Piedecuesta"})
            nm_col = mes_Dict({0: "Enero", 1: "Febrero", 2: "Marzo", 3: "Abril", 4: "Mayo", 5: "Junio", 6: "Julio", 7: "Agosto", 8: "Septiembre", 9: "Octubre", 10: "Noviembre", 11: "Diciembre"})
            print(nm_fil[f], nm_col[sl_col])

###Programa Principal
#Declaración de variables
ingresos =  generador((100,180),(4,12))
egresos = generador((60,130),(4,12))
ganancias = restador(ingresos,egresos)

print("~~~~Ingresos por sucursal en meses~~~~",end = "")
imprimir(ingresos)

print("\n\n~~~~Egresos por sucursal en meses~~~~",end = "")
imprimir(egresos)

if ingresos.shape == egresos.shape:
    print("\n\n~~~~Ganancias y/o perdidas por sucursal en meses~~~~",end = "")
    imprimir(ganancias)

    print(mejor_Ciudad(ganancias, -1, True))
    print(peor_Ciudad(ganancias, -1, True))
    print(mejor_Mes(ganancias, -1, True))
