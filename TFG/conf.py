#datos donde guarda valores de configuracion o de la propia imagen
import cv2
import time


#inicio de video
camara=False
##vs = cv2.VideoCapture('test.mp4')
##vs = cv2.VideoCapture('test2.mp4')
vs = cv2.VideoCapture(0)
#vs = VideoStream(usePiCamera=True).start()
#camara = True


#Rotacion de la imgane( 1 espejo vertical)
rot_img = 1


#margen roi, porcentaje de la ventana
umbral_roi = 0.3

#imagenes de fondo
menu = cv2.imread('./fotos/menu.jpg')
inicio = cv2.imread('./fotos/inicio.jpg')
ajustes = cv2.imread('./fotos/ajustes.jpg')
#imagen help


#parametros camshift
term_crit = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 2, 1)

#extrictante necesirio para iniciar la camara
time.sleep(1.0)

#variables
size_video = None

pretime = None
count_fps = 0
show_fps = str(' ')

predecir = True
evaluar = False
accion = False

gesto = None #Guarda el gesto que la prediccion dijo
new_centro = None #nuevo centro con el tamaño de la pantaña
mouse_down = False #clasifica si mouse 1 esta abajo (si esta clickeado)
cerrando = 0 #contador para cerrar las aplicaciones
cerrado = 20 #numero de iteraciones para salir de la aplicacion

imagen_inicio = False #Indica si esta abierto la imagen dentro de inicio
img_load = None #cargamos la imagen
dentro_imagen = False
accion_zoom = False
centro_y_inicial = None #centro de y inicial para saber su desplazamiento
zoom = 1.2 # zoom por defecto, se guardara los valores nuevos
val_zoom = 50 #diferencia entre inicio y final

accion_rotar = False #Indica si la accion de rotacion en la imagen esta activa, para no entrar en la zona de zoom
centro_x_inicial = None #centro de x inicial para saber su desplazamiento
val_rot = 0 #los grados que rotara la imagen


video_inicio = False

juego_inicio = False
menu_juego = None
run_juego = False
K_SPACE = False
K_RIGHT = False
K_LEFT = False

screen_size = None

periodo_imagen=0 #msm, para mostrar entrada a la red
