# Programa para calcular el precio de una compra con impuesto y sin impuesto
def programa_19():
    Total_sin_impuesto = Articulo_1 + Articulo_2 + Articulo_3 + Articulo_4 + Articulo_5
    Total_con_impuesto = Total_sin_impuesto * 1.07
    Promedio_de_compras = Total_sin_impuesto / 5
    return round(Total_sin_impuesto,2), round(Total_con_impuesto,2), Promedio_de_compras

Articulo_1 = float (input("Precio del articulo: "))
Articulo_2 = float (input("Precio del articulo: "))
Articulo_3 = float (input("Precio del articulo: "))
Articulo_4 = float (input("Precio del articulo: "))
Articulo_5 = float (input("Precio del articulo: "))
Total_sin_impuesto, Total_con_impuesto, Promedio_de_compras = programa_19()

print("El total sin impuesto es: ", Total_sin_impuesto,"\n El total con impuesto es: ", Total_con_impuesto,"\n El promedio de la compra es: ", Promedio_de_compras)

