#%%

import requests
import json
import time
import keyboard
import pyautogui
import random

from selenium import webdriver
# Use Webdriver Manager for Python: https://github.com/SergeyPirogov/webdriver_manager

# Import code:
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

#%%
# Use the `install()` method to set `executabe_path` in a new `Service` instance:
service = Service(executable_path=ChromeDriverManager().install())

# Pass in the `Service` instance with the `service` keyword: 
driver = webdriver.Chrome(service=service)


driver.get("https://sky.lea.moe/stats/Paradis120202/Watermelon")
# get the source code of the page
data = driver.page_source
data1 = data.split("""<div class="additional-stat"><span class="stat-name">Current Area: </span><span class="stat-value">""")
try:
    currentArea = data1[1].split("</span>")[0]
except IndexError:
    currentArea = "None"

print(currentArea)

#%%
import win32gui
import re

#list all apps
def get_windows():
    windows = []
    def enum_windows(hwnd, windows):
        if win32gui.IsWindowVisible(hwnd):
            windows.append((hwnd, win32gui.GetWindowText(hwnd)))
    win32gui.EnumWindows(enum_windows, windows)
    return windows

get_windows()

#%%
win = win32gui.FindWindow(None, "Minecraft 1.8.8")
#%%
# focus win app
win32gui.SetForegroundWindow(win)
#%%
from pywinauto import application

#%%
import pyautogui
import cv2

location = pyautogui.locateOnScreen('ARI.png', confidence=0.8)
print(location)
pyautogui.click(location)

#%%
import psutil

"javaw.exe" in (i.name() for i in psutil.process_iter())

#%%
import os

os.startfile("C:/Users/Lucas/Desktop/mc/MC_oficial")

time.sleep(15)
# check for connection, if not, reconnect
location = pyautogui.locateOnScreen('ARI2.png')
pyautogui.click(location)
time.sleep(15)
location = pyautogui.locateOnScreen('ARI3.png')
pyautogui.click(location)
time.sleep(5)
location = pyautogui.locateOnScreen('ARI4.png')
pyautogui.click(location)
pyautogui.click(location)
time.sleep(5)

# press t and type /skyblock and press enter, wait 2 seconds and press w for 1 second
pyautogui.press('t')
pyautogui.typewrite('/skyblock', interval=0.25)
#check if location is lobby, hub or island 
pyautogui.press('enter')
time.sleep(3)
pyautogui.keyDown('w')
time.sleep(1)
pyautogui.keyUp('w')
pyautogui.press('t')


#%%
os.system("TASKKILL /F /IM javaw.exe")
#%%
os.system("TASKKILL /F /IM Minecraft.exe")
