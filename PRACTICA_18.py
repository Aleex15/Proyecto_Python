# Programa para calcular el capital final 
def programa_18():
    Capital_Final = Capital_inicial * (1 + Tasa)**Periodo
    return Capital_Final

Capital_inicial = float(input('Capital inicial: '))
Tasa = float(input('Cantidad tasa: '))
Periodo = float(input('Cantidad periodo: '))
Capital_Final = programa_18()

print('El capital final es: ',Capital_Final)