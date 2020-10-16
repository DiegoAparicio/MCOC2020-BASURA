# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 11:56:45 2020

@author: jpsil
"""


from reticulado import Reticulado
from barra import Barra
from numpy import *
from math import *

 
def caso_D():
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
    nodos=30
    contador=0
    altura1=sqrt(25-(2.5**2))
    altura2=30
    for i in range (nodos):
        contador+=1
        ret.agregar_nodo(10+i*5,0,100)
    contador1=contador   
    for l in range(nodos):
        ret.agregar_nodo(10+l*5,2,100)
        contador+=1
    contador2=contador
    for j in range (nodos-1):
        contador+=1
        ret.agregar_nodo(12.5+j*5,1,100+altura2)

            
    contador3=contador
        # ret.agregar_nodo(12.5+j*5,2,100+sqrt(25-(2.5**2)))
    r = 15.0*cm
    t = 50.0*mm 
    """
    REVISAR EN PROPS R,R DEBERIA SER R,T
    """
    props = [r, t, 200*GPa, 7600*kg/m**3, 420*MPa]
    for k1 in range (nodos-1):
        ret.agregar_barra(Barra(k1, k1+1, *props))      # 1
    for k2 in range (nodos,2*nodos-1):
        ret.agregar_barra(Barra(k2, k2+1, *props))      # 1
    for k3 in range (2*nodos,3*nodos-2):
        ret.agregar_barra(Barra(k3, k3+1, *props))      # 1

    for k4 in range (nodos-2):
        ret.agregar_barra(Barra(k4+1, k4+nodos+1, *props))
    
    for k5 in range (nodos-1):
        ret.agregar_barra(Barra(k5, k5+nodos*2, *props))
        ret.agregar_barra(Barra(k5+nodos*2,k5+1, *props))
        
    for k6 in range (nodos-1):
        ret.agregar_barra(Barra(k6+nodos, k6+nodos*2, *props))
        ret.agregar_barra(Barra(k6+nodos*2,k6+nodos+1, *props))
    
    """
        for k5 in range (nodos-1):
            ret.agregar_barra(Barra(k5*3, k5*2+nodos*2+1, *props))
            ret.agregar_barra(Barra(k5*2+nodos*2+1,k5*3+3, *props))
            
        for k6 in range (nodos-1):
            ret.agregar_barra(Barra(k6*3+nodos, k6*2+nodos*2+1, *props))
            ret.agregar_barra(Barra(k6*2+nodos*2+1,k6*3+nodos+3, *props))
    """
    
    
    
    
    # for k2 in range(nodos,2*nodos-1):
    #     ret.agregar_barra(Barra(k2, k2+2, *props))
        
    # nodos=47
    # for i in range (nodos):
    #     ret.agregar_nodo(10+i*5,0,100) 
    
    #Nodos

    
    # ret.agregar_nodo(10, 0, 100)       #7 inicio
    # ret.agregar_nodo(10, 2, 100)       #7' inicio
    
    # ret.agregar_nodo(225, 0, 100)       #28 fin
    # ret.agregar_nodo(225, 2, 100)       #28' fin
    

    
    
    #Barras
    """
    PREGUNTAR, PARECIERA SER QUE ES UNA BARRA CUADRADA
    """
    # A = (8*cm)**2
    # r = sqrt(A/3.141593)
    r = 8.0*cm
    t = 5.0*mm 
    """
    REVISAR EN PROPS R,R DEBERIA SER R,T
    """
    """
    props = [r, t, 200*GPa, 7600*kg/m**3, 420*MPa]
    for k1 in range (nodos-1):
        ret.agregar_barra(Barra(k1, k1+1, *props))      # 1
    for k2 in range(nodos,2*nodos-1)
        ret.agregar_barra(Barra(k2, k2+1, *props))      # 1
        
    ret.agregar_barra(Barra(0, 1, *props))      # 1
    ret.agregar_barra(Barra(1, 2, *props))      # 2
    ret.agregar_barra(Barra(2, 3, *props))      # 3
    ret.agregar_barra(Barra(3, 10, *props))     # 4
    ret.agregar_barra(Barra(9, 10, *props))     # 5
    ret.agregar_barra(Barra(8, 9, *props))      # 6
    ret.agregar_barra(Barra(7, 8, *props))      # 7
    ret.agregar_barra(Barra(0, 7, *props))      # 8
    ret.agregar_barra(Barra(1, 7, *props))      # 9
    ret.agregar_barra(Barra(0, 8, *props))      # 10
    ret.agregar_barra(Barra(1, 8, *props))      # 11
    ret.agregar_barra(Barra(2, 8, *props))      # 12
    ret.agregar_barra(Barra(1, 9, *props))      # 13
    ret.agregar_barra(Barra(2, 9, *props))      # 14
    ret.agregar_barra(Barra(3, 9, *props))      # 15
    ret.agregar_barra(Barra(2, 10, *props))     # 16
    ret.agregar_barra(Barra(4, 7, *props))      # 17
    ret.agregar_barra(Barra(0, 4, *props))      # 18
    ret.agregar_barra(Barra(4, 8, *props))      # 19
    ret.agregar_barra(Barra(1, 4, *props))      # 20
    ret.agregar_barra(Barra(5, 8, *props))      # 21
    ret.agregar_barra(Barra(1, 5, *props))      # 22
    ret.agregar_barra(Barra(5, 9, *props))      # 23
    ret.agregar_barra(Barra(2, 5, *props))      # 24
    ret.agregar_barra(Barra(6, 9, *props))      # 25
    ret.agregar_barra(Barra(2, 6, *props))      # 26
    ret.agregar_barra(Barra(6, 10, *props))     # 27
    ret.agregar_barra(Barra(3, 6, *props))      # 28
    ret.agregar_barra(Barra(4, 5, *props))      # 29
    ret.agregar_barra(Barra(5, 6, *props))      # 30
    
    """
    # nodo 0
    ret.agregar_restriccion(0, 0, 0)
    ret.agregar_restriccion(0, 1, 0)
    ret.agregar_restriccion(0, 2, 0)
    # nodo 42 
    ret.agregar_restriccion(nodos-1, 0, 0)
    ret.agregar_restriccion(nodos-1, 1, 0)
    ret.agregar_restriccion(nodos-1, 2, 0)
    # nodo 43
    ret.agregar_restriccion(nodos, 0, 0)
    ret.agregar_restriccion(nodos, 1, 0)
    ret.agregar_restriccion(nodos, 2, 0)
    
    # nodo 85
    ret.agregar_restriccion(nodos*2-1, 0, 0)
    ret.agregar_restriccion(nodos*2-1, 1, 0)
    ret.agregar_restriccion(nodos*2-1, 2, 0)    
    return ret

