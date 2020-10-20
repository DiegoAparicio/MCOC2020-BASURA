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
peso_L = ret_L.calcular_peso_total()


if cumple_combinacion_1:
    print("Combinación de carga 1 : cumple ")
else:
    print("Combinación de carga 1 : NO cumple ")
    
if cumple_combinacion_2:
    print("Combinación de carga 2 : cumple ")
else:
    print("Combinación de carga 2 : NO cumple ")


if abs(peso_D - peso_L) < 1e-9:
    print(f"Peso total = {peso_D}")
else:
    print(f"Estructura pesa distinto en caso D y caso L!")
    print(f"peso_D = {peso_D}")
    print(f"peso_L = {peso_L}")
