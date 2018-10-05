import requests as rq
import json
from random import randint
import numpy as np

INT_MAX = 29  # Global


promo_name = ['UNIFI', 'UNIFIPRO', 'TURBO', 'STUDENT', 'BIZ', 'UNIFILITE',
              'TESTUNIFI', 'TMRND', 'ACE', 'SMARTHELMAT', 'target',
              'Promotion', 'PromoTest', 'PromoTest2', 'promo2']

for each in promo_name:
    starting_point = randint(0, INT_MAX)  # Get the starting number
    array_num = ['0'] * INT_MAX  # Create list of value '0' of len 29

    # Make changes on required position
    if starting_point not in [29, 28, 27, 26]:
        array_num[starting_point] = '1'
        array_num[starting_point+1] = '1'
        array_num[starting_point+2] = '1'
        array_num[starting_point+3] = '1'
    else:
        starting_point = 28
        array_num[starting_point] = '1'
        array_num[starting_point-1] = '1'
        array_num[starting_point-2] = '1'
        array_num[starting_point-3] = '1'

    # print(array_num[0])
    payload = {'title': each,
               'company': 'TSSSB',
               'recipient': [{
                   'female': array_num[0],
                   'male':array_num[1],
                   'age18':array_num[2],
                   'age1821':array_num[3],
                   "age21":array_num[4],
                   "streamyx_1":array_num[5],
                   "streamyx_2":array_num[6],
                   "streamyx_4":array_num[7],
                   "streamyx_8":array_num[8],
                   "streamyx_soho":array_num[9],
                   "unifiadvance":array_num[10],
                   "unifibiz":array_num[11],
                   "unifilite":array_num[12],
                   "johor":array_num[13],
                   "kedah":array_num[14],
                   "kelantan":array_num[15],
                   "pahang":array_num[16],
                   "perak":array_num[17],
                   "perlis":array_num[18],
                   "pulau_pinang":array_num[19],
                   "sabah":array_num[20],
                   "sarawak":array_num[21],
                   "melaka":array_num[22],
                   "negeri_sembilan":array_num[23],
                   "terengganu":array_num[24],
                   "wilayah_persekutuan":array_num[25],
                   "wilayah_persekutuan_putrajaya":array_num[26],
                   "wilayah_persekutuan_labuan":array_num[27],
                   "selangor":array_num[28]
               }]}

    # print(type(json.dumps(payload)))
    header = {'Authorization': 'jh5tvufrppbeov6j8d8objq3jp', 'Content-Type': 'application/json'}
    # print(json.dumps(payload))

    r = rq.post('http://188.166.237.89:8880/ace/api/target/email',
                headers=header, data=json.dumps(payload))
    print(r.text, r.status_code)
