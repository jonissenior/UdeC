#Para esto, en python debemos importar math
from math import pi

"""
Elaborar un algoritmo que ofrezca un menú de opciones, mediante el cual se pueda escoger calcular 
el área de las figuras geométricas: triangulo, cuadrado, rectángulo y circulo. Un vez seleccionada la 
opción, que llame a un método que permita solicitar y leer los datos necesarios, hacer el calculo 
correspondiente e imprimirlo. 

ÁREAS DE FIGURAS GEOMÉTRICAS 
1. TRIANGULO
2.CUADRADO
3.RECTANGULO
4.CIRCULO
5.FIN
OPCIÓN:

Nota:
areaTriangulo = base*altura/2
areaCuadrado=lado**2
areaRectangulo= base*altura
areacirculo= pi*r**2
2
"""
#Nuestra primera funcion sera la encargada de lo que veremos en el menu
def Mostrarmenu():
    print("AREAS DE FIGURAS GEOMETRICAS")
    print("1. Triangulo")
    print("2. Cuadrado")
    print("3. Rectangulo")
    print("4. Circulo")
    print("5. FIN")    
    return int(input("Ingrese la opcion: ")) #Y lo que guardamos en el return es la eleccion
#Creamos la primera funcion, que sera el area de el triangulo
def area_triangulo():
    base = float(input("Ingrese la base de el triangulo ==> "))
    altura = float(input("Ingrese la altura de el triangulo ==> ")) #Es simplemente codigo sencillo
    area = base*altura/2
    print(f"El area de el triangulo es = {area:.1f}")
#Ahora continuamos con el area de el cuadrado
def area_cuadrado():
    lado = float(input("Ingrese el valor de el lado de el cuadrado ==> "))
    area = lado ** 2
    print(f"El area de el cuadrado es = {area:.1f}")
#Ahora hacemos la funcion de el rectangulo
def area_rectangulo():
    base = float(input("Ingrese la base de el rectangulo ==> "))
    altura = float(input("Ingrese la altura de el rectangulo ==> "))
    area = base * altura
    print(f"EL area de el rectangulo = {area:.1f}")
#Y la funcion de el area de el circulo 
def area_circulo():
    radio = float(input("Ingrese el radio de el circulo ==> "))
    area = pi*(radio**2)
    print(f"El area de el circulo es = {area:.1f}")
#Ahora hacemos la funcion para saber que ejecutar 
def main():
    while True:
        opcion = Mostrarmenu()
        if opcion == 1:
            area_triangulo()
        elif opcion == 2:
            area_cuadrado()
        elif opcion == 3:
            area_rectangulo()
        elif opcion == 4:
            area_circulo()
        elif opcion == 5:
            break
        else:
            print("Esa opcion no es correcta, elige de el 1 al 5 !! :)")
            
#Ahora solo ejecutamos el main para que se ejecute todo 
main()
     
    
    


