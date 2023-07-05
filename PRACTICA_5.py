# Programa para encontrar el perimetro de un rectangulo
def programa_5():
    D = AB+BC+CD+DA
    return round(D,2)

AB = float(input("Escriba el valor de la AB: "))
BC = float(input("Escriba el valor de la BC: "))
CD = float(input("Escriba el valor de la CD: "))
DA = float(input("Escriba el valor de la DA: "))
D = programa_5()

print("El resultado es: ",D)