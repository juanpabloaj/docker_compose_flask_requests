# -*- coding: utf-8 -*-
import time
import requests
from datetime import datetime

time.sleep(1)

while True:
    print(datetime.now(), ' request ...')
    r = requests.get('http://flask')
    time.sleep(1)
