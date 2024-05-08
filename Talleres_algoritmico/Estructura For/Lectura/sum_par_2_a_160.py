#For
"""
Elaborar un algoritmo que calcule e imprima la suma de los números pares del 2 hasta el 160
Análisis del problema
2+4+6+8+…+160 = ?
"""
suma = 0
for i in range(1,161,2):
    suma += i
    print(suma)    