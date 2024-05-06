"""
 Elaborar un algoritmo tal que lea una letra e imprima la letra, y si es vocal minúscula o vocal 
mayúscula
    
"""

#Primero vamos a solicitar la letra
letra = str(input("Ingrese la letra a identificar ==> "))
#Usamos condicionales
if letra in ["a","e","i","o","u"]:#Usamos arrays para facilitar el codigo 
    print("Es vocal minuscula ")
elif letra in ["A","E","I","O","U"]:#y con arrays tenemos mejor orden
    print("Es vocal mayuscula ")
else:
    print("No es vocal ")
