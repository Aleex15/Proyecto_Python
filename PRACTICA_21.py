# Programa para calcular el salario de una persona y si debe abonar impuesto
def programa_21():
    if salario  >= 3000:
        print("Esta Persona debe abonar de impuesto: ",(salario * 1.07 - salario ))
    else:
        print("No debe abonar impuesto")

    return salario

salario = float(input("Escriba el salario: "))
salario = programa_21()
