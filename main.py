#This script locates the image stickman.png in the region we give it and tell you if it can see it
from pyautogui import * 
import pyautogui as pt
import time 
import random
from pynput.keyboard import Key, Controller

write = '1'
k = Controller()
sleep(5)
while 1:

    if pt.locateOnScreen('icon.png',region=(817,450,100,100), grayscale=True, confidence=0.4) != None:
        position = pt.locateOnScreen('icon.png', grayscale=True, confidence=0.9)
        print("I can see it")
        x = position[0]
        y = position[1]
        pt.moveTo(x-30, y+5)
        write = '1'
        
        if write == '1':
            pt.click()
            k.type('#WeStandWithPalestine')
            k.press(Key.enter)
            k.release(Key.enter)
            write = '0'
            pt.scroll(-500)
    
    else:
        print("I am unable to see it")
        pt.scroll(-200)    	    
