from caso_D_4 import caso_D
from caso_L_4 import caso_L

ret_D = caso_D()
ret_L = caso_L()

#Peso propio
ret_D.ensamblar_sistema()
ret_D.resolver_sistema()
f_D = ret_D.recuperar_fuerzas()

#Carga Viva
ret_L.ensamblar_sistema()
ret_L.resolver_sistema()
f_L = ret_L.recuperar_fuerzas()

#Combinaciones de carga
f_1 = 1.4*f_D           #Combinacion 1
f_2 = 1.2*f_D + 1.6*f_L #Combinacion 2


# Calcular factores 
cumple_combinacion_1 = ret_D.chequear_diseño(f_1)
cumple_combinacion_2 = ret_L.chequear_diseño(f_2)


peso_D = ret_D.calcular_peso_total()


if cumple_combinacion_1:
    print("Combinación de carga 1 : cumple ")
else:
    print("Combinación de carga 1 : NO cumple ")
    
if cumple_combinacion_2:
    print("Combinación de carga 2 : cumple ")
else:
    print("Combinación de carga 2 : NO cumple ")


if cumple_combinacion_1 and cumple_combinacion_2:
    print(f"Peso total = {peso_D}")

print(f"cantidad de barras con error: {len(ret_D.lista_barras_error)}")