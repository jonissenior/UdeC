#Ahora vemos a While
"""
Elaborar un algoritmo que permita procesar varios empleados, igual al primer ejemplo de Do while
pero con la posibilidad que No se procese ningún empleado (o que No se realice el ciclo repetitivo)
"""
#Hacemos la pregunta
pregunta = str(input("Desea procesar empleado?: Y/N ")).lower().strip()
#hacemos un while segun la pregunta
while pregunta == "y":
    
    nombre = input("Ingrese el nombre de el empleado ==> ")
    numhortra = int(input("Ingrese el numero de horas trabajadas ==> "))
    valhortra = float(input("Ingrese cuanto vale cada hora ==> "))
    #Calculamos 
    sueldo = numhortra * valhortra
    print(f"El empleado {nombre} tiene un salario de {sueldo}")
    #volvemos a preguntar
    pregunta = str(input("Desea procesar empleado?: Y/N ")).lower().strip()
    
