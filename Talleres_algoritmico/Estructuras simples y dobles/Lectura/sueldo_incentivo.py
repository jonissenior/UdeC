"""
Siguiendo con el mismo ejemplo de cálculo de sueldo de un empleado, ahora se otorga un incentivo de 5% 
del sueldo, si el empleado trabaja más de 40 horas; es decir, al sueldo se le agrega el 5% de mismo sueldo.

"""

#Vamos a solicitar los valores necesarios para operar 
nombre = input("Ingrese su nombre ==> ")
numero_horas = int(input("Ingrese el numero de horas trabajadas ==> "))
valor_hora = float(input("ingrese el valor de la hora trabajada ==>"))
#Ahora vamos a calcular el sueldo 
sueldo = numero_horas * valor_hora
#Ahora miramos si cumple con la condicion para el incentivo
if numero_horas > 40:
    
    sueldo_incentivo = sueldo + sueldo * 0.5
    
    print(f"El empleado {nombre} tiene un sueldo de {sueldo:,.0f} pero con el incentivo queda en {sueldo_incentivo:,.0f}. ")
else:
    print(f"El empleado {nombre} tiene un sueldo de {sueldo:,.0f} y no gana incentivo")

