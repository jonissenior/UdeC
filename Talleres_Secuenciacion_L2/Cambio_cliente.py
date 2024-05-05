# Calcula cambio cliente
"""
Elaborar un algoritmo talque dado el precio de un artículo 
vendido y la cantidad de dinero entregada por el cliente, 
que calcule e imprima el cambio que se le debe entregar al mismo
"""
#Ingresar datos
Precio_articulo = float(input("Ingrese el valor del articulo ==> "))
Cantidad_dinero = float(input("Ingrese la cantidad de dinero ==> "))

#calcular cambio
cambio = Cantidad_dinero - Precio_articulo

#Mostrar cambio
print(f"El articulo vale ${Precio_articulo:,.0f} y se entrego un total de ${Cantidad_dinero:,.0f}")
print(f"El cambio a entregar es de: ${cambio:,.0f}")



