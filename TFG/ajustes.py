     #programa ajustes, para la configuracion de la deteccion
import cv2
import conf as cfg
import mascaras
import tracksbars
from contar_frames import contar_FPS

#imagenes
img_ajustes = cfg.ajustes


#Raton
click_ajustes = 0
on_sel_click = (0,0)
def on_mouse1(event, x, y, flags, param):
        global on_sel_click, click_ajustes
        if event == cv2.EVENT_LBUTTONDOWN:  #258 mitad del ancho y 185 mitad del alto $%&cambiar si cambio imagen
                on_sel_click = x, y
                if on_sel_click[0] < 800 and on_sel_click[0] > 135 and on_sel_click[1] < 400 and on_sel_click[1] > 190:
#                        print("primer cuadro")
                        click_ajustes = 1
                if on_sel_click[0] < 1250 and on_sel_click[0] > 840 and on_sel_click[1] < 335 and on_sel_click[1] > 225:
#                        print("segundo cuadro")
                        click_ajustes = 2
                if on_sel_click[0] < 730 and on_sel_click[0] > 135 and on_sel_click[1] < 670 and on_sel_click[1] > 440:
#                        print("tercer cuadro")
                        click_ajustes = 3
                if on_sel_click[0] < 1200 and on_sel_click[0] > 890 and on_sel_click[1] < 1200 and on_sel_click[1] > 475:
#                        print("cuarto cuadrante")
                        click_ajustes = 4


def ajustes(size_video):
    global click_ajustes

    muestra_rango_valores = False
    muestra_conf = False
    rango_valores = False

    while(1):

        cfg.cv2.imshow('Ajustes', img_ajustes)
        cfg.cv2.moveWindow('Ajustes', 300, 50)
        
        click_ajustes = 0
        cv2.setMouseCallback("Ajustes", on_mouse1)

        key = cfg.cv2.waitKey(1) & 0xFF
                  

        if muestra_rango_valores == True:
            rango_valores = True
            if key == ord('a'):
                huemax_track, satmax_track, valuemax_track, huemin_track, satmin_track, valuemin_track = tracksbars.color_pos_window()
                redmax_track, bluemax_track, greenmax_track, redmin_track, bluemin_track, greenmin_track = tracksbars.color_pos_window_BGR()
                tracksbars.export_rango_valores(huemax_track, satmax_track, valuemax_track, huemin_track, satmin_track, valuemin_track, redmax_track, bluemax_track, greenmax_track, redmin_track, bluemin_track, greenmin_track)
                                                                    
        elif muestra_rango_valores == False:
            rango_valores = False
                                                    
                                                                    
        if key == ord(chr(27)) or click_ajustes == 4:
            muestra_rango_valores = False
            muestra_conf = False
            rango_valores = False
            cfg.cv2.destroyAllWindows()
            break
                                                    
        elif key == ord('f') or click_ajustes == 2:
            shot_idx = 0
            print ('Camara de fotos: Pulsa la barra espaciadora para sacar foto')
            while(1):
                if cfg.camara is True:
                    image = cfg.vs.read()
                else:
                    ret, image = cfg.vs.read()
                    if ret is False: #si termina el video
                        print('Video finalizado')
                        cfg.cv2.destroyAllWindows()
                        break
                    
                image=cfg.cv2.flip(image, flipCode=cfg.rot_img) #rotar imagen o hacerla simetrica, cambiar en otra opcion y guardarlo
                show_fps = contar_FPS()
                cfg.cv2.putText(image, show_fps, (10, 30), cfg.cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
                cfg.cv2.imshow('Tomar foto', image)
                cfg.cv2.moveWindow('Tomar foto', 270, 360)
                imgs=[]
                imgs.append(image)

                key = cfg.cv2.waitKey(1) & 0xFF

                if key == ord(' '):
                    for i, image in enumerate(imgs):
                        name = './fotos/foto_%d_%03d.bmp' %(i, shot_idx)
                        cfg.cv2.imwrite(name, image)
                        print(name, 'save')
                        shot_idx += 1

                elif key == ord(chr(27)):
                    print ('camara de fotos desactivada.')
                    cfg.cv2.destroyWindow('Tomar foto')
                    break



        elif key == ord('r') or click_ajustes == 3:
            if muestra_rango_valores == True:
                muestra_rango_valores = False

                cfg.cv2.destroyWindow('Rango valores')
                print('Muestra rango valores DESACTIVADO')

            elif muestra_rango_valores == False:
                tracksbars.color_window()
                tracksbars.color_window_BGR()
                muestra_rango_valores = True
                print('Muestra rango valores ACTIVADO')


        elif key == ord('m') or click_ajustes == 1:
            if muestra_conf == True:
                muestra_conf = False

                cfg.cv2.destroyWindow('mascara_HSV&BGR')
                cfg.cv2.destroyWindow('mascara_HSV')
                cfg.cv2.destroyWindow('mascara_RGB')
                print('Muestra configuracion DESACTIVDA')
                                            
            elif muestra_conf == False:
                muestra_conf = True
                print('Muestra configuracion ACTIVADA')

                if rango_valores is True:
                    huemax_track, satmax_track, valuemax_track, huemin_track, satmin_track, valuemin_track = tracksbars.color_pos_window()
                    redmax_track, bluemax_track, greenmax_track, redmin_track, bluemin_track, greenmin_track = tracksbars.color_pos_window_BGR()

                else:
                    huemax_track, satmax_track, valuemax_track, huemin_track, satmin_track, valuemin_track  = tracksbars.import_rango_valores()
                    redmax_track, bluemax_track, greenmax_track, redmin_track, bluemin_track, greenmin_track = tracksbars.import_rango_valores_RGB()
     
                                                    
                                                    
                                            

                            #elif key == ord('g'):
                            #girar camara o rotarla segun quieras, y guardarse los valores en el txt

                            

        if muestra_conf is True:

            if rango_valores == True:
                huemax_track, satmax_track, valuemax_track, huemin_track, satmin_track, valuemin_track = tracksbars.color_pos_window()
                redmax_track, bluemax_track, greenmax_track, redmin_track, bluemin_track, greenmin_track = tracksbars.color_pos_window_BGR()
            else:
                huemax_track, satmax_track, valuemax_track, huemin_track, satmin_track, valuemin_track  = tracksbars.import_rango_valores()
                redmax_track, bluemax_track, greenmax_track, redmin_track, bluemin_track, greenmin_track = tracksbars.import_rango_valores_RGB()


            if cfg.camara is True:
                image = cfg.vs.read()
            else:
                ret, image = cfg.vs.read()
                if ret is False: #si termina el video
                    print('Video finalizado')
                    cfg.cv2.destroyAllWindows()
                    break
                
            image=cfg.cv2.flip(image, flipCode=cfg.rot_img)            
            mask, imagen_mascara, hsv, rango_hsv_max, rango_hsv_min = mascaras.mascaraHSV(huemax_track, satmax_track, valuemax_track, huemin_track, satmin_track, valuemin_track, image)
            mask_RGB, mascara_colorRGB, rangomaxRGB, rangominRGB = mascaras.mascaraRGB(redmax_track, bluemax_track, greenmax_track, redmin_track, bluemin_track, greenmin_track, image)
            conv_mask = mascaras.mascaraHSVandRGB(mask, mask_RGB)

            show_fps = contar_FPS()
            cfg.cv2.putText(mascara_colorRGB, show_fps, (10, 30), cfg.cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
            
            mascara_colorRGB = cfg.cv2.resize(mascara_colorRGB, (0,0), fx=0.5, fy=0.5)
            cfg.cv2.imshow('mascara_RGB', mascara_colorRGB)
            cfg.cv2.moveWindow('mascara_RGB', 300, 750)
            
            imagen_mascara = cfg.cv2.resize(imagen_mascara, (0,0), fx=0.5, fy=0.5)
            cfg.cv2.imshow('mascara_HSV', imagen_mascara)
            cfg.cv2.moveWindow('mascara_HSV', 750, 750)
            
            conv_mask = cfg.cv2.resize(conv_mask, (0,0), fx=0.5, fy=0.5)
            cfg.cv2.imshow('mascara_HSV&BGR', conv_mask)
            cfg.cv2.moveWindow('mascara_HSV&BGR', 1200, 750)
            
            cfg.cv2.resizeWindow('Rango valores', 300, 0)
            cfg.cv2.moveWindow('Rango valores', 0, 300)

