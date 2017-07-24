# -*- coding: utf-8 -*-
"""
Created on Sun Jul 23 22:14:21 2017

@author: Christian
"""
import pandas as pd
import random
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from  sklearn.metrics import confusion_matrix



cols=['nom_loc','sexo','edad', 'escoacum', 'fecnacm', 'fecnaca','numhij']
data=pd.read_stata(r'C:\Users\Christian\Desktop\Examen\Personas_09.dta',columns=cols)

"""Se seleccionan las columnas bajo ciertos criterios"""
data=data[(data.sexo==3)&(data.fecnaca>=2008)&(data.escoacum!=99)&(data.fecnacm!=99)&(data.numhij<=25)&(data.edad<=60)]

"""Se hace una columna de variables dummy"""
data['Exitos']=((data['fecnaca']==2010)&(data['fecnacm']>=1)&(data['fecnacm']!=99))*1

"""Se parte la data con respecto a los regresores y la variable dependiente"""
X=data[['edad','escoacum']]
Y=data['Exitos']

"""Se divide en muestras de prueba y entrenamiento"""
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.25,random_state=0)


"""Se escalan los valores"""
sC=StandardScaler()
X_train=sC.fit_transform(X_train)
X_test=sC.transform(X_test)


"""Se realiza la regresion logistica"""
cF=LogisticRegression(random_state=0)
cF.fit(X_train,Y_train)

""""Se checa el modelo con los datos de testeo"""
Y_pred=cF.predict(X_test)
cM=confusion_matrix(Y_test,Y_pred)

"""Se toma solo la delegacion de Alvaro Obregon y se hace una proyeccion de los datos a 2017"""
data2=data[data.nom_loc=='Álvaro Obregón']
X2=data2[['edad','escoacum']]
Y2=data2['Exitos']

Xpn=X2['edad']+7
Xpn=Xpn.to_frame()
Xpn.reset_index()

aux=[]
for i,j in zip(X2['escoacum'].values,X2['edad'].values):
    if (j<=20 and i!=99):
        es=random.choice([0,1,2,3,4,5,6])
        aux.append(i+es)
    else:
        aux.append(i)
        
Xpn['escoacum']=aux

"""Se realiza la prediccion"""

Xpn=sC.transform(Xpn)
Y_stimation=cF.predict(Xpn)
