import easygui as eg
import cv2
import imutils
import numpy as no
import time


def abrir_imagen():
    archivo = eg.fileopenbox(msg='Abrir archivo', title='Seliciona una imagen', default='./fotos/imagenes/', filetypes='*.jpg')
    
    if archivo is not None:
        img = cv2.imread(archivo)
        return img

    
if __name__ == '__main__':
    img = abrir_imagen()
    imgx=img
    if(1):

        i = 180
#        img = imutils.rotate_bound(img, i)
        
        num_rows, num_cols = img.shape[:2]
        
        rotation_matrix = cv2.getRotationMatrix2D((num_cols/2, num_rows/2), i, 1)
        img_rotation = cv2.warpAffine(img, rotation_matrix, (num_cols, num_rows))
        
        img2 = img_rotation.copy()
        cv2.putText(img2, str('x9.5'), (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (255, 255, 255), 2)
        cv2.imshow('img_ratate', img2)
        cv2.imshow('img', imgx)
        cv2.moveWindow('img', 800, 180)
        time.sleep(1)
        key = cv2.waitKey(0) & 0xFF #Espero orden
        if key == ord(chr(27)):
            print('Salir')
#            break
    cv2.destroyAllWindows()