import cv2
import numpy as np
import conf as cfg
import tensorflow as tf
from tensorflow.python.keras.applications.mobilenet import preprocess_input
import time
import pyautogui
import explorador


h, w = 224, 224

path = './modelo_3a' #224, 224
cnn = tf.keras.experimental.load_from_saved_model(path)
pyautogui.KEYBOARD_KEYS

#states
STATE_INTRO=-1
STATE_MENU_MAIN=0
STATE_MENU_CHOOSE_LEVEL=1
STATE_MENU_INSTRUCTIONS=2
STATE_MENU_ABOUT=3
STATE_MENU_OPTIONS=4
STATE_MENU_PREMIUM=5
STATE_BALL_IN_PADDLE=6
STATE_PLAY=7
STATE_NEXT_LVL=8
STATE_BALL_OUT=9
STATE_GAME_OVER=10
STATE_WON=11
STATE_SURE_TO_MENU=12
STATE_SURE_TO_QUIT=13
STATE_OUTRO=14


def predict(img):

      x = cv2.resize(img, (h, w))

      #Ver la imagen que entra en la red cada 3 sec

      inicio_time = time.clock()
      if inicio_time >= cfg.periodo_imagen:
        cfg.periodo_imagen += 3
        x1 = cv2.resize(x, (0, 0), fx=0.3, fy=0.3)
        cv2.imshow('Entrada red', x1)
        cfg.cv2.moveWindow('Entrada red', 850, 850)
      
      x = np.expand_dims(x, axis=0)
      
      #cnn.build(input_shape = (None, h, w, 3)) 

      #cnn.summary() #Muestra las capas de mi red neuronal

      x = preprocess_input(x)

      array = cnn.predict(x)
      result = array[0]
#      print(result)
      answer = np.argmax(result)
      if answer == 0:
        print("pred: abierta con, {}% ".format(str(result[answer]*100)[:4]))
      elif answer == 1:
        print("pred: cerrada con, {}% ".format(str(result[answer]*100)[:4]))
      elif answer == 2:
        print("pred: perfil con, {}% ".format(str(result[answer]*100)[:4]))
#      elif answer == 3:
#        print("pred: perfil con, {}% ".format(str(result[answer]*100)[:4]))
#      elif answer == 4:
#        print("pred: pulgar con, {}% ".format(str(result[answer]*100)[:4]))
#      elif answer == 5:
#        print("pred: puntero con, {}% ".format(str(result[answer]*100)[:4]))

      return int(answer), result[answer]

def evaluar(prediccion, porcent_prediccion):
  ans_gesto = cfg.gesto
  cfg.gesto = prediccion
#  print('era, ', ans_gesto,' es ', cfg.gesto, porcent_prediccion, prediccion)
#  print('gestos:', ans_gesto, cfg.gesto)
  if ans_gesto == cfg.gesto:
#      print(porcent_prediccion)
      if porcent_prediccion > 0.9:
          cfg.accion = True
#          print('Accionamos con:', porcent_prediccion)
      else: cfg.accion = False
  else: cfg.accion = False
  


click_inicio = 0
on_sel_click = (0,0)
def on_mouse(event, x, y, flags, param):
        global on_sel_click, click_inicio
        if event == cv2.EVENT_LBUTTONUP:  #258 mitad del ancho y 185 mitad del alto $%&cambiar si cambio imagen
                on_sel_click = x, y
                if on_sel_click[0] < 560 and on_sel_click[0] > 135 and on_sel_click[1] < 350 and on_sel_click[1] > 180:
#                        print("primer cuadro")
                        click_inicio = 1
                if on_sel_click[0] < 1160 and on_sel_click[0] > 850 and on_sel_click[1] < 400 and on_sel_click[1] > 230:
#                        print("segundo cuadro")
                        click_inicio = 2
                if on_sel_click[0] < 430 and on_sel_click[0] > 125 and on_sel_click[1] < 535 and on_sel_click[1] > 375:
#                        print("tercer cuadro")
                        click_inicio = 3
                if on_sel_click[0] < 1175 and on_sel_click[0] > 860 and on_sel_click[1] < 630 and on_sel_click[1] > 470:
#                        print("cuarto cuadrante")
                        click_inicio = 4

#Tamano del monitor
def screen_size():
  size = (None, None)
  scr_size = pyautogui.size()
  size = (int(scr_size[0]), int(scr_size[1]))

  return size

def map(x, in_min, in_max, out_min, out_max):
    return int((x-in_min) * (out_max-out_min) / (in_max-in_min) + out_min)
      
      # [0, 0] --> [ 360,  480]
      # [0, 0] --> [1080, 1920]
      # 1080/360 = 3 y 1920/480 = 4
      
      # añado unos margenes:
      # [90, 120] --> [ 270,  360]
      # [ 0,   0] --> [1080, 1920]
      # 1: (x-90)rl_x = y
      # Si x =  90, y =    0 --> ( 90 - 90)·rl_x = 0
      # Si x = 180, y =  540 --> (180 - 90)·rl_x = 540
      # Si x = 270, y = 1080 --> (270 - 90)·lr_x = 1080

                        
def accion(gesto, centro, size_video):
    global click_inicio
#    print(click_inicio)

    cv2.setMouseCallback("Inicio", on_mouse)

    cfg.accion_gesto = True
    
    if cfg.screen_size is None:
        cfg.screen_size = screen_size() #(x, y)
    
    
    # opciones pyautogui
    """
    salir, atras, etc...
    """
    if cfg.accion_gesto is True:
        

        if gesto == 0 or gesto == 1: #move
#            print('movemos')
            rl_x = map(centro[0], size_video[1]*0.25, size_video[1]*0.75, 0, cfg.screen_size[0])    #se pueden modificar los terminos 1 y 2 para 
            rl_y = map(centro[1],  size_video[0]*0.25, size_video[0]*0.75, 0, cfg.screen_size[1])   #obtener otro mapeo, en conf dibujar un entorno!
              
            new_centro = rl_x, rl_y #con margen
            cfg.new_centro = new_centro
    
            if new_centro[0] < 1920 and new_centro[1] < 1080 and new_centro[0] > 0 and new_centro[1] > 0: #evita problemas de fuera de rango
                new_centro_bool = True
            else: new_centro_bool = False
        
            if new_centro_bool == True:
#                print(new_centro)
                """Auto ayuda en la selecion del menu de inicio"""
                if cfg.imagen_inicio == False and cfg.video_inicio == False and cfg.run_juego == False:
                    if new_centro[0] < 885 and new_centro[0] > 485 and new_centro[1] < 430 and new_centro[1] > 153:
                        x, y=pyautogui.locateCenterOnScreen('./fotos/Imagenes.png')
                        pyautogui.moveTo(x,y)
                    elif new_centro[0] < 1555 and new_centro[0] > 1155 and new_centro[1] < 515 and new_centro[1] > 190: 
                        x, y=pyautogui.locateCenterOnScreen('./fotos/Juegos.png')
                        pyautogui.moveTo(x,y)
                    elif new_centro[0] < 850 and new_centro[0] > 450 and new_centro[1] < 710 and new_centro[1] > 431:
                        x, y=pyautogui.locateCenterOnScreen('./fotos/Video.png')
                        pyautogui.moveTo(x,y)
                    elif new_centro[0] < 1547 and new_centro[0] > 1347 and new_centro[1] < 841 and new_centro[1] > 516:
                        x, y=pyautogui.locateCenterOnScreen('./fotos/Atras.png')
                        pyautogui.moveTo(x,y)
                    else: pyautogui.moveTo(new_centro)
#                
#               pyautogui.moveTo(new_centro)
                
            #Acciones dentro del juego
            if cfg.run_juego == True:
                
                print('estado es : ', cfg.menu_juego)
                if cfg.menu_juego == None: #Menu principal
                    if gesto == 0: #move selection
                        if new_centro[1] < cfg.screen_size[1]*0.3:
                            pyautogui.moveTo(600, 300)
                        elif new_centro[1] > cfg.screen_size[1]*0.3 and new_centro[1] < cfg.screen_size[1]*0.5:
                            pyautogui.moveTo(600, 370)
                        elif new_centro[1] > cfg.screen_size[1]*0.5 and new_centro[1] < cfg.screen_size[1]*0.6:
                            pyautogui.moveTo(600, 460)
                        elif new_centro[1] > cfg.screen_size[1]*0.6 and new_centro[1] < cfg.screen_size[1]*0.7:
                            pyautogui.moveTo(600, 530)
                        elif new_centro[1] > cfg.screen_size[1]*0.7 and new_centro[1] < cfg.screen_size[1]*0.9:
                            pyautogui.moveTo(600, 600)
                        elif new_centro[1] > cfg.screen_size[1]*0.9 and new_centro[1] < cfg.screen_size[1]:
                            pyautogui.moveTo(600, 690)
                            
                    
                if cfg.menu_juego == 0: #dentro del play
                    if gesto == 0:
                        cfg.K_SPACE = True #sirve para sacar y disparar
    #                    print('pres space')
                    else: cfg.K_SPACE = False
                    if gesto == 1:
                        if new_centro[0] > cfg.screen_size[0]*9/16:
                            cfg.K_RIGHT = True
                            
                        elif new_centro[0] < cfg.screen_size[0]*7/16:
                            cfg.K_LEFT = True
                            
                        else:
                            cfg.K_RIGHT = False
                            cfg.K_LEFT = False
                            
                if cfg.menu_juego == 1: #escoger nivel
                    if gesto == 0: #muve selection
                        print('entra')
                        if new_centro[0] < cfg.screen_size[0]*0.2 and new_centro[1] < cfg.screen_size[1]*0.5:
                            x, y=pyautogui.locateCenterOnScreen('./fotos/level_1.png')
                            pyautogui.moveTo(x,y)
                        elif new_centro[0] > cfg.screen_size[0]*0.8 and new_centro[0] < cfg.screen_size[0] and new_centro[1] > cfg.screen_size[1]*0.75:
                            x, y=pyautogui.locateCenterOnScreen('./fotos/back.png')
                            pyautogui.moveTo(x,y)
                        elif new_centro[0] < cfg.screen_size[0]*0.2 and new_centro[1] > cfg.screen_size[1]*0.5:
                            x, y=pyautogui.locateCenterOnScreen('./fotos/level_6.png')
                            pyautogui.moveTo(x,y)
                        elif new_centro[0] > cfg.screen_size[0]*0.2 and new_centro[0] < cfg.screen_size[0]*0.4 and new_centro[1] < cfg.screen_size[1]*0.5:
                            x, y=pyautogui.locateCenterOnScreen('./fotos/level_2.png')
                            pyautogui.moveTo(x,y)
                        elif new_centro[0] > cfg.screen_size[0]*0.2 and new_centro[0] < cfg.screen_size[0]*0.4 and new_centro[1] > cfg.screen_size[1]*0.5:
                            x, y=pyautogui.locateCenterOnScreen('./fotos/level_7.png')
                            pyautogui.moveTo(x,y)
                        elif new_centro[0] > cfg.screen_size[0]*0.4 and new_centro[0] < cfg.screen_size[0]*0.6 and new_centro[1] < cfg.screen_size[1]*0.5:
                            x, y=pyautogui.locateCenterOnScreen('./fotos/level_3.png')
                            pyautogui.moveTo(x,y)
                        elif new_centro[0] > cfg.screen_size[0]*0.4 and new_centro[0] < cfg.screen_size[0]*0.6 and new_centro[1] > cfg.screen_size[1]*0.5:
                            x, y=pyautogui.locateCenterOnScreen('./fotos/level_8.png')
                            pyautogui.moveTo(x,y)
                        elif new_centro[0] > cfg.screen_size[0]*0.6 and new_centro[0] < cfg.screen_size[0]*0.8 and new_centro[1] < cfg.screen_size[1]*0.5:
                            x, y=pyautogui.locateCenterOnScreen('./fotos/level_4.png')
                            pyautogui.moveTo(x,y)
                        elif new_centro[0] > cfg.screen_size[0]*0.6 and new_centro[0] < cfg.screen_size[0]*0.8 and new_centro[1] > cfg.screen_size[1]*0.5:
                            x, y=pyautogui.locateCenterOnScreen('./fotos/level_9.png')
                            pyautogui.moveTo(x,y)
                        elif new_centro[0] > cfg.screen_size[0]*0.8 and new_centro[0] < cfg.screen_size[0] and new_centro[1] < cfg.screen_size[1]*0.5:
                            x, y=pyautogui.locateCenterOnScreen('./fotos/level_5.png')
                            pyautogui.moveTo(x,y)
                        elif new_centro[0] > cfg.screen_size[0]*0.8 and new_centro[0] < cfg.screen_size[0] and new_centro[1] > cfg.screen_size[1]*0.5:
                            x, y=pyautogui.locateCenterOnScreen('./fotos/level_10.png')
                            pyautogui.moveTo(x,y)
                        
                if cfg.menu_juego == 2 or cfg.menu_juego == 3:
                    if gesto == 0: #move selection
                        x, y=pyautogui.locateCenterOnScreen('./fotos/back.png')
                        pyautogui.moveTo(x,y)
                        
                if cfg.menu_juego == 4:
                    if gesto == 0: #move selection
                        if new_centro[1] < cfg.screen_size[1]*0.2:
                            x, y=pyautogui.locateCenterOnScreen('./fotos/Music.png')
                            pyautogui.moveTo(x,y)
                        elif new_centro[1] > cfg.screen_size[1]*0.2 and new_centro[1] < cfg.screen_size[1]*0.4:
                            x, y=pyautogui.locateCenterOnScreen('./fotos/effects.png')
                            pyautogui.moveTo(x,y)
                        elif new_centro[1] > cfg.screen_size[1]*0.4 and new_centro[1] < cfg.screen_size[1]*0.6:
                            x, y=pyautogui.locateCenterOnScreen('./fotos/Paddle.png')
                            pyautogui.moveTo(x,y)
                        elif new_centro[1] > cfg.screen_size[1]*0.6 and new_centro[1] < cfg.screen_size[1]*0.8:
                            x, y=pyautogui.locateCenterOnScreen('./fotos/speed.png')
                            pyautogui.moveTo(x,y)
                        elif new_centro[1] > cfg.screen_size[1]*0.8 and new_centro[1] < cfg.screen_size[1]:
                            x, y=pyautogui.locateCenterOnScreen('./fotos/back.png')
                            pyautogui.moveTo(x,y)
       
                
        if gesto == 2 and cfg.new_centro:
            if cfg.imagen_inicio == False and cfg.video_inicio == False and cfg.run_juego == False:
#                print(cfg.new_centro)
                if cfg.new_centro[0] < 1920 and cfg.new_centro[1] < 1080 and cfg.new_centro[0] > 0 and cfg.new_centro[1] > 0:
                    cfg.mouse_down = True
                    pyautogui.mouseDown() #Presiona el click, pero no suelta hasta cambiar de gesto, evita multiclick
#                    print(pyautogui.position())
            elif cfg.imagen_inicio == True and cfg.accion_rotar == False and cfg.accion_zoom == False or cfg.run_juego == True:
                #Tiene que aguantar el movimiento 5 ciclos para cerrar
                cfg.cerrando += 1
                if cfg.cerrando > cfg.cerrado:
                    cv2.destroyWindow('Imagen selecionada')
                    cv2.destroyWindow('zoom')
                    cfg.imagen_inicio = False
                    cfg.run_juego = False
                    cfg.cerrando = 0
        else:
            if cfg.mouse_down == True:
                pyautogui.mouseUp()     #al cambiar de gesto termina el click
                cfg.mouse_down = False
                cfg.cerrando = 0
    
    
    if click_inicio == 1:
        cfg.img_load = explorador.abrir_imagen()
        if cfg.img_load is None:
            cfg.imagen_inicio = False
        else: cfg.imagen_inicio = True

    if click_inicio == 3:
#        video_inicio = True
        print('Video')
        
    if click_inicio == 2:
        cfg.juego_inicio = True
        print('Juego')
        

            
    click_inicio = 0
