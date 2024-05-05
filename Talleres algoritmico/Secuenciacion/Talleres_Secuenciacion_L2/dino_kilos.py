"""
Elaborar un algoritmo tal que dado como datos el nombre de un 
dinosaurio, su peso  y su longitud, expresados estos 
dos últimos en toneladas y pies respectivamente; que 
imprima el nombre del dinosaurio, su peso en kilogramos y 
su longitud en metros. 
"""

#Solicitar datos
nombre = input("Dime el nombre de tu dinosaurio ==> ")
peso = float(input("Ahora dime su peso en toneladas ==> "))
longitud = float(input("Y por ultimo su longitud en pies ==> "))

#transformar datos y guardar los mismos
ton_a_kilos = peso * 1000
pies_a_metros = longitud * 0.32

#mostrar los datos
print
print(f"El nombre de tu dinosaurio es: {nombre}")
print(f"El peso inicial era de {peso:,.0f} toneladas, las cuales en kilos equivalen a {ton_a_kilos:,.0f} kilos. ")
print(f"Y la longitud inical era de {longitud:,.0f} pies, que a la hora de pasarlo a metros seria {pies_a_metros:,.0f} metros. ") 



