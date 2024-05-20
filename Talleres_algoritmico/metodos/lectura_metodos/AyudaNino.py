"""
referentes a las operaciones 
aritméticas fundamentales: sumar, restar, multiplicar y dividir. 
 
El proceso es el siguiente: 
 
Se ofrecerá un menú de opciones para escoger lo que desea hacer  de acuerdo con el siguiente formato: 
 
 
TE PUEDO AYUDAR A: 
1. SUMAR 
2.RESTAR 
3.MULTIPLICAR 
4.DIVIDIR 
5.FIN 
OPCIÓN: 
 
En caso de el niño seleccione la opción 1; está indicando que desea revisar operaciones de sumar, 
enseguida se debe establecer un proceso interactivo para que el niño introduzca los dos números a 
sumar y su resultado, luego que el computador le indique si la suma está correcta o incorrecta; en 
seguida le pregunte si desea revisar otra suma, si es así, deberá repetir todo el proceso para revisar la 
siguiente suma.  Y así con las demás operaciones. 
 
Ejemplo: 
 
    5 + 3 = 7        la suma es incorrecta 
    5 + 3 = 8       la suma es correcta
"""
#Empezamos haciendo una funcion que dara las opciones
def mostrarMenu():
    print("TE PUEDO AYUDAR A:") #Mostramos opciones
    print("1.Sumar")
    print("2.Restar")
    print("3.Multiplicar")
    print("4.Dividir")
    print("5.Salir")
    return int(input("OPCION ==> "))#Guardamos la eleccion

#Aca la funcion de la suma
def ayuda_sumar():
    while True:
        num1 = int(input("Ingrese el primer numero ==> "))#Se piden los valores
        num2 = int(input("Ingrese el segundo numero ==> "))
        resultado_Niño = int(input("Introduzca el resultado de la suma ==> "))
        resultado_Maquina = num1 + num2
        if resultado_Maquina == resultado_Niño: #Se usa un if para comparar resultados
            print("LA SUMA ES CORRECTA!")
        else:
            print("LA SUMA ES INCORRECTA!")
        continuar = str(input("¿Desea comprobar otra suma (Y/N) ? ==>")).upper()
        if continuar != "Y": #Otro if para saber si seguir mirando las sumas
            break

#Aca esta la funcion de la resta
def ayuda_resta():
    while True:
        num1 = int(input("Ingrese el primer numero ==> "))
        num2 = int(input("Ingrese el segundo numero ==> "))
        resultado_Niño = int(input("Introduzca el resultado de la resta ==> "))
        resultado_Maquina = num1 - num2
        if resultado_Maquina == resultado_Niño: #En esta todo es igual a la suma pero cambia el calculo
            print("LA RESTA ES CORRECTA!")
        else:
            print("LA RESTA ES INCORRECTA!")
        continuar = str(input("¿Desea comprobar otra resta (Y/N) ? ==> ")).upper()
        if continuar != "Y":
            break
        
#Ahora la funcion de la multiplicacion
def ayuda_multiplicacion():
    while True:
        num1 = int(input("Ingrese el primer numero ==> "))
        num2 = int(input("Ingrese el segundo numero ==> "))
        resultado_Niño = int(input("Introduzca el resultado de la multiplicacion ==> "))
        resultado_Maquina = num1 * num2
        if resultado_Maquina == resultado_Niño: #Aca igualmente es lo mismo pero con otro calculo
            print("LA MULTIPLICACION ES CORRECTA!")
        else:
            print("LA MULTIPLICACION ES INCORRECTA!")
        continuar = str(input("¿Desea comprobar otra multiplicacion (Y/N) ? ==> ")).upper()
        if continuar != "Y":
            break

#Sigue la funcion de la division 
def ayuda_division():
    while True:
        num1 = int(input("Ingrese el primer numero ==> "))
        num2 = int(input("Ingrese el segundo numero ==> "))
        resultado_Niño = int(input("Introduzca el resultado de la division ==> "))
        if num2 != 0:
            resultado_Maquina = num1/num2
            if resultado_Maquina == resultado_Niño: #En esta se usa un if para verificar que la division no sea por 0
                print("LA DIVISION ES CORRECTA!") #Pero como tal es la misma logica
            else:
                print("LA DIVISION ES INCORRECTA!")
        else:
            print("Error: Division por cero no permitida")
        continuar = str(input("¿Desea comprobar otra division (Y/N) ? ==> ")).upper()
        if continuar != "Y":
            break
    
#Ahora solo nos queda una funcion main con la que elegir que funcion sera usada
def main():
    while True:
        opcion = mostrarMenu() #mostramos el menu y guardamos su return
        #Usamos unos if y elif para saber que opcion es
        if opcion == 1:
            ayuda_sumar()
        elif opcion == 2:
            ayuda_resta()
        elif opcion == 3:
            ayuda_multiplicacion()
        elif opcion == 4:
            ayuda_division()
        elif opcion == 5:
            break
        else:
            print("Opcion no valida, por favor, elija una opcion del 1 al 5.")

#Solo quedam llamar la opcion main para ejecutar todo
main()