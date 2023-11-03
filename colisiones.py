def calcular_radio(rect):
    return rect.height // 2

def distancia_entre_puntos(punto_1,punto_2):
    x1, y1 = punto_1
    x2, y2 = punto_2
    return  ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    



def detectar_colision_circulo(rect_1,rect_2):
    distancia = distancia_entre_puntos(rect_1.center, rect_2.center)
    return distancia <= (calcular_radio(rect_1) + calcular_radio(rect_2))

    

