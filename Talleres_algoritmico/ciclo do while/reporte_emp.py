#Vamos de vuelta
"""
 En el problema anterior de sueldos de varios empleados, es necesario que los datos se impriman en 
forma de un reporte que tenga el siguiente formato.

     REPORTE DE EMPLEADOS
     
|  NOMBRE           |       SUELDO    |
|___________________|_________________|
| XXXXXXXXXXXX      |       999.99    |
| XXXXXXXXXXXX      |       999.99    |
| .                 |                 |
| .                 |                 |
| .                 |                 |
| XXXXXXXXXXXX      |       999.99    |

|TOTAL 99 EMPLEADOS         9999.99   |

"""
total_emp = 0
sueldototal = 0
#Abrimos el while 
while True:
    #Lo primero es pedir los datos
    nombre = input("Ingrese el nombre de el empleado ==> ").capitalize()
    num_hor = int(input("Ingrese el numero de hora trabajada ==> "))
    val_hor = float(input("Ingrese el valor de la hora ==> "))
    #Calculamos el valor de su sueldo 
    sueldo = num_hor * val_hor
    print("NOMBRE                 SUELDO ")
    print(f"{nombre:<20} {sueldo:>10,.2f}")
    #Hacemos un calculo
    total_emp = total_emp + 1
    sueldototal = sueldototal + sueldo
    #preguntamos si se quiere añadir otro empleado
    otro = str(input("Desea añadir otro empleado: Y/N ").lower().strip())
    if otro == "y":
        ok = 0
    else:
        print("Muchas gracias!")
        break







