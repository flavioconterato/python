#O objetivo desse script é não ficar afk no GTA5 e com isso pegar pesquisa por tempo no Bunker
#O script basicamente vai ficar andando automaticamente para frente, se ele ficar parado em uma parede, ele tenta andar e não fica afk do mesmo jeito
#Recomendo a cada 30/40 minutos ir pegar a pesquisa. O tempo não é acumulativo, se ele finalizar uma pesquisa e não for coletada, não estará adiantando em nada, logo coletem.
#Script adaptado do SENTDEX: https://www.youtube.com/watch?v=ks4MPfMq8aQ&list=PLQVvvaa0QuDeETZEOy4VdocT7TOjfSA8a

import numpy as np
from PIL import ImageGrab
import cv2
import time
import pyautogui
from directkeys import PressKey, W, A, S, D

def process_img(image):
    original_image = image
    # convert to gray
    processed_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # edge detection
    processed_img =  cv2.Canny(processed_img, threshold1 = 200, threshold2=300)
    return processed_img

def main():
    
    for i in list(range(4))[::-1]:
        print(i+1)
        time.sleep(1)

    last_time = time.time()
    while True:
        PressKey(W)
        screen =  np.array(ImageGrab.grab(bbox=(0,40,800,640)))
        #print('Frame took {} seconds'.format(time.time()-last_time))
        last_time = time.time()
        new_screen = process_img(screen)
        cv2.imshow('window', new_screen)
        #cv2.imshow('window',cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
