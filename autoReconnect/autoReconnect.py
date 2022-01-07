import requests
import time
import psutil
import pyautogui
import os
import win32gui
import re
import random

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


def log(text):
    with open("autoReconnect/log.txt", "a") as f:
        f.write(text + "\n")


def getCurrentArea():
    link = "https://sky.lea.moe/stats/Paradis120202/Watermelon"
    res = requests.get(link)
    data = res.content.decode("utf-8")
    data = data.split(
        """<div class="additional-stat"><span class="stat-name">Current Area: </span><span class="stat-value">""")
    try:
        currentArea = data[1].split("</span>")[0]
    except IndexError:
        log("GCA: something went wrong, waiting 120 seconds and attempting again")
        time.sleep(120)
        res2 = requests.get(link)
        data2 = res2.content.decode("utf-8")
        data2 = data2.split(
            """<div class="additional-stat"><span class="stat-name">Current Area: </span><span class="stat-value">""")
        try:
            currentArea = data2[1].split("</span>")[0]
            log("GCA: current area is " + currentArea)
        except IndexError:
            log("GCA: second attempt failed, assuming area is not island")
            currentArea = "None"

    return currentArea


def internetIsUp():
    try:
        requests.get("https://www.google.com")
        return True
    except:
        return False


def isOnline(key="65e824e4-6703-4c0e-8092-648c6411c267", UUID="09980bb88cd94609b175cfc9f447b45c"):
    data = requests.get(
        "https://api.hypixel.net/player?key=" + key + "&uuid=" + UUID).json()
    return data["player"]["lastLogin"] > data["player"]["lastLogout"]


def checkIfGameIsOpen():
    return "javaw.exe" in (i.name() for i in psutil.process_iter())


def closeGameAndLauncher():
    log("CGAL: closing game")
    os.system("TASKKILL /F /IM javaw.exe")
    time.sleep(2)
    log("CGAL: closing launcher")
    os.system("TASKKILL /F /IM Minecraft.exe")
    time.sleep(2)


def openGameAndEnterServer():
    log("OGAES: opening game")
    try:
        os.startfile("C:/Users/Lucas/Desktop/mc/MC_oficial")
    except:
        log("OGAES: error opening game")
        return
    time.sleep(15)
    # check for connection, if not, reconnect
    location = pyautogui.locateOnScreen('autoReconnect/playButt.png')
    if location is None:
        log("OGAES: game not found, stopping")
        return
    pyautogui.click(location)
    time.sleep(15)
    location = pyautogui.locateOnScreen('autoReconnect/multiplayerButt.png')
    log("OGAES: clicking multiplayer")
    if location is None:
        log("OGAES: multiplayer not found, stopping")
        return
    pyautogui.click(location)
    time.sleep(5)
    location = pyautogui.locateOnScreen('autoReconnect/HPlogo.png')
    log("OGAES: clicking HPlogo")
    if location is None:
        log("OGAES: HPlogo not found, stopping")
        return
    pyautogui.click(location)
    pyautogui.click(location)
    time.sleep(5)

    # press t and type /skyblock and press enter, wait 2 seconds and press w for 1 second
    pyautogui.press('t')
    pyautogui.typewrite('/skyblock', interval=0.25)
    # check if location is lobby, hub or island
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.keyDown('w')
    time.sleep(1)
    pyautogui.keyUp('w')
    pyautogui.press('t')
    log("OGAES: movement done, assuming everything is ok, checking area")
    if getCurrentArea() == "Hub":
        log("OGAES: in hub, going to island")
        goFromHubToIs()


def goFromHubToIs():
    # press t, type /is and press enter, wait 2 seconds and press w for 1 second
    pyautogui.typewrite('/is', interval=0.25)
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.keyDown('w')
    time.sleep(1)
    pyautogui.keyUp('w')
    pyautogui.press('t')


cicle = 0
wait = True
while True:
    try:
        # pick a random number between 13 and 24
        num = random.randint(13, 24)
        if cicle > 0 and wait is True:
            time.sleep(num * 60)
            # log current time
            log("\n" + str(time.ctime()))
            log(str(num) + " minutes passed checking. starting cicle id " + str(cicle))
        if wait is False:
            log("Wait is false, starting cicle id " + str(cicle))
            wait = True
        cicle += 1

        area = getCurrentArea()
        log("Current area: " + area)
        if area == "Private Island":
            log("Current area is private island, continuing")
            continue
        elif area == "Hub":
            log("Going from hub to island")
            pyautogui.press('t')
            goFromHubToIs()
            # and check if now its fine
            if getCurrentArea() == "Private Island":
                # log this
                log("Now in island")
                continue
            else:
                # log this
                log("Something went wrong, restarting")
                closeGameAndLauncher()
                openGameAndEnterServer()
                continue
        elif area == "None":
            log("No area found, restarting")
            closeGameAndLauncher()
            openGameAndEnterServer()
            # continue
        # at this point i know im not in the hub or island
        if not isOnline():
            log("Not online, checking internet and starting game")
            if not internetIsUp():
                # log this
                log("Internet is down, waiting for next cicle")
                continue
            if checkIfGameIsOpen():
                log("Game is open, closing it")
                closeGameAndLauncher()
            openGameAndEnterServer()
        # at this point i know i am online, and that internet is up
        # so i close the game and try to log back in
        if not checkIfGameIsOpen():
            # game cant open, retry
            log("Game is closed, restarting")
            openGameAndEnterServer()
        if getCurrentArea() == "Private Island":
            # log everthing works fine
            log("Final cicle passed")
            continue
    except Exception as e:
        log("Unexpected error: " + str(e) + " last cicle ran: " + str(cicle))
        wait = False
