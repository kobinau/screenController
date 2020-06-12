from ctypes import windll, Structure, c_long, byref
import pyautogui
import time
from PIL import ImageGrab
from PIL import Image
import numpy as np
import cv2
import random
def timer():
    now=time.localtime(time.time())
    return now[5]


class POINT(Structure):
    _fields_ = [("x", c_long), ("y", c_long)]


def queryMousePosition():
    arr=[0, 0]
    arr=[0, 0]
    pt = POINT()
    windll.user32.GetCursorPos(byref(pt))
    arr[0]=pt.x
    arr[1]=pt.y
    return arr


def imAverage(image):
    a = np.asarray(image)
    average = cv2.mean(a,mask=None)
    return average

def movekeyboard(i):
    if i == 1:
        pyautogui.keyDown('up')
        time.sleep(.5)
        pyautogui.keyUp('up')
    elif i == 2:
        pyautogui.keyDown('down')
        time.sleep(.5)
        pyautogui.keyUp('down')
    elif i == 3:
        pyautogui.keyDown('right')
        time.sleep(.5)
        pyautogui.keyUp('right')
    else:
        pyautogui.keyDown('left')
        time.sleep(.5)
        pyautogui.keyUp('left')

def mse(imageA, imageB):
    # the 'Mean Squared Error' between the two images is the
    # sum of the squared difference between the two images;
    # NOTE: the two images must have the same dimension
    a = np.asarray(imageA)
    b = np.asarray(imageB)
    err = np.sum((a.astype(float) - b.astype(float)) ** 2)
    err /= float(a.shape[0] * a.shape[1])

    # return the MSE, the lower the error, the more "similar"
    # the two images are
    return err
fightbox=(43,466,122,484)
hpboxdims=(47, 276, 59, 280)
pokeballboxdims=(170, 292, 184, 299)

hpbox = ImageGrab.grab(bbox=(hpboxdims))
hpbox.save("C:/Users/Nauckerman/PycharmProjects/screencontrol/kobiscode/hp.png",'PNG')
im = ImageGrab.grab(bbox=(pokeballboxdims))
im.save("C:/Users/Nauckerman/PycharmProjects/screencontrol/kobiscode/test.png",'PNG')
poke_cornerx=45
poke_cornery=485
#impoke = ImageGrab.grab(bbox=(poke_cornerx-20, poke_cornery, poke_cornerx-1, poke_cornery+12))
#impoke.save("C:/Users/Nauckerman/PycharmProjects/screencontrol/kobiscode/notcaught.png",'PNG')
#im=cv2.imread("C:/Users/Nauckerman/PycharmProjects/screencontrol/kobiscode/test.png")
im.load()
pokeballavg=imAverage(im)
hpbox.load()
hpboxavg=imAverage(hpbox)
timer()
changepos=0
changePos=True
while True:
    pos=queryMousePosition()
    changePos=changePos+1
    changePos=changePos%2

    print(changePos)



    movekeyboard(random.randrange(1, 5))
    movekeyboard(random.randrange(1, 5))
    hpnew = ImageGrab.grab(bbox=(hpboxdims))
    imnew = ImageGrab.grab(bbox=(pokeballboxdims))
    hpboxavgnew=imAverage(hpnew)
    imnewaverage=imAverage(imnew)
    #newimpoke = ImageGrab.grab(bbox=(poke_cornerx, poke_cornery, poke_cornerx+19, poke_cornery+12))
    #newimpoke.save("C:/Users/Nauckerman/PycharmProjects/screencontrol/kobiscode/caught.png", 'PNG')
    #newimpoke = ImageGrab.grab(bbox=(280, 650, 299, 662))
    #newaverage=imAverage(newimpoke)
    lhp=mse(hpbox,hpnew)
    l = mse(im,imnew)
    print(l,",",lhp)
    catch=False
    #for k in range(3):
    #    time.sleep(5)
    print(pos)

    if lhp<100 and l>1000:
        print("can catch")
        catch=True
    else:
        print("not catching")
    if catch:
        while True:
             kobi=5
            # time.sleep(5)
            # pyautogui.moveTo(pos[0]+30, pos[1])
            # if changePos:
            #     pyautogui.moveTo(pos[0]+30 + 5, pos[1], .5)
            #     changePos = not changePos
            # else:
            #     pyautogui.moveTo(pos[0]+30 - 5, pos[1], .5)
            # pyautogui.click(pos[0]+30, pos[1])
            # time.sleep(5)
            # pyautogui.moveTo(pos[0]-30, pos[1]+45)
            # if changePos:
            #     pyautogui.moveTo(pos[0] + 5, pos[1]+45, .5)
            #     changePos = not changePos
            # else:
            #     pyautogui.moveTo(pos[0] - 5, pos[1]+45, .5)
            # pyautogui.click(pos[0],pos[1]+45)
    elif not catch:
        if changePos==0:
            pyautogui.moveTo(55 + 5, 470, .5)
            pyautogui.click()
        else:
            pyautogui.moveTo(55 , 472, .5)
            pyautogui.click()
        # if pos[0]>174 and pos[0]<286 and pos[1]>849 and pos[1]<879:
        #     if changePos:
        #         pyautogui.moveTo(pos[0]+5, pos[1], .5)
        #         changePos= not changePos
        #     else: pyautogui.moveTo(pos[0]-5, pos[1], .5)
        #     pyautogui.click(pos[0], pos[1])

