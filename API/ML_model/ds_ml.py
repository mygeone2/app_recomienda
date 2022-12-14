# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np

from sklearn.neighbors import NearestNeighbors
import functools
import json
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix


df = pd.read_csv('/code/ML_model/summaryFinal.csv',delimiter=',',low_memory=False)
folder = Path('/code/ML_model/data_raw')

def shape_into_KNN_shape(data,x,y,z):
  data_shaped = data[['alumnos_promedio_por_curso','deportes','infraestructura']]
  data_shaped = data_shaped.to_numpy()
  return data_shaped

def get_neighbors(id_colegio, id_level, comuna):
  global df
  res = {
    'error' : 0
  }

  #filter by comuna, codigo nivel
  try:
    df = df[df['id_comuna'] == str(comuna)]
    df = df[df['codigo_nivel'] == str(id_level)]
  except IndexError:
    res['error'] = 'comuna or id_level not found'
    return res

  #access the row that has the id_colegio as id_colegio and str(id_level) as codigo_nivel
  try:
    school_requested = df[df['id_colegio'] == str(id_colegio)].iloc[0]
    print(school_requested)
  except IndexError:
      res['error'] = 'id_colegio not found'
      return res  
     
  


	
  x = int(school_requested['alumnos_promedio_por_curso'])
  y = int(school_requested['deportes'])
  z = int(school_requested['infraestructura'])
  points_of_school_to_compare = (x,y,z)
  

  data_shaped = shape_into_KNN_shape(df,x,y,z)
  nrst_neigh = NearestNeighbors(n_neighbors = 2, algorithm = 'ball_tree')
  a = nrst_neigh.fit(data_shaped)
  distances,indexes = a.kneighbors([points_of_school_to_compare], 10, return_distance=True)
  

  return build_res_json(distances,indexes,df,school_requested)
  

def build_res_json(distances,indexes,df,school_requested):
  res = {
    'error' : 0
  }


  schools = []
  for d,i in zip(distances[0],indexes[0]):
    if d != 0:
        rbd = df.iloc[i]['id_colegio']

        file = folder / f'{ rbd }.json'
        file = open(file, encoding="utf8")
        data = json.load(file)
      
        if data not in schools:
          schools.append({
            'rbd' : data['rbd'],
            'name' : data['nombre'],
            'street' : data['sedes'][0]['direccion']['calle'],
            'similarity': school_requested.eq(df.iloc[i].values).mean().round(2)

          })
        
  res['schools'] = schools
  return res

        