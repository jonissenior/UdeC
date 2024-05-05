# Calcula precio venta articulo
"""
Elaborar un algoritmo que calcule e imprima el precio  
de venta de un artículo. Se tiene los datos  descripción  
de artículo y el costo de producción. El precio de venta 
se calcula  añadiéndole al costo 120% como utilidad y el 
15% de impuesto. 
"""

#Requerir los datos del producto
articulo = input("Ingrese la descripcion del articulo ==> ").capitalize()
costo_produccion = float(input("Ingrese el costo de produccion del producto ==> "))

#calculamos precio de venta 
precio_venta = costo_produccion + costo_produccion * 1.2 + (costo_produccion + costo_produccion * 1.2) * 0.15
#Mostramos resultados
print(f"El valor de produccion de {articulo} es de ${costo_produccion:,.0f} ")
print(f"EL valor de venta quedaria en: ${precio_venta:,.0f}")
