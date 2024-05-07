"""
Elaborar un algoritmo que lea tres números enteros diferentes, que calcule e imprima el mayor. 
Hacerlo de tres formas diferente, así:
a. Utilizando If then / else
b. Utlizando if then y AND
c. Utilizando if then/ else y AND

"""
#Separacion entre codigos 
"""
#Este es el codigo de la primera forma A. 
#Primero vamos a requerir los 3 numeros 
num1 = int(input("Ingrese el primer numero ==> "))
num2 = int(input("Ingrese el segundo numero ==> "))
num3 = int(input("Ingrese el tercer numero ==> "))
#Empezamos a aplicar los modos 
if num1 > num2:
    if num1 > num3:
        print(f"El numero mayor es {num1}")
    else:
        print(f"El numero mayor es {num3}")
else:
    if num2 > num3:
        print(f"El numero mayor es {num2}")    
    else:
        print(f"El numero mayor es {num3}")  
"""
#Separacion entre codigos
"""
#Este es el codigo de la forma B.
#Primero vamos a requerir los 3 numeros 
num1 = int(input("Ingrese el primer numero ==> "))
num2 = int(input("Ingrese el segundo numero ==> "))
num3 = int(input("Ingrese el tercer numero ==> "))
#Empezamos a aplicar los modos 
if num1 > num2 and num1 > num3:
    print(f"El numero mayor es {num1}")

if num2 > num1 and num2 > num3:
    print(f"El numero mayor es {num2}")

if num3 > num1 and num3 > num2:
    print(f"El numero mayor es {num3}")
"""   
#Separacion entre codigos
#Primero vamos a requerir los 3 numeros 
num1 = int(input("Ingrese el primer numero ==> "))
num2 = int(input("Ingrese el segundo numero ==> "))
num3 = int(input("Ingrese el tercer numero ==> "))
#Empezamos a aplicar los modos 
if num1 > num2 and num1 > num3:
    print(f"El numero mayor es {num1}")
else:
    if num2 > num3:
        print(f"El numero mayor es {num2}")
    else:
        print(f"El numero mayor es {num3}")