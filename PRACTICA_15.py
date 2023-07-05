# Programa para calcular el precio total de una compra 
def programa_15():
    Total = (Articulo_1 + Articulo_2 + Articulo_3) * 1.07
    return round(Total,2)

Articulo_1 = float (input("Precio del articulo: "))
Articulo_2 = float (input("Precio del articulo: "))
Articulo_3 = float (input("Precio del articulo: "))
Total = programa_15()

print("El total de la compra es: ", Total)