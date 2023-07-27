import cv2
import conf as cfg
import msm
import imutils
import Arkanoid.games as gs

def funcion_imagenes_inicio(gesto, centro):
        bigger = cv2.resize(cfg.img_load, (0,0), fx=cfg.zoom, fy=cfg.zoom)
        
        def onmouse(event, x, y, flags, param):
            h, w = cfg.img_load.shape[:2]
            h1, w1 = bigger.shape[:2]
            x, y = 1.0*x*h1/h, 1.0*y*h1/h
            zoom = cv2.getRectSubPix(bigger, (500, 375), (x+0.5, y+0.5))
                
            if gesto == 1 and cfg.accion_rotar == False and cfg.accion_zoom == False: # No entro a la img si estoy haciendo una accion
                cv2.imshow('zoom', zoom)
                cv2.moveWindow('zoom', 0, 400)
            else: 
                cv2.destroyWindow('zoom')
        
        if cv2.getWindowProperty('zoom', 0) >= 0: #los gestos no funcionan si el zoom esta activo
            cfg.dentro_imagen = True
                
        if gesto == 1 and cfg.dentro_imagen == False: # si entro a la imagen o cambio de gesto no hay accion
#            print(cfg.new_centro[0], msm.screen_size()[0]/2)
            
            """ZOOM"""
            #Hacer el gesto 1 en el borde derecho de la pantalla, el desplazamiento es la cantidad
            if cfg.new_centro[0] > int(msm.screen_size()[0])*2/3 and cfg.accion_rotar == False:
#                print('activar zoom')
                cfg.accion_zoom = True
                    
                if cfg.centro_y_inicial == None:
                    cfg.centro_y_inicial = centro[1]
                centro_y_final = centro[1]
                cfg.val_zoom = abs(centro_y_final - cfg.centro_y_inicial)
#                print(cfg.centro_y_inicial, centro_y_final, val_zoom)
                    
                """ROTACION"""
            #Hacer el gesto 1 en el borde inferior de la pantalla, el desplazamiento es la cantidad
            elif cfg.new_centro[1] > int(msm.screen_size()[1])*2/3 and cfg.accion_zoom == False:
#                print('Rotación')
                cfg.accion_rotar = True
                
                if cfg.centro_x_inicial == None:
                    cfg.centro_x_inicial = centro[0]
                centro_x_final = centro[0]
                cfg.val_rot = (centro_x_final - cfg.centro_x_inicial)/5
#                print(centro_x_final, cfg.centro_x_inicial, cfg.val_rot)
                
                """Funciona pero al rotar corta la imagen
                num_rows, num_cols = cfg.img_load.shape[:2]
                rotation_matrix = cv2.getRotationMatrix2D((num_cols/2, num_rows/2), cfg.val_rot, 1)
                cfg.img_load = cv2.warpAffine(cfg.img_load, rotation_matrix, (num_cols, num_rows))
                """
                
                img_rotada = imutils.rotate_bound(cfg.img_load, cfg.val_rot)
                

                
            else:
                cfg.accion_zoom = False
                cfg.accion_rotar = False
                
                
                
        else:
            cfg.zoom = cfg.val_zoom/20 #Nuevo valor del zoom
            cfg.centro_x_inicial = None
            cfg.centro_y_inicial = None
            if cfg.zoom == 0:
                cfg.zoom = 1
            
            print(cfg.val_rot)
            if cfg.val_rot >= 25:   #rota la imagen si supera los 50º
                cfg.img_load = cv2.rotate(cfg.img_load, cv2.ROTATE_90_CLOCKWISE)
                cfg.val_rot = 0
            elif cfg.val_rot <= -25:
                cfg.img_load = cv2.rotate(cfg.img_load, cv2.ROTATE_90_COUNTERCLOCKWISE)
                cfg.val_rot = 0

            
        zoom_string = 'x' + str(cfg.zoom)
        try:
            img = img_rotada.copy()
        except:
            img = cfg.img_load.copy()
        cv2.putText(img, zoom_string, (30, 50), cfg.cv2.FONT_HERSHEY_SIMPLEX, 1.3, (255, 255, 255), 2)
        cv2.imshow('Imagen selecionada', img)
        cv2.moveWindow('Imagen selecionada', 500, 200)
        cv2.setMouseCallback('Imagen selecionada', onmouse)
        cfg.dentro_imagen = False

    