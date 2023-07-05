# Programa para calcular la calificacion
def programa_28():
    value = 1
    while value <= 5: 
        calificacion = float(input(" Escriba la calificacion: ")) 
        if calificacion >= 90 :
            print("La nota es A ")
        if calificacion >= 80 and calificacion <= 89 :
            print("La nota es B ")
        if calificacion >= 70 and calificacion <= 79:
            print("La nota es C")
        if calificacion >= 60 and calificacion <= 69:
            print("La nota es D")
        elif calificacion < 60:
            print("La nota es F")   
        value += 1
    return calificacion

calificacion = programa_28()
