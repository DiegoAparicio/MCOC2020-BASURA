# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 20:17:14 2020

@author: jpsil
"""


archivo=open("Nodos_Puente.txt","r")
contador=0
for i in archivo:
    
    lista=i.split()
    x=str(lista[1])
    x=x.replace(',','.')
    x=float(x)
    
    y=str(lista[3])
    y=y.replace(',','.')
    y=float(y)
    if contador%2==0:
        print(f'ret.agregar_nodo({x},2,{y})')
    # else:
    #     print(f'ret.agregar_nodo({x},1,{y})')
    contador+=1
    
    

