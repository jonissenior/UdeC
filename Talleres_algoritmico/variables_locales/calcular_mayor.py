"""
Elaborar un algoritmo que permita leer tres números de tipo entero e imprima el mayor, utilizando un 
método para leer los números, otro método para obtener y devolver el mayor y método para imprimir 
el mayor.
"""
# Definir método para capturar los números
def capturar_numeros():
    n1 = int(input("Ingrese el primer número ==> "))
    n2 = int(input("Ingrese el segundo número ==> "))
    n3 = int(input("Ingrese el tercer número ==> "))
    return n1, n2, n3

# Método para obtener el mayor de tres números
def obtener_mayor(x, y, z):
    mayor = x
    if y > mayor:
        mayor = y
    if z > mayor:
        mayor = z
    return mayor

# Método para imprimir el número mayor
def imprimir_mayor(m):
    print("El número mayor es:", m)

# Método principal
def main():
    # Capturar los números
    n1, n2, n3 = capturar_numeros()
    
    # Obtener el mayor
    mayor = obtener_mayor(n1, n2, n3)
    
    # Imprimir el mayor
    imprimir_mayor(mayor)

# Llamar al método principal
main()
