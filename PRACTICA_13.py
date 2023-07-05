# Programa para calcular el salario neto de un empleado
def programa_13():
    Seguro_Social = Salario_Bruto * 0.0514
    Seguro_Educativo = Salario_Bruto * 0.02
    Cuota_de_Prestamo = 50
    Salario_Neto = Salario_Bruto - Seguro_Social - Seguro_Educativo - Cuota_de_Prestamo
    return round(Salario_Neto,2)

Salario_Bruto = float(input("Valor de Salario bruto: "))
Salario_Neto = programa_13()

print("El salario neto es: ",Salario_Neto)