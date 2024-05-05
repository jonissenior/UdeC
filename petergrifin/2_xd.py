#Promedio salarial 
"""
si una persona recibe por un salario por trabajar 30 dias y 8 horas dias, determine el salario si:
1. Si el salario es 1.800.000 y trabaja 15 dias mas 6 horas cual es el salario
2. Si el salario es de 1.500.000 y trabaja 80 horas con recargo del 25% y 40 horas de recargo del 35%, cual es su salario
3. Si el salario es de 1.600.000 y tabaja 2 semanas mas 3 dias + 7 horas con un descuento del 10% por cada hora trabajada cual es el salario
"""
#1. Se le pide el salario al usuario 
salario = int(input("Ingrese su salario ==> "))

# Segun el salario ingresado se hara su respectivo calculo 
if salario == 1800000:
    dia = salario/30 #promedio por dia
    hora = dia/8 #Promedio por hora
    total_1 = (dia*15 + hora * 6) + salario
    total_2 = (dia*15 + hora * 6)
    print(f"El salario ${salario:,.0f} tendra un monto de ${total_2:,.0f}")
    print(f"Por 15 dias y 6 horas de trabajo para un total de: ${total_1:,.0f}")
elif salario == 1500000:
    dia = salario/30 #promedio por dia
    hora = dia/8 #Promedio por hora
    recargo_1 = ((hora * 80)*0.25) + hora * 80
    recargo_2 = ((hora * 40)*0.35) + hora * 40
    total_1 = salario + recargo_1 + recargo_2
    total_2 = recargo_1 + recargo_2
    print(f"El salario ${salario:,.0f} tendra un monto de ${total_2:,.0f}")
    print(f"Por un recargo de 80 horas (25%) y 40 horas (35%) ${total_1:,.0f}")
elif salario == 1600000:
    dia = salario/30 #promedio por dia
    hora = dia/8 #Promedio por hora
    recargo = (hora * 7)
    descuento = salario + ((dia * 17) + recargo)
    total_1 = descuento - (descuento * 0.10)
    total_2 = (dia * 17) + recargo
    print(f"El salario ${salario:,.0f} tendra un monto de ${total_2:,.0f}")
    print(f"Por el recargo de 2 semanas mas 3 dias y 7 horas con un descuento del 10% {total_1:,.0f}")
else:
    print("salario no registrado")
