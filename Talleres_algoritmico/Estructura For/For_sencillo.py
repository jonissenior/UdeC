#FOR
"""
Pequeño documento de el uso de el ciclo For en python
"""
#Vamos a hacer una pequeña iteracion en una lista de valores
num = [1,2,3,4,5]
#Con el ciclo For podemos ir iterando cada valor para un uso
for i in range(len(num)):
    num[i] = num[i] * 2

print(f"Aquí está la iteración de la lista num y cada uno de sus valores multiplicado por dos")
print(f"== {num}")
