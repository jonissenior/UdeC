"""
Elaborar un algoritmo similar al anterior de CALCULO DE SUELDO DOBLE DE UN EMPLEADO, pero ahora 
teniendo en cuenta que se tiene otra alternativa: las horas que exceden de 50 se pagan al triple del valor 
por hora.

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
    if numero_horas <= 50:
        sueldo =  40 * valor_hora+(numero_horas-40)* valor_hora*2
        #Aprovechamos para mostrar el resultado
        print(f"El empleado {nombre} tiene un salario de {sueldo:,.0f} gracias al doble")
    else:
        sueldo = 40*valor_hora + 10 *valor_hora *2 + (numero_horas-50)*valor_hora*3
        #Tambien mostramos si es necesario
        print(f"El empleado {nombre} tiene un sueldo de {sueldo:,.0f} gracias a el triple")

