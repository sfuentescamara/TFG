import conf as cfg
import inicio, ajustes
import cv2


##Imagenes
menu = cfg.menu
ayuda = cfg.inicio


## Tamano del video
if cfg.camara is True:
        imagen = cfg.vs.read()
else:
        ret, imagen = cfg.vs.read()
        
cfg.size_video= imagen.shape #(y, x, dim)

#Raton
click_menu = 0
on_sel_click = (0,0)
def on_mouse(event, x, y, flags, param):
        global on_sel_click, click_menu
        if event == cv2.EVENT_LBUTTONUP:  #258 mitad del ancho y 185 mitad del alto $%&cambiar si cambio imagen
                on_sel_click = x, y
                if on_sel_click[0] < 525 and on_sel_click[0] > 100 and on_sel_click[1] < 350 and on_sel_click[1] > 170:
#                        print("primer cuadro")
                        click_menu = 1
                if on_sel_click[0] < 525 and on_sel_click[0] > 100 and on_sel_click[1] < 535 and on_sel_click[1] > 350:
#                        print("segundo cuadro")
                        click_menu = 2
                if on_sel_click[0] < 1200 and on_sel_click[0] > 780 and on_sel_click[1] < 400 and on_sel_click[1] > 235:
#                        print("tercer cuadro")
                        click_menu = 3
                if on_sel_click[0] < 1200 and on_sel_click[0] > 780 and on_sel_click[1] < 630 and on_sel_click[1] > 450:
#                        print("cuarto cuadrante")
                        click_menu = 4


cv2.destroyAllWindows()

## Menu
while(1):

        cv2.imshow('Menu', menu) #Presento menu
        cv2.moveWindow('Menu', 300, 50)
        
        click_menu = 0
        cv2.setMouseCallback("Menu", on_mouse)


        key = cv2.waitKey(1) & 0xFF #Espero orden

        ## Listado de ordenes
        if key == ord("i") or click_menu == 1:
                print('Inicio')
                
                cv2.destroyWindow('Menu')
                inicio.inicio_p()

        elif key == ord("h") or click_menu == 3:
                print('Help')
                while(1):
                        cv2.destroyWindow('Menu')
                        cv2.imshow('Ayuda', ayuda)
                        key = cv2.waitKey(1) & 0xFF #Espero orden
                        if key == ord(chr(27)):
                                cv2.destroyWindow('Ayuda')
                                break

        elif key == ord("c") or click_menu == 2:
                print('Configuracion')
                cv2.destroyWindow('Menu')
                ajustes.ajustes(cfg.size_video)
                                
        elif key == ord(chr(27)) or click_menu == 4:
            print('Salir')
            break
        

cfg.vs.release()
cv2.destroyAllWindows()
