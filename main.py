


import pygame
#from aleatorios import *
from funciones import *
#from random import *
#from sys import exit
#from config import *
from colisiones import detectar_colision_circulo
#from pygame.locals import *
#from utilis import *
#from menu import *
import json


#inicializar los modulos de pygame
pygame.init()

#---> creo un reloj
clock = pygame.time.Clock()

#CONFIGURO LA PANTALLA PRINCIPAL


#imagen_fondo = pygame.transform.scale(pygame.image.load("Recursos/fondo de pant principal.jpg"), size_screen)
#----> crear ventana
screen = pygame.display.set_mode(size_screen) #A partir de ese punto, puedes utilizar la variable screenpara dibujar elementos en la ventana, como gráficos, texto y otros elementos del juego.
pygame.display.set_caption("Mi Primer Jueguito")

#---> CONFIGURO LA DIRECCION

acender = False
decender = False
mover_izq = False
move_der = False


rect_w = 70
rect_h = 70
monedas = 0
width_coin = 30
height_coin = 30
width_dona = 30
height_dona = 30

count_conis = 20
count_donas = 10

#--->seteo sonidos 
golpe_sound = pygame.mixer.Sound("Recursos/recoleccion.wav")
game_over_sound = pygame.mixer.Sound("Recursos/game_over.mp3")
#----> fondo del juego en curso
background = pygame.transform.scale(pygame.image.load("Recursos/fondo/summer 2/Summer2.png"),size_screen)
#--->musica  fondo (solo 1 se permite)
pygame.mixer.music.load("Recursos/Interstellar musica fondo.ogg")


# --->  sonido .PLAY tiene 3 parametros
#pygame.mixer.music.play()

#-->control de volumen 
pygame.mixer.music.set_volume(0.5)
playing_music = True

#-->creo boton

boton_comenzar= pygame.Rect(screen.get_width() // 2 - size_button[0] // 2, 100, *size_button)
#--->CARGA DE IMAGENES

imagen_player = pygame.image.load("Recursos/pibito.png")
imagen_pelota = pygame.image.load("Recursos/pelota_dorada-nuevo.png")
imagen_dona = pygame.image.load("Recursos/dona.png")
#-->eventos personales
EVENT_NWE_COIN = pygame.USEREVENT + 1 #definir un nuevo tipo de evento personalizado
EVEN_NWE_DONA = pygame.USEREVENT +1 
pygame.time.set_timer(EVENT_NWE_COIN,2000) # configura un temporizador para que genere un evento de tipo EVENT_NEW_COINcada 3 segundos
pygame.time.set_timer(EVEN_NWE_DONA,3500)

imagen_fondo = pygame.transform.scale(pygame.image.load("Recursos/fondo de pant principal.jpg"), size_screen)

block = create_block(imagen_player,randint(0,width - rect_w),randint(0,height - rect_h),rect_w,rect_h,get_color(colors),radio= 30)
max_contador = 0 #top score, aca se puede modificar
max_contador_donas = 0
"""
while True:
            game_data = {
                'score': 100,
    
        }

      # Guardar el diccionario en un archivo JSON
            with open('game_data.json', 'w') as file:
                json.dump(game_data, file)
"""

while True:
    
    #---> extablesco fuente
    laser = None
    monedas = 0
    fuente = pygame.font.SysFont("MV Boli",20)
    texto = fuente.render(f"COINS :{monedas}",True,black)
    rec_texto = texto.get_rect()
    rec_texto.midtop = (width // 2 , 30)
    donasas = 0
    fuente = pygame.font.SysFont("MV Boli",20)
    texto = fuente.render(f"DONAS :{donasas}",True,black)
    rec_texto = texto.get_rect()
    rec_texto.midtop = (width // 2 , 30)


    #---> creo lista de coins
    coins = []
    generate_coins(coins,count_coins,imagen_pelota)
    cont_comer = 0

    #---> creo lista de donas
    donas = []
    generate_donas(donas, count_donas, imagen_dona)
    cont_comer_dona = 0
    #--> aca lo vuelvo hacer vicible al cursos del mouse
    pygame.mouse.set_visible(True)
    screen.fill(black)
    #imagen_fondo = pygame.transform.scale(pygame.image.load("Recursos/fondo de pant principal.jpg"), size_screen)
    mostar_texto(screen,"DRAGON BALL",fuente,(width //2 ,50 ),white)
   #-->creo el boron,, lo muestro en su estado final
   
    pygame.display.flip()
    click_boton(boton_comenzar)

    #---> aca dejo invicible el mouse
    pygame.mouse.set_visible(False)

    pygame.mixer.music.play(-1)
    

    time_plate = FPS * 30

    is_running = True

    while is_running:

        time_plate -= 1
        if time_plate == 0:
            is_running = False
        
        
       
        clock.tick(FPS)

        #--->detectar los eventos
        for evento in pygame.event.get():
            if evento.type == QUIT:
                is_running = False
            
            if evento.type == KEYDOWN:
                if evento.key == K_f:
                    laser = create_laser(block["rect"].midtop,speed_laser)
                if evento.key == K_RIGHT or evento.key == K_d:
                    move_der = True
                    mover_izq = False
                if evento.key == K_LEFT or evento.key == K_a:
                    mover_izq = True
                    move_der = False
                if evento.key == K_UP or evento.key == K_w:
                    acender = True
                    decender = False
                if evento.key == K_DOWN or evento.key == K_s:
                    decender = True
                    acender = False
                # pausa musica
                if evento.key == K_m:
                    if playing_music:
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.unpause()
                    playing_music = not playing_music
        #------>aca se pausa el juego
                if evento.key == K_p:
                    if playing_music:
                        pygame.mixer.music.pause()
                        mostar_texto(screen,"PAUSA",fuente,center_screen,red,white)
                        pausar()
                    if playing_music:
                        pausar()
                        pygame.mixer.music.unpause()
                    
            if evento.type == KEYUP:
                if evento.key == K_RIGHT:
                        move_der = False
                if evento.key == K_LEFT:
                        mover_izq = False
                if evento.key == K_UP:
                        acender = False
                if evento.key == K_DOWN:
                        decender = False
               
            if evento.type == EVENT_NWE_COIN:
                coins.append(create_block(imagen_pelota,randint(0,width - width_coin),randint(0,height - height_coin),
                                        width_coin,height_coin,green,0,0,height_coin // 2))    
            if evento.type == EVEN_NWE_DONA:
                donas.append(create_block(imagen_dona,randint(0,width - width_dona),randint(0,height - height_dona),
                                        width_dona,height_dona,green,0,0,height_dona // 2))    

            if evento.type == MOUSEBUTTONDOWN:
                if evento.button == 1:
                    new_coin = create_block(imagen_pelota,evento.pos[0],evento.pos[1],
                                            width_coin,height_coin,cyan,0,0,height_coin // 2)
                    new_coin["rect"].left -= width_coin // 2
                    new_coin["rect"].top -= height_coin // 2
                    
                    coins.append (new_coin)
                if evento.button == 3:
                    block["rect"].center = center_screen

            if evento.type == MOUSEBUTTONDOWN:
                if evento.button == 1:
                    new_dona = create_block(imagen_dona,evento.pos[0],evento.pos[1],
                                            width_dona,height_dona,cyan,0,0,height_dona // 2)
                    new_dona["rect"].left -= width_dona // 2
                    new_dona["rect"].top -= height_dona // 2
                    
                    donas.append (new_dona)
                if evento.button == 3:
                    block["rect"].center = center_screen
            
    #----> aca es cuando el mouse se mueva por la apantalla del juego
            if evento.type == MOUSEMOTION:
                block["rect"].center = evento.pos
                
        #----> ACTUALIZO LOS ELEMNTOS------------------->

    

        #MUEVO SU BLOQUE DE ACUERDO A SU DRIRECCION
    
        if acender and block["rect"].top >= 0:
            #-->muevo arriba
            block["rect"].top -= SPEED
        if decender and block["rect"].bottom <= height:
            #--> muevo abajo
            block["rect"].top += SPEED
        if mover_izq and block["rect"].left >= 0:
            #--->muevo izquierda
            block["rect"].left -= SPEED
        if move_der and block["rect"].right <= width:
            #-->muevo derecha
            block["rect"].left += SPEED


        pygame.mouse.set_pos(block["rect"].centerx,block["rect"].centery)    
    

        #--->muevo los asteroides en caida
        for coin in coins:
            if coin["rect"].top <= height:
               coin["rect"].move_ip(0,coin["speed_y"])
            else:
               coin["rect"].bottom = 0
        #--->creo el movimiento del laser 
            if laser:
                laser["rect"].move_ip(0, -laser["speed_y"])
        #-->de detecta colocion del pibito con las pelotas
                colision  = False
                for coin in coins[:]:       
                    if detectar_colision_circulo(coin["rect"],laser["rect"]):
                        coins.remove(coin)
                        monedas += 1 
                        texto = fuente.render(f"COINS :{monedas}",True,black)
                        rec_texto = texto.get_rect()
                        rec_texto.midtop =     (width // 2,100)
                        cont_comer = 10
                        colision = True
                        if playing_music:
                            golpe_sound.play()
                       
                if colision:
                    laser = None


        for coin in coins[:]:       
            if detectar_colision_circulo(coin["rect"],block["rect"]):
                coins.remove(coin)
                monedas += 1 
                texto = fuente.render(f"COINS :{monedas}",True,black)
                #texto = fuente.render(f"" :{monedas}",True,red)
                rec_texto = texto.get_rect()
                rec_texto.midtop =     (width // 2,100)
                cont_comer = 10
                if playing_music:
                    golpe_sound.play()
                
        
            
        if cont_comer >= 0:
            cont_comer -= 1
            block["rect"].width = rect_w + 5
            block["rect"].height = rect_h + 5
        else:
            block["rect"].width = rect_w
            block["rect"].height = rect_h

        
        #--->muevo las pelotas en caida
        for dona in donas:
            if dona["rect"].top <= height:
               dona["rect"].move_ip(0,dona["speed_y"])
            else:
               dona["rect"].bottom = 0
        #--->creo el movimiento del laser 
            if laser:
                laser["rect"].move_ip(0, -laser["speed_y"])#se utiliza para cambiar la posición del rectángulo asociado al láser en un juego en 2D. El rectángulo se mueve verticalmente hacia arriba en la pantalla, y la cantidad de movimiento está determinada por el valor de laser["speed_y"]. Esto simula el movimiento del láser hacia arriba en el juego.
        #-->de detecta colocion del pibito con las donas
                colision  = False
                for dona in donas[:]:       
                    if detectar_colision_circulo(dona["rect"],laser["rect"]):
                        donas.remove(dona)
                        donasas += 1 
                        #texto = fuente.render(f"DONAS :{donasas}",True,black)
                        rec_texto = texto.get_rect()
                        rec_texto.midtop =     (width // 2,50)
                        cont_comer_dona = 10
                        colision = True
                        if playing_music:
                            golpe_sound.play()
                       
                if colision:
                    laser = None


        for dona in donas[:]:       
            if detectar_colision_circulo(dona["rect"],block["rect"]):
                donas.remove(dona)
                monedas -= 1 
                #texto = fuente.render(f"DONAS :{donasas}",True,black)
                #texto = fuente.render(f"" :{monedas}",True,red)
                rec_texto = texto.get_rect()
                rec_texto.midtop =     (width // 2,50)
                cont_comer_dona= 10
                if playing_music:
                    golpe_sound.play()
                
        
            
        if cont_comer_dona >= 0:
            cont_comer_dona -= 1
            block["rect"].width = rect_w + 5
            block["rect"].height = rect_h + 5
        else:
            block["rect"].width = rect_w
            block["rect"].height = rect_h


        #---> dibujar pantalla-------------------->
        #SCREEN.BLIT = dibujar una superficie (como una imagen o un objeto gráfico) en la pantalla en una posición específica definida por las coordenadas (x, y).
        #surface: Esto representa la superficie que deseas dibujar en la pantalla. Puede ser una imagen, un objeto gráfico, un texto renderizado, etc.
        #(x, y): Estas son las coordenadas en las que deseas colocar la esquina superior izquierda de la superficie en la pantalla. xes la coordenada horizontal (izquierda/derecha), y yes la coordenada vertical (arriba/abajo).
        #Cuando lo utilizas screen.blit(), estás básicamente tomando una superficie y copiándola en la pantalla en una ubicación específica.
        #screen.fill(black)
        screen.blit(background,origin)

        dibujar_pelota(screen,coins)
        dibujar_dona(screen,donas)
        
        
        screen.blit(block["imagen"],block["rect"])
        #-->creo el laser 
        #if laser:
        #    pygame.draw.rect(screen,laser["color"],laser["rect"])

        screen.blit(texto,rec_texto) #muestra el score en pantalla
    
        #----->ACTUALIZO PANTALLA----------------->
        pygame.display.flip()
        
        
      

    if monedas > max_contador:
        max_contador = monedas
    if donasas > max_contador_donas:
        max_contador_donas = donasas

    #--> mensajes del score, el juego termino y una tecla precionar para continuar
    pygame.mixer.music.stop()
    game_over_sound.play()
    screen.fill(black)
    mostar_texto(screen,f"Score:{monedas}",fuente,(140, 20),white)
    mostar_texto(screen,f"Top Score:{max_contador}",fuente,(width - 150, 20),white)
    mostar_texto(screen,"Game Over",fuente,center_screen,blue)
    mostar_texto(screen,"Presione una tecla para comenzar....",fuente,(width //2 , height - 50 ),white)
    """
    data_file = "game_data.json"
  
    def guardar_datos(puntaje, premios):
        data = {
            "puntaje": puntaje,
            "premios": premios
        }
        with open(data_file, "w") as file:
            json.dump(data, file)
    """

    pygame.display.flip()
    pausar()


terminar()


