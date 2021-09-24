"""Constantes"""

GRAVEDAD = 9.81


""" Calcula la calificación del usuario"""

def calificacion (respuesta_t1n1_1, respuesta_t1n1_2, respuesta_t1n1_3):

    cont = 0

    if respuesta_t1n1_1 == "a":

        cont= cont+1

        print ("Correcto")
    else:

        print ("Incorrecto")
    
    if respuesta_t1n1_2 == notacion_cientifica(3890000):

        cont= cont+1
        
        print ("Correcto")
    else:

        print ("Incorrecto")

    if respuesta_t1n1_3 == notacion_decimal ("01.7E+05"):

        cont= cont +1

        print ("Correcto")
    else:

        print ("Incorrecto")

    calif = (cont*100/3)

    print ("Tu calificación final es:", ("{:.2f}".format(calif)))
    

""" Se hará uso de condicionales donde se compraran las respuestas del usuario
con los resultados obtenidos en python, determinando si el resultado es
correcto o incorrecto (le mostrará esto al usuario, y se le sumará ciertos
puntos a la calificación final"""

#Solo un ejemplo de como serán usadas las condicionales, agregar el uso de listas para guardar las respuestas dadas por el usuario
#Modificar cuando se encuentre una manera de hacerlo más corto y eficiente 



""" Tema 1_Operaciones_Notación científica"""

def notacion_cientifica(numero_nd):
    return format(numero_nd, ".1E")

def notacion_decimal(numero_nc):
    return float(numero_nc)


"""Tema 1_Preguntas_Notación científica"""

def tema1_dificultad1(tema_e, dificultad_e):

    print ("Tema 1: " + tema_e + "\n\nNivel " + dificultad_e)


    respuesta_t1n1_1 = input("""

¿Para qué seutiliza la notación científica?

a) Para expresar cantidades muy grandes o muy pequeñas

b) Solo para expresar cantidades muy grandes

c) Solo para expresar cantidades muy pequeñas

""")
    

    respuesta_t1n1_2 = input("""

¿Cuál es la notación científica de 3890000?

favor de expresar el valor como en el siguente ejemplo:

1400 sería 1.4E+03

→ Solo un decimal

""")

    (notacion_cientifica(3890000))


    respuesta_t1n1_3 = float(input("""

Para el número en notación científica a notación decimal:

1.7E+05

"""))

    (notacion_decimal ("1.7E+05"))

    calificacion (respuesta_t1n1_1, respuesta_t1n1_2, respuesta_t1n1_3)
    

def tema1_dificultad2(tema_e, dificultad_e):
    print ("Tema 1: " + tema_e + "\n\nNivel " + dificultad_e)
    print ("La misma temática de nivel uno, pero más difícil")
    
    
def tema1_dificultad3(tema_e, dificultad_e):
    print ("Tema 1: " + tema_e + "\n\nNivel " + dificultad_e)
    print ("La misma temática de nivel uno, pero más difícil que uno y dos")



"""" Tema 2_Operaciones"""

#MRU

def velocidad_mru(distancia_mru, tiempo_mru):
    return ("{:.2f}".format(distancia_mru/tiempo_mru))

def distancia_mru(velocidad_mru, tiempo_mru):
    return ("{:.2f}".format(velocidad_mru*tiempo_mru))

def tiempo_mru(distancia_mru, velocidad_mru):
    return  ("{:.2f}".format(distancia_mru/velocidad_mru))

#MRUA

"""Tiempo"""

def tiempo_mrua_vfvia (velocidad_f_mrua, velocidad_i_mrua, aceleracion_mrua):
    return ("{:.2f}".format((velocidad_f_mrua-velocidad_i_mrua)/aceleracion_mrua))

def tiempo_mrua_vfvid (velocidad_f_mrua, velocidad_i_mrua, distancia_mrua):
    return ("{:.2f}".format((distancia_mrua/((velocidad_f_mrua+ velocidad_i_mrua)/2))))

def tiempo_mrua_da (distancia_mrua, aceleracion_mrua):
    return ("{:.2f}".format(((2* distancia_mrua)/aceleracion_mrua)**(1/2)))


"""Distancia"""

def distancia_mrua_vita (velocidad_i_mrua, tiempo_mrua, aceleracion_mrua):
    return ("{:.2f}".format((velocidad_i_mrua *  tiempo_mrua + ( (1/2)* aceleracion_mrua* tiempo_mrua**2))))

def distancia_mrua_vfvit (velocidad_f_mrua, velocidad_i_mrua, tiempo_mrua):
    return ("{:.2f}".format((((velocidad_f_mrua  + velocidad_i_mrua) / 2) * tiempo_mrua)))

def distancia_mrua_vfvia (velocidad_f_mrua, velocidad_i_mrua,aceleracion_mrua):
    return ("{:.2f}".format((velocidad_f_mrua**2  - velocidad_i_mrua**2) / (2*aceleracion_mrua)))


"""Velocidad Inicial"""

def velocidad_i_mrua_vfat (velocidad_f_mrua, aceleracion_mrua, tiempo_mrua):
    return ("{:.2f}".format((velocidad_f_mrua-(aceleracion_mrua* tiempo_mrua))))

def velocidad_i_mrua_vfda (velocidad_f_mrua, distancia_mrua, aceleracion_mrua):
    return ("{:.2f}".format((velocidad_f_mrua**2 - 2*distancia_mrua * aceleracion_mrua)**(1/2)))


"""Velocidad Final"""

def velocidad_f_mrua_viat (velocidad_i_mrua, aceleracion_mrua, tiempo_mrua):
    return ("{:.2f}".format((aceleracion_mrua*tiempo_mrua + velocidad_i_mrua)))

def velocidad_f_mrua_viad (velocidad_i_mrua, aceleracion_mrua, distancia_mrua):
    return ("{:.2f}".format((2*distancia_mrua * aceleracion_mrua + velocidad_i_mrua**2)**(1/2)))


"""Aceleración"""

def aceleracion_mrua_v0vft (velocidad_f_mrua, velocidad_i_mrua, tiempo_mrua):
    return ("{:.2f}".format((velocidad_f_mrua-velocidad_i_mrua)/tiempo_mrua))

def aceleracion_mrua_v0vfd (velocidad_f_mrua, velocidad_i_mrua, distancia_mrua):
    return ("{:.2f}".format((velocidad_f_mrua**2-velocidad_i_mrua**2)/(2*distancia_mrua)))



""" Tema 2_Preguntas_MRU y MRUA"""


def tema2_dificultad1(tema_e, dificultad_e):

    print ("Tema 1: " + tema_e + "\n\nNivel " + dificultad_e)
    

    respuesta_t2n1_1 = input("""

¿Cuál es la fórmula para calcular la velocidad en MRU?

a) v = d/t

b) v = d*t

c) v = d+t

""")
    

    respuesta_t2n1_2 = float(input("""

Calcula la velocidad de un auto que se mueve a  450 m en 120 segundos

(solo ingrese el número con dos decimales)

"""))

    velocidad_mru(450.0, 120.0)



    respuesta_t2n1_3 = float(input("""

¿Cuál es la aceleración de un objeto que de tener una velocidad de 0 m/s
pasó a tener una velocidad de 45 m/s en 89 segundos?

(solo ingrese el número con dos decimales)


"""))

    aceleracion_mrua_v0vft (45.0, 0.0, 89.0)
    

def tema2_dificultad2(tema_e, dificultad_e):
    print ("Tema 1: " + tema_e + "\n\nNivel " + dificultad_e)
    print ("La misma tematica de nivel uno, pero más difícil")
    
def tema2_dificultad3(tema_e, dificultad_e):
    print ("Tema 1: " + tema_e + "\n\nNivel " + dificultad_e)
    print ("La misma tematica de nivel uno, pero más difícil que uno y dos")


    


"""Tema 3_Operaciones_Caída Libre"""

""" Altura """

def altura_cl_t (tiempo_cl):
    return ("{:.2f}".format((1/2)*GRAVEDAD*tiempo_cl**2))

def altura_cl_vit (velocidad_i_cl, tiempo_cl):
    return ("{:.2f}".format((velocidad_i_cl*tiempo_cl)+(1/2)*GRAVEDAD* tiempo_cl**2))

def altura_cl_vivft (velocidad_i_cl, velocidad_f_cl, tiempo_cl):
    return ("{:.2f}".format(((velocidad_i_cl + velocidad_f_cl)/2)*tiempo_cl))


""" Tiempo """

def tiempo_cl_a (altura_cl):
    return ("{:.2f}".format(((2*altura_cl)/GRAVEDAD)**(1/2)))

def tiempo_cl_vivf (velocidad_i_cl, velocidad_f_cl):
    return ("{:.2f}".format((velocidad_f_cl-velocidad_i_cl)/GRAVEDAD))

def tiempo_cl_vivfa (velocidad_i_cl, velocidad_f_cl, altura_cl):
    return ("{:.2f}".format(altura_cl/((velocidad_i_cl+velocidad_f_cl)/2)))


""" Velocidad Inicial """

def velocidad_i_cl_vft (velocidad_f_cl, tiempo_cl):
    return ("{:.2f}".format(velocidad_f_cl-GRAVEDAD*tiempo_cl))

def velocidad_i_cl_vfa (velocidad_f_cl, altura_cl):
    return ("{:.2f}".format((velocidad_f_cl**2-2*GRAVEDAD*altura_cl)**(1/2)))

def velocidad_i_cl_at (altura_cl, tiempo_cl):
    return ("{:.2f}".format((altura_cl-(1/2)*GRAVEDAD*(tiempo_cl**2))/tiempo_cl))

def velocidad_i_cl_vfat (velocidad_f_cl, altura_cl, tiempo_cl):
    return ("{:.2f}".format(((2*altura_cl)/tiempo_cl)-velocidad_f_cl))


""" Velocidad Final """

def velocidad_f_cl_vit (velocidad_i_cl, tiempo_cl):
    return ("{:.2f}".format(velocidad_i_cl+GRAVEDAD*tiempo_cl))

def velocidad_f_cl_via (velocidad_i_cl, altura_cl):
    return ("{:.2f}".format((velocidad_i_cl**2+2*GRAVEDAD*altura_cl)**(1/2)))

def velocidad_f_cl_viat (velocidad_i_cl, altura_cl, tiempo_cl):
    return ("{:.2f}".format(((2*altura_cl)/tiempo_cl)-velocidad_i_cl))


"""Tema 3_Preguntas_Caída Libre"""

def tema3_dificultad1(tema_e, dificultad_e):

    print ("Tema 1: " + tema_e + "\n\nNivel " + dificultad_e)
    

    respuesta_t3n1_1 = input("""

"¿Cuál sería la mejor definición para caída libre?

a) Un objeto que cae

b) Cualquier objeto bajo la acción de la gravedad en un lugar donde
    la resistencia del aire es despresiable

c) Un objeto en caída libre

""")
    

    respuesta_t3n1_2 = float(input("""

Calcula la altura de un objeto que cae en un tiempo de 67 segundos
[considera que tu velocidad inicial es 0 m/s y tu gravedad de 9.81 m/s^2]

(solo ingrese el número con dos decimales)

"""))

    (altura_cl_t (67.0))



    respuesta_t3n1_3 = float(input("""

¿Cuál es la velocidad final de un objeto que recorre 450 m durante 20 segundos
y que tiene una velocidad inicial de 13 m/s?

(solo ingrese el número con dos decimales)


"""))

    (velocidad_f_cl_viat(13.0, 450.0, 20.0))



def tema3_dificultad2(tema_e, dificultad_e):
    print ("Tema 1: " + tema_e + "\n\nNivel " + dificultad_e)
    print ("La misma temática de nivel uno, pero más difícil")
    
def tema3_dificultad3(tema_e, dificultad_e):
    print ("Tema 1: " + tema_e + "\n\nNivel " + dificultad_e)
    print ("La misma temática de nivel uno, pero más difícil que uno y dos")
    





"""Tema 4_Operaciones_Masa y Peso"""

def masa_mp (peso):
    return ("{:.2f}".format(peso/GRAVEDAD))

def peso_mp (masa):
    return ("{:.2f}".format(masa*GRAVEDAD))

   
"""Tema 4_Preguntas_Masa y Peso"""

def tema4_dificultad1(tema_e, dificultad_e):

    print ("Tema 1: " + tema_e + "\n\nNivel " + dificultad_e)

    respuesta_t4n1_1 = input("""

La unidad de medida de la masa en el SI es:

a) gramos

b) onzas

c) Kilogramos

""")
    

    respuesta_t4n1_2 = float(input("""

Calcula la masa de un automovil que pesa 17500 N

(solo ingrese el número con dos decimales)

"""))

    masa_mp (17500.0)



    respuesta_t4n1_3 = float(input("""

¿Cuál es el peso de una caja, cuando su masa es igual a 75 Kg?

(solo ingrese el número con dos decimales)


"""))

    peso_mp (75.0)
    

def tema4_dificultad2(tema_e, dificultad_e):
    print ("Tema 1: " + tema_e + "\n\nNivel " + dificultad_e)
    print ("La misma temática de nivel uno, pero más difícil")
    
def tema4_dificultad3(tema_e, dificultad_e):
    print ("Tema 1: " + tema_e + "\n\nNivel " + dificultad_e)
    print ("La misma temática de nivel uno, pero más difícil que uno y dos")

    
    

"""Tema 5_Operaciones_Leyes de Newton"""

def fuerza_neta (masa_n, aceleracion_n):
    return ("{:.2f}".format(masa_n *aceleracion_n))

def masa_2n (fuerza_n, aceleracion_n):
    return ("{:.2f}".format(fuerza_n/aceleracion_n))

def aceleracion_2n (fuerza_n, masa_n):
    return ("{:.2f}".format(fuerza_n/masa_n))

    
"""Tema 5_Preguntas_Leyes de Newton"""

def tema5_dificultad1(tema_e, dificultad_e):
    
    print ("Tema 1: " + tema_e + "\n\nNivel " + dificultad_e)

    respuesta_t5n1_1 = input("""

"A toda acción corresponde una reacción de igual magnitud,
pero en sentido contrario"

¿De qué ley estamos hablando?

a) 1ra Ley de Newton

b) 2da Ley de Newton

c) 3ra Ley de Newton

""")
    

    respuesta_t5n1_2 = float(input("""

¿Cuál es la Fuerza Neta de un obeto con una masa= 40 Kg y una aceleración = 3.5 m/s^2?

(solo ingrese el número con dos decimales)


"""))

    (fuerza_neta (40.0,3.5))


    respuesta_t5n1_3 = input("""

¿Qué otro nombre se le da a la primera Ley de Newton?

a) Karma

b) Ley de la Inercia

c) Ley de los objetos estáticos

""")
    

def tema5_dificultad2(tema_e, dificultad_e):
    print ("Tema 1: " + tema_e + "\n\nNivel " + dificultad_e)
    print ("La misma temática de nivel uno, pero más difícil")
    
def tema5_dificultad3(tema_e, dificultad_e):
    print ("Tema 1: " + tema_e + "\n\nNivel " + dificultad_e)
    print ("La misma temática de nivel uno, pero más difícil que uno y dos")


    
    

"""Elegir  tema y nivel"""

def tema_y_nivel ():

    tema = int(input("""

    1.- Notación científica
    2.- MRU y MRUA
    3.- Caída Libre 
    4.- Masa y Peso
    5.- Leyes de Newton

    """))


    if tema < 1 or tema > 5:    

        tema = int(input("""
    Lo siento el número seleccionado no está en los parámetros,
    por favor ingrese un número que este dentro de los parámetros:

    1.- Notación científica
    2.- MRU y MRUA
    3.- Caída Libre 
    4.- Masa y Peso
    5.- Leyes de Newton

    """))


    dificultad = int(input("""
    ¿Qué nivel deseas completar? Escribe el número:

    1.- Sencillo 
    2.- Normal
    3.- Avanzado

    """))

    if dificultad < 0 or dificultad > 3:    

        dificultad = int(input("""
    Lo siento el número seleccionado no está en los parámetros,
    por favor ingrese un número que este dentro de los parámetros:

    1.- Sencillo 
    2.- Normal
    3.- Avanzado
    """))


        
    if tema == 1 and dificultad == 1:
        tema1_dificultad1("Notación Cinetífica", "1")

    elif tema == 1 and dificultad == 2:
        tema1_dificultad2("Notación Cinetífica", "2")

    elif tema == 1 and dificultad == 3:
        tema1_dificultad3 ("Notación Cinetífica", "3")



    elif tema == 2 and dificultad == 1:
        tema2_dificultad1("MRU y MRUA", "1")

    elif tema == 2 and dificultad == 2:
        tema2_dificultad2("MRU y MRUA", "2")


    elif tema == 2 and dificultad == 3:
        tema2_dificultad3("MRU y MRUA", "3")



    elif tema == 3 and dificultad == 1:
        tema3_dificultad1("Caída Libre", "1")

    elif tema == 3 and dificultad == 2:
        tema3_dificultad2("Caída Libre", "2")


    elif tema == 3 and dificultad == 3:
        tema3_dificultad3("Caída Libre", "3")



    elif tema == 4 and dificultad == 1:
        tema4_dificultad1("Masa y Peso", "1")

    elif tema == 4 and dificultad == 2:
        tema4_dificultad2("Masa y Peso", "2")


    elif tema == 4 and dificultad == 3:
        tema4_dificultad3("Masa y Peso", "3")



    elif tema == 5 and dificultad == 1:
        tema5_dificultad1("Leyes de Newton", "1")

    elif tema == 5 and dificultad == 2:
        tema5_dificultad2("Leyes de Newton", "2")


    elif tema == 5 and dificultad == 3:
        tema5_dificultad3("Leyes de Newton", "3")







""" Algoritmo principal"""

        

print ("¡Hola usuario! ¿Qué tema deseas repasar? Por favor ingresa el número")

tema_y_nivel ()


continuar_p = input("¿Deseas repasar otro tema?\n a)Sí\n b)No\n")

while continuar_p == "a" or continuar_p == "A":
    
    tema_y_nivel ()
    
    continuar_p = input("¿Deseas repasar otro tema?\n a)Sí\n b)No\n")


print ("¡Gracias por repasar en este programa!")

