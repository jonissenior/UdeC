

print("Bienvenido a este programa donde sabrás el número mayor, menor y la diferencia.")
print("Ingresa 5 números:")
num1 = int(input("Número 1: "))
num2 = int(input("Número 2: "))
num3 = int(input("Número 3: "))
num4 = int(input("Número 4: "))
num5 = int(input("Número 5: "))

# Encuentra el número máximo
num_max = max(num1, num2, num3, num4, num5)

# Encuentra el número mínimo
num_min = min(num1, num2, num3, num4, num5)

# Calcula la diferencia
diferencia = num_max - num_min

print("El número mayor de los que ingresaste es:", num_max)
print("El número menor de los números ingresados es:", num_min)
print("La diferencia entre los dos números es:", diferencia)

