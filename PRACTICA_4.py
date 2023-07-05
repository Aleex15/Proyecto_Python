# Programa para encontrar el area de un triangulo
def programa_4():
    Area = (B * A)/2
    return round(Area,2)

B = float(input("Escriba el valor de la Base: " ))
A = float(input("Escriba el valor de la Altura: "))
Area = programa_4()

print("El area es: ",Area)