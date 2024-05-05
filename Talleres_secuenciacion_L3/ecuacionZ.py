#importamos math, para usar pi y raiz(sqrt)
import math
#Realizar la ecuacion
"""
Elaborar un  algoritmo que lea el valor de W e 
imprima el valor de Z, de la siguiente ecuación 

z = e**w**3  + Ln |w|
    √2 pi w  
"""
#Vamos a recibir el valor de W
w = int(input("Ingrese el valor de W ==> "))
#el if se encargara de realizar la ecuacion solo si w es positivo
if w > 0:
    #Vamos a empezar a realizar cada paso a paso desde a a g
    a = w ** 3 # w ** 3
    b = math.exp(a) # e ** w ** 3
    c = 2 * math.pi * w # 2*pi*w
    d = math.sqrt(c) # raiz de 2*pi*w
    f = abs(w) #absoluto de w |w|
    g = math.log(f) # Ln|w|
    z = b/d + g #final
    print("***************** ECUACION ****************")
    print("Ecuacion == z = e**w**3  + Ln |w|√2 pi w  ")
    print("*******************************************")
    print("Resultado ecuacion ")
    print(f"Teniendo que el valor de W es {w} , el resultado de Z equivale a {z:,.2f}")
#El else es para dar a entender que solo entero y postivo     
else:
    print("Debe ser un numero entero y positivo")