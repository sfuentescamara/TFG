#contador de FPS
# Mostrarla con:
#cv2.putText(img2, show_fps, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

import time
import conf as cfg


def contar_FPS():
    
    cfg.count_fps += 1
    if cfg.pretime is None:
        cfg.pretime = time.clock()
        cfg.show_fps = str(' ')
    if (time.clock() - cfg.pretime) >= 1:
        cfg.pretime = time.clock()
        cfg.show_fps = str('FPS: %d' %cfg.count_fps)
        cfg.count_fps = 0

    return cfg.show_fps
