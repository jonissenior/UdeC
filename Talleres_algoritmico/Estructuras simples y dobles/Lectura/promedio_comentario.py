#Algoritmo para promedio de calificaciones de un estudiante
"""
Elaborar un algoritmo para calcular el promedio de calificaciones de un estudiante, los datos disponibles 
para lectura son el nombre, calificación 1, calificación 2, calificación 3 y calificación 4; de cada uno de los 
cuatro exámenes presentados. La información que se debe imprimir es el nombre del estudiante, el promedio 
de calificaciones y un comentario de “ Aprobado” si obtiene 3.0 o más, o “Reprobado” en caso contrario.
"""
#Primero solicitamos los datos a usar de los examenes
Nombre = input("Ingrese su nombre ==> ")
calificacion1 = float(input("Ingrese la primera calificación ==> "))
calificacion2 = float(input("Ingrese la segunda calificación ==> "))
calificacion3 = float(input("Ingrese la tercera calificación ==> "))
calificacion4 = float(input("Ingrese la cuarta calificación ==> "))
#Calculamos el promedio 
promedio = (calificacion1 + calificacion2 + calificacion3 + calificacion4)/4
#Ahora usamos el if para saber que comentario usar
if promedio >= 3.0:
    comentario = "APROBADO"
else:
    comentario = "REPROBADO"

#Ahora mostramos el promedio y el comentario
print(f"El estudiante {Nombre} tiene un promedio de {promedio:.1f} por lo tanto ha {comentario}")
