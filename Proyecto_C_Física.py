
"""Los valores asignados son solo para comprobar y demostrar el uso
y ejecución correcto de los operadores en las formulas empeladas"""

"""Por motivos prácticos los valores presentados en MRU, MRUA, Caída Libre y Tiro Vertical,
son parte de un mismo problema (Uno por tema. Por lo tanto, los resultados dados por la función
deberán de coincidir con los valores presentados endicho apartado. Sin embargo, no estan ligados
ni son modíficados a lo largo de la ejecución del programa """

# Guardar notación número entero
guardar_nne = 34573848589
# Guardar notación número decimal 
guardar_nnd = 0.8678996677

#Número notación científica 
num_nc_ = 4.5E5
# Lo mismo pero con un 1 para diferenciar 
num_nc_1_ = 9.5E-4

"""MRU Valores"""
velocidad_mru = 14.81
distancia_mru = 78.5
tiempo_mru = 5.3

"""MRUA Valores"""

velocidad_i_mrua = 6.0
velocidad_f_mrua = 45.0
tiempo_mrua = 20.0
distancia_mrua = 510.0
aceleracion_mrua = 1.95

"""Caída Libre Valores"""

gravedad_cl = 9.81
gravedad_tv =  -9.81
tiempo_cltv = 34.0
velocidad_i_cltv = 2.0
velocidad_f_cltv = 335.54
altura_cltv = 5738.18

"""Masa y Peso"""
masa = 34.0
peso = 333.54

"""Segunda Ley de Newton"""

aceleracion_2ln = 3.6
fuerza = 122.4

print ("""
Problemas de Notación científica de:
decimales o enteros muy grandes a notación científica
""")

num_nc = format( guardar_nne, ".1E")

num_nc_1 = format( guardar_nnd, ".1E")


print (num_nc)

print (num_nc_1)

print ("""
Problemas de Notación científica de:
notación decimal a decimales o enteros muy grandes
""")

guardar_nnc_cadena = str(num_nc_)

guardar_nnc_1_cadena = str(num_nc_1_)


num_nd = float(guardar_nnc_cadena)

num_nd_1 = float (guardar_nnc_1_cadena)


print (num_nd)

print (num_nd_1)


#El número marcado después de mru es para evitar alteraciones en los valores declarados al principio del documento 

print ("""
Fórmulas de MRU
""")

velocidad_mru_1 = float (distancia_mru/tiempo_mru)
print ("""Velocidad""")
print ("{:.4}".format(velocidad_mru_1))

distancia_mru_1 = float (velocidad_mru* tiempo_mru)
print ("""Distancia""")
print ("{:.4}".format(distancia_mru_1))

tiempo_mru_1 = float (distancia_mru/velocidad_mru)
print ("""Tiempo""")
print ("{:.4}".format(tiempo_mru_1))




print ("""
Formulas MRUA
""")

#El número marcado después de mrua es para marcar las diferentes formulas para llegar a un resultado en base a valores proporcionados
#Y para evitar alteraciones en los valores declarados al principio del documento 

print ("""Distancia""")

distancia_mrua_1 =  (velocidad_i_mrua *  tiempo_mrua + ( (1/2)* aceleracion_mrua* tiempo_mrua**2))

distancia_mrua_2 = (((velocidad_f_mrua  + velocidad_i_mrua) / 2) * tiempo_mrua)

distancia_mrua_3 = (velocidad_f_mrua**2  - velocidad_i_mrua**2) / (2*aceleracion_mrua)

print (distancia_mrua_1)

print (distancia_mrua_2)

print (distancia_mrua_3)



print ("""Tiempo""")

tiempo_mrua_1 = (velocidad_f_mrua-velocidad_i_mrua)/aceleracion_mrua

tiempo_mrua_2 = (distancia_mrua/((velocidad_f_mrua+ velocidad_i_mrua)/2))

tiempo_mrua_3 = ((2* distancia_mrua)/aceleracion_mrua)**(1/2)

print ("{:.4}".format(tiempo_mrua_1))

print ("{:.4}".format(tiempo_mrua_2))

print ("{:.4}".format(tiempo_mrua_3))



print ("""Velocidad Inicial""")

velocidad_i_mrua_1 = (velocidad_f_mrua-(aceleracion_mrua* tiempo_mrua))

velocidad_i_mrua_2 = (velocidad_f_mrua**2 - 2*distancia_mrua * aceleracion_mrua)**(1/2)

print (velocidad_i_mrua_1)

print (velocidad_i_mrua_2)



print ("""Velocidad Final""")

velocidad_f_mrua_1 = (aceleracion_mrua*tiempo_mrua + velocidad_i_mrua)

velocidad_f_mrua_2 = (2*distancia_mrua * aceleracion_mrua + velocidad_i_mrua**2)**(1/2)

print ("{:.4}".format(velocidad_f_mrua_1))

print ("{:.4}".format(velocidad_f_mrua_2))


print ("""Aceleración""")

aceleracion_mrua_1 = (velocidad_f_mrua  - velocidad_i_mrua) / tiempo_mrua

aceleracion_mrua_2 = (velocidad_f_mrua**2  - velocidad_i_mrua**2) / (2*distancia_mrua)

print ("{:.4}".format(aceleracion_mrua_1))

print ("{:.4}".format(aceleracion_mrua_2))


print ("""
Caída Libre
""")

#El número marcado después de mrua es para marcar las diferentes formulas para llegar a un resultado en base a valores proporcionados
#Y para evitar alteraciones en los valores declarados al principio del documento
# Gravedad positiva


print ("""Altura""")

altura_cltv_1 = ((velocidad_i_cltv + velocidad_f_cltv)/2) * tiempo_cltv

altura_cltv_2 = (velocidad_i_cltv * tiempo_cltv) + (1/2) * gravedad_cl * tiempo_cltv**2


# En esta se considera que la Velocidad Inicial es = 0
altura_cltv_3 = (1/2) * gravedad_cl * tiempo_cltv**2


altura_cltv_4 = (velocidad_f_cltv**2 - velocidad_i_cltv**2) / (2*gravedad_cl)

print ("{:.10}".format(altura_cltv_1))

print ("{:.10}".format(altura_cltv_2))

print ("{:.10}".format(altura_cltv_3))

print ("{:.10}".format(altura_cltv_4))



print ("""Tiempo""")

# En esta se considera que la Velocidad Inicial es = 0		
tiempo_cltv_1 = ((2*altura_cltv) / gravedad_cl)**(1/2)


tiempo_cltv_2 = altura_cltv / ((velocidad_i_cltv + velocidad_f_cltv) / 2)

tiempo_cltv_3 = ( velocidad_f_cltv - velocidad_i_cltv) / gravedad_cl

print ("{:.4}".format(tiempo_cltv_1))

print ("{:.4}".format(tiempo_cltv_2))

print ("{:.4}".format(tiempo_cltv_3))



print ("""Velocidad Inicial""")

velocidad_i_cltv_1 = velocidad_f_cltv - gravedad_cl * tiempo_cltv

velocidad_i_cltv_2 = (velocidad_f_cltv**2 - 2 * gravedad_cl * altura_cltv)**(1/2)

velocidad_i_cltv_3 = (altura_cltv - (1/2)*gravedad_cl * (tiempo_cltv**2) ) / tiempo_cltv

velocidad_i_cltv_4 = ((2*altura_cltv) / tiempo_cltv) - velocidad_f_cltv

print ("{:.4}".format(velocidad_i_cltv_1))

print ("{:.4}".format(velocidad_i_cltv_2))

print ("{:.4}".format(velocidad_i_cltv_3))

print ("{:.4}".format(velocidad_i_cltv_4))



print ("""Velocidad Final""")

velocidad_f_cltv_1 = velocidad_i_cltv + gravedad_cl * tiempo_cltv

velocidad_f_cltv_2 = (velocidad_i_cltv **2 + 2 * gravedad_cl * altura_cltv)**(1/2)

velocidad_f_cltv_3 = ((2*altura_cltv) / tiempo_cltv) - velocidad_i_cltv

print ("{:.4}".format(velocidad_f_cltv_1))

print ("{:.9}".format(velocidad_f_cltv_2))

print ("{:.4}".format(velocidad_f_cltv_3))


print ("""
Masa y Peso
""")

masa_1 = peso / gravedad_cl

peso_1 = masa * gravedad_cl

print (masa_1)

print (peso_1)


print ("""
Segunda Ley de Newton
""")

fuerza_1 = masa * aceleracion_2ln

aceleracion_2ln_1 = fuerza / masa

masa_2 = fuerza / aceleracion_2ln

print (fuerza_1)

print (aceleracion_2ln_1)

print (masa_2)
