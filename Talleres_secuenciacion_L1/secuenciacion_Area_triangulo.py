# Calcula area de un triangulo 
"""
Elaborar un algoritmo para calcular el área de un triángulo.  
Se requiere imprimir como salida el área del triángulo.  
Los datos disponibles para lectura son la base y la altura del triángulo.
"""
#Pedir datos del triangulo
print("Area del triangulo")
base = float(input("Ingrese la base del triangulo ==> "))
altura = float(input("Ingrese la altura del triangulo ==> "))

#Calcular el area
area_triagulo = (base * altura)/2
#mostrar resultados
print(f"El area es: {area_triagulo}")