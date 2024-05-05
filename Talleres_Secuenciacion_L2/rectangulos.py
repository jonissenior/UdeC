# Calcule perimetro y superficie de un rectangulo
"""
Elaborar un algoritmo talque dado como datos la base y la 
altura  de un rectángulo, que calcule e imprima su 
perímetro y su superficie 
"""
#Vamos a recibir la base y altura del rectangulo
base = float(input("Ingrese la base ==> "))
altura = float(input("Ingrese su altura ==> "))

#Ahora vamos a realizar las operaciones, y guardar sus resultados 
perimetro = (base * 2) + (altura * 2)
superficie = base * altura

#Mostramos los resultados
print("************ RECTANGULO **************")
print("Perimetro del rectangulo ")
print(f"Con una base de {base:.0f} y una altura de {altura:.0f}, se obtiene un perimetro de {perimetro:.0f}.")
print("**************************************")
print("Superficie del rectangulo ")
print(f"Con una base de {base:.0f} y una altura de {altura:.0f}, se obtiene una superficie de {superficie:.0f}. ")

