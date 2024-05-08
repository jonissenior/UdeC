#Otro mas no hace daño
"""
En un hospital se ha hecho un estudio sobre los pacientes registrados durante los últimos 10 años, 
con el objeto de hacer una aproximación de los costos de internación por paciente. Se obtuvo un costo 
promedio diario según el tipo de enfermedad que aqueja al paciente. Además, se pudo determinar que 
en promedio todos los pacientes con edad entre 14 y 22 años implican un costo adicional del 10%. La 
siguiente tabla expresa los costos diarios, según el tipo de enfermedad.

|TIPO ENFERMEDAD |  COSTO/PACIENTE/DÍA |
|       1        |       $250000       | 
|       2        |       $160000       | 
|       3        |       $200000       | 
|       4        |       $320000       |
 
Elaborar un algoritmo que calcule e imprima el costo total que representa un paciente.

"""
#Para empezar vamos a requerir todos los datos del paciente
nombre = str(input("Dame el nombre de el paciente ==> "))
documento = int(input("Ahora su documento de identidad ==> "))
edad = int(input("Dame la edad ==> "))
print("Tipos de enfermedad: 1,2,3,4")
tipo_enfermedad = int(input("Dame el numero de el tipo de enfermedad ==> "))
num_dias_interno = int(input("Y por ultimo los dias internados ==> "))
#Ahora vamos a dar el valor total dependiendo de el numero de dias y el tipo de enfermedad
if tipo_enfermedad == 1:
    costo = num_dias_interno * 250000
elif tipo_enfermedad == 2:
    costo = num_dias_interno * 160000
elif tipo_enfermedad == 3:
    costo = num_dias_interno * 200000
elif tipo_enfermedad == 4:
    costo = num_dias_interno * 320000
else:
    print("Ese tipo de enfermedad no existe")
#Ahora verificamos con la edad si se agrega un 10%
if edad >= 14 and edad <= 22:
    costo = costo + costo*0.10
else:
    costo = costo
#Ahora solo resta mostrar los resultados 
print(f"El paciente es {nombre} de documento {documento} con edad de {edad}, lleva {num_dias_interno} dias interno con una enfermedad tipo {tipo_enfermedad}")
print(f"Por lo tanto su costo total es de {costo:,.0f}")