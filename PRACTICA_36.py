# Programa contador de numeros mayores, menores o iguales a 5
def programa_36():
    for numero in range (15):
        print(numero)
        if numero > 5 :
            print("El número es mayor a 5 ")
        elif numero <= 0:
            print("El numero es igual o menor a 0")
        else:
            print("El numero es menor a 5")
        
        if numero == 9:
            break
numero = programa_36()
