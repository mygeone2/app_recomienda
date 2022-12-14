import pandas as pd 
import requests
import json
import time
from pathlib import Path

folder = Path('E:/Github/app_recomienda/API/ML_model/data_raw')

def getProcessedData(id):
    url = 'https://apisae.mineduc.cl/sae-api-vitrina/v1/establecimientos/'+str(id)
    headers = {'Content-Type': 'application/json'}
    

    try:
        print('Getting data from: '+str(id))
        v = requests.get(url, headers=headers)
        data = v.json()
    except IOError:
        print("Error")

    else:
        file = folder / f'{str(id)}.json'
        with open(file, 'w') as outfile:
            json.dump(v.json(), outfile)
       
for id in range(2224,10000):
    getProcessedData(id)



