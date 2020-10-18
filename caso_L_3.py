# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 17:55:53 2020

@author: jpsil
"""



from reticulado import Reticulado
from barra import Barra
from numpy import *
from math import *

 
def caso_L():
    # Unidades base
    m = 1.
    kg = 1.
    s = 1. 
    
    
    #Unidades derivadas
    N = kg*m/s**2
    cm = 0.01*m
    mm = 0.001*m
    KN = 1000*N
    
    Pa = N / m**2
    KPa = 1000*Pa
    MPa = 1000*KPa
    GPa = 1000*MPa
    
    # #Parametros
    # L = 5.0  *m
    # F = 100*KN
    # B = 2.0 *m
    # #Parametros cargas vivas
    # Q=400*(kg/(m**2))
    # g=9.8*(m/(s**2))
    # A0=7.5*(m**2)
    # A1=15*(m**2)
    
    #Inicializar modelo
    
    ret = Reticulado()
    nodos=37
    factor=6
    altura2=sqrt(25-(2.5**2))
    altura2=20.
    altura_pilares=20.
    """
    Nodos calle
    """
    # import math
    siguiente_1=0.5
    for i in range (nodos):
        if i != nodos//2 and i!= nodos//2+1:    
            
            ret.agregar_nodo(10+i*factor-floor(siguiente_1),0,100) # nodos 0-36
            # print(f'AA nodo {i}:{10+i*factor-floor(siguiente_1)}')
        else:
            
            ret.agregar_nodo(10+i*factor-siguiente_1,0,100)
            # print(f'BB nodo {i}:{10+i*factor-siguiente_1}')
            siguiente_1+=0.5
    siguiente_2=0.5
    for l in range(nodos):
        if l != nodos//2 and l!= nodos//2+1:    
            ret.agregar_nodo(10+l*factor-floor(siguiente_2),2,100) # nodos 37-73
            # print(f'CC nodo {l+37}:{10+l*factor-floor(siguiente_2)}')
        else:
            ret.agregar_nodo(10+l*factor-siguiente_2,2,100)
            # print(f'DD nodo {l+37}:{10+l*factor-siguiente_2}')
            siguiente_2+=0.5
    
    
    """
    Nodos Arco
    """
    altura_puente=33
    nodos_mitad=11
    posicion_x_arco=10
    posicion_z_arco=100
    for i in range(nodos_mitad):
        if i==0:
            posicion_x_arco+=7.5
            posicion_z_arco+=altura_puente/10.0
            ret.agregar_nodo(posicion_x_arco,0,round(posicion_z_arco,1))
            # ret.agregar_nodo(posicion_x_arco,2,round(posicion_z_arco,1))
            print(f'el nodo {i+74} = {posicion_x_arco} y {round(posicion_z_arco,1)}')
            
        else:
            posicion_x_arco+=10
            posicion_z_arco+=altura_puente/10.0
            ret.agregar_nodo(posicion_x_arco,0,round(posicion_z_arco,1))
            # ret.agregar_nodo(posicion_x_arco,2,round(posicion_z_arco,1))
            print(f'el nodo {i+74} = {posicion_x_arco} y {round(posicion_z_arco,1)}')
    for j in range(nodos_mitad):
        if j!=nodos_mitad-1:
            posicion_x_arco+=10
            posicion_z_arco-=altura_puente/10.0
            ret.agregar_nodo(posicion_x_arco,0,round(posicion_z_arco,1))
            print(f'el nodo {j+85} = {posicion_x_arco} y {round(posicion_z_arco,1)}')
        else:
            posicion_x_arco+=7.5
            posicion_z_arco-=altura_puente/10.0
            ret.agregar_nodo(posicion_x_arco,0,round(posicion_z_arco,1))
            print(f'el nodo {j+85} = {posicion_x_arco} y {round(posicion_z_arco,1)}')
    
    
    posicion_x_arco=10
    posicion_z_arco=100       
    for i in range(nodos_mitad):
        if i==0:
            posicion_x_arco+=7.5
            posicion_z_arco+=altura_puente/10.0
            ret.agregar_nodo(posicion_x_arco,2,round(posicion_z_arco,1))
            # ret.agregar_nodo(posicion_x_arco,2,round(posicion_z_arco,1))
            print(f'el nodo {i+86} = {posicion_x_arco} y {round(posicion_z_arco,1)}')
            
        else:
            posicion_x_arco+=10
            posicion_z_arco+=altura_puente/10.0
            ret.agregar_nodo(posicion_x_arco,2,round(posicion_z_arco,1))
            # ret.agregar_nodo(posicion_x_arco,2,round(posicion_z_arco,1))
            print(f'el nodo {i+86} = {posicion_x_arco} y {round(posicion_z_arco,1)}')
    for j in range(nodos_mitad):
        if j!=nodos_mitad-1:
            posicion_x_arco+=10
            posicion_z_arco-=altura_puente/10.0
            ret.agregar_nodo(posicion_x_arco,2,round(posicion_z_arco,1))
            print(f'el nodo {j+96} = {posicion_x_arco} y {round(posicion_z_arco,1)}')
        else:
            posicion_x_arco+=7.5
            posicion_z_arco-=altura_puente/10.0
            ret.agregar_nodo(posicion_x_arco,2,round(posicion_z_arco,1))
            print(f'el nodo {j+96} = {posicion_x_arco} y {round(posicion_z_arco,1)}')
    # ret.agregar_nodo(10,0,100+altura_pilares)  # 74
    # ret.agregar_nodo(10,2,100+altura_pilares)  # 75
    # ret.agregar_nodo(225,0,100+altura_pilares) # 76
    # ret.agregar_nodo(225,2,100+altura_pilares) # 77
    # """
    # Nodos de anclaje  
    # """    
    # ret.agregar_nodo(-25,0,100) # 78
    # ret.agregar_nodo(-25,2,100) # 79
    # ret.agregar_nodo(-20,0,100) # 80
    # ret.agregar_nodo(-20,2,100) # 81
    # ret.agregar_nodo(-15,0,100) # 82
    # ret.agregar_nodo(-15,2,100) # 83
    # ret.agregar_nodo(-10,0,100) # 84
    # ret.agregar_nodo(-10,2,100) # 85
    # ret.agregar_nodo(-5,0,100)  # 86
    # ret.agregar_nodo(-5,2,100)  # 87
    # ret.agregar_nodo(0,0,100)   # 88
    # ret.agregar_nodo(0,2,100)   # 89
    # ret.agregar_nodo(5,0,100)   # 90
    # ret.agregar_nodo(5,2,100)   # 91
    
    # ret.agregar_nodo(230,0,100) # 92
    # ret.agregar_nodo(230,2,100) # 93
    # ret.agregar_nodo(235,0,100) # 94
    # ret.agregar_nodo(235,2,100) # 95
    # ret.agregar_nodo(240,0,100) # 96
    # ret.agregar_nodo(240,2,100) # 97
    # ret.agregar_nodo(245,0,100) # 98
    # ret.agregar_nodo(245,2,100) # 99
    # ret.agregar_nodo(250,0,100) # 100
    # ret.agregar_nodo(250,2,100) # 101
    # ret.agregar_nodo(255,0,100) # 102
    # ret.agregar_nodo(255,2,100) # 103
    
    
    # # ret.agregar_nodo(12.5+j*5,2,100+sqrt(25-(2.5**2)))
    # r = 20.0*cm
    # t = 40.0*mm 
    # """
    # REVISAR EN PROPS R,R DEBERIA SER R,T
    # """
    # props = [r, t, 200*GPa, 7600*kg/m**3, 420*MPa]
    # """
    # Barras calle
    # """
    
    # for k1 in range (nodos-1):
    #     ret.agregar_barra(Barra(k1, k1+1, *props))      # 1
    # for k2 in range (nodos,2*nodos-1):
    #     ret.agregar_barra(Barra(k2, k2+1, *props))      # 1
    # for k4 in range (nodos-1):
    #     ret.agregar_barra(Barra(k4+1, k4+nodos+1+1, *props))
    # """
    # Pilares
    # """
    # # Verticales
    # ret.agregar_barra(Barra(0, 74, *props))
    # ret.agregar_barra(Barra(37, 75, *props))
    # ret.agregar_barra(Barra(36, 76, *props))
    # ret.agregar_barra(Barra(73, 77, *props))
    # # Horizontales
    # ret.agregar_barra(Barra(74, 75, *props))
    # ret.agregar_barra(Barra(76, 77, *props))
    # """
    # Cacles Exteriores a Tierra
    # """
    # for i in range (7):
    #     ret.agregar_barra(Barra(4+74+i*2, 74, *props))
    # for j in range (7):
    #     ret.agregar_barra(Barra(4+75+j*2, 75, *props))
    
    # for k in range (6):
    #     ret.agregar_barra(Barra(92+k*2, 76, *props))
    # for f in range (6):
    #     ret.agregar_barra(Barra(93+f*2, 77, *props))

    # """
    # Cables Interiores a la calle
    # """
    # for i in range (18):
    #     ret.agregar_barra(Barra(74, i+1, *props))
    # for i in range (18):
    #     ret.agregar_barra(Barra(75, i+37+1, *props))
    # for i in range (18):
    #     ret.agregar_barra(Barra(76, 18+i, *props))
    # for i in range (18):
    #     ret.agregar_barra(Barra(77, 18+37+i, *props))
    
    # """
    #     for k5 in range (nodos-1):
    #         ret.agregar_barra(Barra(k5*3, k5*2+nodos*2+1, *props))
    #         ret.agregar_barra(Barra(k5*2+nodos*2+1,k5*3+3, *props))
            
    #     for k6 in range (nodos-1):
    #         ret.agregar_barra(Barra(k6*3+nodos, k6*2+nodos*2+1, *props))
    #         ret.agregar_barra(Barra(k6*2+nodos*2+1,k6*3+nodos+3, *props))
    # """
    
    
    
    
    # # for k2 in range(nodos,2*nodos-1):
    # #     ret.agregar_barra(Barra(k2, k2+2, *props))
        
    # # nodos=47
    # # for i in range (nodos):
    # #     ret.agregar_nodo(10+i*5,0,100) 
    
    # #Nodos

    
    # # ret.agregar_nodo(10, 0, 100)       #7 inicio
    # # ret.agregar_nodo(10, 2, 100)       #7' inicio
    
    # # ret.agregar_nodo(225, 0, 100)       #28 fin
    # # ret.agregar_nodo(225, 2, 100)       #28' fin
    

    
    
    # #Barras
    # """
    # PREGUNTAR, PARECIERA SER QUE ES UNA BARRA CUADRADA
    # """
    # # A = (8*cm)**2
    # # r = sqrt(A/3.141593)
    # r = 8.0*cm
    # t = 5.0*mm 
    # """
    # REVISAR EN PROPS R,R DEBERIA SER R,T
    # """
    # """
    # props = [r, t, 200*GPa, 7600*kg/m**3, 420*MPa]
    # for k1 in range (nodos-1):
    #     ret.agregar_barra(Barra(k1, k1+1, *props))      # 1
    # for k2 in range(nodos,2*nodos-1)
    #     ret.agregar_barra(Barra(k2, k2+1, *props))      # 1
        
    # ret.agregar_barra(Barra(0, 1, *props))      # 1
    # ret.agregar_barra(Barra(1, 2, *props))      # 2
    # ret.agregar_barra(Barra(2, 3, *props))      # 3
    # ret.agregar_barra(Barra(3, 10, *props))     # 4
    # ret.agregar_barra(Barra(9, 10, *props))     # 5
    # ret.agregar_barra(Barra(8, 9, *props))      # 6
    # ret.agregar_barra(Barra(7, 8, *props))      # 7
    # ret.agregar_barra(Barra(0, 7, *props))      # 8
    # ret.agregar_barra(Barra(1, 7, *props))      # 9
    # ret.agregar_barra(Barra(0, 8, *props))      # 10
    # ret.agregar_barra(Barra(1, 8, *props))      # 11
    # ret.agregar_barra(Barra(2, 8, *props))      # 12
    # ret.agregar_barra(Barra(1, 9, *props))      # 13
    # ret.agregar_barra(Barra(2, 9, *props))      # 14
    # ret.agregar_barra(Barra(3, 9, *props))      # 15
    # ret.agregar_barra(Barra(2, 10, *props))     # 16
    # ret.agregar_barra(Barra(4, 7, *props))      # 17
    # ret.agregar_barra(Barra(0, 4, *props))      # 18
    # ret.agregar_barra(Barra(4, 8, *props))      # 19
    # ret.agregar_barra(Barra(1, 4, *props))      # 20
    # ret.agregar_barra(Barra(5, 8, *props))      # 21
    # ret.agregar_barra(Barra(1, 5, *props))      # 22
    # ret.agregar_barra(Barra(5, 9, *props))      # 23
    # ret.agregar_barra(Barra(2, 5, *props))      # 24
    # ret.agregar_barra(Barra(6, 9, *props))      # 25
    # ret.agregar_barra(Barra(2, 6, *props))      # 26
    # ret.agregar_barra(Barra(6, 10, *props))     # 27
    # ret.agregar_barra(Barra(3, 6, *props))      # 28
    # ret.agregar_barra(Barra(4, 5, *props))      # 29
    # ret.agregar_barra(Barra(5, 6, *props))      # 30
    
    # """
    # # nodo 0
    # ret.agregar_restriccion(0, 0, 0)
    # ret.agregar_restriccion(0, 1, 0)
    # ret.agregar_restriccion(0, 2, 0)
    # # nodo 36 
    # ret.agregar_restriccion(nodos, 0, 0)
    # ret.agregar_restriccion(nodos, 1, 0)
    # ret.agregar_restriccion(nodos, 2, 0)
    # # nodo 37
    # ret.agregar_restriccion(nodos+1, 0, 0)
    # ret.agregar_restriccion(nodos+1, 1, 0)
    # ret.agregar_restriccion(nodos+1, 2, 0)
    
    # # nodo 73
    # ret.agregar_restriccion(nodos*2+1, 0, 0)
    # ret.agregar_restriccion(nodos*2+1, 1, 0)
    # ret.agregar_restriccion(nodos*2+1, 2, 0) 
    
    # for i in range(78,104):
    #     ret.agregar_restriccion(i, 0, 0)
    #     ret.agregar_restriccion(i, 1, 0)
    #     ret.agregar_restriccion(i, 2, 0) 
    
        
    return ret