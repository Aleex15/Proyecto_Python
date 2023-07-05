# Programa para transformar kilogramos, gramos, centimetros y metros
def programa_17():
    Gramos = Kl * 1000
    Kilogramos = Gr / 1000
    Centimetros = Mt * 100
    Metros = Cm / 100
    return Gramos, Kilogramos, Centimetros, Metros

Mt = float(input('Valor del metro: '))
Cm = float(input('Valor del centimetro: '))
Gr = float(input('Valor del gramo: '))
Kl = float(input('Valor del kilogramo: '))
Gramos, Kilogramos, Centimetros, Metros = programa_17()

print("Metros: ",Metros, "\n Centimetros: ",Centimetros, "\n Gramos: ",Gramos, "\n Kilogramos: ", Kilogramos)