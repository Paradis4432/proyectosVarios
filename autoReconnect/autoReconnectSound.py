import requests
import time
import winsound, time

link = "https://sky.lea.moe/stats/Paradis120202/Watermelon"

def constantCheckWithSound():

    def checkArea():
        res = requests.get(link)
        data = res.content.decode("utf-8")
        data = data.split("""<div class="additional-stat"><span class="stat-name">Current Area: </span><span class="stat-value">""")
        try:
            currentArea = data[1].split("</span>")[0]
        except IndexError:
            currentArea = "None"
        return currentArea

    while True:
        time.sleep(120)
        currentArea = checkArea()
        if currentArea != "Private Island":
            time.sleep(120)
            currentArea = checkArea()
            if currentArea != "Private Island":
                duration = 300
                freq = 440
                while True:
                    winsound.Beep(freq, duration)
                    currentArea = checkArea()
                    if currentArea == "Private Island":
                        break
                    time.sleep(5)
                    


constantCheckWithSound()