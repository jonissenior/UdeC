"""
 Elaborar un algoritmo que permita leer el tamaño de un ángulo en radianes, que calcule e imprima el 
valor del seno y del coseno.

"""
import math

# Función para establecer el tamaño del ángulo
def establecer_angulo(ang):
    global tamAngulo
    tamAngulo = ang

# Función para calcular el seno del ángulo
def calcular_seno():
    global senAng
    senAng = math.sin(tamAngulo)

# Función para calcular el coseno del ángulo
def calcular_coseno():
    global cosAng
    cosAng = math.cos(tamAngulo)

# Función para obtener el seno del ángulo
def obtener_seno():
    return senAng

# Función para obtener el coseno del ángulo
def obtener_coseno():
    return cosAng

# Método principal
def main():
    # Solicitar al usuario el tamaño del ángulo en radianes
    angulo = float(input("Ingrese el tamaño del ángulo en radianes: "))

    # Establecer el tamaño del ángulo
    establecer_angulo(angulo)

    # Calcular el seno y el coseno del ángulo
    calcular_seno()
    calcular_coseno()

    # Imprimir el seno y el coseno del ángulo
    print("Seno del ángulo:", obtener_seno())
    print("Coseno del ángulo:", obtener_coseno())

# Llamar al método principal
main()
