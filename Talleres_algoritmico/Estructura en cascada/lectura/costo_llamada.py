#Vamos por uno mas :)
"""
 El costo de las llamadas telefónicas internacionales dependen de la zona geográfica en la que se 
encuentre el país destino y del número de minutos hablados. En la siguiente tabla se presenta el costo 
de minuto por zona. A cada zona se le ha asignado una clave.

|CLAVE|       ZONA          |    PRECIO |
|12   | América del Norte   |       2   | 
|15   |  América Central    |     2.2   | 
|18   |   América del Sur   |     4.5   |
|19   |      Europa         |     3.5   |
|23   |       Asia          |       6   |
|25   |      África         |       6   |
|29   |       Oceanía       |       5   |

Elaborar un algoritmo que permita calcular e imprimir el costo total de una llamada.
"""
#Primero vamos a recibir las variables para operar
num_min = int(input("Ingresa el numero de minutos ==> "))
clave = int(input("Ingrese su clave ==> "))
#Ahora usamos ifs para dar resultado dependiendo de las elecciones
if clave == 12:
    cost = num_min * 2
elif clave == 15:
    cost = num_min * 2.2
elif clave == 18:
    cost = num_min * 4.5
elif clave == 19:
    cost = num_min * 3.5
elif clave == 23:
    cost = num_min * 6
elif clave == 25:
    cost = num_min * 6
elif clave == 29:
    cost = num_min * 5
else:
    print("Este clave no es correcta ;C")
#Mostramos el costo total
print(f"El total de la llamada es de ${cost}")



