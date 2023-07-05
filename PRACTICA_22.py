# Prpgrama para calcular la temperatura
def programa_22():
    temperatura = float(input(" Escriba la temperatura "))
    if temperatura < 20:
        if temperatura < 10:
            print("Nivel azul")
        else:
            print("Nivel verde")
    else:
        if temperatura < 30:
            print("Nivel naranja")
        else:
            print("Nivel rojo")
    return temperatura 

temperatura = programa_22()
print(temperatura)

