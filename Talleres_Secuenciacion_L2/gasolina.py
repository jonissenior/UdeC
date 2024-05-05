# Calcula precio venta estacion de gasolina
"""
Elaborar un algoritmo  que resuelva el problema que tienen 
en una estación de gasolina. Los surtidores de la misma 
registran lo que “surten” en galones, pero el precio de la gasolina 
está fijado en litros. El algoritmo  debe calcular 
e imprimir lo que hay que cobrarle al cliente.
"""

#Registrar el surtido de gasolina
galones = float(input("Ingrese cuantos galones de gasolina contiene ==> "))
litros = float(input("Ingrese cuantos litros son ==> "))

#Ahora hacemos la opereacion para obetener el precio de venta
precio = galones * 3.785 * litros

#Mostramos el precio final 
print(f"El precio que se debe cobrar es de ${precio:.0f} dolares ")

