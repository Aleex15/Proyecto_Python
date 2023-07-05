# Prpgrama para calcular el descuento de un articulo
def programa_25():
    Precio_Final = (Precio_Original - (Precio_Original * (Porcentaje_Descuento/100)))
    print("El precio con descuento es ", Precio_Final)

    if Precio_Final  < 50:
        print("!Oferta especial¡ ")
    return Precio_Final

Precio_Original = float(input("Escriba el precio original del producto : "))
Porcentaje_Descuento = float(input("Escriba el descuento a aplicar : "))
Precio_Final = programa_25()
