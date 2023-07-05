# Programa para encontrar el volumen de un prisma rectangular
def programa_7():
    Vol = ( Largo * Ancho * Altura )
    return round(Vol,2)

Largo = float(input("Escriba el valor de largo: "))
Ancho = float(input("Escriba el valor de la Ancho: ")) 
Altura = float(input("Escriba el valor de la Altura: "))
Vol = programa_7()

print("El volumen = ",Vol)