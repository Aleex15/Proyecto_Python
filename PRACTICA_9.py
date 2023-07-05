# Programa para resolver operaciones aritmeticas_2
def programa_9():
    C1 = ( y * x) + ( x * 2)
    C2 = (21 * x) - 18 + (8 * x) - 5
    C3 = (y * x) + (x * y) + 7
    C4 = (2 * x ) + (x * y)
    C4 = C4**5
    C5 = (y * x) + (6 * y )
    C5 = C5**2
    return C1, C2,C3, C4, C5

x = 3
y = 4
C1, C2,C3, C4, C5 = programa_9()

print("C1 = ",C1,"\n","C2 = ",C2,"\n","C3 = ",C3,"\n","C4 = ",C4,"\n","C5 = ",C5)
