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
  #filter by comuna
  df = df[df['id_comuna'] == str(comuna)]
  df = df[df['codigo_nivel'] == str(id_level)]

  #access the row that has the id_colegio as id_colegio and str(id_level) as codigo_nivel
  df_filtered = df[df['id_colegio'] == str(id_colegio)]

  #find why the df_filtered is returning more than one row
  print(df_filtered)
	
  x = int(df_filtered['alumnos_promedio_por_curso'])
  y = int(df_filtered['deportes'])
  z = int(df_filtered['infraestructura'])

  point_of_school_to_compare = (x,y,z)

  data_shaped = shape_into_KNN_shape(df,x,y,z)

  x_school_requested = df[df['id_colegio'] == id_colegio]['alumnos_promedio_por_curso']
  y_school_requested = df[df['id_colegio'] == id_colegio]['deportes']
  z_school_requested = df[df['id_colegio'] == id_colegio]['infraestructura']

  school_requested = (x_school_requested,y_school_requested,z_school_requested)

  nrst_neigh = NearestNeighbors(n_neighbors = 2, algorithm = 'ball_tree')
  a = nrst_neigh.fit(data_shaped)

  distances,indexes = nrst_neigh.kneighbors([point_of_school_to_compare], 2, return_distance=True)


  #row_school_requested = df[df['id_colegio'] == str(id_colegio) & df['codigo_nivel'] == str(id_level) & df['id_comuna'] == str(comuna)]
  #print(row_school_requested)


  #print(point_of_school_to_find_similar)
  #distances, indices = nrst_neigh.kneighbors(point_of_school_to_find_similar)


#id_colegio,internado,politica_uniforme,orientacion_religiosa,alumnos_matriculados,alumnos_prom_curso,genero,actividades_extra,apoyo_academico,deportes,idioma,infraestructura,programas
