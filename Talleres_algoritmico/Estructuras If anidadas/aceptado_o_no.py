"""
En una universidad aplican dos exámenes a sus aspirantes, por lo que cada uno de ellos obtiene dos 
calificaciones denotadas como c1 y c2. El aspirante que obtenga calificaciones mayores a 80 puntos en 
ambos exámenes es aceptado, en caso contrario es rechazado
"""
#Primero vamos a recibir los estudiantes y notas
nombre = input("Ingrese el nombre de el estudiante  ==> ")
c1 = int(input("Ingrese la primera calificacion de estudiante  ==>"))
c2 = int(input("Ingrese la segunda calificacion de estudiante  ==>"))

if c1 > 80 and c2 > 80:
    
    print(f"El estudiante {nombre} a APROBADO")
else:
    print(f"El estudiante {nombre} REPROBADO")
