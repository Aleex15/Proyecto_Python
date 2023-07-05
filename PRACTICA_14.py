# Programa para calcular el precio de la gasolina con impuesto y sin impuesto
def programa_14():
    Costo_Sin_Impuesto = Gasolina * Litro
    Costo_Total = Costo_Sin_Impuesto * 1.07
    return Costo_Sin_Impuesto, round(Costo_Total,2)

Gasolina = float(input("Valor de Precio de Gasolina "))
Litro = float(input("Valor de Cantidad de litros "))
Costo_Sin_Impuesto, Costo_Total = programa_14()

print("El costo total es: ", Costo_Total)


