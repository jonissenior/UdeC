"""
Elaborar un algoritmo que lea un número de día (un valor de a 1 a 7) ; e imprima domingo si es 1, 
lunes si es 2, ….., sábado si e 7

"""
#Vamos a recibir el valor que representa la opcion
dia = int(input("Ingrese una opcion de el 1 a el 7 ==> "))

#Vamos a hacer un if, elif y else para poder ordenar todas las opciones
if dia == 1:
    print("DOMINGO")
elif dia == 2:
    print("LUNES")
elif dia == 3:
    print("MARTES")
elif dia == 4:
    print("MIERCOLES")
elif dia == 5:
    print("JUEVES")
elif dia == 6:
    print("VIERNES")
elif dia == 7:
    print("SABADO")
else:
    print("Esa opcion no es valida :C")
