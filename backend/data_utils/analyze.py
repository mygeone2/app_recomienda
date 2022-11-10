 # -*- coding: utf-8 -*-
import json

from itertools import count
from tkinter import E
import pandas as pd
from pathlib import Path
import json

folder = Path('E:/data_recomienda/Data_Colegios_API/')

'''

'''
orientacionMap = {
    # del menos religoso al menos religioso
    'sin orientación religiosa':0,

    'Laica': 1,
    'Laico': 1, 
    'LAICO': 1,
    'laico': 1,
    'laica':1,

    'Valórica': 2,
    'Católica y Evangélica': 2, 
    'FORMACION VALORICA': 2,
    'valorica':2,
    'Valorica y social':2,
    'Valorico':2,
    'Centrado en lo valórico':2,

    'humanista': 3, 

    'CRISTIANO': 4,
    'cristiana':4,
    'CRISTIANA': 4,
    'Cristiana': 4,
    'LUTERANA (CRISTIANA)': 4,
    'Cristiana Reformada': 4, 
    'ORIENTACION CRISTIANA': 4, 
    'Ecuménica': 4, 
    'Creencia en Dios':4, 

    'Católica': 5,
    'de inspiración católica': 5,
    'catolico y evangelico':5,
    'Orientacion Cristiana':5,
    'Orientacion cristiana':5,
    'Orientación cristiana':5,
    'Católica y Evangélica.':5,
    'cristiana-valórica':5,
    'CRISTIANO VALORICO':5,

    'Evangélica': 7, 

    "ECUMÉNICO": 6,

    'Adventista del 7° Día': 8, 
    'Adventista': 8,
    'ADVENTISTA': 8,
    'Adventista del Séptimo Día': 8,
    'Adventista del septimo día': 8, 
    'ADVENTISTA DEL 7º DIA': 8, 
    'Confesional - Adventista': 8,
    'adventistas.':8,

    "Metodista": 9,

    'cosmovisión mapuche': 10, 
    'Bahai': 20,
}

orientacionMap2 = {
  'sin orientación religiosa': 0,
  'Laica': 1,
  'Laico': 1,
  'LAICO': 1,
  'laico': 1,
  'laica': 1,
  'Valórica': 2,
  'Católica y Evangélica': 2,
  'FORMACION VALORICA': 2,
  'valorica': 2,
  'Valorica y social': 2,
  'Valorico': 2,
  'Centrado en lo valórico': 2,
  'humanista': 3,
  'CRISTIANO': 4,
  'cristiana': 4,
  'CRISTIANA': 4,
  'Cristiana': 4,
  'LUTERANA (CRISTIANA)': 4,
  'Cristiana Reformada': 4,
  'ORIENTACION CRISTIANA': 4,
  'Ecuménica': 4,
  'Creencia en Dios': 4,
  'Católica': 5,
  'de inspiración católica': 5,
  'catolico y evangelico': 5,
  'Orientacion Cristiana': 5,
  'Orientacion cristiana': 5,
  'Orientación cristiana': 5,
  'Católica y Evangélica.': 5,
  'cristiana-valórica': 5,
  'CRISTIANO VALORICO': 5,
  'Evangélica': 7,
  'Adventista del 7° Día': 8,
  'Adventista': 8,
  'ADVENTISTA': 8,
  'Adventista del Séptimo Día': 8,
  'Adventista del septimo día': 8,
  'ADVENTISTA DEL 7º DIA': 8,
  'Confesional - Adventista': 8,
  'adventistas.': 8,
  'cosmovisión mapuche': 10,
  'Bahai': 20,



  'Humanista Cristiana': 4,
  'cristiana basada en lo valórico': 5952,
  'orientacion cristiana': 4,

  'Centrada en valores Cristianos': 4,
  'se deja a elección de los padres': 0,
  'SIN RELIGION': 0,

  'ECUMENICA': 4,
  'mapuche': 10,

  'católica -evangéilica': 5,
  'LAICA': 1,
  'Cristocéntrica': 4,
  'Fe Bahá`í': 20,
  'Mapuzugun': 10,
  'sin distinción': 0,
  'Layca': 1,

  'Formación en valores': 2,
  'catolica - evangelica': 5,

  'Cristiana Evangélica': 4,
  'CATÓLICA Y EVANGÉLICA': 4,
  'evangélica y catolica': 7,
  'Adventista del 7º día': 8,
  'exención  de asignatura': 0,
  'no tiene orientación religiosa': 0,
  'Valores Cristianos': 4,
  'ecumenica': 4,

  'Adventista del 7° dia': 8,

  'ADVENTISTA-CRISTIANA': 8,

  'cristiano-valorico': 4,
  'LAICO ECUMÉNICO': 1,
  'Humanista cristiana': 4,
  'Católica con Espiritualidad Franciscana': 4,
  'Cristiana ': 4,
  'Cristiano': 4,
  'UNIVERSAL': 0,
  'CULTURA RELIGIOSA GENERAL O UNIVERSAL': 0,
  'Humanista': 3,
  'catolica, evamgelica': 5,
  'ADVENTISTA DEL 7° DIA': 8,
  'Valórica Cristiana': 2,
  'Valórica - Cristiana': 2,
  'orientación Valórica': 2,
  'SE RESPETAN TODAS LAS RELIGIONES': 0,
  'Evangelica Luterana': 7,
  'Metodista': 9,
  'Laico Católico': 1,
  'Cristocentrica': 4,
  'Formación en Valores': 2,
  'CRISTIANA NO CONFESIONAL': 4,
  'diversidad de credos': 0,
  'Ed. Valórica': 2,
  'Formación Valórica': 2,
  'Valórica, respeto a todas las religiones y credos': 2,
  'Laica orientación católica': 0,
  'valores cristianos': 4,
  'Con orientación cristiana': 4,
  'valórica': 2,
  'ORIENTACIÓN CRISTIANA': 4,
  'todas las orientaciones religiosas': 0,
  'Educación de la Fé': 0,
  'Orientación Valórica Integral': 2,
  'ADVENTISTA DEL SEPTIMO DIA': 8,
  'Ecuménico, no confesional': 4,
  'adventista': 8,
  'valores': 2,
  'CATÓLICA - EVANGÉLICA': 5,
  'Valores cristianos': 4,
  'pluralista': 0,
  'cultural mapuche': 10,
  'creyente cristiano': 4,
  'Valorica': 2,
  'cristiana valorica': 4,
  'Humanista-Cristiana': 4,
  'Educación valórica': 2,
  'Pluralista': 0,
  'católica y evangélica': 5,
  'Mapuche': 10,
  'integral': 0,
  'VALORICA ': 2,
  'orientación cristiana': 4,
  'Católica no excluyente': 5,
  'cultural': 0,
  'ADVENTISTA DEL 7º DÍA': 8,
  'sin ejercicio': 0,
  'Laico respetuoso de la diversidad': 0,
  'Formación de valores': 2,
  'Se imparte religión evangélica y cat': 5,
  'VALORICA': 2,
  'holistica': 15,
  'Programa de Desarrollo Humano': 2,
  'ECUMÉNICO': 22749,
  'FORMACIÓN VALÓRICA': 2,
  'EVANGÉLICA LUTERANA': 6,
  'VALÓRICA': 2,
  'Laica - Valorica': 2,
  'Cristiana Universal': 4,
  'Laico con Orientación Cristiano Católica': 1,
  'VALORES CRISTIANO': 4,
  'Cristiana- Valórica': 4,
  'Laico Humanista': 1,
  'Laica - Valórica': 1,
  'eucomenica': 6,
  'PRINCIPIOS Y VALORES CRISTIANOS': 4,
  'No Confesional': 0,
  'Todas': 0,
  'cristiano': 4,
  'Diversidad': 0,
  'Politeísta': 12
}

regimenMap = {
    'Mixto': 1, 'Mujeres': 2, 'Hombres': 3
}

actividadesMap = ['ACTIVIDADES EXTRAPROGRAMÁTICAS','APOYO ACADÉMICO', 'DEPORTES', 'IDIOMA', 'INFRAESTRUCTURA', 'PROGRAMAS']

indicadoresDesempenio = {
    'Insuficiente': 1,
    'Medio': 2,
    'Medio bajo': 3, 
    'Alto': 4, 
    'Sin categoría': 0, 
    'SIN CATEGORIA': 0,
    None: 0
}

especialidadMap = {'Atención de Párvulos': 1, 'Construcciones Metálicas': 2, 'Electricidad': 3, 'Electrónica': 4, 'Gastronomía': 5, 'Mecánica Automotriz': 6, 'Mecánica Industrial': 7, 'Administración': 8, 'Programación': 9, 'Servicios de Turismo': 10, 'Agropecuaria': 11, 'Operaciones Portuarias': 12, 'Contabilidad': 13, 'Atención de Enfermería': 14, 'Servicios de Hotelería': 15, 'Asistencia en Geología': 16, 'Metalurgia Extractiva': 17, 'Telecomunicaciones': 18, 'Química Industrial': 19, 'Explotación Minera': 20, 'Construcción': 21, 'Montaje Industrial': 22, 'Gráfica': 23, 'Acuicultura': 24, 'Elaboración Industrial de Alimentos': 25, 'Conectividad y Redes': 26, 'Dibujo Técnico': 27, 'Refrigeración y Climatización': 28, 'Instalaciones Sanitarias': 29, 'Vestuario y Confección Textil': 30, 'Muebles y Terminaciones de la Madera': 31, 'Tripulación de Naves Mercantes y Especiales': 32, 'Forestal': 33, 'Mecánica de Mantenimiento de Aeronaves': 34}

especialidadMap2 = {'Atención de Párvulos': 1, 'Construcciones Metálicas': 2, 'Electricidad': 3, 'Electrónica': 4, 'Gastronomía': 5, 'Mecánica Automotriz': 6, 'Mecánica Industrial': 7, 'Administración': 8, 'Programación': 9, 'Servicios de Turismo': 10, 'Agropecuaria': 11, 'Operaciones Portuarias': 12, 'Contabilidad': 13, 'Atención de Enfermería': 14, 'Servicios de Hotelería': 15, 'Asistencia en Geología': 16, 'Metalurgia Extractiva': 17, 'Telecomunicaciones': 18, 'Química Industrial': 19, 'Explotación Minera': 20, 'Construcción': 21, 'Montaje Industrial': 22, 'Gráfica': 23, 'Acuicultura': 24, 'Elaboración Industrial de Alimentos': 25, 'Conectividad y Redes': 26, 'Dibujo Técnico': 27, 'Refrigeración y Climatización': 28, 'Instalaciones Sanitarias': 29, 'Vestuario y Confección Textil': 30, 'Muebles y Terminaciones de la Madera': 31, 'Tripulación de Naves Mercantes y Especiales': 32, 'Forestal': 33, 'Mecánica de Mantenimiento de Aeronaves': 34}

def getCountActividades(data):
    temp = list()
    for actividad in actividadesMap:
        counter = 0
        for item in data['actividades']:
            if item['tipo'] == actividad:
                counter = counter + 1
        temp.append(str(counter))
    return ','.join(temp)

def extractEspecialidad(i,data):
    list = []
    try:
        for item in data['especialidades']:
            return (especialidadMap[item])
            #list.append(str(especialidadMap[item]))
        return ','.join(list)
    except Exception as e:
        pass
    
def getReligionState(i,data):

    if(orientacionMap2[data['informacionInstitucional']['orientacionReligiosa']] != None):
        return str(orientacionMap2[data['informacionInstitucional']['orientacionReligiosa']])
    else:
        return str(data['informacionInstitucional']['orientacionReligiosa'])

def initSummaryFile():
    with open('summary.csv', 'a') as f:
        f.write('id_colegio,id_sede,id_comuna,codigo_nivel,vacantes,internado,uniforme,religion,matriculados,alumnos_promedio_por_curso,regimen,latitud,longitud,act_extra,apoyo_academico,deportes,idioma,infraestructura,programas\n')

def writeSummary(summary):
    #write content of summary to end of file and keep old content
    with open('summary.csv', 'a') as f:
        f.write(summary)


def extractSedes(sede):
    #codigoSede, codigoRegion, 
    temp = ""
    
    try:
        temp += str(sede['codigoSede'])+','+str(sede['direccion']['codigoRegion'])+','+str(sede['direccion']['codigoComuna'])
        
        if(nivel['codigoEnsenanza'] == 510):
            nivel = nivel['codigoEnsenanza'] + 10
        temp += nivel['codigoNivel'] + ',' + str(nivel)
        return str(temp)

    except Exception as e:
       pass
        
def getIdSchool(data):
    return str(data['rbd'])

def getInternadoState(data):
    return str(1 if data['informacionInstitucional']['internado'] == True else 0)

def getUniformState(data):
    return str(1 if data['informacionInstitucional']['politicaUniforme'] == "Uniforme propio" else 0)

def getMatriculados(data):
    return str(data['informacionInstitucional']['alumnosMatriculados'])

def getAlumnosPromediosPorCurso(data):
    return str(data['informacionInstitucional']['promedioAlumnosPorCurso'])

def getRegimen(data):
    return str(regimenMap[data['informacionInstitucional']['regimen']])

def getLocation(data):
    return str(data['coordenadas']['coordinates'][0])+','+str(data['coordenadas']['coordinates'][1])

def getCodigoNivel(data):
    if (data['codigoEnsenanza'] == 510):
        return str(data['codigoNivel'] + 10)
    else:
        return str(data['codigoNivel'])

def getIdSede(data):
   return str(data['codigoSede'])

def getVacantes(data):
    return str(data['cantidadPreVacantesInferior'])

def getIdComuna(data):
    return str(data['direccion']['codigoComuna'])


count = 0
initSummaryFile()
for i in range(1, 42000):
   
    file = folder / f'{i}.json'
    try:

        file = open(file, encoding="utf8")
        data = json.load(file)
        
    except:
        pass
          
    else:
        for sede in data['sedes']:
            for nivel in data['sedes'][0]['niveles']:
                summary = ''

                idColegio = getIdSchool(data)
                idSede = getIdSede(sede)
                idComuna = getIdComuna(sede)
                codigoNivel = getCodigoNivel(nivel)
                vacantes = getVacantes(nivel)
                internado = getInternadoState(data)
                uniforme = getUniformState(data)
                religion = getReligionState(i,data)
                matriculados = getMatriculados(data)
                alumnosPromediosPorCurso = getAlumnosPromediosPorCurso(data)
                regimen = getRegimen(data)
                location = getLocation(sede['direccion'])
                actividades = getCountActividades(data)

                summary = (idColegio+','+idSede+','+idComuna+','+codigoNivel+','+vacantes+','+internado+','+uniforme+','+religion+','+matriculados+','+alumnosPromediosPorCurso+','+regimen+','+location+','+actividades+'\n')
                #print(summary)
                writeSummary(summary)
#