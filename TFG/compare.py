#funcion para la entrada de la red neuronal y su escalado no afecte a la imagen
#En los bordes la imagen no compartira el mismo ancho y alto y al reescalar se vera
#afectada

import conf as cfg


def img2compare(img, size_vent, centro):
    w = size_vent[0]
    h = size_vent[1]
    if w < h:
        size_cuadro = int(h/2)
    else:
        size_cuadro = int(w/2)

        
    x1, y1 = int(centro[0]) - size_cuadro, int(centro[1]) - size_cuadro #x_1, y_1
    x2, y2 = int(centro[0]) + size_cuadro, int(centro[1]) + size_cuadro #x_2, y_2


##  (x1, y1)
##    .-------------.
##    |             |
##    |             |
##    |             |
##    .-------------.
##              (x2, y2)


    #Aumento el recuadro para que ol objeto se vea mas centrado y no en los bordes
    #la variable cfg.umbral_roi esta en conf.py

    y1 = int(y1 - size_cuadro*cfg.umbral_roi)
    y2 = int(y2 + size_cuadro*cfg.umbral_roi)
    
    altura = abs(y2 - y1)
    y1 = int(y1 - y1*0.3)
    y2 = int(y1 + altura)
    x1 = int(x1 - size_cuadro*cfg.umbral_roi)
    x2 = int(x2 + size_cuadro*cfg.umbral_roi)


        ## si tiene valores negativos no puede mostrar la imagen
    if y1 < 0:
        y1 = 0
##        print 'Alejate de los bordes y1'
    if y2 < 0:
        y2 = 0
##        print 'Alejate de los bordes y2'
    if x1 < 0:
        x1 = 1
##        print 'Alejate de los bordes x1'
    if x2 < 0:
        x2 = 1
##        print 'Alejate de los bordes x2'

    vent_in = img[y1:y2, x1:x2]

    if vent_in.shape[0] is not vent_in.shape[1]:
        warning = 'WARNING: La imagen se deformara alejate de los bordes'
    else:
        warning = 'Good'
            

    return vent_in, warning
