#For dificilito
"""
Una Universidad tiene actualmente 10000 estudiantes, se espera tener un crecimiento anual del 5%. 
Elaborar un algoritmo que calcule e imprima la población estudiantil que se espera tener en el año 2025.
"""
#Asignamos los 10000 estudiantes 
poblacion = 10000

#Vamos directos a el ciclo for 
#Donde haremos el calculo
for i in range(2021,2025, 1):
    #calculamos la poblacion
    poblacion = poblacion + poblacion * 0.5 
print("En el 2021 la poblacion es de 10,000")
print(f"La poblacion en el 2025 sera de {poblacion:,.0f}")