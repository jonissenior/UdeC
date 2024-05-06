#Sueldo soble
"""
 Siguiendo con el ejemplo de cálculo de sueldo de un empleado, ahora si el número de horas trabajadas es 
mayo que 40, el excedente de 40 se paga al doble del valor por hora. En caso de no ser mayor que 40, se paga 
el valor de hora normal.
"""
#Vamos a solicitar los valores necesarios para operar 
nombre = input("Ingrese su nombre ==> ")
numero_horas = int(input("Ingrese el numero de horas trabajadas ==> "))
valor_hora = float(input("ingrese el valor de la hora trabajada ==> "))
#Ahora usamos el if para saber cual sera el sueldo a dar
if numero_horas <= 40:
    sueldo = numero_horas*valor_hora
    #Aprovechamos para mostrar el resultado
    print(f"El empleado {nombre} tiene un salario de {sueldo:,.0f} y no cuenta con extra")
else:
    sueldo = 40*valor_hora + (numero_horas-40)*valor_hora*2
    #Tambien mostramos si es necesario
    print(f"El empleado {nombre} tiene un sueldo de {sueldo:,.0f} gracias a el doble")

