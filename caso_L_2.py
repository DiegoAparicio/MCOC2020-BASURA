# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 11:58:10 2020

@author: jpsil
"""


from reticulado import Reticulado
from barra import Barra
from numpy import *
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
    # L = 5.0  *m
    # F = 100*KN
    # B = 2.0 *m
    #Parametros cargas vivas
    nodos=36
    factor=215.0/nodos
    
    Q=400*(kg/(m**2))
    g=9.81*(m/(s**2))
    A0=(factor/2)*(m**2)
    A1=factor*(m**2)
    
    #Inicializar modelo
    ret = Reticulado()
    nodos=36
    factor=215.0/nodos
    altura2=sqrt(25-(2.5**2))
    altura2=20.
    altura_pilares=20.
    """
    Nodos calle
    """
    for i in range (nodos+1):
        ret.agregar_nodo(10+i*factor,0,100) # nodos 0-36  
    for l in range(nodos+1):
        ret.agregar_nodo(10+l*factor,2,100) # nodos 37-73
    
    
    """
    Nodos Pilares
    """
    ret.agregar_nodo(10,0,100+altura_pilares)  # 74
    ret.agregar_nodo(10,2,100+altura_pilares)  # 75
    ret.agregar_nodo(225,0,100+altura_pilares) # 76
    ret.agregar_nodo(225,2,100+altura_pilares) # 77
    """
    Nodos de anclaje  
    """    
    ret.agregar_nodo(-25,0,100) # 78
    ret.agregar_nodo(-25,2,100) # 79
    ret.agregar_nodo(-20,0,100) # 80
    ret.agregar_nodo(-20,2,100) # 81
    ret.agregar_nodo(-15,0,100) # 82
    ret.agregar_nodo(-15,2,100) # 83
    ret.agregar_nodo(-10,0,100) # 84
    ret.agregar_nodo(-10,2,100) # 85
    ret.agregar_nodo(-5,0,100)  # 86
    ret.agregar_nodo(-5,2,100)  # 87
    ret.agregar_nodo(0,0,100)   # 88
    ret.agregar_nodo(0,2,100)   # 89
    ret.agregar_nodo(5,0,100)   # 90
    ret.agregar_nodo(5,2,100)   # 91
    
    ret.agregar_nodo(230,0,100) # 92
    ret.agregar_nodo(230,2,100) # 93
    ret.agregar_nodo(235,0,100) # 94
    ret.agregar_nodo(235,2,100) # 95
    ret.agregar_nodo(240,0,100) # 96
    ret.agregar_nodo(240,2,100) # 97
    ret.agregar_nodo(245,0,100) # 98
    ret.agregar_nodo(245,2,100) # 99
    ret.agregar_nodo(250,0,100) # 100
    ret.agregar_nodo(250,2,100) # 101
    ret.agregar_nodo(255,0,100) # 102
    ret.agregar_nodo(255,2,100) # 103
    
    
    # ret.agregar_nodo(12.5+j*5,2,100+sqrt(25-(2.5**2)))
    r = 20.0*cm
    t = 40.0*mm 
    """
    REVISAR EN PROPS R,R DEBERIA SER R,T
    """
    props = [r, t, 200*GPa, 7600*kg/m**3, 420*MPa]
    """
    Barras calle
    """
    
    for k1 in range (nodos-1):
        ret.agregar_barra(Barra(k1, k1+1, *props))      # 1
    for k2 in range (nodos,2*nodos-1):
        ret.agregar_barra(Barra(k2, k2+1, *props))      # 1
    for k4 in range (nodos-1):
        ret.agregar_barra(Barra(k4+1, k4+nodos+1+1, *props))
    """
    Pilares
    """
    # Verticales
    ret.agregar_barra(Barra(0, 74, *props))
    ret.agregar_barra(Barra(37, 75, *props))
    ret.agregar_barra(Barra(36, 76, *props))
    ret.agregar_barra(Barra(73, 77, *props))
    # Horizontales
    ret.agregar_barra(Barra(74, 75, *props))
    ret.agregar_barra(Barra(76, 77, *props))
    """
    Cacles Exteriores a Tierra
    """
    for i in range (7):
        ret.agregar_barra(Barra(4+74+i*2, 74, *props))
    for j in range (7):
        ret.agregar_barra(Barra(4+75+j*2, 75, *props))
    
    for k in range (6):
        ret.agregar_barra(Barra(92+k*2, 76, *props))
    for f in range (6):
        ret.agregar_barra(Barra(93+f*2, 77, *props))

    """
    Cables Interiores a la calle
    """
    for i in range (18):
        ret.agregar_barra(Barra(74, i+1, *props))
    for i in range (18):
        ret.agregar_barra(Barra(75, i+37+1, *props))
    for i in range (18):
        ret.agregar_barra(Barra(76, 18+i, *props))
    for i in range (18):
        ret.agregar_barra(Barra(77, 18+37+i, *props))
    
    # Carga viva en nodos 
    ret.agregar_fuerza(0, 2, -Q*A0*g)
    ret.agregar_fuerza(nodos, 2, -Q*A0*g)
    ret.agregar_fuerza(nodos+1, 2, -Q*A0*g)
    ret.agregar_fuerza(nodos*2+1, 2, -Q*A0*g)
    
    for i in range (1,nodos):
        ret.agregar_fuerza(i, 2, -Q*A1*g)
    for j in range(nodos+2,nodos*2+1):
        ret.agregar_fuerza(j, 2, -Q*A1*g)
    # ret.agregar_fuerza(1, 2, -Q*A1*g)
    # ret.agregar_fuerza(2, 2, -Q*A1*g)
    # ret.agregar_fuerza(8, 2, -Q*A1*g)
    # ret.agregar_fuerza(9, 2, -Q*A1*g)
     # nodo 1
    # nodo 0
    ret.agregar_restriccion(0, 0, 0)
    ret.agregar_restriccion(0, 1, 0)
    ret.agregar_restriccion(0, 2, 0)
    # nodo 36 
    ret.agregar_restriccion(nodos, 0, 0)
    ret.agregar_restriccion(nodos, 1, 0)
    ret.agregar_restriccion(nodos, 2, 0)
    # nodo 37
    ret.agregar_restriccion(nodos+1, 0, 0)
    ret.agregar_restriccion(nodos+1, 1, 0)
    ret.agregar_restriccion(nodos+1, 2, 0)
    
    # nodo 73
    ret.agregar_restriccion(nodos*2+1, 0, 0)
    ret.agregar_restriccion(nodos*2+1, 1, 0)
    ret.agregar_restriccion(nodos*2+1, 2, 0) 
    
    for i in range(78,104):
        ret.agregar_restriccion(i, 0, 0)
        ret.agregar_restriccion(i, 1, 0)
        ret.agregar_restriccion(i, 2, 0) 
              

    return ret












