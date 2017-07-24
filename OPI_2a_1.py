# -*- coding: utf-8 -*-
"""
@author: Christian
"""
"""Importacion de los paquetes"""
import pandas as pd
import matplotlib.pylab as plt
from pandas import DataFrame


"""Se mandan a llamar a los archivos"""
ecoAbr=pd.read_csv(r'C:\Users\Christian\Desktop\Examen\2017-04.csv',usecols=[3,4,5,6,7,8])
ecoMay=pd.read_csv(r'C:\Users\Christian\Desktop\Examen\2017-05.csv',usecols=[3,4,5,6,7,8])
ecoJun=pd.read_csv(r'C:\Users\Christian\Desktop\Examen\2017-06.csv',usecols=[3,4,5,6,7,8])

"""Concatenacion de archivos"""
data=pd.concat([ecoAbr,ecoMay,ecoJun])


"""Se convierte a Fecha_Arribo como un datetime"""
data['Fecha_Arribo']=pd.to_datetime(data.Fecha_Arribo)
"""Se obtiene la hora de l a columna Hora_Arribo"""
data['Hora_Arribo'] = data['Hora_Arribo'].apply(lambda x: int(x.split(':')[0]))

week=['Monday', 'Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
modes={}
eConA={}
eConM={}

"""Se obtiene la frecuencia por dia de las estaciones"""

for day in week:
    data.loc[data.Fecha_Arribo.dt.weekday_name==day].hist(column='Hora_Arribo',bins=24)
    plt.xlabel('Hour')
    plt.ylabel('Frecuency')
    plt.title(day)
    aux=data.loc[data.Fecha_Arribo.dt.weekday_name==day]
    modes[day]=aux['Hora_Arribo'].mode()


def cDict(a):
    a=DataFrame(a).to_dict(orient='dict')
    for i in a:
        a[i]=a[i][0]
    return a
        
modes=cDict(modes)

"""Se obtiene la estacion con mayor frecuencia"""
for day in week:
    aux=data.loc[(data.Fecha_Arribo.dt.weekday_name==day) & (data.Hora_Arribo==modes[day])]
    eConA[day]=aux['Ciclo_Estacion_Arribo'].mode()
eConA=cDict(eConA)


AnHour={'Monday':8, 'Tuesday':18,'Wednesday':19,'Thursday':19,'Friday':18,'Saturday':18,'Sunday':9}

"""Se obtiene la segunda estacion con mayor frecuencia por dia"""

for day in week:
    aux=data.loc[(data.Fecha_Arribo.dt.weekday_name==day) & (data.Hora_Arribo==AnHour[day])]
    eConM[day]=aux['Ciclo_Estacion_Arribo'].mode()
eConM=cDict(eConM)



dfModes=pd.DataFrame([modes],columns=week)
dfAnHour=DataFrame([AnHour],columns=week)
dfEconA=DataFrame([eConA],columns=week)
dfEconM=DataFrame([eConM],columns=week)


Rs=pd.concat([dfModes,dfEconA,dfAnHour,dfEconM])
Rs.set_index([['Crowded time','Station','Second crowded time','Station']],inplace=True)
print(Rs.T)

