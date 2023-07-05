# Programa para calcular el interes mensual de un prestamo, la cuota y el capital mensual
def programa_12():
    Tasa_de_Porcentaje = Tasa * 100 
    Tasa_Mensual = Tasa / 12
    Cuota =  Monto * (Tasa_Mensual /(1 -(1 + Tasa_Mensual )**(- Plazo)))
    Interes_Mensual = Monto * Tasa_Mensual
    Capital_Mensual = Cuota - Interes_Mensual
    return round(Cuota,2), round(Interes_Mensual,2), round(Capital_Mensual,2)

Monto = float(input("Valor de Monto:"))
Tasa = float(input("Valor de tasa: "))
Plazo = float(input("Valor de Plazo: "))
Cuota, Interes_Mensual, Capital_Mensual = programa_12()

print("El total de cuota es:", Cuota, "\n El total de Interes es: ", Interes_Mensual, "\n El total de capital es: ", Capital_Mensual )

