# Programa para resolver operaciones aritmeticas
def programa_8():
    A = 20 - (7 * 3)
    B = (-7 * x ) + 2 - (10 * x ) + 5
    C = ( 4 * x ) + 4 + (9 * x ) + 18
    D = ( 6 * x ) - 5 - (8 * x ) + 2
    E = ((( 5 * x)) + 78 ) / 28
    F = (((6 * x )  - 7 ) /4) + (((3 * 7 ) - 5 )/7)
    return round(A,2), round(B,2), round(C,2), round(D,2), round(E,2), round(F,2)

x = float(input("Escriba el valor de x: "))
A,B,C,D,E,F = programa_8()

print("A = ",A,"\n","b = ",B,"\n","C = ",C,"\n","D = ",D,"\n","E = ",E,"\n","F = ",F) 




