
"""
Elaborar un algoritmo tal que dado como datos el nombre de 
un empleado, el valor de la hora trabajada y  número de horas 
trabajadas, que permita calcular su sueldo e imprima el nombre 
del empleado y su sueldo. 
"""
#Dar sueldo del empleado

#Preguntar datos
Nombre = input("Ingrese su nombre ==> ")
Valor_Hora = int(input("Cual es el valor de la hora ==> "))
horas_trabajadas = int(input("Cuantas horas trabajo ==> "))
#Calcular sueldo
sueldo = horas_trabajadas * Valor_Hora
#mostrar datos
print(f"Bienvenido {Nombre}!!, su sueldo es de {sueldo:,.0f}")


