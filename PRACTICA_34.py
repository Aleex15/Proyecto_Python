# Programa que calcula si el numero es positivo, negativo o cero
def programa_34():
    value = 1
    while value <= 5:
        numero = float(input(" Escriba el número: "))

        if numero > 0 :
            print("El número es positivo", "\U0001F600")
                
        if numero < 0:
            print("El número es negativo ", "\U0001F600")
                
        if numero == 0: 
            print("El número es cero ", "\U0001F600")
        value += 1
    return numero
numero = programa_34()