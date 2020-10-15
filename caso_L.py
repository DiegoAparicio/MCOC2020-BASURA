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
    Q=400*(kg/(m**2))
    g=9.81*(m/(s**2))
    A0=2.5*(m**2)
    A1=5*(m**2)
    
    #Inicializar modelo
    ret = Reticulado()
    nodos=47
    for i in range (nodos):
        ret.agregar_nodo(10+i*5,0,100)
    for l in range(nodos):
        ret.agregar_nodo(10+l*5,2,100)
    for j in range (nodos-1):
        ret.agregar_nodo(12.5+j*5,0,100+sqrt(25-(2.5**2)))
    for j in range (nodos-1):
        ret.agregar_nodo(12.5+j*5,2,100+sqrt(25-(2.5**2)))
        # ret.agregar_nodo(10+i*5,2,100)
    # for j in range (nodos-1):
    #     ret.agregar_nodo(12.5+j*5,0,100+sqrt(25-(2.5**2)))
        # ret.agregar_nodo(12.5+j*5,2,100+sqrt(25-(2.5**2)))
    r = 8.0*cm
    t = 5.0*mm 
    """
    REVISAR EN PROPS R,R DEBERIA SER R,T
    """
    props = [r, t, 200*GPa, 7600*kg/m**3, 420*MPa]
    for k1 in range (nodos-1):
        ret.agregar_barra(Barra(k1, k1+1, *props))      # 1
    for k2 in range (nodos,2*nodos-1):
        ret.agregar_barra(Barra(k2, k2+1, *props))      # 1
    for k3 in range (2*nodos+2,3*nodos-2):
        ret.agregar_barra(Barra(k3, k3+1, *props))      # 1
    for k4 in range (3*nodos+1,4*nodos-1):
        ret.agregar_barra(Barra(k4, k4+1, *props)) 
    # for k2 in range(nodos,2*nodos-1):
    #     ret.agregar_barra(Barra(k2, k2+2, *props))
    
    
    # nodo 1
    ret.agregar_restriccion(0, 0, 0)
    ret.agregar_restriccion(0, 1, 0)
    ret.agregar_restriccion(0, 2, 0)
    # nodo 7 
    ret.agregar_restriccion(7, 0, 0)
    ret.agregar_restriccion(7, 1, 0)
    ret.agregar_restriccion(7, 2, 0)
    # nodo 3
    ret.agregar_restriccion(3, 1, 0)
    ret.agregar_restriccion(3, 2, 0)
    
    # nodo 10
    ret.agregar_restriccion(10, 1, 0)
    ret.agregar_restriccion(10, 2, 0)
    
    # Carga viva en nodos 
    # ret.agregar_fuerza(0, 2, -Q*A0*g)
    # ret.agregar_fuerza(7, 2, -Q*A0*g)
    # ret.agregar_fuerza(3, 2, -Q*A0*g)
    # ret.agregar_fuerza(10, 2, -Q*A0*g)
    
    # ret.agregar_fuerza(1, 2, -Q*A1*g)
    # ret.agregar_fuerza(2, 2, -Q*A1*g)
    # ret.agregar_fuerza(8, 2, -Q*A1*g)
    # ret.agregar_fuerza(9, 2, -Q*A1*g)
     # nodo 1
    ret.agregar_restriccion(0, 0, 0)
    ret.agregar_restriccion(0, 1, 0)
    ret.agregar_restriccion(0, 2, 0)
    # nodo 46 
    ret.agregar_restriccion(nodos-1, 0, 0)
    ret.agregar_restriccion(nodos-1, 1, 0)
    ret.agregar_restriccion(nodos-1, 2, 0)
    # nodo 47
    ret.agregar_restriccion(nodos, 0, 0)
    ret.agregar_restriccion(nodos, 1, 0)
    ret.agregar_restriccion(nodos, 2, 0)
    
    # nodo 10
    ret.agregar_restriccion(2*nodos-1, 0, 0)
    ret.agregar_restriccion(2*nodos-1, 1, 0)
    ret.agregar_restriccion(2*nodos-1, 2, 0)    

    return ret












