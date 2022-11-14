# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import matplotlib.patches as mpatches
import seaborn as sb
from sklearn.neighbors import NearestNeighbors
import functools
from mpl_toolkits import mplot3d
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

def convert_str_to_int(data):
#Because all data are str and we need int
  data = list(zip(x,y,z))
  new_data = []
  for i in data:
    try:
        new_data.append( (int(i[0]),int(i[1]),int(i[2]) ))
    except Exception as e:
      pass
  return new_data

def get_neighbors(id_colegio, comuna, df):
  x = df['alumnos_matriculados']
  y = df['alumnos_prom_curso']
  z = df['infraestructura']

  new_data = convert_str_to_int(df)

  nrst_neigh = NearestNeighbors(n_neighbors = 15, algorithm = 'ball_tree')
  a = nrst_neigh.fit(new_data)
  distances, indices = nrst_neigh.kneighbors(new_data)


df = pd.read_csv(r'summary.csv',delimiter=',')
#id_colegio,internado,politica_uniforme,orientacion_religiosa,alumnos_matriculados,alumnos_prom_curso,genero,actividades_extra,apoyo_academico,deportes,idioma,infraestructura,programas

get_neighbors(1,1,df)