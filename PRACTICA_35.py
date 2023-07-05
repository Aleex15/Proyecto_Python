# Programa contador de numeros pares e impares
def programa_35():
    value = 1

    while value <= 15:

        if value %2 == 0 :
            print("El número es par ")
        else:
            print("El numero es impar ")
        if value == 16:
            break
        
        print(value)
        value += 1
    return value
value = programa_35()
        

    
   