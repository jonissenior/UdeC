# Conversor dias a segundos
"""
Elaborar un algoritmo  que calcule e imprima el número de 
segundos que hay en un determinado número de días. 
"""
#Recibimos los dias que se quiera saber cuantos segundos hay
dias = int(input("Ingrese los dias ==> "))

#Realizamos la operacion para saber el total de segundos

segundos = dias * 86400 #Aca 86,400 es el total de segundos en un dia, es una constante

#Mostramos el resultado de segundos 
print(f"En {dias} dias, hay {segundos} segundos ")
