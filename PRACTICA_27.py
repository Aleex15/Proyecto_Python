# Programa para calcular si el numero es positivo, negativo o cero 
def programa_27():
    if Numero > 0 :
        print("El número es positivo ", "\U0001F600")
            
    if Numero < 0:
        print("El número es negativo ", "\U0001F600")
            
    if Numero == 0: 
        print("El número es cero ", "\U0001F600")
    return Numero
    
Numero = float(input(" Escriba el número "))   
Numero = programa_27()