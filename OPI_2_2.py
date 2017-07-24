# -*- coding: utf-8 -*-
"""
@author: Christian
"""

import pandas as pd
import matplotlib.pylab as plt
from pandas import Series


ecoAbr=pd.read_csv(r'C:\Users\Christian\Desktop\Examen\2017-04.csv',usecols=[3,4,6])
ecoMay=pd.read_csv(r'C:\Users\Christian\Desktop\Examen\2017-05.csv',usecols=[3,4,6])
ecoJun=pd.read_csv(r'C:\Users\Christian\Desktop\Examen\2017-06.csv',usecols=[3,4,6])


data=pd.concat([ecoAbr,ecoMay,ecoJun])
indx=data.Fecha_Retiro.unique()
Stn=sorted(data.Ciclo_Estacion_Retiro.unique())


"""Se saca la serie de tiempo de cada estacion"""
fq={}
for j in Stn:
    x=[]
    for i in indx:
        x.append(data.loc[(data.Fecha_Retiro==i)&(data.Ciclo_Estacion_Retiro==j)].Ciclo_Estacion_Retiro.count())
    fq[j]=x

"""Se compara cada dia con el de la semana anterior para cada estacion"""
deltafq={}
for j in fq:
    x=len(fq[j])
    aux=[]
    while (x!=0):
        aux.append((fq[j][x-1]-fq[j][x-8])/float(fq[j][x-8]))
        x=-1
    deltafq[j]=aux


"""Se grafican las series de tiempo"""
for c in deltafq:
    tSerie=Series(deltafq[c],index=indx[4:])
    tSerie.plot()
    
plt.xlabel('Hour')
plt.ylabel('% Change respect to last week')
plt.title('Time Series')