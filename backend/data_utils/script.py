import pandas as pd 
import requests
import json
import time

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
        with open('Data_Colegios_API/'+str(id)+'.json', 'w') as outfile:
            json.dump(v.json(), outfile)

       

    

    

df = pd.read_csv('Directorio-oficial-EE-2022/20220914_Directorio_Oficial_EE_2022_20220430_WEB.csv', delimiter=';')

idSchools = df['RBD']

for id in idSchools:
    getProcessedData(id)



