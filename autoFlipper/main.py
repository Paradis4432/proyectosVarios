#%%
id = "09980bb88cd94609b175cfc9f447b45c"
key = "65e824e4-6703-4c0e-8092-648c6411c267"
profileID = "8d1aed97cc02422d9b9baa52632c0911"

import requests
import json

data = requests.get("https://api.hypixel.net/skyblock/auctions?key=" + key).json()

data["auctions"]