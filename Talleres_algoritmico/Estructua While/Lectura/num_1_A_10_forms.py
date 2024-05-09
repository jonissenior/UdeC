#Estructuras
"""
 Elaborar un algoritmo que imprima los números enteros del 1 al 10, de tres formar diferentes
a. Utilizando FOR
b. Utilizando Do while
c. Utilizando While
"""
#Primero un ciclo for
for i in range(1, 11):
    print(i)

#Ahora vamos por un while
i = 1
while i <= 10:
    print(i)
    i += 1

#Y por ultimo Do while
i = 1
while True:
    print(i)
    i += 1
    if i > 10:
        break
