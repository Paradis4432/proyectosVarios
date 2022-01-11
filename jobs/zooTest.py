from twocaptcha import TwoCaptcha
from fake_headers import Headers

import httpx

print("starting")
TWOCAPTCHA_API_KEY = '33a1c886c37c666b6cbfd5e8b7cbdd19'

token = TwoCaptcha(TWOCAPTCHA_API_KEY).hcaptcha(
    sitekey='41092c54-1ee4-42eb-9bcc-a31d3a665dbd', url='https://www.zoosk.com/login/email')['code']

#print("token is:", token)
print("token set")

username = "Lucasezequiel1202021@gmail.com"
password = "kL!3#4Caf8GnuKb"
data = {
    "login": username,
    "password": password,
    'pong_light': '1',
    # 'blackbox': '',
    'hCaptcha_Token': token
}

headers = {
    'authority': 'www.zoosk.com',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
    'accept': 'application/json, text/plain, */*',
    'x-zoosk-csrf': 'zoosk-csrf-2019',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
    'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
    'origin': 'https://www.zoosk.com',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.zoosk.com/',
    'accept-language': 'en-US,en;q=0.9,fr-FR;q=0.8,fr;q=0.7',
}

proxy_login = 'system'
proxy_pass = '1234567'
prx = "gate.smartproxy.com:7000"
proxy = {'http://': f'http://{proxy_login}:{proxy_pass}@{prx}',
         'https://': f'http://{proxy_login}:{proxy_pass}@{prx}'}

headers = Headers(os='win', browser='firefox', headers=True).generate()
headers['x-zoosk-csrf'] = 'zoosk-csrf-2019'
headers['Accept-Encoding'] = 'gzip, deflate'
session = httpx.Client(proxies=proxy)

print("getting login page")
session.get('https://www.zoosk.com/')
response = session.post('https://www.zoosk.com/v4.0/login/general_v42.php?format=json&product=1&locale=en_US',
                        data=data, headers=headers, timeout=15)

print(response.json())