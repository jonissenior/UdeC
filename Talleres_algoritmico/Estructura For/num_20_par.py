#For 
"""
 Elaborar un algoritmo que lea 20 números enteros y que calcule e imprima el promedio de dichos 
números.
Solución
Análisis del problema
5, 7, 9,….15

"""
# Inicializamos la suma en 0
suma = 0
# Leemos 20 números
for i in range(20):
    numero = int(input(f"Ingrese el número {i+1}: "))
    suma += numero
# Calculamos el promedio
promedio = suma / 20
# Imprimimos el promedio
print(f"El promedio de los números ingresados es: {promedio}")
