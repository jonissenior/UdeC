"""
Elaborar un algoritmo tal que dado como datos el nombre, cédula, la categoría y el sueldo de un 
trabajador, que calcule el aumento correspondiente del sueldo, teniendo en cuenta la siguiente tabla. E 
imprima el nombre, cédula, y el nuevo sueldo.

|Categoria |  Aumento |
|   1      |     15%  |
|   2      |     10%  |
|   3      |     8%   |
|   4      |     7%   |

"""

#Empezamos pidiendo y recibiendo los valores que son ncesarios 
nombre = input("Ingrese su nombre ==> ")
cedula = int(input("Ingrese el numero de su cedula ==> "))
categoria = int(input("Ingrese su categoria (De 1 a 4) ==> "))
sueldo = float(input("Ingrese su sueldo ==> "))

#Ahora vamos a verificar que categoria es y asi mismo ver el resultado
if categoria == 1:
    sueldo_aumento = sueldo + sueldo * 0.15
elif categoria == 2:
    sueldo_aumento = sueldo + sueldo * 0.10
elif categoria == 3:
    sueldo_aumento = sueldo + sueldo * 0.8
elif categoria == 4:
    sueldo_aumento = sueldo + sueldo * 0.7
else:
    sueldo_aumento = sueldo 

print(f"El empleado {nombre} de cedula {cedula}, tiene un sueldo de {sueldo:,.0f}, el cual, al revisar su categoria, quedaria en {sueldo_aumento:,.0f}.")