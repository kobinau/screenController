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
import smtplib,ssl

fightbox=(43,466,122,484)
hpboxdims=(57, 280, 63, 282)
pokeballboxdims=(178, 295, 182, 303)
pokemon_ev_sprite_dems=[362,328,376,354]
fishing_strip = [144,419,378,420]
shin_or_elite_box = [52,266,56,276]
elite_box = [50,266,64,274]
port=465
smtp_server = "smtp.gmail.com"
sender_email = "sendermail@gmail.com"  # Enter your address
receiver_email = "madeupemail@gmail.com"  # Enter receiver address
message1="""\
Subject: You can catch a pokemon!

Go check it out!"""
message2="""\
Subject: This might be a shiny or elite!

Go check it out!"""

message3="""\
Subject: This be a shiny yall!

Go check it out!"""
password = "Madeuppassword123"


__running=0x01
__running_ev=0x11
__fishing=0x02
__fishing_ev=0x12
def timer():
    now=time.localtime(time.time())
    return now[5]

def sendEmail(message):
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
    return

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
    else:
        pyautogui.keyDown('down')
        time.sleep(.5)
        pyautogui.keyUp('down')
    # elif i == 2:
    #     pyautogui.keyDown('down')
    #     time.sleep(.5)
    #     pyautogui.keyUp('down')
    # elif i == 3:
    #     pyautogui.keyDown('up')
    #     time.sleep(.5)
    #     pyautogui.keyUp('up')
    # else:
    #     pyautogui.keyDown('down')
    #     time.sleep(.5)
    #     pyautogui.keyUp('down')

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

def fight_to_kill(ev_sprite):
    pyautogui.keyDown('1')
    time.sleep(.25)
    pyautogui.keyUp('1')
    return

def run_away(ev_sprite):
    pyautogui.keyDown('4')
    time.sleep(.25)
    pyautogui.keyUp('4')
    return

def compare_battle_images(hpbox,im,changePos):
    changePos=(changePos+1)%2
    hpnew = ImageGrab.grab(bbox=(hpboxdims))
    imnew = ImageGrab.grab(bbox=(pokeballboxdims))
    lhp=mse(hpbox,hpnew)
    l = mse(im,imnew)
    return l,lhp,changePos
def move_positions(i):
    movekeyboard(i)
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
                    # print(i, color)
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

def fishing_yo(pokesprite,im,hpbox):
    num_pokes=0
    while True:
        fishing_state()

        time.sleep(1)
        timer()
        changePos = 0
        catching_state = True
        while catching_state == True:
            catch = False
            pos = queryMousePosition()
            # move_positions()
            print(pos)
            time.sleep(1)
            l, lhp, changePos = compare_battle_images(hpbox, im, changePos)
            time.sleep(.5)
            print(l, lhp)
            if lhp < 100 and l > 1000:
                print("can catch")
                catch = True
            elif lhp > 15000 and l > 15000:
                num_pokes=num_pokes+1
                print(num_pokes )
                print("catching over")
                catching_state = False
            else:
                print("not catching")
            if catch:
                sendEmail(message1)
                sys.exit()

            elif not catch:
                sample_sprite=ImageGrab.grab(bbox=pokemon_ev_sprite_dems)
                ev_sprite_arr=[]
                for i in pokesprite:
                    ev_sprite_arr.append(mse(i,sample_sprite))
                # ev_sprite = 10
                ev_sprite=min(ev_sprite_arr)
                if ev_sprite < 1000:
                    run_away(ev_sprite)
                else:
                    fight_to_kill(ev_sprite)


def run_fight(pokesprite, im, hpbox,elitetok,firstBracket):
    changePos = 0
    numEncounters = 0
    # fishing_yo(hpbox,pokesprite,im)
    timer()
    while True:

        # move position state
        keep_moving = True
        while keep_moving == True:
            pos = queryMousePosition()
            print(pos)
            move_positions(changePos)
            l, lhp, changePos = compare_battle_images(hpbox, im, changePos)
            print(l,lhp)
            if lhp < 100:
                keep_moving = False
                print("leaving moving state")
            time.sleep(.25)
        catching_state = True
        while catching_state == True:
            pos = queryMousePosition()
            print(pos)
            catch = False
            time.sleep(1)
            l, lhp, changePos = compare_battle_images(hpbox, im, changePos)
            time.sleep(.5)
            print(l, lhp)
            if lhp < 100 and l > 1000:
                print("can catch")
                catch = True
            elif lhp > 1000 and l > 15000:
                print("catching over")
                numEncounters = numEncounters + 1
                print(numEncounters)
                catching_state = False
            else:
                print("not catching")
            if catch:
                print(numEncounters)
                sendEmail(message1)
                sys.exit()

            elif not catch:
                sample_sprite=ImageGrab.grab(bbox=pokemon_ev_sprite_dems)
                # elite_sample = ImageGrab.grab(bbox=elite_box)
                firstBracket_test = ImageGrab.grab(bbox=shin_or_elite_box)
                ev_sprite_arr=[]
                for i in pokesprite:
                    ev_sprite_arr.append(mse(i,sample_sprite))
                # ev_sprite = 10
                ev_sprite=min(ev_sprite_arr)
                # elite_mse=mse(elitetok,elite_sample)
                bracket_mse=mse(firstBracket,firstBracket_test)
                print(
                    ev_sprite
                )
                if bracket_mse < 10:
                    elite_sample = ImageGrab.grab(bbox=elite_box)
                    elite_mse=mse(elitetok,elite_sample)
                    if elite_mse<10:
                        print("elite,",mse,numEncounters)
                        run_away(ev_sprite)
                    else:44
                        print(mse,numEncounters)
                        sendEmail(message3)
                        sys.exit()
                elif ev_sprite > 1000:
                    run_away(ev_sprite)
                else:
                    fight_to_kill(ev_sprite)
