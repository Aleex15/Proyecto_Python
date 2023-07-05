# Programa para calcular que numero es mas grande 
def programa_24():
    if V_1  > V_2 and V_1 > V_3:
        print("el numero mas grande es ", V_1 )
    if V_2 > V_1 and V_2 > V_3:
        print("el numero mas grande es ", V_2)
    if V_3 > V_1 and V_3 > V_2:
        print("el numero mas grande es ", V_3) 
    if V_1 == V_2 == V_3:
        print("Los numeros son iguales")
    return V_1, V_2, V_3
    
V_1 = float(input("Escriba el primer numero: "))
V_2 = float(input("Escriba el segundo numero: "))
V_3 = float(input("Escriba el tercer numero: "))
V_1, V_2, V_3 = programa_24() 

