#!/usr/bin/env python
# coding: utf-8

# <center><img src="https://media-exp1.licdn.com/dms/image/C4E22AQEbIXZiRVkJPQ/feedshare-shrink_2048_1536/0?e=1602115200&v=beta&t=XHE3KbzKbKy54WYDTfq7VFNUPfNjoIOrjBw6dzFPTfA" width="1000"></center>

# # Seccion Manejo Basico Python 1
# 
# ### Prof. Manuel Sigüeñas, M.Sc.(c) 

# <a id='beginning'></a>
# 
# 1. [Hola mundo](#part5) 
# 2. [Sentencias de control](#part6) 

# In[1]:


from IPython.display import Image
get_ipython().run_line_magic('matplotlib', 'inline')


# <a id='part5'></a>
# ## Hola Mundo

# Una vez instalado **Python** puede acceder al **Entorno de Desarrollo Integrado** (**IDE** según sus siglas en inglés) a través del **Jupyter** (**IDE** más popular).

# In[1]:


print("Hola Mundo") #print función para imprimir


# **Python** es un lenguaje **basado en la identificación**, no utiliza bloques de instrucciones encerrados entre llaves **({})** como los lenguajes de la familia **C**, **Java** o **JavaScript**, sino que solo se basa en la identificación a nivel de funciones, clases, etc.
# 
# La **identificación** es lo que tradicionalmente se conoce como **sangría**, separando el texto del código del margen izquierdo para darle un orden visual y lógico.

# In[3]:


import random
def Grafico_de_cluster(X,n_clusters,init,n_init,max_iter,tol,name_colors_c_list,name_colors_edgecolor_list,name_makers_list):
    km = KMeans(n_clusters=n_clusters,
                    init=init, #elija k observaciones (filas) para los centroides iniciales
                    n_init=n_init, #número de veces que el algoritmo se ejecutará
                    max_iter=max_iter,#número máximo de iteraciones para una ejecución
                    tol=tol, #tolerancia para declarar convergencia
                    random_state=0) #semilla
    y_km = km.fit_predict(X)
    for i in range(0,km.n_clusters):
        plt.scatter(X[y_km == i, 0], #primer clúster
                    X[y_km == i, 1],
                    s=50,
                    c=name_colors_c_list[i],#El color de los puntos
                    edgecolor=name_colors_edgecolor_list[i],#El punto de colors
                    marker=name_makers_list[random.randint(0,1)],#El tipo de representación
                    label='cluster '+str(i+1))
    plt.scatter(km.cluster_centers_[:, 0], km.cluster_centers_[:, 1],
                s=250, marker='*', c='red', label='centroides')
    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.show()    


# ### Sentencia import

# Cuando se desea importar un **módulo** se utiliza **import** y una vez importado se utilizan los objetos que este contienen.
# 
# En el siguiente código se importa **math** y se hace uso de su función **pow(x,y)** que devuelve el resultado de elevar el número x a la potencia y.
# 
# El módulo ofrece como ventaja la reutilización del código.

# In[ ]:


pip install pandas


# In[2]:


import pandas


# In[3]:


import math


# In[4]:


import model_evaluation_utils


# In[5]:


print(math.pow(2,3))
#x: número a elevar a la potencia
#y: indicador de potencia


# Además de módulos, **Python** también incluye otro tipo de contenedor conocido como **paquete**. Un **paquete** es un módulo de **Python** que incluye otros módulos y paquetes. Lo diferencia de un módulo es que incluye un atributo **_path_** que representa la ruta en el disco duro donde está almacenado el paquete.
# 
# En el siguiente código se importa **pandas** que es un **paquete de python** destinado al **análisis de datos**, que proporciona unas estructuras de datos flexibles y que permiten trabajar con ellos de forma muy eficiente.

# In[16]:


#!pip install pandas


# In[8]:


import pandas as pd


# El **Python Path** indica las rutas donde se buscarán los módulos, dicha ruta puede consultarse por medio de la variable **path** del módulo **sys** (sistema)
# 
# En el **Python Path** podemos indicar nuevas rutas a **Python** para que busque módulos y paquetes.

# In[6]:


import sys
sys.path


# Para conocer la lista de librerías instaladas en **Python** se utiliza la función **pip list**

# In[8]:


get_ipython().system('pip list')


# [Ir a Inicio](#beginning)
# 
# _____

# <a id='part6'></a>
# ## Sentencias de control

# Al igual que otros lenguajes de programación, Python incorpora una serie de sentencias de control. Entre ellas, encontramos algunas tan básicas y comunes a otros lenguajes como **if/else**, **while** y **for**.

# ###### if, else y elif

# La sentencia **if** funciona evaluando la condición indicada, si el resultado es True se ejecutará la siguiente sentencia o sentencias, en caso negativo se ejecutarán las sentencias que aparecen a continuación del **else**. Recordemos que Python utiliza la indentación para establecer sentencias que pertenecen al mismo bloque. Además, en el carácter dos puntos (:) indica el comienzo de bloque. A continuación, vemos un ejemplo:

# In[1]:


x = 4
y = 0


# In[2]:


if x == 4:
    y = 5
else:
    y = 2


# Obviamente, también es posible utilizar solo la sentencia **if** para comprobar si se cumple una determinada condición y actuar en consecuencia. Además, podemos anidar diferentes niveles de comprobación a través de **elif**:

# In[7]:


if x== 4:
    y = 1
elif x == 5:
    y = 2
elif x == 6:
    y = 3
else:
    y = 5


# Como el lector habrá podido observar y a diferencia de otros lenguajes de programación, los paréntesis para indicar las condiciones han sido omitidos. Para **Python** son opcionales y habitualmente no suelen ser utilizados. Por otro lado, a pesar de que Python emplea la indentación, también es posible escribir una única sentencia a continuación del final de la condición. Así pues, la siguiente línea de código es válida:

# In[10]:


a = 12
b = 9


# In[11]:


if a > b: print("a es mayor que b")


# ###### for y while

# Para iterar contamos con dos sentencias que nos ayudarán a crear bucles, nos referimos a **for** y **while**. La primera de ellas aplica una serie de sentencias sobre cada uno de los elementos que contiene el objeto sobre el que aplicamos utilizar para iterar sobre una serie de valores. Por ejemplo, echemos un vistazo al siguiente ejemplo:

# In[7]:


for x in range (1,12):
    print (x)


# Asimismo, es muy común iterar a través de **for** sobre los elementos de una tupla o de una lista:

# **código sencillo**

# In[12]:


lista = ["uno ", "dos ", "tres ", "cuatro ", "cinco"] # obj. tipo lista


# In[13]:


cad = "" #objeto string vacío


# In[18]:


lista[0]


# In[19]:


cad+=lista[0]
cad


# In[20]:


cad+=lista[1]
cad


# In[21]:


cad+=lista[2]
cad+=lista[3]
cad+=lista[4]


# In[22]:


cad


# **código optimizado mediante el bucle for**

# In[23]:


lista = ["uno ", "dos ", "tres ", "cuatro ", "cinco"]


# In[24]:


cad = ""


# In[25]:


lista


# In[26]:


for ele in lista:
    cad += ele


# In[27]:


cad


# Opcionalmente, **for** admite la sentencia **else**. Si esta aparece, todas las sentencias posteriores serán ejecutadas si no se encuentra otra sentencia que provoque la salida del bucle. Por ejemplo, en las sentencias que pertenecen al **else** al finalizar el bucle. A Continuación, veamos un ejemplo para la ilustrar este caso :

# In[28]:


for item in  (1, 2, 3):
    print(item)
else:
    print("fin")


# Otra sentencia utilizada para iterar es **while**, la cual ejecutada una serie de sentencias siempre y cuando se cumpla una determinada condición o condiciones.

# Para salir del bucle podemos utilizar diferentes técnicas. La más sencilla es cambiar la condición o condiciones iniciales para así dejar que se cumplan y detener la iteración. Otra técnica es llamar directamente a break que provocará la salida inmediata del bucle. Esta última sentencia también funciona con **for**. A continuación, veamos un ejemplo de cómo utilizar while.

# In[29]:


x = 0
y = 9


# In[47]:


while x < y:
    print(x)
    x += 1


# Al igual que **for**, **while** también admite opcionalmente **else**. Observamos el siguiente código y el resultado de su ejecución:

# In[49]:


x = -4
y = 3


# In[50]:


while x < y:
    print (x)
    x+=1
    if x == 2: 
        break
    else:
        print ("se detiene cuando x es igual a 2")


# Si en el ejemplo anterior eliminamos la sentencia **break**, comprobaremos cómo la última sentencia **print** es ejecutada.

# Además de **break**, otra sentencia a **for** y **while** es **continue**, la cual se emplea para provocar un salto inmediato a la siguiente iteración del bucle. Esto puede ser útil, por ejemplo, cuando no deseamos ejecutar una determinada sentencia y solo queremos imprimir los números pares:

# In[2]:


for i in range (1, 10):
    if i % 2 != 0:
        continue
    print (i)


# [Ir a Inicio](#beginning)
# 
# _____
