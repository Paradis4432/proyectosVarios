import requests
import time

link = "https://sky.lea.moe/stats/Paradis120202/Watermelon"
while True:
    res = requests.get(link)
    data = res.content.decode("utf-8")
    data = data.split("""<div class="additional-stat"><span class="stat-name">Current Area: </span><span class="stat-value">""")
    try:
        currentArea = data[1].split("</span>")[0]
    except IndexError:
        currentArea = "None"
    if currentArea != "Private Island": 
        print("something went wrong")
        print(currentArea)
    time.sleep(60)