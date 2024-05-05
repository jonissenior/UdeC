from math import pi

def AreaTriangulo(b, h):
    return (b * h)/2
print("Esta es la base del triangulo ")
b = float(input("Ingrese base ==> "))
h = float(input("Ingrese altura ==> "))

print("Area del triangulo = ", AreaTriangulo(b,h))

def AreaRectangulo(b, h):
    return b * h
print("Esta es la base del rectangulo ")
b = float(input("Ingrese base ==> "))
h = float(input("Ingrese altura ==> "))

print("Area del rectangulo = ", AreaRectangulo(b,h))

def AreaCirculo(r):
    return pi * r ** 2
print("Esta es la base del circulo")
r = float(input("Ingrese radio ==> "))

print("Area del circulo = ", AreaCirculo(r))

