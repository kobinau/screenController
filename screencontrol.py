from ctypes import windll, Structure, c_long, byref
import pyautogui
import time
from PIL import ImageGrab
from twilio.rest import Client
from PIL import Image
import numpy as np
import cv2
import random
import sys

fightbox=(43,466,122,484)
hpboxdims=(54, 278, 63, 287)
pokeballboxdims=(178, 295, 182, 300)
pokemon_ev_sprite_dems=[362,328,376,354]
fishing_strip = [144,419,378,420]
__running=0x01
__running_ev=0x11
__fishing=0x02
__fishing_ev=0x12
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
        pyautogui.keyDown('up')
        time.sleep(.5)
        pyautogui.keyUp('up')
    else:
        pyautogui.keyDown('down')
        time.sleep(.5)
        pyautogui.keyUp('down')

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

def check_sample_pokemon_image(pokemon_ev_sprite_dems,samplepokemonImage,spritebox):
    samplepokemonImage = ImageGrab.grab(bbox=pokemon_ev_sprite_dems)
    ev_sprite=mse(samplepokemonImage,spritebox)
    if ev_sprite>100:
        if changePos == 0:
            pyautogui.moveTo(168 + 5, 512, .25)
            pyautogui.click()
        else:
            pyautogui.moveTo(168, 512, .25)
            pyautogui.click()
    return ev_sprite

def fight_to_kill(ev_sprite,changePos):
    if ev_sprite<1000:
        if changePos == 0:
            pyautogui.moveTo(55 + 5, 470, .25)
            pyautogui.click()
        else:
            pyautogui.moveTo(55, 472, .25)
            pyautogui.click()
    return changePos

def run_away(ev_sprite, changePos):
    if ev_sprite > 1000:
        if changePos == 0:
            pyautogui.moveTo(160 + 5, 515, .25)
            pyautogui.click()
        else:
            pyautogui.moveTo(160, 515, .25)
            pyautogui.click()
    return changePos

def compare_battle_images(hpbox,im,changePos):

    changePos=(changePos+1)%2
    hpnew = ImageGrab.grab(bbox=(hpboxdims))
    imnew = ImageGrab.grab(bbox=(pokeballboxdims))
    lhp=mse(hpbox,hpnew)
    l = mse(im,imnew)
    return l,lhp,changePos
def move_positions():
    movekeyboard(random.randrange(1, 5))
    movekeyboard(random.randrange(1, 5))
    return

def fishing_state():
    print("In Fishing State")
    # fish_box = ImageGrab.grab(bbox=(fishing_strip))
    # fish_box=Image.open("C:/Users/Nauckerman/PycharmProjects/screencontrol/kobiscode/fishing.png")
    #fish_box.save("C:/Users/Nauckerman/PycharmProjects/screencontrol/kobiscode/fishing2.png",'PNG')


    fish_array = []
    while len(fish_array) == 0:
        fish_box = ImageGrab.grab(bbox=(fishing_strip))
        width, height = fish_box.size
        for i in range(width):
            for j in range(height):
                color = fish_box.getpixel((i, j))
                # print(i, color)
                if color[0] >= 250 and color[1] <= 220 and color[1] >= 210 and color[2] >= 20 and color[2] <= 30:
                    fish_array.append((i, color))
                    print(i, color)
        length_fish_array=len(fish_array)
        if length_fish_array > 0:
            our_desired_index=15


    small_fish_box = (
    fishing_strip[0] + fish_array[our_desired_index][0], fishing_strip[1], fishing_strip[0] + fish_array[our_desired_index][0] + 1,
    fishing_strip[3])
    # print(fishing_strip)
    # print(small_fish_box)
    fishing_state_stable = True
    while fishing_state_stable == True:
        smaller_fish = ImageGrab.grab(bbox=small_fish_box)
        # print(smaller_fish)
        smallwidth, h = smaller_fish.size
        #print(smaller_fish)
        color2 = smaller_fish.getpixel((0, 0))
        if color2 != fish_array[0][1]:
            pyautogui.keyDown('space')
            pyautogui.keyUp('space')
            fishing_state_stable = False


# hpbox = ImageGrab.grab(bbox=(hpboxdims))
# hpbox.save("C:/Users/Nauckerman/PycharmProjects/screencontrol/kobiscode/hp.png",'PNG')
# hpbox.load()
hpbox=Image.open("C:/Users/Nauckerman/PycharmProjects/screencontrol/kobiscode/hp.png")
# im = ImageGrab.grab(bbox=(pokeballboxdims))
# im.save("C:/Users/Nauckerman/PycharmProjects/screencontrol/kobiscode/test.png",'PNG')
# im.load()
im = Image.open("C:/Users/Nauckerman/PycharmProjects/screencontrol/kobiscode/test.png")
# pokesprite =  ImageGrab.grab(bbox=(pokemon_ev_sprite_dems))
# pokesprite.save("C:/Users/Nauckerman/PycharmProjects/screencontrol/kobiscode/sprite.png",'PNG')
pokesprite=Image.open("C:/Users/Nauckerman/PycharmProjects/screencontrol/kobiscode/sprite.png")
program_state=__fishing_ev
while True:
    fishing_state()

    time.sleep(1)
    timer()
    changePos=0
    catching_state=True
    while catching_state==True:
        catch=False
        pos=queryMousePosition()
        #move_positions()
        print(pos)
        l, lhp, changePos = compare_battle_images(hpbox,im,changePos)
        time.sleep(.5)
        print(l,lhp)
        if lhp<100 and l>1000:
            print("can catch")
            catch=True
        elif lhp>15000 and l>15000:
            print("catching over")
            catching_state=False
        else:
            print("not catching")
        if catch:
          sys.exit()

        elif not catch:
            sample_sprite=ImageGrab.grab(bbox=pokemon_ev_sprite_dems)
            ev_sprite=mse(pokesprite,sample_sprite)
            #ev_sprite=check_sample_pokemon_image(pokemon_ev_sprite_dems,samplepokemonImage,spritebox)
            run_away(ev_sprite, changePos)
            fight_to_kill(ev_sprite,changePos)


