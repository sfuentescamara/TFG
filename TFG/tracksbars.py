

import cv2

ventana = 'Rango valores'


def export_rango_valores(a1, a2, a3, c1, c2, c3, r1, r2, r3, t1, t2, t3):
        rango_valores_dat = open('datos.txt', 'w')
        rango_valores_dat.write(str(a1) + '\n' + str(a2) + '\n' + str(a3) + '\n' + str(c1) + '\n' + str(c2) + '\n' + str(c3) + '\n' + str(r1) + '\n' + str(r2) + '\n' + str(r3) + '\n' + str(t1) + '\n' + str(t2) + '\n' + str(t3))
        rango_valores_dat.close()
        

def import_rango_valores():
        rango_valores_dat = open('datos.txt', 'r')
        rango_val = rango_valores_dat.readlines()
        huemax_track1 = int(rango_val[0])
        satmax_track1 = int(rango_val[1])
        valuemax_track1 = int(rango_val[2])
        huemin_track1 = int(rango_val[3])
        satmin_track1 = int(rango_val[4])
        valuemin_track1 = int(rango_val[5])
        rango_valores_dat.close()
        
        
        return huemax_track1, satmax_track1, valuemax_track1, huemin_track1, satmin_track1, valuemin_track1


def import_rango_valores_RGB():
        rango_valores_dat = open('datos.txt', 'r')
        rango_val = rango_valores_dat.readlines()
        redmax_track1 = int(rango_val[6])
        bluemax_track1 = int(rango_val[7])
        greenmax_track1 = int(rango_val[8])
        redmin_track1 = int(rango_val[9])
        bluemin_track1 = int(rango_val[10])
        greenmin_track1 = int(rango_val[11])
        rango_valores_dat.close()
        
        
        return redmax_track1, bluemax_track1, greenmax_track1, redmin_track1, bluemin_track1, greenmin_track1

def on_trackbar(value):
        pass

def color_window():
        huemax_track, satmax_track, valuemax_track, huemin_track, satmin_track, valuemin_track = import_rango_valores()
        cv2.namedWindow(ventana)
        cv2.createTrackbar('Matiz MAX', ventana, huemax_track, 255, on_trackbar)
        cv2.createTrackbar('Saturacion MAX', ventana, satmax_track, 255, on_trackbar)
        cv2.createTrackbar('Valor MAX', ventana, valuemax_track, 255, on_trackbar)
        cv2.createTrackbar('Matiz min', ventana, huemin_track, 255, on_trackbar)
        cv2.createTrackbar('Saturacion min', ventana, satmin_track, 255, on_trackbar)
        cv2.createTrackbar('Valor min', ventana, valuemin_track, 255, on_trackbar) 

        

def color_pos_window():
        RM = cv2.getTrackbarPos('Matiz MAX', ventana)
        BM = cv2.getTrackbarPos('Saturacion MAX', ventana)
        GM = cv2.getTrackbarPos('Valor MAX', ventana)
        rm = cv2.getTrackbarPos('Matiz min', ventana)
        bm = cv2.getTrackbarPos('Saturacion min', ventana)
        gm = cv2.getTrackbarPos('Valor min', ventana)

        return RM, BM, GM, rm, bm, gm


def on_trackbar_BGR(value):
        pass

def color_window_BGR():
        redmax_track, bluemax_track, greenmax_track, redmin_track, bluemin_track, greenmin_track = import_rango_valores_RGB()
        cv2.namedWindow(ventana)
        cv2.createTrackbar('Rojo MAX', ventana, redmax_track, 255, on_trackbar_BGR)
        cv2.createTrackbar('Azul MAX', ventana, bluemax_track, 255, on_trackbar_BGR)
        cv2.createTrackbar('Verde MAX', ventana, greenmax_track, 255, on_trackbar_BGR)
        cv2.createTrackbar('Rojo min', ventana, redmin_track, 255, on_trackbar_BGR)
        cv2.createTrackbar('Azul min', ventana, bluemin_track, 255, on_trackbar_BGR)
        cv2.createTrackbar('Verde min', ventana, greenmin_track, 255, on_trackbar_BGR)
        

def color_pos_window_BGR():
        RM = cv2.getTrackbarPos('Rojo MAX', ventana)
        BM = cv2.getTrackbarPos('Azul MAX', ventana)
        GM = cv2.getTrackbarPos('Verde MAX', ventana)
        rm = cv2.getTrackbarPos('Rojo min', ventana)
        bm = cv2.getTrackbarPos('Azul min', ventana)
        gm = cv2.getTrackbarPos('Verde min', ventana)

        return RM, BM, GM, rm, bm, gm
