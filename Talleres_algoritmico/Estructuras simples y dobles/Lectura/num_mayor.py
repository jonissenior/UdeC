#Vamos a sacar el numero mayor de una lista de numeros 
"""
Elaborar un algoritmo que lea cinco números enteros y calcule e imprima el mayor. Se supone que son 
números diferentes
"""
#Primero vamos a solicitar los 5 numeros 
num1 = int(input("Ingresa el primer numero ==> "))
num2 = int(input("Ingresa el segundo numero ==> "))
num3 = int(input("Ingresa el tercer numero ==> "))
num4 = int(input("Ingresa el cuarto numero ==> "))
num5 = int(input("Ingresa el quinto numero ==> "))

#Ahora vamos a calcular el mayor numero con if
mayor = num1

if num2 > mayor:
    mayor = num2

if num3 > mayor:
    mayor = num3

if num4 > mayor:
    mayor = num4
    
if num5 > mayor:
    mayor = num5

#Ahora solo nos queda mostrar el numero mayor
print(f" Teniendo los numeros {num1,num2,num3,num4,num5} sabemos que el numero mayor es {mayor}")