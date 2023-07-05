# Programa para calcular el salario neto
def programa_20():
    Seguro_social = (Salario_bruto * 0.08) 
    Seguro_educativo = (Salario_bruto * 0.02) 
    Impuestos = (Salario_bruto * 0.15) 
    Prestamos = 100
    Salario_neto = Salario_bruto - Seguro_social - Seguro_educativo - Impuestos - Prestamos
    return round(Seguro_social,2), round(Seguro_educativo,2), round(Impuestos,2), round(Salario_neto,2)

Salario_bruto = float(input("Salario bruto del empleado: "))
Seguro_social, Seguro_educativo, Impuestos, Salario_neto, = programa_20()

print("El descuento de seguro social es: ", Seguro_social, "\n El descuento de seguro educativo es: ", Seguro_educativo, "\n El descuento con impuesto es: ", Impuestos, "\n El total del salario neto es: ", Salario_neto)
