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
import Scan_data
__running=0x01
__running_ev=0x11
__fishing=0x02
__fishing_ev=0x12

# hpbox = ImageGrab.grab(bbox=(Scan_data.hpboxdims))
# hpbox.save("C:/Users/Nauckerman/PycharmProjects/screencontrol/kobiscode/hp.png",'PNG')
# hpbox.load()
hpbox=Image.open("C:/Users/Nauckerman/PycharmProjects/screencontrol/kobiscode/hp.png")
# im = ImageGrab.grab(bbox=(Scan_data.pokeballboxdims))
# im.save("C:/Users/Nauckerman/PycharmProjects/screencontrol/kobiscode/test.png",'PNG')
# im.load()
im = Image.open("C:/Users/Nauckerman/PycharmProjects/screencontrol/kobiscode/test.png")
# pokesprite =  ImageGrab.grab(bbox=(Scan_data.pokemon_ev_sprite_dems))
# pokesprite.save("C:/Users/Nauckerman/PycharmProjects/screencontrol/kobiscode/sprite.png",'PNG')
pokesprite=Image.open("C:/Users/Nauckerman/PycharmProjects/screencontrol/kobiscode/sprite.png")
program_state=__fishing_ev
Scan_data.run_fight(pokesprite,im,hpbox)