
import json
from pathlib import Path

folder = Path('E:/data_recomienda/Data_Colegios_API/')

for i in range(1, 42000):
    file = folder / f'{i}.json'
    try:   
        with open(file, "r", encoding='utf-8') as f:
            data = json.load(f)
            #print(data)
            data['informacionInstitucional']['resumenProyecto'] = ""
            f.close()

        with open(file, 'w') as f:
            
            json.dump(data, f, indent=4)
            f.close()
        

    except Exception as e:
        print(e)

    else:
        #dataEncoded = json.dumps(data, ensure_ascii=False)
        #print(dataEncoded)
        pass

