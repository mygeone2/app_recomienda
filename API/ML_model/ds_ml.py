# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np

from sklearn.neighbors import NearestNeighbors
import functools
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix



def shape_into_KNN_shape(data,x,y,z):
  data_shaped = data[['alumnos_promedio_por_curso','deportes','infraestructura']]
  data_shaped = data_shaped.to_numpy()
  return data_shaped

def get_neighbors(id_colegio, id_level, comuna):
 
  df = pd.read_csv('/code/ML_model/summary.csv',delimiter=',',low_memory=False)
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
  
  schools = {}
  for d,i in zip(distances[0],indexes[0]):
    if d != 0:
      if (df.iloc[i]['id_colegio'] not in res.keys()):
        similarity = df.iloc[i].eq(school_requested.values).mean()
        schools[(df.iloc[i]['id_colegio'])] = similarity.round(2)
  res['schools'] = schools
  return (res)

