width = 800 #ancho
height = 600 #alto
size_screen = (width,height) #tamaño
origin = (0,0)
center_screen = (width // 2, height // 2)
 
centro_pantalla_x = width // 2
centro_pantalla_y = height // 2

FPS = 60 #velocidad de actualizacion de la pantalla
SPEED = 5 #velocidad de movimiento en el programa




#COLORES
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)
black = (0,0,0)
cyan = (0,255,255)
magenta = (255,0,255)
yelloy = (255,255,0)
custom = (255,174,201)
colors = [red,green,blue,white,cyan,magenta,yelloy,custom] #lista de colores

size_button = (200,50)
font_color = red # indica que se usará el color rojo para el texto en la interfaz de usuario.

def get_color(lista): #tomamos una lista de colores y elegimos un aleatoriamente
    from random import randrange #generar números enteros aleatorios dentro de un rango.
    return lista[randrange(len(lista))] # La función devuelve un elemento aleatorio de la lista que se pasa como argumento. Para hacer esto, se utiliza randrange(len(lista))para generar un índice aleatorio dentro del rango de la longitud de la lista y, a continuación,
                                        #se utiliza ese índice para acceder al elemento correspondiente en la lista y se devuelve como resultado.



