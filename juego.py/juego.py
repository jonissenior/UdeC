import random


user_option = input("piedra, papel o tijera: ").lower().strip()
computer_option = ""

if user_option == computer_option:
    print("Empate")
elif user_option == "piedra":
    if computer_option == "tijera":
        print("Piedra gana a tijera")
        print("user gano!")
    else:
        print("papel gana a piedra")
        print("computer gano!")
elif user_option == "papel":
    if computer_option == "piedra":
        print("papel gana a piedra")
        print("User gano!")
    else:
        print("tijera gana a papel")
        print("computer gana!")
elif user_option == "tijera":
    if computer_option == "papel":
        print("tijera gana a papel")
        print("user gano!")
    else:
        print("piedra gana a tijera")
        print("computer gano")
