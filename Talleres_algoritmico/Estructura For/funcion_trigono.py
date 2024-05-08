#FOr(Duro)
import math
"""
 Elaborar un algoritmo que imprima el valor del seno, coseno y arcotangente de X; para valores de X 
desde -1 hasta 1 con intervalos de 0.2. Debe imprimir la siguiente tabla.

|X    | SENOX  |   COSENOX   |    ARCOTANGENTEX |
|_____|________|_____________|_________________ |
|-1.0 | 99.99  |   99.99     |       99.99      |
|-0.8 | 99.99  |   99.99     |       99.99      |
|.    |        |             |                  |
|.    |        |             |                  |
|.    |        |             |                  |
|1.0  | 99.99  |   99.99     |       99.99      |
"""
# Imprime los encabezados de la tabla
print("|  X  | SENOX | COSENOX | ARCOTANGENTEX |")
print("|-----|-------|---------|---------------|")

# Calcula e imprime los valores para cada X en el rango [-1, 1] con intervalos de 0.2
for i in range(-10, 11, 2):
    x = i / 10.0
    seno = math.sin(x)
    coseno = math.cos(x)
    arcotangente = math.atan(x)
    print("| {:.1f} | {:.4f} |  {:.4f} |     {:.4f}     |".format(x, seno, coseno, arcotangente))
