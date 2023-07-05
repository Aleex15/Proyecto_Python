# Programa que calcula el total, sub-total e impuesto de una compra
def programa_33():
    Precio = 1
    Sub_Total = 0

    while Precio <= 5:
        Articulo = float(input("Ingrese el precio del artículo " + str(Precio) + ": "))
        Sub_Total += Articulo
        Precio += 1

    Impuesto = Sub_Total * 0.07
    Total = Sub_Total + Impuesto
    return Sub_Total, round(Impuesto,2), Total

Sub_Total, Impuesto, Total = programa_33()
print("Subtotal: ", Sub_Total, "\n Impuesto 7%: ", Impuesto, "\n Total: ", Total)

