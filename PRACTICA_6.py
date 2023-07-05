# Programa para encontrar el area de un trapecio 
def programa_6():
    Area = (Base1+Base2)*Altura/2
    return Area

Base1 = float(input("Escriba el valor de la Base1: "))
Base2 = float(input("Escriba el valor de la Base2: "))
Altura = float(input("Escriba el valor de la Altura: "))
Area = round(programa_6(),2)

print("El area es: ",Area)