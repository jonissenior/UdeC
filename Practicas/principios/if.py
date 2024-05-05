pet = input("que mascota tienes?: ")

if pet == "perro":
    print("Que bonis perro")
elif pet == "gato":
    print("que bonis gatito")
elif pet == "pez":
    print("Rarito, un pez")
else:
    print("nuv, eso que")



stock = input("Digita tu stock: ")
stock = int(stock)

if stock >= 100 and stock <= 1000:
    print("el stock es el correcto")
else:
    print("stock incorrecto")


num = input("digita un numero: ")
num = int(num)

if num % 2 == 0:
    print("el numero es par")
else:
    print("El numero es inpar")


