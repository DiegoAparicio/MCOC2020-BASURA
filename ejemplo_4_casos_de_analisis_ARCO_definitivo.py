# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 20:07:21 2020

@author: jpsil
"""


from caso_D_4 import caso_D
from caso_L_4 import caso_L
from graficar3d import ver_reticulado_3d
import itertools
from operator import itemgetter
from numpy import *
import matplotlib.pyplot as plt
ret_D = caso_D()
ret_L = caso_L()
#Casos optimizados
ret_D_muerto = caso_D()
ret_D_vivo_muerto = caso_D()
ret_D_5_barras = caso_D()
factor_a=30.0
numero_de_grafica=7
ver_reticulado_3d(ret_D, 
	axis_Equal=True, 
	opciones_barras={
	"ver_numeros_de_barras": False
	}, 
    llamar_show=True,
    zoom=900.,
    deshabilitar_ejes=True)
peso=ret_D.calcular_peso_total()
plt.title(f"Grafica_{numero_de_grafica}_Estructura \n Peso: {peso} [N]")
# plt.savefig("C:/Users/jpsil/Documents/Universidad de los Andes/Universidad 2020 octavo semestre/MCOC/Proyecto 3/Imagenes informe/ Primer_Gráfico_1_4D.PNG")

#Peso propio
ret_D.ensamblar_sistema()
ret_D.resolver_sistema()
ret_D_muerto.ensamblar_sistema()
ret_D_muerto.resolver_sistema()
ret_D_vivo_muerto.ensamblar_sistema()
ret_D_vivo_muerto.resolver_sistema()
ret_D_5_barras.ensamblar_sistema()
ret_D_5_barras.resolver_sistema()

f_D = ret_D.recuperar_fuerzas()
f_D_muerto = ret_D_muerto.recuperar_fuerzas()
f_D_vivo_muerto = ret_D_vivo_muerto.recuperar_fuerzas()
f_D_5_barras = ret_D_5_barras.recuperar_fuerzas()

#Carga Viva
ret_L.ensamblar_sistema()
ret_L.resolver_sistema()
f_L = ret_L.recuperar_fuerzas()
#Combinaciones de carga
f_1 = 1.4*f_D           #Combinacion 1
f_2 = 1.2*f_D + 1.6*f_L #Combinacion 2
f_3_D_muerto = 1.4*f_D_muerto
f_4_D_vivo_muerto = 1.2*f_D_vivo_muerto + 1.6*f_L
f_5_D_5_barras = 1.2*f_D_5_barras + 1.6*f_L

# Calcular factores 
FU_caso1 = ret_D.recuperar_factores_de_utilizacion(f_1)
FU_caso2 = ret_D.recuperar_factores_de_utilizacion(f_2)

lista_max_Fu=[]
for i in range (len(f_1)):
    a=max([abs(f_1[i]),abs(f_2[i])])
    if abs(f_1[i]) > abs(f_2[i]):
        a=f_1[i]
    else:
        a=f_2[i]
    lista_max_Fu.append(a)
# for i in range(len(lista_max_Fu)):
    # print(f_1[i],f_2[i],"    ",lista_max_Fu[i])


FU_caso_general=ret_D.recuperar_factores_de_utilizacion(lista_max_Fu)

cumple_combinacion_1 = ret_D.chequear_diseño(f_1)
cumple_combinacion_2 = ret_L.chequear_diseño(f_2)

condicion_1=""
condicion_2=""

if cumple_combinacion_1:
    condicion_1="Combinación de carga 1 : cumple "
else:
    condicion_1="Combinación de carga 1 : NO cumple "
    
if cumple_combinacion_2:
    condicion_2="Combinación de carga 2 : cumple "
else:
    condicion_2="Combinación de carga 2 :NO cumple "
"""



peso_D = ret_D.calcular_peso_total()
peso_L = ret_L.calcular_peso_total()



"""





# CASO 1
ver_reticulado_3d(ret_D, 
    opciones_nodos = {
        "usar_posicion_deformada": True,
        "factor_amplificacion_deformada": factor_a,
        "datos_desplazamientos_nodales":ret_D.u*1.4,
    },
    opciones_barras = {
        "color_barras_por_dato": True,
        "ver_numeros_de_barras": False,
        "ver_dato_en_barras": False,
        "dato": f_1,
        "color_fondo": [1,1,1,0.4]
    }, 
    llamar_show=False,
    zoom=180.,
    deshabilitar_ejes=True)

plt.suptitle("Tensiones en caso 1: 1.4 D ")

plt.title(f"El desplazamiento máximo es: {round(1000*min(ret_D.u*1.4),3)} [mm]\n {condicion_1}")

# ret_D_desplazamientos_max=sorted(ret_D.desplazamientos_verticales, key=itemgetter(1))[0]
# plt.title(f'Desplazamiento maximo en el nodo {ret_D_desplazamientos_max[0]}: {round(ret_D_desplazamientos_max[1]*1000,3)}[mm] ')
# print(array(ret_D.desplazamientos_verticales)[:,0])
# ret_D.desplazamientos_verticales=[]
# plt.legend()
# plt.savefig("C:/Users/jpsil/Documents/Universidad de los Andes/Universidad 2020 octavo semestre/MCOC/Proyecto 3/Imagenes informe/ Primer_Gráfico_1_4D.PNG")
plt.show()


# CASO 2
ver_reticulado_3d(ret_D, 
    opciones_nodos = {
        "usar_posicion_deformada": True,
        "factor_amplificacion_deformada": factor_a,
        "datos_desplazamientos_nodales":ret_D.u*1.2 + ret_L.u*1.6,
    },
    opciones_barras = {
        "color_barras_por_dato": True,
        "ver_numeros_de_barras": False,
        "ver_dato_en_barras": False,
        "dato": f_2,
        "color_fondo": [1,1,1,0.4]
    }, 
    llamar_show=False,
    zoom=180.,
    deshabilitar_ejes=True)

plt.suptitle("Tensiones en caso 1: 1.2 D + 1.6 L")
plt.title(f"El desplazamiento máximo es: {round(1000*min(ret_D.u*1.2+ret_L.u*1.6),3)} [mm]\n {condicion_2}")
# ret_D_desplazamientos_max=sorted(ret_D.desplazamientos_verticales, key=itemgetter(1))[0]
# plt.title(f'Desplazamiento maximo en el nodo {ret_D_desplazamientos_max[0]}: {round(ret_D_desplazamientos_max[1]*1000,3)}[mm] ')
# ret_D.desplazamientos_verticales=[]

plt.show()

# print

# CASO 3
ver_reticulado_3d(ret_D, 
    opciones_nodos = {
        "usar_posicion_deformada": True,
        "factor_amplificacion_deformada": factor_a,
        "datos_desplazamientos_nodales":ret_D.u*1.4,
    },
    opciones_barras = {
        "color_barras_por_dato": True,
        "ver_numeros_de_barras": False,
        "ver_dato_en_barras": False,
        "dato": FU_caso1,
        "color_fondo": [1,1,1,0.4]
    }, 
    llamar_show=False,
    zoom=180.,
    deshabilitar_ejes=True)

plt.suptitle("FU caso 1: 1.4 D ")
plt.title(f"El desplazamiento máximo es: {round(1000*min(ret_D.u*1.4),3)} [mm]")
# ret_D_desplazamientos_max=sorted(ret_D.desplazamientos_verticales, key=itemgetter(1))[0]
# plt.title(f'Desplazamiento maximo en el nodo {ret_D_desplazamientos_max[0]}: {round(ret_D_desplazamientos_max[1]*1000,3)}[mm] ')
# ret_D.desplazamientos_verticales=[]
plt.show()


# CASO 4
ver_reticulado_3d(ret_D, 
    opciones_nodos = {
        "usar_posicion_deformada": True,
        "factor_amplificacion_deformada": factor_a,
        "datos_desplazamientos_nodales":ret_D.u*1.2 + ret_L.u*1.6,
    },
    opciones_barras = {
        "color_barras_por_dato": True,
        "ver_numeros_de_barras": False,
        "ver_dato_en_barras": False,
        "dato": FU_caso_general,
        "color_fondo": [1,1,1,0.4]
    }, 
    llamar_show=False,
    zoom=180.,
    deshabilitar_ejes=True)

plt.suptitle("FU caso 2: 1.2 D + 1.6 L")
plt.title(f"El desplazamiento máximo es: {round(1000*min(ret_D.u*1.2+ret_L.u*1.6),3)} [mm]")
# ret_D_desplazamientos_max=sorted(ret_D.desplazamientos_verticales, key=itemgetter(1))[0]
# plt.title(f'Desplazamiento maximo en el nodo {ret_D_desplazamientos_max[0]}: {round(ret_D_desplazamientos_max[1]*1000,3)}[mm] ')
# ret_D.desplazamientos_verticales=[]
plt.show()


peso = ret_D.calcular_peso_total()

print(f"peso original = {peso}")

barras_a_rediseñar = [i for i in range(386)]

# barras_a_rediseñar = [8,9,12,14,15]

#                   CASO DE CARGA MUERTA OPTIMIZADA
barras_muerto = ret_D_muerto.obtener_barras()
# print(barras_muerto)
barras_vivas=ret_L.obtener_barras()

for i in barras_a_rediseñar:
    barras_muerto[i].rediseñar(f_3_D_muerto[i],ret_D_muerto)
    barras_vivas[i].rediseñar(f_3_D_muerto[i],ret_D_muerto)
    # print(f'R:{ret_D_muerto}')
        

ret_D_muerto.ensamblar_sistema()
ret_D_muerto.resolver_sistema()        

ret_L.ensamblar_sistema()
ret_L.resolver_sistema()

f_L = ret_L.recuperar_fuerzas()

FU_caso_muerto = ret_D_muerto.recuperar_factores_de_utilizacion(f_3_D_muerto)
f_D_muerto = ret_D_muerto.recuperar_fuerzas()
f_3_D_muerto = 1.4*f_D_muerto  

"""
AÑADIDO NUEVO
"""
cumple_combinacion_1 = ret_D.chequear_diseño(f_1)
cumple_combinacion_2 = ret_L.chequear_diseño(f_2)

condicion_1=""
condicion_2=""

if cumple_combinacion_1:
    condicion_1="Combinación de carga 1 : cumple "
else:
    condicion_1="Combinación de carga 1 : NO cumple "
    
if cumple_combinacion_2:
    condicion_2="Combinación de carga 2 : cumple "
else:
    condicion_2="Combinación de carga 2 :NO cumple "



ver_reticulado_3d(ret_D_muerto, 
    opciones_nodos = {
        "usar_posicion_deformada": True,
        "factor_amplificacion_deformada": factor_a,
        "datos_desplazamientos_nodales":ret_D_muerto.u*1.4,
    },
    opciones_barras = {
        "color_barras_por_dato": True,
        "ver_numeros_de_barras": False,
        "ver_dato_en_barras": True,
        "dato": f_3_D_muerto,
        "color_fondo": [1,1,1,0.4]
    }, 
    llamar_show=False,
    zoom=180.,
    deshabilitar_ejes=True)

plt.suptitle("Tensiones en caso 3: 1.4 D  OPTIMIZADO")
plt.title(f"El desplazamiento máximo es: {round(1000*min(ret_D_muerto.u*1.4),3)} [mm]")
# ret_D_muerto_desplazamientos_max=sorted(ret_D_muerto.desplazamientos_verticales, key=itemgetter(1))[0]
# plt.title(f'Desplazamiento maximo en el nodo {ret_D_muerto_desplazamientos_max[0]}: {round(ret_D_muerto_desplazamientos_max[1]*1000,3)}[mm] ')
plt.show()

peso = ret_D_muerto.calcular_peso_total()
print(f"peso optimizado 1.4 D = {peso}")

ver_reticulado_3d(ret_D_muerto, 
    opciones_nodos = {
        "usar_posicion_deformada": True,
        "factor_amplificacion_deformada": factor_a,
        "datos_desplazamientos_nodales":ret_D_muerto.u*1.4,
    },
    opciones_barras = {
        "color_barras_por_dato": True,
        "ver_numeros_de_barras": False,
        "ver_dato_en_barras": True,
        "dato": FU_caso_muerto,
        "color_fondo": [1,1,1,0.4]
    }, 
    llamar_show=False,
    zoom=180.,
    deshabilitar_ejes=True)

plt.suptitle("FU caso 3: 1.4 D OPTIMIZADO")
# plt.title(f"El desplazamiento máximo es: {round(1000*min(ret_D_muerto.u*1.4),3)} [mm]")
plt.title(f"El desplazamiento máximo es: {round(1000*min(ret_D.u*1.4),3)} [mm]\n {condicion_1}")
plt.show()
