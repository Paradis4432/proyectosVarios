#%%
import requests

u = "https://valorant-api.com/v1/weapons/skins"

r = requests.get(url = u)

data = r.json()

print(data)

#%%

import pyautogui, time

time.sleep(5)

#move the mouse 50 pixels to the right
pyautogui.moveRel(500, 0, duration=1)
