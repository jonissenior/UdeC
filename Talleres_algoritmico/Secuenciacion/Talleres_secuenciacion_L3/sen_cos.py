#Importamos la libreria math donde usaremos las funciones de sin(seno) y cos(coseno)
import math
# Calcula seno y coseno
"""
Elaborar un algoritmo que permita leer el tamaño de un ángulo 
en radianes, luego que calcule e imprima el valor del seno y del coseno 
"""
#Recibimos el angulo en radianes
angulo = float(input("Ingrese el angulo (en radianes) ==> "))
#Vamos a usar math para pasar el angulo a su correspondiente y guardamos su resultado en una variable
seno = math.sin(angulo)
coseno = math.cos(angulo)
#Ahora mostramos los resultados 
print("************** SENO Y COSENO **************")
print("El seno es ")
print(f"Dado un angulo {angulo}, su seno corresponde a {seno:.3f}. ")
print("*******************************************")
print("El coseno es ")
print(f"Dado el angulo {angulo}, tenemos que su coseno es {coseno:.3f}. ")
