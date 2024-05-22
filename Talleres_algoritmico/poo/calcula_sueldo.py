"""
laborar un algoritmo que permita calcular el sueldo de un empleado, conociendo su nombre, 
número de horas trabajadas y valor de hora trabajada. El algoritmo debe imprimir el nombre y el sueldo. 
Utilizar POO.
"""

# Definir funciones para establecer datos del empleado y calcular su sueldo
def establecer_nom_empl(nomE):
    global nomEmp
    nomEmp = nomE

def establecer_valor_hra_trab(valorHraT):
    global valorHraTrab
    valorHraTrab = valorHraT

def establecer_num_hr_trab(numHTrab):
    global numHrasTrab
    numHrasTrab = numHTrab

def calcular_sueldo():
    global sueldo
    sueldo = valorHraTrab * numHrasTrab

def obtener_nom_empl():
    return nomEmp

def obtener_sueldo():
    return sueldo

# Método principal
def main():
    # Solicitar datos del empleado al usuario
    nom = input("Ingrese el nombre del empleado: ")
    numHT = int(input("Ingrese el número de horas trabajadas: "))
    valorHT = float(input("Ingrese el valor de la hora trabajada: "))

    # Establecer datos del empleado
    establecer_nom_empl(nom)
    establecer_valor_hra_trab(valorHT)
    establecer_num_hr_trab(numHT)

    # Calcular sueldo
    calcular_sueldo()

    # Imprimir nombre del empleado y sueldo
    print("Nombre del empleado:", obtener_nom_empl())
    print("Sueldo:", obtener_sueldo())

# Llamar al método principal
main()
