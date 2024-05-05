# Promedio estudiante 
"""
Elaborar un algoritmo para calcular el promedio de calificaciones 
de un estudiante. Los datos disponibles para lectura son el nombre, 
el código, calificación1, calificación2, calificación3, y calificación4; 
de cada uno de los cuatro exámenes presentados. La información 
que se debe imprimir es el nombre del estudiante y el promedio 
de calificaciones. 
"""
#Recibir datos
Nombre = input("Ingrese su nombre ==> ")
codigo = int(input("Ingrese el codigo == > "))
calificacion1 = float(input("Ingrese la primera calificación ==> "))
calificacion2 = float(input("Ingrese la segunda calificación ==> "))
calificacion3 = float(input("Ingrese la tercera calificación ==> "))
calificacion4 = float(input("Ingrese la cuarta calificación ==> "))

#Sacar promedio
promedio = (calificacion1 + calificacion2 + calificacion3 + calificacion4)/4
 
#Mostrar datos
print(f"El estudiante {Nombre} obtuvo un promedio de: {promedio:.1f}")

