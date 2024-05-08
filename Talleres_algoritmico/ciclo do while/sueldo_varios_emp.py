#Aca seguimos 
"""
un algoritmo que calcule e imprima el sueldo de varios empleados, cada empleado se tratará 
en forma similar al problema de cálculo de sueldo de un empleado.
"""
#Creamos el while 
while True:
    #Vamos a empezar pidiendo la informacion
    nombre = input("Ingrese el nombre de el empleado ==> ").capitalize()
    num_hor = int(input("Ingrese el numero de hora trabajada ==> "))
    val_hor = float(input("Ingrese el valor de la hora ==> "))
    #Calculamos el valor de su sueldo 
    sueldo = num_hor * val_hor
    print(f"El empleado {nombre} tiene un sueldo de ${sueldo:,.0f}")
    #preguntamos si se quiere añadir otro empleado
    otro = str(input("Desea añadir otro empleado: Y/N ").lower().strip())
    
    if otro == "y":
        print("Perfecto!")
    else:
        print("Muchas gracias!")
        break
    
