# -*- coding: utf-8 -*-
"""
@author: Christian
"""

import pandas as pd
import matplotlib.pylab as plt
from sklearn.cluster import KMeans
from sklearn import metrics
import numpy as np


ecoAbr=pd.read_csv(r'C:\Users\Christian\Desktop\Examen\2017-04.csv',usecols=[3,4,5,6,7,8])
ecoMay=pd.read_csv(r'C:\Users\Christian\Desktop\Examen\2017-05.csv',usecols=[3,4,5,6,7,8])
ecoJun=pd.read_csv(r'C:\Users\Christian\Desktop\Examen\2017-06.csv',usecols=[3,4,5,6,7,8])


data=pd.concat([ecoAbr,ecoMay,ecoJun])

"""Se cuentan el numero de veces que aparece cada estacion"""
cRetiro=data['Ciclo_Estacion_Retiro'].value_counts().sort_index()
cArribo=data['Ciclo_Estacion_Arribo'].value_counts().sort_index()

n=cRetiro.index.tolist()

plt.subplot(2,2,1)

cRetiro=cRetiro.tolist()
cArribo=cArribo.tolist()

""" Se forma una matriz con la cRetiro y cArribo"""
X=np.column_stack((np.transpose(cRetiro),np.transpose(cArribo)))


"""Secomienza a plottear """
plt.title('Scatter plot')
#plt.xlabel('#times a station was a source of departure')
#plt.ylabel('#times a station was an arrival source ')
plt.scatter(cRetiro,cArribo)

#for i, txt in enumerate(n):
#    plt.annotate(txt, (cRetiro[i],cArribo[i]))

colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'b']
markers = ['o', 's', 'D', 'v', '^', 'p', '*', '+']

tests = [2, 3, 4]
subplot_counter = 1


""" Se grafican los  diferentes clusters"""
for t in tests:
    subplot_counter += 1
    plt.subplot(2, 2, subplot_counter)
    """Se hacen los clusters de acuerdo a t"""
    kmeans_model = KMeans(n_clusters=t).fit(X)
    for i, l in enumerate(kmeans_model.labels_):
        plt.plot(cRetiro[i], cArribo[i], color=colors[l], marker=markers[l],ls='None')
        #plt.xlabel('#times a station was a source of departure')
        #plt.ylabel('#times a station was an arrival source')
        
        """Se obtiene el coeficiente de silhoutte"""
        plt.title('K = %s, Silhouette coefficient = %.03f' % (t, metrics.silhouette_score(X, kmeans_model.labels_,metric='euclidean')))

plt.tight_layout()
plt.suptitle('K-means Clustering')
plt.text(1, 0, 'x axis=#times a station was a source of departure\ny axis=#times a station was an arrival source',
        verticalalignment='bottom',
         fontsize=10)

plt.show()    
