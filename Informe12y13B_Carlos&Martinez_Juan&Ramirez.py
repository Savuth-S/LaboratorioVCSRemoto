# -*- coding: utf-8 -*-
"""
Created on 05/02/2020

@author: Savuth S.
"""
###Librerias
import random as rn

###Funciones
def combinar(dc, ls):
    "Combina una lista de strings con un diccionario de strings"
    
    dic = {key+value:dc[key] for key in dc for value in ls} #Ciclo para acceder a las keys del diccionarioc, ciclo para acceder los valores en la lista
    return dic

def revolver(dic):
    "Desordena las entradas en un diccionario de manera pseudoaleatoria"
    
    keys = [key for key in dic] #Lista de keys del diccionario
    values = [dic[key] for key in dic] #Lista de valores del diccionario
    
    for length in range(len(keys)): #Ciclo para mover las entradas en la lista de manera pseudoaleatoria
        index = rn.randint(0,len(keys)-1) #Indice pseudoaleatorio
        
        temp_keys = keys[index] #Bloque de la lista de keys
        keys[index] = keys[0]
        keys[0] = temp_keys
        
        temp_values = values[index] #Bloque de la lista de valores
        values[index] = values[0]
        values[0] = temp_values
    
    dic = {keys[length]:values[length] for length in range(len(keys))} #Se combinan las dos listas en un diccionario, respectivamente
    return dic
    
def repartir(hand, deck):
    "Reparte las cartas de manera pseudoaleatoria a la mano que lo solicita"
    
    keys = [key for key in deck] #Lista de keys
    index = rn.randint(0,len(keys)-1) #Indice pseudoaleatorio de la lista de keys
    
    if len(hand) == 0: #Si la mano no tiene cartas, devolver dos
        for i in range(2):
            hand.append(keys[index])
            del deck[keys[index]]
            del keys[index]
            index = rn.randint(0,len(keys)-1)
    else: #Devuelve una carta en posición x a la mano
        hand.append(keys[index])
        del deck[keys[index]]
    return hand

def sumar_cartas(hand, values):
    "Suma los valores de las cartas en la mano solicitada"
    
    score = [values[key[0]] for key in hand if key[0] != 'A'] #Lista de las cartas en mano, sin los ases
    a_list = [values[key[0]] for key in hand if key[0] == 'A'] #Lista especial solo con los ases
    
    if int(sum(score))+int(sum(a_list))*11 < 22: #Si la suma de los ases en valor 10 es menor a 21, devolver puntaje con ases en 10
        return int(sum(score))+int(sum(a_list))*11
    else: #Devolver puntaje con ases en valor 1
        return int(sum(score))+int(sum(a_list))

def mostrar(hand,values):
    "Imprime la mano solicitada y el puntaje de esta"
    
    print("Puntaje: "+ str(sumar_cartas(hand,values)))
    print("Mano: "+ str(hand))
    

###Valores Iniciales
ponderado={"A":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "J":10, "Q":10, "K":10}
simbolos = ["(C)", "(D)", "(T)", "(P)"]
baraja = combinar(ponderado,simbolos)
games = 0
wins = 0
loses = 0


###Programa Prinipal
while(True):
    #Declaración de variables
    cartas_jugador = []
    cartas_tallador = []
    shuffled_deck = revolver(baraja)
        
    while(True): #Ciclo para la selección de cartas por el jugador
        if sumar_cartas(cartas_jugador,ponderado) >= 21:
            break
        else:
            cartas_jugador = repartir(cartas_jugador,shuffled_deck)
        
            print("\n\n¿Desea seguir recibiendo cartas?") #Check si desea seguir recibiendo cartas
            print("1- Si\n2- No\n\nPuntaje: "+ str(sumar_cartas(cartas_jugador,ponderado)), end='')
            temp = int(input("Mano: "+ str(cartas_jugador)+"\n"))
        
            if temp == 2: 
                break
        
    if sumar_cartas(cartas_jugador,ponderado) <= 21: #Check si el puntaje del jugador es menor a 21 y puede seguir jugando
        while(True): #Cliclo de la maquina, toma cartas de la baraja hasta que es mayor o igual al puntaje del jugador
            if sumar_cartas(cartas_tallador,ponderado) >= 21 or sumar_cartas(cartas_tallador,ponderado) >= sumar_cartas(cartas_jugador,ponderado):
                break
            else: 
                cartas_tallador = repartir(cartas_tallador,shuffled_deck)
        
        print("\n\n~~~Tú mano~~~") #Imprime las manos de la maquina y el jugador, para que el jugador pueda comparar
        mostrar(cartas_jugador,ponderado)  
        print("\n~~~Mano del tallador~~~")    
        mostrar(cartas_tallador,ponderado)
        
        #Impresiones de las distintas pantallas de fin de juego
        if sumar_cartas(cartas_jugador,ponderado) > sumar_cartas(cartas_tallador,ponderado) and sumar_cartas(cartas_jugador,ponderado) < 22:
            wins += 1
            games += 1
            print("\nGanaste.")
        elif sumar_cartas(cartas_jugador,ponderado) < sumar_cartas(cartas_tallador,ponderado) and sumar_cartas(cartas_tallador,ponderado) > 21:
            wins += 1
            games += 1
            print("\nGanaste.")
        else:
            loses += 1
            games += 1
            print("\nPerdiste.")
            
    else: #Imprime pantalla de perder
        loses += 1
        games += 1
        print("\n\nPerdiste.")
    
    print("\nPartidas jugadas: "+ str(games)) #Contadores de las partidas jugadas, ganadas y perdidas
    print("Partidas ganadas: "+ str(wins))
    print("Partidas perdidas: "+ str(loses))    
    
    print("\n¿Desea continuar jugando?", end='') #Check si el jugador desea seguir jugando
    temp = str(input("YES- Si\nNO- No\n\n"))
        
    if temp == "NO":
        break
