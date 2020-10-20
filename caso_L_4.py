# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 20:06:25 2020

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
    
    #Parametros
    L = 5.0  *m
    F = 100*KN
    B = 2.0 *m
    #Parametros cargas vivas
    Q=400*(kg/(m**2))
    g=9.8*(m/(s**2))
    A0=3*(m**2)
    A1=6*(m**2)
    A2=5.75*(m**2)
    A3=5.5*(m**2)
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
            print(f'AA nodo {i}:{10+i*factor-floor(siguiente_1)}')
        else:
            
            ret.agregar_nodo(10+i*factor-siguiente_1,0,100)
            print(f'BB nodo {i}:{10+i*factor-siguiente_1}')
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
    Nodos 
    """


    ret.agregar_nodo(22.0,1,107.5025) #74
    ret.agregar_nodo(34.0,0,106.6626)
    ret.agregar_nodo(34.0,1,113.8474)
    ret.agregar_nodo(46.0,0,112.2212)
    ret.agregar_nodo(46.0,1,119.1587)
    ret.agregar_nodo(58.0,0,116.7813)
    ret.agregar_nodo(58.0,1,123.5269) #80
    ret.agregar_nodo(70.0,0,120.4193)
    ret.agregar_nodo(70.0,1,127.0186)
    ret.agregar_nodo(82.0,0,123.1911)
    ret.agregar_nodo(82.0,1,129.6824)
    ret.agregar_nodo(94.0,0,125.1358)
    ret.agregar_nodo(94.0,1,131.5533)
    ret.agregar_nodo(106.0,0,126.2798)
    ret.agregar_nodo(106.0,1,132.6546)
    ret.agregar_nodo(117.5,0,126.6385)
    ret.agregar_nodo(117.5,1,133.0) #90
    ret.agregar_nodo(129.0,0,126.2798)
    ret.agregar_nodo(129.0,1,132.6546)
    ret.agregar_nodo(141.0,0,125.1358)
    ret.agregar_nodo(141.0,1,131.5533)
    ret.agregar_nodo(153.0,0,123.1911)
    ret.agregar_nodo(153.0,1,129.6824)
    ret.agregar_nodo(165.0,0,120.4193)
    ret.agregar_nodo(165.0,1,127.0186)
    ret.agregar_nodo(177.0,0,116.7813)
    ret.agregar_nodo(177.0,1,123.5269) #100
    ret.agregar_nodo(189.0,0,112.2212)
    ret.agregar_nodo(189.0,1,119.1587)
    ret.agregar_nodo(201.0,0,106.6626)
    ret.agregar_nodo(201.0,1,113.8474)
    ret.agregar_nodo(213.0,1,107.5025) #105
    
    ret.agregar_nodo(34.0,2,106.6626) #106
    ret.agregar_nodo(46.0,2,112.2212)
    ret.agregar_nodo(58.0,2,116.7813)
    ret.agregar_nodo(70.0,2,120.4193)
    ret.agregar_nodo(82.0,2,123.1911) #110
    ret.agregar_nodo(94.0,2,125.1358)
    ret.agregar_nodo(106.0,2,126.2798)
    ret.agregar_nodo(117.5,2,126.6385)
    ret.agregar_nodo(129.0,2,126.2798)
    ret.agregar_nodo(141.0,2,125.1358)
    ret.agregar_nodo(153.0,2,123.1911)
    ret.agregar_nodo(165.0,2,120.4193)
    ret.agregar_nodo(177.0,2,116.7813)
    ret.agregar_nodo(189.0,2,112.2212)
    ret.agregar_nodo(201.0,2,106.6626) #120

    
    
    """
    Barras calle
    """
    r = 20.0*cm
    t = 40.0*mm 
    """
    REVISAR EN PROPS R,R DEBERIA SER R,T
    """
    props = [r, t, 200*GPa, 7600*kg/m**3, 420*MPa]
    # Horizontales
    for k1 in range (nodos-1):
        ret.agregar_barra(Barra(k1, k1+1, *props))      # 1
    for k2 in range (nodos,2*nodos-1):
        ret.agregar_barra(Barra(k2, k2+1, *props))      # 1
    # Verticales
    for k4 in range (nodos-2):
        ret.agregar_barra(Barra(k4+1, k4+nodos+1, *props))
    # Diagonales
    for i in range (18):
        ret.agregar_barra(Barra(i, i+38, *props))
        ret.agregar_barra(Barra(i+55,i+19 , *props))
    # arco1 parte en 75
    for i in range(16):
        if i ==0:
            ret.agregar_barra(Barra(i+2, i+75, *props))
        elif i==15:
            ret.agregar_barra(Barra(103, 34, *props))  
        else:
            ret.agregar_barra(Barra((i-1)*2+75, i*2+75, *props))
    # arco2 parte en 74
    for i in range(17):
        if i ==0:
            # ret.agregar_barra(Barra(i+2, i+74, *props))
            a=2
        elif i==16:
            ret.agregar_barra(Barra(104, 105, *props))            
        else:
            ret.agregar_barra(Barra((i-1)*2+74, i*2+74, *props))
        
    # arco3 
    for i in range(16):
        if i ==0:
            ret.agregar_barra(Barra(i+39, i+106, *props))
        elif i==15:
            ret.agregar_barra(Barra(120, 71, *props))
        else:
            ret.agregar_barra(Barra(i+106-1, i+106, *props))
    # Horizontales arco1 y arco3
    for i in range (15):
        ret.agregar_barra(Barra(i*2+75, i+106, *props))
    # diagonales tablero de arco
    for i in range(8):
        if i ==0:
            ret.agregar_barra(Barra(i+39, i+75, *props))
        else:
            ret.agregar_barra(Barra(i+105, i*2+75, *props))
    for i in range(8):
        if i ==0:
            ret.agregar_barra(Barra(i+89, i+114, *props))
        elif i==7:
            ret.agregar_barra(Barra(103, 71, *props))
        else:
            ret.agregar_barra(Barra(i*2+89, i+114, *props))
    # triangulo arco
    for i in range(17):
        if i ==0:
            ret.agregar_barra(Barra(i+2, i+74, *props))
            ret.agregar_barra(Barra(i+39, i+74, *props))
        elif i==16:
            ret.agregar_barra(Barra(105, 34, *props))
            ret.agregar_barra(Barra(105, 71, *props))
        else:
            ret.agregar_barra(Barra(i*2+73, i*2+74, *props))
            ret.agregar_barra(Barra(i+105, i*2+74, *props))

    ret.agregar_barra(Barra(0, 74, *props))            
    ret.agregar_barra(Barra(1, 74, *props))
    ret.agregar_barra(Barra(37, 74, *props))
    ret.agregar_barra(Barra(38, 74, *props))
    
    ret.agregar_barra(Barra(35, 105, *props))            
    ret.agregar_barra(Barra(36, 105, *props))
    ret.agregar_barra(Barra(72, 105, *props))
    ret.agregar_barra(Barra(73, 105, *props))
    
    
    
    # Diagonales arco
    for i in range(8):
        if i ==0:
            ret.agregar_barra(Barra(i+74, i+75, *props))
            ret.agregar_barra(Barra(i+74, i+106, *props))
            
        else:
            ret.agregar_barra(Barra(i*2+74, i*2+75, *props))
            ret.agregar_barra(Barra(i*2+74, i+106, *props))
            
    for i in range(8):
        if i ==0:
            ret.agregar_barra(Barra(i+89, i+92, *props))
            ret.agregar_barra(Barra(i+113, i+92, *props))
            
        elif i==7:
            ret.agregar_barra(Barra(103, 105, *props))
            ret.agregar_barra(Barra(120, 105, *props))
        else:
            ret.agregar_barra(Barra(i*2+89, i*2+92, *props))
            ret.agregar_barra(Barra(i+113, i*2+92, *props))
    # Cables lado 1
    for i in range (15):
        if i==0:
            ret.agregar_barra(Barra(i*2+75, i*3+3, *props))
            ret.agregar_barra(Barra(i*2+75, i*3+4, *props))
            ret.agregar_barra(Barra(i*2+75, i*3+5, *props))
        else:
            ret.agregar_barra(Barra(i*2+75, i*2+3, *props))
            ret.agregar_barra(Barra(i*2+75, i*2+4, *props))
            ret.agregar_barra(Barra(i*2+75, i*2+5, *props))
    # Cables lado 2
    for i in range (15):
        if i==0:
            ret.agregar_barra(Barra(i+106, i*3+3+37, *props))
            ret.agregar_barra(Barra(i+106, i*3+4+37, *props))
            ret.agregar_barra(Barra(i+106, i*3+5+37, *props))
        else:
            ret.agregar_barra(Barra(i+106, i*2+3+37, *props))
            ret.agregar_barra(Barra(i+106, i*2+4+37, *props))
            ret.agregar_barra(Barra(i+106, i*2+5+37, *props))
    
    
    
    
    
    
    
    
    # Carga viva en nodos 
    ret.agregar_fuerza(0, 2, -Q*A0*g)
    ret.agregar_fuerza(36, 2, -Q*A0*g)
    ret.agregar_fuerza(37, 2, -Q*A0*g)
    ret.agregar_fuerza(73, 2, -Q*A0*g)
    
    for i in range (1,17):
        ret.agregar_fuerza(i, 2, -Q*A1*g)
    
    ret.agregar_fuerza(17, 2, -Q*A2*g)
    ret.agregar_fuerza(18, 2, -Q*A3*g)
    ret.agregar_fuerza(19, 2, -Q*A2*g)
    
    for i in range (20,36):
        ret.agregar_fuerza(i, 2, -Q*A1*g)
    
    for i in range (38,54):
        ret.agregar_fuerza(i, 2, -Q*A1*g)
    
    ret.agregar_fuerza(54, 2, -Q*A2*g)
    ret.agregar_fuerza(55, 2, -Q*A3*g)
    ret.agregar_fuerza(56, 2, -Q*A2*g)
    
    for i in range (57,73):
        ret.agregar_fuerza(i, 2, -Q*A1*g)

    # nodo 0
    ret.agregar_restriccion(0, 0, 0)
    ret.agregar_restriccion(0, 1, 0)
    ret.agregar_restriccion(0, 2, 0)
    # nodo 36 
    ret.agregar_restriccion(36, 0, 0)
    ret.agregar_restriccion(36, 1, 0)
    ret.agregar_restriccion(36, 2, 0)
    # nodo 37
    ret.agregar_restriccion(37, 0, 0)
    ret.agregar_restriccion(37, 1, 0)
    ret.agregar_restriccion(37, 2, 0)
    
    # nodo 73
    ret.agregar_restriccion(73, 0, 0)
    ret.agregar_restriccion(73, 1, 0)
    ret.agregar_restriccion(73, 2, 0) 
    
    return ret