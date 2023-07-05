# Programa para calcular el impuesto de una compra 
def programa_37():
    Contador = 0
    Total = 0

    while Contador < 5:
        Precio = float(input("Ingrese el precio del artículo: "))
        Impuesto = Precio * 0.07
        Total += Impuesto
        Contador += 1
    return round(Total,2)

Total = programa_37()

print("El total del impuesto a pagar es:", Total)

