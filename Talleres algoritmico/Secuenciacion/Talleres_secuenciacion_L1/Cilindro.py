from math import pi

# Calcula area y volumen de un cilindro
"""
Elaborar un algoritmo tal que dado como datos  
el radio y la altura de un cilindro.  
Que calcule e imprima el área y su volumen.
"""
#Ingresar datos
print("Area y volumen de cilindro")
radio = float(input("Ingrese el radio ==> "))
altura = float(input("Ingrese la altura ==> "))

#Calcular area y volumen
area = 2*pi*radio*altura
volumen = 2*pi * radio*(radio+altura)

#Mostrar resultados
print(f"El area del cilindro es: {area:.4f}")
print(f"El volumen del cilindro es: {volumen:.4f}")