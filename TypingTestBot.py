import cv2
from PIL import ImageGrab
import numpy as np
import pyautogui
import pytesseract
import time

t =time.time()
time.sleep(3) 
while(time.time()<t+55):
    printscreen_pil=ImageGrab.grab(bbox=(86,270,930,320))
    printscreen_numpy =   np.array(printscreen_pil.getdata(),dtype='uint8')\
    .reshape((printscreen_pil.size[1],printscreen_pil.size[0],3)) 
    cv2.imshow('window',printscreen_numpy)
    text = pytesseract.image_to_string(printscreen_numpy)
    text = text[:-1]
    text = text[:-1]
    text = text+" "
    # pyautogui.write(text)
    time.sleep(1)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break

