#Continuamos con mas
"""
 Elaborar un algoritmo tal que dado como datos el código de un estudiante, la carrera en la que está 
inscrito, su semestre y su promedio; determine si el estudiante es apto para pertenecer a alguna de las 
facultades menores que tiene la universidad. Si el estudiante es aceptado teniendo en cuenta las 
especificaciones que se listan a continuación, se debe imprimir su código, carrera y la palabra 
“ACEPTADO”.

Especificaciones para pertenecer a las facultades menores:
Economía: semestre >= 6 , promedio =>8.8
Computación: semestre > 6 , promedio >=9.0
Administración: semestre > 5 , promedio >=8.5
Contabilidad: semestre > 5 , promedio >=8.5
"""
#Vamos a pedir los datos que necesitamos 
codigo = int(input("Ingrese su codigo ==> "))
print("opcines de carrera: Economia, Computacion, Administracion, Contabilidad")
carrera = str(input("Ingrese la carrera que esta inscrito ==> ")).lower().strip()
semestre = int(input("Ingrese su semestre ==> "))
promedio = float(input("Ahora ingrese su promedio (1.0 a 10) ==> "))
#Ahora vamos a comprobar si es aceptado 
if carrera == "economia":
    if semestre >= 6 and promedio >= 8.8:
        print(f"El estudiante de codigo {codigo} ha sido APROBADO en la carrera {carrera}")
    else:
        print("No ha aprobado")
elif carrera == "computacion":
    if semestre > 6 and promedio >= 9.0:
        print(f"El estudiante de codigo {codigo} ha sido APROBADO en la carrera {carrera}")
    else:
        print("No ha aprobado")
elif carrera == "administracion":
    if semestre > 5 and promedio >= 8.5:
        print(f"El estudiante de codigo {codigo} ha sido APROBADO en la carrera {carrera}")
    else:
        print("No ha aprobado")
elif carrera == "contabilidad":
    if semestre > 5 and promedio >= 8.5:
        print(f"El estudiante de codigo {codigo} ha sido APROBADO en la carrera {carrera}")
    else:
        print("No ha aprobado")
else:
    print("Esa carrera no esta disponible a verificar") 

