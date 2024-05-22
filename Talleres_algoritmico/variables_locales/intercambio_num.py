"""
Elaborar un algoritmo que permita leer dos números de tipo real en el método principal; que en un 
método los intercambie vía parámetros por referencia, y los imprima en el método principal.
Solución
Análisis del problema
5.0 3.0
3.0 5.0
"""

# Definir el método para intercambiar los valores
def intercambiar(valores):
    aux = valores[0]
    valores[0] = valores[1]
    valores[1] = aux

# Método principal
def main():
    # Solicitar los dos números
    a = float(input("Ingrese el primer número ==> "))
    b = float(input("Ingrese el segundo número ==> "))

    # Mostrar los valores antes del intercambio
    print(f"Antes del intercambio: a = {a}, b = {b}")

    # Llamar al método intercambiar
    valores = [a, b]
    intercambiar(valores)

    # Mostrar los valores después del intercambio
    print(f"Después del intercambio: a = {valores[0]}, b = {valores[1]}")

# Ejecutar el método principal
main()
