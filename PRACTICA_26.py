# Programa para calcular las clases de triangulos 
def programa_26():
        if Lado_1 == Lado_2 == Lado_3:
                print("El triángulo es equilátero", "\U0001F600")
                
        if Lado_1 == Lado_2 != Lado_3:
                print("El triangulo es isóceles ", "\U0001F600")

        if Lado_1 != Lado_2 != Lado_3:
                print("El triangulo es escaleno ", "\U0001F600")
        return Lado_1, Lado_2, Lado_3

Lado_1 = float(input(" Escriba la longitud del lado1 "))
Lado_2 = float(input(" Escriba la longitud del lado2 "))
Lado_3 = float(input(" Escriba la longitud del lado3 "))
Lado_1, Lado_2, Lado_3 = programa_26()


