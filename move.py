#%%
import pyautogui
import time
import keyboard
import requests
import random

#%%
#get a random number between 1 and 4
def getRandom():
    return random.randint(1,4)

# %%
def move1():
    keyboard.press("w")
    time.sleep(1)
    keyboard.release("w")

def move2():
    keyboard.press("s")
    time.sleep(1)
    keyboard.release("s")

def move3():
    keyboard.press("a")
    time.sleep(1)
    keyboard.release("a")

def move4():
    keyboard.press("d")
    time.sleep(1)
    keyboard.release("d")


#%%

id = "09980bb88cd94609b175cfc9f447b45c"
key = "65e824e4-6703-4c0e-8092-648c6411c267"
profileID = "8d1aed97cc02422d9b9baa52632c0911"
#Get players' profile response
def getPlayerData(UUID, SBUUID):
    data = requests.get("https://api.hypixel.net/skyblock/profile?key="+ key +"&uuid="+ UUID +"&profile=" + SBUUID).json()
    return data

#Get players' collections
def getCollection(playerID, profileID):
    data = getPlayerData(playerID, profileID)
    collectionData = data['profile']['members'][playerID]['collection']
    return collectionData

#%%
def a():
    cont = 0
    while True:

        num = getRandom()
        print("random num: " + str(num))
        if num == 1:
            move1()
        elif num == 2:
            move2()
        elif num == 3:
            move3()
        elif num == 4:
            move4()
        if cont % 30 == 0:
            cont = 0
            print("last saved: " + str(getPlayerData(id, profileID)["profile"]["members"][id]["last_save"]))
            print("current leve: " + str(getCollection(id, profileID)["RABBIT"]))

        cont += 1
        print("cont: " + str(cont))
#%%
getCollection(id, profileID)
#%%


def clickEveryRandomTime():
    cont = 0
    while True:
        time.sleep(random.randint(0,4))
        if cont % 10 == 0:
            print("last saved: " + str(getPlayerData(id, profileID)["profile"]["members"][id]["last_save"]))
            print("current leve: " + str(getCollection(id, profileID)["RABBIT"]))
            cont = 0
        cont += 1
        pyautogui.click()

#%%
def check():
    # listen when C is pressed
    while True:
        if keyboard.is_pressed('c'):
            keyboard.press_and_release("9")
            # right click
            pyautogui.rightClick()
            # move mouse to (890, 350)
            pyautogui.moveTo(850, 390)
            pyautogui.leftClick()
            pyautogui.leftClick()
            # move mouse to (1120, 390)
            pyautogui.moveTo(1150, 390)
            time.sleep(2)
            keyboard.press_and_release("esc")
            keyboard.press_and_release("1")
            
check()