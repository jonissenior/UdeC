#Otro ejemplo mas 
"""
Una empresa vende hojas de hielo seco, con las condiciones siguientes: 
|Tipo cliente  |  Descuento |
|     1        |      5%    | 
|     2        |      8%    |
|     3        |      12%   |
|     4        |      15%   |
     
Cuando un cliente realiza una compra se generan los siguientes datos: nombre del cliente, tipo de 
cliente, cantidad de hojas compradas, precio hoja.
Elaborar un algoritmo que permita procesar varios clientes e imprima el siguiente reporte:
                        REPORTE DE CLIENTES
                        
NOMBRE              SUBTOTAL              DESCUENTO               NETO PAGAR
______________________________________________________________________________
XXXXXXXXXX           99.99                  99.99                   999.99
XXXXXXXXXX           99.99                  99.99                   999.99
.
.
.
XXXXXXXXXX           99.99                  99.99                   999.99

Total/999/clientes   999.99                999.99                   9999.99
 
Nota:
SUBTOTAL = CANTIDAD DE HOJAS* PRECIOHOJA
DESCUENTO = porcentaje del subtotal de acuerdo al tipo de cliente
NETO PAGAR = SUBTOTAL - DESCUENTO
"""
print("NOMBRE              SUBTOTAL              DESCUENTO               NETO PAGAR")
total_clientes = 0
totalsubtotal = 0
total_descuento = 0
tot_neto_pagar = 0
#Para esto vamos a empezar abriendo el while
while True:
    #Vamos a pedir los datos
    nombre = input("Ingrese el nombre ==> ")
    tip_cliente = int(input("Ingrese el tipo de el cliente ==> "))
    cantidad_hojas = int(input("Ingrese la cantidad de hojas ==> "))
    precio_hoja = float(input("Ingrese el precio de las hojas ==> "))
    #Hacemos un pequeño calculo 
    subtotal = cantidad_hojas * precio_hoja
    #Usamos ifs para saber el tipo de cliente 
    if tip_cliente == 1:
        descuento = subtotal * 0.5
    elif tip_cliente == 2:
        descuento = subtotal * 0.8
    elif tip_cliente == 3:
        descuento = subtotal * 0.12
    elif tip_cliente == 4:
        descuento = subtotal * 0.15
    else:
        print("Ese tipo no esta disponible :c")
    #Ahora calculamos el pago neto 
    neto = subtotal - descuento
    print(f"{nombre}         {subtotal}            {descuento}                    {neto}")
    total_clientes = total_clientes + 1
    totalsubtotal = totalsubtotal + subtotal
    total_descuento = total_descuento + descuento
    tot_neto_pagar = tot_neto_pagar + neto
    #preguntamos si desea otro cliente 
    pregunta = str(input("Quiere añadir otro cliente?: Y/N ")).lower().strip()
    if pregunta != "y":
        print("Perfecto !!")
        break
#Mostramos mas
print("NOMBRE              SUBTOTAL              DESCUENTO               NETO PAGAR")
print(f"{nombre}         {subtotal}            {descuento}                    {neto}")
print(f"{total_clientes}     {totalsubtotal}     {total_descuento}      {tot_neto_pagar}")

