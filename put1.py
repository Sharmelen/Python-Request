import requests as rq
import json
from random import randint
import numpy as np


promo_name = ['UNIFI', 'UNIFIPRO', 'TURBO', 'STUDENT', 'BIZ', 'UNIFILITE',
              'TESTUNIFI', 'TMRND', 'ACE', 'SMARTHELMAT', 'target',
              'Promotion', 'PromoTest', 'PromoTest2', 'promo2']
for each in promo_name:
    url = 'http://94.237.64.189:8880/ace/api/hitcount?title='+each+'&company=TSSSB'
    header = {'Content-Type': 'application/json'}
    r = rq.put(url, headers=header)

    print(r.text, r.status_code)
