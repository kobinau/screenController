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
hpbox=Image.open("C:/Users/Nauckerman/PycharmProjects/screencontrol/kobiscode/hp.png")
# im = ImageGrab.grab(bbox=(Scan_data.pokeballboxdims))
# im.save("C:/Users/Nauckerman/PycharmProjects/screencontrol/kobiscode/test.png",'PNG')
im = Image.open("C:/Users/Nauckerman/PycharmProjects/screencontrol/kobiscode/test.png")
# pokesprite =  ImageGrab.grab(bbox=(Scan_data.pokemon_ev_sprite_dems))
# pokesprite.save("C:/Users/Nauckerman/PycharmProjects/screencontrol/kobiscode/sprite.png",'PNG')
pokesprite=[]
pokesprite.append(Image.open("C:/Users/Nauckerman/PycharmProjects/screencontrol/kobiscode/sprite.png"))
# pokesprite.append(Image.open("C:/Users/Nauckerman/PycharmProjects/screencontrol/kobiscode/sprite2.png"))
# pokesprite.append(Image.open("C:/Users/Nauckerman/PycharmProjects/screencontrol/kobiscode/sprite3.png"))
# elitesprite =  ImageGrab.grab(bbox=(Scan_data.elite_box))
# elitesprite.save("C:/Users/Nauckerman/PycharmProjects/screencontrol/kobiscode/elitetokgrass.png",'PNG')
elitesprite = Image.open("C:/Users/Nauckerman/PycharmProjects/screencontrol/kobiscode/elitetokgrass.png")
# firstBracket = ImageGrab.grab(bbox=Scan_data.shin_or_elite_box)
# firstBracket.save("C:/Users/Nauckerman/PycharmProjects/screencontrol/kobiscode/bracket.png",'PNG')
firstBracket = Image.open("C:/Users/Nauckerman/PycharmProjects/screencontrol/kobiscode/bracket.png")
program_state=__fishing_ev

Scan_data.run_fight(pokesprite,im,hpbox,elitesprite,firstBracket)
