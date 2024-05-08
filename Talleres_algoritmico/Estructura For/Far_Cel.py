#For
"""
Una temperatura en grados Fahrenheit se convierte a grados Celsius, con la siguiente ecuación 
C=5/9*(F -32). Elaborar un algoritmo que imprima una tabla desde 1 hasta 65 ( con intervalos de 1) 
grados Fahrenheit con sus equivalencias en grados Celsius.

Fahrenheit    Celsius
______________________
1              99.99
2              99.99
3              99.99
.
.
.
65             99.99
"""
#Primero imprimimos el encabezado
print("Fahrenheit    Celsius")
print("_____________________")
#Empezamos a usar el ciclo for
c = 0
for i in range(1,65, 1):
    c = 5/9*(i - 32)
    print(f"{i}              {c:,.2f}")
