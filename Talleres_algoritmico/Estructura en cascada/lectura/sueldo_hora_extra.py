#OTRO MAS
"""
 Elaborar un algoritmo que permita calcular lo que hay que pagarle a un trabajador teniendo en 
cuenta su sueldo y las horas extras trabajadas. Para el pago de horas extras se tiene en cuenta la 
categoría del trabajador, de acuerdo con la siguiente tabla.

|CATEGORIA  |  PRECIO HORA EXTRA |
|    1      |        $10000      |
|    2      |        $15000      |
|    3      |        $20000      |
|    4      |        $25000      |
    
A los trabajadores con categoría mayor a 4 no se les pagan horas extras.
Cada trabajador puede tener como máximo 30 horas extra, si tiene más se le pagarán 30.
El algoritmo debe imprimir nombre del trabajador, categoría, nuevo sueldo.
"""
#Primero vamos a solicitar la informacion necesaria
nombre = str(input("Ingrese el nombre de el trabajodor ==> "))
categoria = int(input("Ingrese la categoria (1,2,3,4) ==> "))
sueldo = float(input("Ingrese su sueldo ==> "))
num_horas_ext = int(input("Ingrese el numero de horas extras ==> "))
#Ahora vamos a añadir el valor dependiendo de la categoria 
if categoria == 1:
    precio_extra = 10000
elif categoria == 2:
    precio_extra = 15000
elif categoria == 3:
    precio_extra = 20000
elif categoria == 4:
    precio_extra = 25000
else:
    precio_extra = 0
#Ahora daremos el nuevo sueldo
if num_horas_ext <= 30:
    new_sueldo = sueldo + num_horas_ext*precio_extra
else:
    new_sueldo = sueldo + 30*num_horas_ext
#Ahora mostramos el resultado final 
print(f"El empleado {nombre} se encuentra en categoria {categoria} y con un sueldo de ${sueldo:,.0f} por lo tanto el  su nuevo sueldo es de ${new_sueldo:,.0f}")
