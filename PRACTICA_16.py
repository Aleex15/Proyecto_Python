# Programa para calcular la nota final de 5 evaluaciones con pesos diferentes
def programa_16():
    Nota_Final = ((N1*0.20) + (N2*0.15) + (N3*0.25) + (N4*0.10) + (N5*0.30))
    return Nota_Final

N1 = float(input("Primera evaluacion: "))
N2 = float(input("Degunda evaluacion: "))
N3 = float(input("Tercera evaluacion: "))
N4 = float(input("Cuarta evaluacion: "))
N5 = float(input("Quinta evaluacion: "))
Nota_Final = programa_16()

print("La nota final es: ", Nota_Final)