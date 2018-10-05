import requests as rq
import json
from random import randint
import numpy as np

url = 'http://94.237.64.189:8880/ace/api/hitcount?title=&company=TSSSB'
header = { 'Content-Type':'application/json'}
r = rq.put(url,headers= header)

print(r.text, r.status_code)
