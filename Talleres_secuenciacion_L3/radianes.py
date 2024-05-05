#Aca importamos math, para usar la funcion pi
import math

# Conversor de rad-grad y grad-rad
"""
Elaborar un algoritmo que permita leer un número en radianes e 
imprima su equivalencia en grados; asimismo, que permita 
leer un número en grados e imprima su equivalencia en radianes. 
"""
#vamos  a  radianes y angulo para operar
radian = float(input("Ingrese los radianes ==> "))
grados = float(input("Ingrese los grados ==> "))
#Ahora calculamos grados y radianes
radian_to_grado = radian * 180 / math.pi
grado_to_radian = grados * math.pi / 180
#Mostramos la informacion y los datos obtenidos 
print("************ GRADO Y RADIAN ************")
print("De radian a grado ")
print(f"Nos dan {radian} radian, lo cual al pasar a grado es igual a {radian_to_grado:.3f} grados.")
print("****************************************")
print("De grado a radian ")
print(f"Con un total de {grados} grados, al pasarlo a radian nos da como resultado {grado_to_radian:.3f} radian.")

