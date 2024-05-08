#OLIS
"""
En este codigo sencillo lo unico que vamos a hacer es una pequeña pregunta en un ciclo while
"""
#Vamos a ello
while True:
    
    respuesta = str(input("Intenta adivinar la vocal: digita una vocal ==> "))
    
    if respuesta == "a":
        print("Es correcto, esa es!!")
        break
    else:
        print("mmm, esa no parece ser la opcion correcta :C ")