# -*- coding: utf-8 -*-
"""
@author: Christian
"""

import pandas as pd
import numpy as np
#import seaborn as sns
#import matplotlib.pylab as plt


ecoAbr=pd.read_csv(r'C:\Users\Christian\Desktop\Examen\2017-04.csv',usecols=[3,4,6])
ecoMay=pd.read_csv(r'C:\Users\Christian\Desktop\Examen\2017-05.csv',usecols=[3,4,6])
ecoJun=pd.read_csv(r'C:\Users\Christian\Desktop\Examen\2017-06.csv',usecols=[3,4,6])


data=pd.concat([ecoAbr,ecoMay,ecoJun])
"""Se obtienen los datos unicos de dias y estaciones"""
indx=data.Fecha_Retiro.unique()
Stn=sorted(data.Ciclo_Estacion_Retiro.unique())


data2=data[['Fecha_Retiro','Ciclo_Estacion_Retiro','Ciclo_Estacion_Arribo']]
Matrix=np.zeros((451,451))

"""Se obtiene la matriz de origen destino"""

for day in indx:
    data2.loc[data.Fecha_Retiro==day]
    j=data2.groupby(['Ciclo_Estacion_Retiro','Ciclo_Estacion_Arribo']).size().unstack().fillna(0)
    Matrix=Matrix+np.matrix(j.as_matrix())

Matrix/=len(indx)

"""Se transforma a un data frame a la matriz de OD"""
hM=pd.DataFrame(Matrix,index=Stn,columns=Stn)

"""Se pretendio graficar el heat map pero se traba mi computadora"""

#plt.xlabel('Ciclo_Estacion_Retiro')
#plt.ylabel('Ciclo_Estacion_Arribo')
#plt.title('Head Map')
#sns.heatmap(hM,annot=True,linewidths=0.25,square=True,cmap='Blues_r')