"""
 Elaborar un algoritmo que lea un número entero entre 0 y 9 e imprima el número y si es par o impar
"""
#Creamos dos arrays donde guardar los numeros
#Es un pequeño adicional que he decidido agregar :)
par = [0,2,4,6,8]
impar = [1,3,5,7,9]

#Recibimos el numero que queramos usar 
num = int(input("Ingrese el numero que quiera verificar==> "))

#Utilizaremos las condicionales para ddeterminar el resultado 
#y de una mostramos el resultado
if num in par:
    print("Es par")
elif num in impar:
    print("Es impar")
else:
    print("Ese numero no esta de el 0 al 9")
