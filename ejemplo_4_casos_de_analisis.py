from caso_D import caso_D
from caso_L import caso_L
from graficar3d import ver_reticulado_3d

ret_D = caso_D()
ret_L = caso_L()
#Casos optimizados
ret_D_muerto = caso_D()
ret_D_vivo_muerto = caso_D()
ret_D_5_barras = caso_D()


ver_reticulado_3d(ret_D, 
	axis_Equal=True, 
	opciones_barras={
	"ver_numeros_de_barras": False
	}, 
    llamar_show=True,
    zoom=180.,
    deshabilitar_ejes=True)


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


import matplotlib.pyplot as plt

# CASO 1
ver_reticulado_3d(ret_D, 
    opciones_nodos = {
        "usar_posicion_deformada": True,
        "factor_amplificacion_deformada": 10000.,
    },
    opciones_barras = {
        "color_barras_por_dato": True,
        "ver_numeros_de_barras": False,
        "ver_dato_en_barras": True,
        "dato": f_1,
        "color_fondo": [1,1,1,0.4]
    }, 
    llamar_show=False,
    zoom=180.,
    deshabilitar_ejes=True)

plt.title("Tensiones en caso 1: 1.4 D ")
plt.show()


# CASO 2
ver_reticulado_3d(ret_D, 
    opciones_nodos = {
        "usar_posicion_deformada": True,
        "factor_amplificacion_deformada": 10000.,
    },
    opciones_barras = {
        "color_barras_por_dato": True,
        "ver_numeros_de_barras": False,
        "ver_dato_en_barras": True,
        "dato": f_2,
        "color_fondo": [1,1,1,0.4]
    }, 
    llamar_show=False,
    zoom=180.,
    deshabilitar_ejes=True)

plt.title("Tensiones en caso 1: 1.2 D + 1.6 L")
plt.show()



# CASO 3
ver_reticulado_3d(ret_D, 
    opciones_nodos = {
        "usar_posicion_deformada": True,
        "factor_amplificacion_deformada": 10000.,
    },
    opciones_barras = {
        "color_barras_por_dato": True,
        "ver_numeros_de_barras": False,
        "ver_dato_en_barras": True,
        "dato": FU_caso1,
        "color_fondo": [1,1,1,0.4]
    }, 
    llamar_show=False,
    zoom=180.,
    deshabilitar_ejes=True)

plt.title("FU caso 1: 1.4 D ")
plt.show()


# CASO 4
ver_reticulado_3d(ret_D, 
    opciones_nodos = {
        "usar_posicion_deformada": True,
        "factor_amplificacion_deformada": 10000.,
    },
    opciones_barras = {
        "color_barras_por_dato": True,
        "ver_numeros_de_barras": False,
        "ver_dato_en_barras": True,
        "dato": FU_caso2,
        "color_fondo": [1,1,1,0.4]
    }, 
    llamar_show=False,
    zoom=180.,
    deshabilitar_ejes=True)

plt.title("FU caso 2: 1.2 D + 1.6 L")
plt.show()


peso = ret_D.calcular_peso_total()

print(f"peso = {peso}")



barras_a_rediseñar = [i for i in range(30)]
barras_a_rediseñar = [8,9,12,14,15]

#                   CASO DE CARGA MUERTA OPTIMIZADA
barras_muerto = ret_D_muerto.obtener_barras()
for i in barras_a_rediseñar:
    barras_muerto[i].rediseñar(f_3_D_muerto[i],ret_D_muerto)
        
FU_caso_muerto = ret_D_muerto.recuperar_factores_de_utilizacion(f_3_D_muerto)
f_D_muerto = ret_D_muerto.recuperar_fuerzas()
f_3_D_muerto = 1.4*f_D_muerto  




ver_reticulado_3d(ret_D_muerto, 
    opciones_nodos = {
        "usar_posicion_deformada": True,
        "factor_amplificacion_deformada": 10000.,
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

plt.title("Tensiones en caso 3: 1.4 D  OPTIMIZADO")
plt.show()

peso = ret_D_muerto.calcular_peso_total()
print(f"peso_optimizado_ = {peso}")

ver_reticulado_3d(ret_D_muerto, 
    opciones_nodos = {
        "usar_posicion_deformada": True,
        "factor_amplificacion_deformada": 10000.,
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

plt.title("FU caso 3: 1.4 D OPTIMIZADO")
plt.show()

#                            CASO DE COMBINACION DE CARGA 2 OPTIMIZADA (1.2*D + 1.6*L)
barras_vivo_muerto= ret_D_vivo_muerto.obtener_barras()
for i in barras_a_rediseñar:
    barras_vivo_muerto[i].rediseñar(f_4_D_vivo_muerto[i],ret_D_vivo_muerto)
        
FU_caso_vivo_muerto = ret_D_vivo_muerto.recuperar_factores_de_utilizacion(f_4_D_vivo_muerto)
f_D_vivo_muerto = ret_D_vivo_muerto.recuperar_fuerzas()
f_4_D_vivo_muerto = 1.2*f_D_vivo_muerto + 1.6*f_L  




ver_reticulado_3d(ret_D_vivo_muerto, 
    opciones_nodos = {
        "usar_posicion_deformada": True,
        "factor_amplificacion_deformada": 10000.,
    },
    opciones_barras = {
        "color_barras_por_dato": True,
        "ver_numeros_de_barras": False,
        "ver_dato_en_barras": True,
        "dato": f_4_D_vivo_muerto,
        "color_fondo": [1,1,1,0.4]
    }, 
    llamar_show=False,
    zoom=180.,
    deshabilitar_ejes=True)

plt.title("Tensiones en caso 4: 1.2 D + 1.6 L  OPTIMIZADO")
plt.show()

peso = ret_D_muerto.calcular_peso_total()
print(f"peso_optimizado_ = {peso}")

ver_reticulado_3d(ret_D_vivo_muerto, 
    opciones_nodos = {
        "usar_posicion_deformada": True,
        "factor_amplificacion_deformada": 10000.,
    },
    opciones_barras = {
        "color_barras_por_dato": True,
        "ver_numeros_de_barras": False,
        "ver_dato_en_barras": True,
        "dato": FU_caso_vivo_muerto,
        "color_fondo": [1,1,1,0.4]
    }, 
    llamar_show=False,
    zoom=180.,
    deshabilitar_ejes=True)

plt.title("FU caso 4: 1.2 D + 1.6 L OPTIMIZADO")
plt.show()


barras_a_rediseñar = [8,9,12,14,15]

#                            CASO DE 5 BARRAS PARA COMBINACION DE CARGA 2 OPTIMIZADA (1.2*D + 1.6*L)
barras_5_barras= ret_D_5_barras.obtener_barras()
for i in barras_a_rediseñar:
    barras_5_barras[i].rediseñar(f_5_D_5_barras[i],ret_D_5_barras)
        
FU_caso_5_barras = ret_D_5_barras.recuperar_factores_de_utilizacion(f_5_D_5_barras)
f_D_5_barras = ret_D_5_barras.recuperar_fuerzas()
f_5_D_5_barras = 1.2*f_D_5_barras + 1.6*f_L 




ver_reticulado_3d(ret_D_5_barras, 
    opciones_nodos = {
        "usar_posicion_deformada": True,
        "factor_amplificacion_deformada": 10000.,
    },
    opciones_barras = {
        "color_barras_por_dato": True,
        "ver_numeros_de_barras": False,
        "ver_dato_en_barras": True,
        "dato": f_5_D_5_barras,
        "color_fondo": [1,1,1,0.4]
    }, 
    llamar_show=False,
    zoom=180.,
    deshabilitar_ejes=True)

plt.title("Tensiones en caso 5 BARRAS: 1.2 D + 1.6 L  OPTIMIZADO")
plt.show()

peso = ret_D_5_barras.calcular_peso_total()
print(f"peso_optimizado_ = {peso}")

ver_reticulado_3d(ret_D_5_barras, 
    opciones_nodos = {
        "usar_posicion_deformada": True,
        "factor_amplificacion_deformada": 10000.,
    },
    opciones_barras = {
        "color_barras_por_dato": True,
        "ver_numeros_de_barras": False,
        "ver_dato_en_barras": True,
        "dato": FU_caso_5_barras,
        "color_fondo": [1,1,1,0.4]
    }, 
    llamar_show=False,
    zoom=180.,
    deshabilitar_ejes=True)

plt.title("FU caso 5 BARRAS: 1.2 D + 1.6 L OPTIMIZADO")
plt.show()
