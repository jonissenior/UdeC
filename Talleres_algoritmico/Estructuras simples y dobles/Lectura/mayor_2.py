#num mayor de 2 nums
"""
Elaborar un algoritmo que lea dos números enteros diferentes y que calcule e imprima el mayor.
Solución
"""
#Primero pedimos los dos numeros
num1 = int(input("Ingrese el primer numero ==> "))
num2 = int(input("Ingrese el segundo numero ==> "))
#usamos el if para saber cual es mayor
if num1 > num2:
    mayor = num1
else:
    mayor = num2
    
print(f"Tenemos los numeros {num1,num2} por lo que el mayor es {mayor}")