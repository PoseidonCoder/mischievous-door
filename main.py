import requests
import time
from pywinauto import Desktop, Application

windows = Desktop(backend='uia').windows()
alternate = Application(backend='uia').start("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")

while True:
    r = requests.get('http://192.168.1.51/')
    if r.status_code == 200:
        if r.text.strip() == 'True':
            print('hide!')
            for w in windows:
                try:
                    w.minimize()
                except:
                    pass
    else:
        time.sleep(60)