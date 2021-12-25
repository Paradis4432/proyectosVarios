#%%
import pyautogui as pag
import time
import keyboard

#%%
time.sleep(2)
#move mouse 100 pixels to the right
pag.mouseDown(button='left')
pag.moveRel(500, 0)
pag.moveRel(0, 500)

#%%
time.sleep(2)
#%%
def moveRight():
    pag.click(button='left')
    pag.moveRel(28, 0)

def moveDown():
    pag.click(button='left')
    pag.moveRel(0, 140)


while True:
    try:
        if keyboard.is_pressed('y'):
            moveRight()
        if keyboard.is_pressed('o'):
            moveDown()
        elif keyboard.is_pressed('t'):
            break
    except:
        break