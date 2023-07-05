# Programa de valores
def programa_1():
    A = 10
    B = 5
    AUX = A 
    A = B
    B = AUX
    return A,B,AUX 

A,B,AUX = programa_1()
print(A,B,AUX)
