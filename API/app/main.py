from typing import Union
from fastapi import FastAPI, Response, status
import psycopg2
import pandas as pd
import numpy as np
from sklearn.neighbors import NearestNeighbors
import functools
import sys
import json
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:80",
]


# import a function from another file 
from ML_model.ds_ml import get_neighbors


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

conn = psycopg2.connect(
    host="172.20.1.2",
    database="postgres",
    user="postgres",
    password="postgres",
    port="5432"
)

cursor = conn.cursor()


@app.get("/getProbability/{id_school}/{id_level}", status_code=200)
def getProbability(id_school: int, id_level: int, response: Response) -> Union[dict, str]:
    query = ""
    prob = 0

    for year in (2021,2020,2019,2018):
        query += "SELECT v.rbd,v.cod_nivel,v.vacantes_regular,'{year}' as ano,v.cod_espe, ( SELECT count (*) as postulaciones  FROM c1_{year} WHERE rbd = '{id_colegio}'AND cod_nivel = '{id_curso}' ) FROM A1_{year} v WHERE rbd = '{id_colegio}' AND cod_nivel = '{id_curso}' ".format(year=year,id_colegio = id_school,id_curso=id_level)
        if year != 2018:
            query += ' UNION '
    cursor.execute(query)
    res = pd.DataFrame(cursor.fetchall(),columns=['rbd','cod_nivel','vacantes_regular','ano','cod_espe','postulaciones'])

    for ind in res.index:
        prob += 0 if (res['postulaciones'][ind]) >= int(res['vacantes_regular'][ind]) else 1

    try: 
        prob_prom = float(prob/len(res.index))
        return {"probability": prob_prom}
    except:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"probability": -1}


@app.get("/getSimilarSchools/{id_school}/{id_level}/{comuna}",status_code=200)
def getSimilarSchools(id_school: int, id_level: int, comuna: int,response: Response) -> Union[dict, str]:
    res = get_neighbors(id_school, id_level,comuna)
    if res['error'] != 0:
        response.status_code = status.HTTP_404_NOT_FOUND
        return res
    else:
        return res


class Student(BaseModel):
    id_school: int
    id_level: int
    siblingsInSchool: bool
    isPriority: bool
    isSonOfTeacher: bool
    isExStudent: bool

@app.post("/getProbabilitySecondStage",status_code=200)
async def getSimilarSchools(student: Student,response: Response) -> Union[dict, int]:
    # req to json
    req = student.dict()
    query = ""
    id_school = req['id_school']
    id_level = req['id_level']
    siblingsInSchool = req['siblingsInSchool']
    isPriority = req['isPriority']
    isSonOfTeacher = req['isSonOfTeacher']
    isExStudent = req['isExStudent']

    try:
        for year in (2021,2020,2019,2018):
            query += "SELECT v.rbd,v.cod_nivel,v.vacantes_regular,'{year}' as ano,v.cod_espe, ( SELECT count (*) as postulaciones  FROM c1_{year} WHERE rbd = '{id_colegio}'AND cod_nivel = '{id_curso}' ) FROM A1_{year} v WHERE rbd = '{id_colegio}' AND cod_nivel = '{id_curso}' ".format(year=year,id_colegio = id_school,id_curso=id_level)
            if year != 2018:
                query += ' UNION '
        cursor.execute(query)
        res = pd.DataFrame(cursor.fetchall(),columns=['rbd','cod_nivel','vacantes_regular','ano','cod_espe','postulaciones'])
        if(req['siblingsInSchool'] ):
            res = (1 - ( int(res.iloc[0]['postulaciones']) / int(res.iloc[0]['vacantes_regular'])))
        if( req['siblingsInSchool'] == 0):
            if(req['isPriority'] ):
                res = 0.75 - ( int(res.iloc[0]['postulaciones']) / int(res.iloc[0]['vacantes_regular']))
        if( req['siblingsInSchool'] == 0 and req['isPriority'] == 0):
            if(req['isSonOfTeacher'] ):
                res = 0.5 - ( int(res.iloc[0]['postulaciones']) / int(res.iloc[0]['vacantes_regular']))
        if( req['siblingsInSchool'] == 0 and req['isPriority'] == 0 and req['isSonOfTeacher'] == 0):
            if(req['isExStudent'] ):
                res = 0.25 - ( int(res.iloc[0]['postulaciones']) / int(res.iloc[0]['vacantes_regular']))
        if( req['siblingsInSchool'] == 0 and req['isPriority'] == 0 and req['isSonOfTeacher'] == 0 and req['isExStudent'] == 0):
            res = 0

        return res

    except:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"probability": -1}
