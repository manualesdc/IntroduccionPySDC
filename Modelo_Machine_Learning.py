#!/usr/bin/env python
# coding: utf-8

# # Modelo de Machine Learning
# 
# ### Prof. Manuel Sigüeñas, M.Sc.(c) 

# <a id='beginning4'></a>
# 
# 1. [Importacion](#part1d)
# 2. [Preprocesamiento](#part2d)
# 3. [Modelado](#part3d)
# 4. [Evaluacion](#part4d)

# ## Informacion del Conjunto de Datos

# La aplicación muestra la importancia del análisis de componentes principale(PCA) en el dominio bancario, más exactamente en el problema de los préstamos al consumidor. Cuando un solicitante solicita un préstamo para necesidades personales, un oficial de crédito recopila datos de él y realiza una calificación. Los factores analizados pueden ser tanto significativos como insignificantes. El análisis del componente principal puede ayudar en este caso a extraer esos factores, que producen un mejor modelo de calificación crediticia. El conjunto de datos utilizado para el análisis es proporcionado por una base de datos pública que contiene datos de crédito de un banco alemán. Los resultados enfatizan la utilidad de PCA en el sector bancario para reducir la dimensión de los datos, sin mucha pérdida de información.

# ## Informacion de los atributos

# 1. **duration**: duración del crédito (en mes).
# 2. **chist**: historial crediticio. 
# 3. **reason**: Propósito del préstamo. 
# 4. **camt**: monto del crédito (en DM).
# 5. **telephne**: cuenta de ahorro (poco, moderado, bastante rico, rico. 
# 6. **lenemp**: años de empleo. 
# 7. **instrate**: tasa de pago.
# 8. **perstat**: Estado personal 
# 9. **residlen**: Residencia.
# 10. **prpownr**: Propiedad
# 11. **age**: edad. 
# 12. **housng**: vivienda (propio, alquiler o gratis).
# 13. **numcred**: número de créditos en el banco 
# 14. **emptype**: Trabajo. 
# 15. **numliab**: Dependientes 
# 16. **customer**: Aprobación de crédito (variable objetivo)
# 

# In[1]:


import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


# <a id='part1d'></a>
# ## Importacion

# In[2]:


filesav = 'data_credit.csv'
df = pd.read_csv(filesav, 
                 sep=",",
                 encoding="ISO-8859-1")
df.head()


# In[3]:


df.info()


# ____
# * [Ir al inicio de la seccion](#beginning4)

# <a id='part2d'></a>
# ## Preprocesamiento

# Analizar la existencia de correlacion positiva o negativa entre las diferentes variables

# In[4]:


df.corr()


# La proporcion entre las dos clases

# In[5]:


df.groupby('customer').size().plot(kind='bar')


# ### Particionamiento de datos

# In[6]:


from sklearn.model_selection import train_test_split

X, y = df.iloc[:, 0:15].values, df.iloc[:, 15].values

X_train, X_test, y_train, y_test =     train_test_split(X, y, test_size=0.3, 
                     stratify=y,
                     random_state=0)


# ### Escalamiento de variables

# In[7]:


from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
X_train_std = sc.fit_transform(X_train)#entrenamiento
X_test_std = sc.transform(X_test)#testeo


# In[8]:


df_cont=pd.DataFrame(X_train_std,columns=["duration","chist","reason", "camt", "telephne",
                                         "lenemp","instrate","perstat", "residlen", "prpownr",
                                         "age","housng","numcred","emptype","numliab"])
df_cont.head()


# ____
# * [Ir al inicio de la seccion](#beginning4)

# <a id='part3d'></a>
# ## Modelado

# In[9]:


from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB


# In[10]:


rows_list_score = []

models = [[LogisticRegression(max_iter=10000),"Regresion Logistica"],
[DecisionTreeClassifier(max_depth=3),"Decision Tree"],                        
[GaussianNB(),"Naive Bayes"]]


# In[11]:


from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score


# In[12]:


import matplotlib.pyplot as plt

def grafico_importances(importances):
    plt.title('Grafico')
    # Ordene la importancia de la característica en orden descendente
    sorted_indices = np.argsort(importances)[::-1]
    #Generar el grafico
    plt.bar(range(15), importances[sorted_indices], align='center')
    plt.xticks(range(15), df_cont.columns[sorted_indices], rotation=90)
    plt.tight_layout()
    plt.show()


# In[13]:


for i in range(len(models)):
        print(models[i][1].title())#El titulo del Modelo
        models[i][0].fit(X_train_std, y_train)#Entrenamiento del modelo
        #Prediccion
        y_pred_train=models[i][0].predict(X_train_std)
        y_pred_test=models[i][0].predict(X_test_std)
        #Obtener el Accuracy
        acc_train=round(accuracy_score(y_train, y_pred_train),3)
        acc_test=round(accuracy_score(y_test, y_pred_test),3)
        #Mostrar resultados
        print("El Accuracy de Entrenamiento es: "+str(acc_train))
        print("El Accuracy de Testeo es: "+str(acc_test))
        #Para el Algoritmo Decision tree mostrar sus variables mas importantes
        if(models[i][1].title()=="Decision Tree"):
            print("Variables mas importantes")
            list_importances=models[i][0].feature_importances_
            #LLamar a la funcion para que gener el grafico
            grafico_importances(list_importances)
        
        #Guardar los score
        rows_list_score.append([models[i][1],acc_train,acc_test])
        print("----------------------------------------------")
        print("-----------------------------------------------")


# ____
# * [Ir al inicio de la seccion](#beginning4)

# <a id='part4d'></a>
# ##  Evaluacion

# In[24]:


pd.DataFrame(rows_list_score,columns=["Nombre","Acc_Train","Acc_Test"])


# Como se muestra en el Dataframe si bien el algoritmo de Decision Tree tiene un accuracy mejor que la Regresion Logistica, pero si realizamos la diferencia entre el accuracy de entrenamiento y testeo nos muestra que la Regresion logistica tiene un menor sobreajuste lo que nos daria un mejor resultado con nuevos datos ingresados al modelo.

# Tambien el Decision Tree nos da un panorama de cuales podrian ser las variables que deberiamos considerar si deseamos reducir el numero de variables
