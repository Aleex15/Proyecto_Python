# Programa para resolver operaciones aritmeticas_3
def programa_10():
    C1 = ( 4 * A) + ( 3 * B)
    C2 = (21 * A) - 18 + (8 * B) - 5
    C3 = (4 * A) + (3 * B) + 7
    C4 = (2 * A ) + (3 * B)-(C**5)
    C5 = (2 * A) + (3 * B)-(C**2)
    return C1, C2,C3, C4, C5

A = int(input("Escriba el numero: "))
B = int(input("Escriba el numero: "))
C = int(input("Escriba el numero: "))
C1, C2, C3, C4, C5 = programa_10()

print("C1 = ",C1,"\n","C2 = ",C2,"\n","C3 = ",C3,"\n","C4 = ",C4,"\n","C5 = ",C5)