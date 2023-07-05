# Programa de operaciones matematicas 
def programa_3():
    D = (A + B + C) / 3
    return round(D,2)

A = float(input("leer A: ") )
B = float(input("leer B: ") )
C = float(input("leer C: ") )
D = programa_3()

print("El resultado es: ", D)
