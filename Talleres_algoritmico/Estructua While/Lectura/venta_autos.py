#Uno duro
"""
l sueldo que perciben los vendedores de una empresa automotriz, está integrado de la siguiente 
manera. El salario mínimo (quincenal), más $100000 por cada auto vendido, más el 2% del valor de los 
autos vendidos.
Sueldo = SalarioMinimo + 100000*TotalAutosVendidos+ TotalVendido*0.02
Datos que se tienen por cada vendedor:
Nombre del vendedor: XXXXXXXXXXXXXXXX
 precioAuto: 999999.99
 precioAuto: 999999.99
 .
 .
 precioAuto: 999999.99
Nombre del vendedor: XXXXXXXXXXXXXXXX
 precioAuto: 999999.99
 precioAuto: 999999.99
 .
 .
 precioAuto: 999999.99
.
.
.
Como se puede apreciar, se tienen varios vendedores; por cada vendedor se tiene el nombre y el precio 
de cada auto vendido en la quincena. Es posible que algunos vendedores no hayan realizado venta 
alguna, en tal caso solo se le paga el salario mínimo quincenal.
Elaborar un algoritmo que permita leer los datos e imprimir el siguiente reporte:
 NOMINA QUINCENAL
NOMBRE VENDEDOR SUELDO
__________________________________________________
XXXXXXXXXXXXXXXXX 999999.99
XXXXXXXXXXXXXXXXX 999999.99
.
.
.
XXXXXXXXXXXXXXXXX 999999.99
Total 999 Vendedores 9999999.99
"""
# Inicializamos las variables
vendedores = []
total_vendedores = 0
total_sueldo = 0

# Definimos el salario mínimo quincenal
salario_minimo = 1000  # Ajusta este valor según sea necesario

while True:
    nombre = input("Ingrese el nombre del vendedor (o 'N' para terminar) ==> ")
    if nombre.upper() == 'N':
        break

    total_autos_vendidos = int(input(f"Ingrese el total de autos vendidos por {nombre} ==> "))
    total_vendido = 0
    for i in range(total_autos_vendidos):
        precio_auto = float(input(f"Ingrese el precio del auto  {str(i+1)} ==> "))
        total_vendido += precio_auto

    sueldo = salario_minimo + 100000*total_autos_vendidos + total_vendido*0.02
    vendedores.append((nombre, sueldo))
    total_vendedores += 1
    total_sueldo += sueldo

# Imprimimos el reporte
print("NOMINA QUINCENAL")
print("NOMBRE VENDEDOR SUELDO")
print("__________________________________________________")
for nombre, sueldo in vendedores:
    print(f"{nombre} {sueldo}")
print("Total", total_vendedores, "Vendedores", total_sueldo)
