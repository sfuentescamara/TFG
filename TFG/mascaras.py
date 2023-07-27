#!/home/pi/entornos_virtuales/cv/local/bin python

import cv2
import numpy as np

#Funcion importada:
#mask, imagen_mascara, hsv, rango_hsv_max, rango_hsv_min, _= mascaraHSV(huemax_track, satmax_track, valuemax_track, huemin_track, satmin_track, valuemin_track, image)
#..


def mascaraHSV(huemax, satmax, valuemax, huemin, satmin, valuemin, image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    rangomaxHSV=np.array([satmax, valuemax, huemax])
    rangominHSV=np.array([satmin, valuemin, huemin])
    mascaraHSV=cv2.inRange(hsv, rangominHSV, rangomaxHSV)
    mascara_colorHSV=cv2.bitwise_and(hsv, hsv, mask=mascaraHSV)
    
    return mascaraHSV, mascara_colorHSV, hsv, rangomaxHSV, rangominHSV


def mascaraRGB(redmax, bluemax, greenmax, redmin, bluemin, greenmin, image):
    RGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) #opencv trabaja por defecto con colores BGR
    rangomaxRGB=np.array([redmax, greenmax, bluemax]) #bgr
    rangominRGB=np.array([redmin, greenmin, bluemin])
    mascaraRGB=cv2.inRange(image, rangominRGB, rangomaxRGB)
##    mascaraRGB = cv2.cvtColor(mascaraRGB, cv2.COLOR_RGB2BGR)
    mascara_colorBGR=cv2.bitwise_and(image, image, mask=mascaraRGB)
    
    return mascaraRGB, mascara_colorBGR, rangomaxRGB, rangominRGB

def mascaraHSVandRGB(mascaraHSV, mascaraRGB):
    resultado = cv2.bitwise_and(mascaraRGB, mascaraRGB, mask=mascaraHSV)

    return resultado



if __name__ == '__main__':
    print(' ')
