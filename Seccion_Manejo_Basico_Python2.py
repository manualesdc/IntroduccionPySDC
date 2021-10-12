#!/usr/bin/env python
# coding: utf-8

# <center><img src="https://media-exp1.licdn.com/dms/image/C4E22AQEbIXZiRVkJPQ/feedshare-shrink_2048_1536/0?e=1602115200&v=beta&t=XHE3KbzKbKy54WYDTfq7VFNUPfNjoIOrjBw6dzFPTfA" width="1000"></center>

# # Seccion Manejo Basico Python 2
# 
# ### Prof. Manuel Sigüeñas, M.Sc.(c) 

# En esta sección revisaremos cuáles son las estructuras de datos y tipos básicos con los que cuenta este lenguaje. Paso previo, revisaremos algunos conceptos importantes indispensables para la comprensión del lenguaje.

# <a id='beginning'></a>
# Las estructuras de datos nos dicen como organizar y almacenar los datos que usamos. Tales estructuras van de lo simple a lo compuesto, y se les usa segun la necesidad particular. Veamos 4 de estas:
# 
# 1. [Conceptos básicos](#part1)
# 2. [Números](#part2)
# 3. [Conjuntos](#part3)
# 4. [Cadenas de texto](#part4)
# 5. [Listas](#part5) 
# 6. [Tuplas](#part6) 
# 7. [Dictionarios](#part7) 
# 8. [Data frames](#part8)
# 9. [Laboratorio 2](#part9) 
# 
# Las listas y tuplas son estructuras simples; un **Data Frame** (DF) es una compuesta. Los **dictionarios** (tcc **dicts**) son estructuras versatiles a pesar de su simplicidad. Los **Data Frame**s necesitan la instalación de librerías adicionales (no están en el sistema base del Python)

# In[1]:


from IPython.display import Image
get_ipython().run_line_magic('matplotlib', 'inline')


# ____
# [Ir a inicio](#beginning)

# <a id='part1'></a>
# ## Conceptos Básicos

# ##### Objeto

# In[3]:


X = [23,25,25]
X


# In[4]:


num = 255


# Componente que **se aloja en la memoria** y que tiene asociados una serie de vectores y operaciones que pueden ser realizadas con él. **Un objeto en Python** puede ser una cadena de texto, un número real, un  diccionario o un objeto propiamente dicho, según el paradigma OOP, creado a partir de una clase determinada. En otros lenguajes de programación se emplea el término estructura de datos para referirse al objeto. Podemos considerar ambos términos como equivalentes.

# ##### Tipos de componentes

# 1. Objeto
# 2. Expresiones: combinación de valores, constantes, variables, operadores y funciones que son aplicadas siguiendo una serie de reglas.
# 3. Sentencias: agrupamiento de expresiones y son consideradas estas como unidades mínimas ejecutables de un programa.
# 4. Módulos: nos ayudan a formar grupos de diferentes sentencias.

# ##### Objetos integrados

# Para **facilitar** su uso **Python** cuenta con una serie de **objetos integrado** (built-in). Entre las ventajas que nos ofrecen, caben destacar, el **ahorro de tiempo**, al no ser necesario construir estas estructuras de datos de forma manual, la **facilidad para crear complejas estructuras** basadas en ellos y el **alto rendimiento** y **mínimo consumo de memoria** en tiempos de ejecución.

# Contamos con:
# 1. Números
# 2. Conjuntos
# 3. Cadenas de texto
# 4. Listas
# 5. Tuplas
# 6. Diccionarios
# 
# Además, se cuenta con un tipo de objeto especial llamado **None** que se emplea para asignar un valor nulo.

# ##### Tipado dinámico

# **Python** al declarar una variable no se puede indicar su tipo. En la ejecución, el tipo será asignado a la variable, empleando una técnica conocida como tipado dinámico.

# **¿Cómo diferencia el intérprete entre diferentes tipos y estructuras de datos?**

# La respuesta se encuentra en el funcionamiento interno que realiza el **intérprete** de la **memoria**. Cuando se asigna a una variable un valor, el intérprete, en tiempo de ejecución, realiza un proceso que consiste en varios pasos:
# 
# 1. Se crea un objeto en la memoria con el valor asignado.
# 2. Se comprueba de que exista la variable, si no es así se crea una referencia que enlaza la nueva variable con el objeto.
# 3. Si por el contrario ya existe la variable, entonces, se cambia la referencia hacia el objeto creado.
# 
# **Tanto las variables como los objetos se almacenan en diferentes zonas de la memoria.**

# Gracias al **tipado dinámico** podemos, en el mismo bloque de código, asignar diferentes tipos de datos a la misma variable, siendo el intérprete en tiempo de ejecución el que se encargará de crear los objetos y referencias que sean necesarios.

# Para ejemplificar el proceso ingresaremos el siguiente código:

# In[5]:


x = 8
y = x


# In[6]:


x


# In[7]:


y


# Después de ejecutar las sentencias anteriores, en memoria tendríamos una situación como se muestra en el gráfico siguiente.

# In[5]:


Image(filename='D:/Python/1. Nivel I/2/imagenes/02_01.png', width=200) 


# Posteriormente ejecutamos una nueva sentencia como la siguiente:

# In[8]:


x = "test"


# In[9]:


x


# In[10]:


y


# Los cambios efectuados en la memoria pueden visualizarse en la gráfica siguiente.

# In[9]:


Image(filename='D:/Python/1. Nivel I/2/imagenes/02_02.png', width=200) 


# Sin embargo, para algunos tipos de objetos. **Python** realiza la asignación entre objetos y variables de forma diferente a la que hemos explicado previamente. Un ejemplo de este caso es cuando se cambia el valor de un elemento dentro de una **lista**.

# In[129]:


lista_1 = [9, 8, 7]
lista_2 = lista_1


# In[130]:


lista_1


# In[131]:


lista_2


# Ahora modificamos el segundo elemento de la primera lista, ejecutando la siguiente sentencia:

# In[132]:


lista_1[2] = 5


# In[133]:


lista_1


# Como resultado ambas listas han sido modificadas:

# In[134]:


lista_1


# In[135]:


lista_2


# Una función que nos puede resultar muy útil para ver de qué tipo es una variable es **type()**. Como argumento recibe el nombre de la variable en cuestión y **devuelve el tipo**.

# In[27]:


z = 20


# In[28]:


type(z)


# In[31]:


z = "Manuel"
type(z)


# ____
# [Ir a inicio](#beginning)

# <a id='part2'></a>
# ## Números

# Presente en todo lenguaje de programación. Para trabajar con ellos, **Python** cuenta con una serie de tipos y operaciones integradas.

# ##### Tipos: enteros, reales y complejos

# In[34]:


num_entero = 8
num_entero


# In[35]:


type(num_entero)


# In[36]:


#en el contexto de los números enteros
num_negativo = -100
num_negativo


# In[37]:


type(num_negativo)


# In[38]:


num_real = 4.5
num_real


# In[39]:


type(num_real)


# In[40]:


#otra manera de expresar un número real es:
num_real = 0.5e-7
num_real


# In[42]:


num_real = 0.00000005
num_real


# In[43]:


#números formados por una parte real y otra imaginaria
num_complejo = 3.2 + 7j
num_complejo


# ##### Sistemas de representación

# **Python** puede representar los números enteros en los sistemas decimal, octal, binario y hexadecimal. 

# Para la representación decimal no es necesario indicar nada más que el número en cuestión. Sin embargo, para el resto de sistemas es necesario que el número sea precedido por uno o dos caracteres concretos.

# In[44]:


#el número 7 en binario se representa de la siguiente forma:
num_binario = 0b111


# In[45]:


num_binario


# In[23]:


#el número 8 en octak se representa de la siguiente forma:


# In[46]:


num_octal = 0o10


# In[47]:


num_octal


# In[48]:


#el número 255 en el sistema hexadecimal se representa de la siguiente forma:
num_hex = 0xff


# In[49]:


num_hex


# ##### Operadores

# Los **operadores** resultan importantes para trabajar con los números. Entre estos tenemos:
# 1. Operadores aritméticos: suma, resta, división entera y real y multiplicación.
# 2. Operadores de bajo nivel y entre bits: NOT, NOR, XOR y AND.
# 3. Operadores para comprobar igualdad y desigualdad y para realizar operaciones lógicas: AND y OR

# In[28]:


Image(filename='D:/Python/1. Nivel I/2/imagenes/02_03.png', width=200) 


# ##### Funciones matemáticas

# **Python** nos permite aplicar otras funciones matemáticas a través del módulo **math**.

# In[35]:


#valor absoluto
abs(-47.67)


# Para algunas operaciones necesitamos importar el módulo **math**

# In[50]:


import math as m
m.sqrt(144)


# **Python** cuenta con las funciones *int()*, *hex()*, *oct()* y *bin()*. La siguiente sentencia muestra como obtener en hexadecimal el valor entero 16:

# In[54]:


hex(8)


# In[55]:


oct(8)


# Debemos tener en cuenta que las funciones de cambio de base admiten como argumentos cualquier representación numérica admitida por **Python**.

# In[58]:


bin(0o10)


# ____
# [Ir a inicio](#beginning)

# <a id='part3'></a>
# ## Conjuntos

# Definir y operar con conjuntos matemáticos también es posible en **Python**. La función para crear un conjunto se llama *set()* y acepta como argumentos una serie de valores pasados entre comas, como si se tratara de una cadena de texto. Por ejmplo, la siguiente línea de código define un conjunto tres números diferentes:

# In[62]:


conjunto = set("846")
conjunto


# In[40]:


type(conjunto)


# Un conjunto también puede ser definido empleando llaves *[{}]* y separando los elementos por comas.

# In[60]:


conjunto = {8, 4, 6}
conjunto


# Operaciones como *unión*, *intersección*, *creación de subconjuntos* y *diferencia* están disponibles para conjuntos en **Python**.

# In[63]:


conjunto_2 = set("785")
conjunto & conjunto_2


# In[64]:


conjunto_2


# In[65]:


conjunto


# In[66]:


#nombredeconjunto1.intersection(nombredeconjunto2)
conjunto.intersection(conjunto_2)
#intersection()


# Si creamos un conjunto con valores repetidos, estos serán automáticamente eliminados, es decir, no formarán parte del conjunto:

# In[67]:


duplicados = {2, 3, 6, 7, 6, 8, 2, 1}
duplicados


# ____
# [Ir a inicio](#beginning)

# <a id='part4'></a>
# ## Cadenas de texto

# Las **cadenas de texto** *(strings)* son otro de los tipos de datos más utilizados en programación. Una **Cadena de texto** es un conjunto inmutable y ordenado de caracteres. Para su representación y definición se pueden utilizar tanto comillas dobles *(")*, como simples *(')*.  

# In[68]:


cadena = "esto es una cadena de texto"
cadena


# In[70]:


cadena2 = """Esta cadena de texto 
 tiene más de una línea. En concreto, cuenta 
 con tres líneas diferentes"""

cadena2


# In[71]:


type(cadena)


# ##### Tipos

# Por defecto todas las cadenas de texto son Unicode. Así, cualquier **string** declarado en Python será automáticamente de tipo **Unicode**. Los tipos son:
# 
# 1. Unicode
# 2. Byte
# 3. Bytearray.

# ###### Byte
# El tipo **byte** solo admite caracteres en codificación **ASCII** y, al igual que los de tipo *Unicode*, son inmutables.
# 
# Para declarar un **string** de tipo **byte**, basta con anteponer la letra *b* antes de las comillas:

# In[72]:


cad = b"cadena de tipo byte"


# In[73]:


cad


# In[74]:


type(cad)


# ###### Bytearray
# 
# El tipo **bytearray** es una versión mutable del tipo *byte* La declaración de un tipo *bytearray* debe hacerse utilizando la función integrada que nos ofrece el intérprete. Además, es **imprescindible indicar el tipo de codificación que deseamos emplear**. El siguiente ejemplo utiliza la codificación de los caracteres *latin1* para crear un **string** de este tipo:

# In[76]:


lat = bytearray("España", #contenido
                "latin1") #tipo de formato
print(lat)


# In[77]:


str = "España"
array1 = bytearray(str, 'utf-8') 
print(array1)


# In[78]:


bytearray("España", "utf16")


# **encode()**: transforma un tipo *str* en tipo *byte*

# In[79]:


cad = "es de tipo str"
#objetounicode.encode()
cad.encode()


# **decode()**: transforma un tipo *byte* en tipo *str*

# In[80]:


cad = b"es de tipo byte"
cad.decode()


# ###### Principales funciones y métodos

# In[81]:


cad = "cadena de texto de ejemplo"
len(cad) #count de los elementos del objeto cad


# In[66]:


cad = "xyza"
cad.find("a") #find() realiza una búsqueda del elemento


# In[82]:


cad = "Hola Mundo"
cad.replace("Hola", #objeto a reemplazar
            "Adiós") #reemplazo


# In[83]:


#eliminar espacios en blanco
cad = " cadena con espacios en blanco "


# In[84]:


cad


# In[85]:


cad.strip()


# In[71]:


cad.lstrip()


# In[72]:


cad.rstrip()


# In[86]:


#convertir a mayúsculas y minúsculas
cad2 = cad.upper()
print(cad2)


# In[74]:


print(cad2.lower())


# In[87]:


#convertir primer carácter a mayúscula
cad = "un ejemplo"
cad.capitalize()


# In[89]:


#dividir una cadena de texto basándose en un carácter
cad = "primer valor; segundo; tercer valor"
cad


# In[90]:


cad.split(";") #split para señalar un elemento que nos ayudará a dividir el objeto


# In[91]:


",".join("abc")


# ###### Operaciones

# In[93]:


#concatenar
cad_concat = "¡Hola" + " Mundo!"
print(cad_concat)


# In[1]:


str(23)


# In[2]:


print("Hola Mundo " * 4)


# In[79]:


cad = "Nueva cadena de texto"
"d" in cad #consulta si el valor d está presente en el objeto cad


# In[3]:


cad = "Cadenas"
print(cad[2])


# In[4]:


print(cad[:3])


# In[77]:


cad[-3]


# In[5]:


cad[3:]


# ____
# [Ir a inicio](#beginning)

# <a id='part5'></a>
# ## Listas

# Las listas contienen valores de cualquier tipo simple (numérico o no numérico), y podrían ser estructuras **compuestas** (lista de listas). Si usamos como referencia a una hoja de calculo con datos sobre individuos, una lista podria ser una **fila** que tiene los datos de los individuos.

# In[6]:


Estudiante=["Manuel Ponte",23,"False"]


# El object ‘Estudiante’ almacena temporalmente la lista en la computadora. Los nombre pueden contener letras del alfabeto y números (y algunos caracteres de puntuación), pero no debe comenzar con un número.
# 
# En el código anterior, sólo se ha pedido crear la lista. Python lo ejecuta y nada más, no tienes que esperar ningún mensaje ni resultado. Si quieres ver lo que has creado, escribelo de manera explicita, así:

# In[7]:


Estudiante


# Nota que hay varios tipos de datos en la lista:
# 
# * *Nombre y apellido* es texto o caracteres.
# * *edad* es un numero.
# * *Mujer* es un valor lógico.
# 
# Para acceder a cada uno de los elemento tu lista:

# In[8]:


Estudiante[0] # primer elemento comienza con indice '0'


# In[9]:


Estudiante[:2] # todo antes de índice 2 


# In[10]:


Estudiante[-2] # ultimo elementos


# Si quieres **cambiar** algun valor:

# In[12]:


Estudiante[0]='Omar Escobedo'
Estudiante


# Para **añadir** elementos:

# In[13]:


Estudiante.append('UNFV')

# Ahora tienes:
Estudiante


# In[23]:


del Estudiante[3] 


# In[24]:


Estudiante


# Para **borrar**, se puede hacer por...
# 
# * posición
# * valor
# 
# Así, ante estas listas:

# In[16]:


elementsA=[11,22,33,44] 
elementsB=[11,22,33,44] 


# Entonces:

# In[17]:


## borrar tercer elemento
del elementsA[2]  
# luego:
elementsA  # 


# In[18]:


#  borrar valor '22'
# se puede eliminar por posición o por valor
elementsB.remove(22)
elementsB 


# Si lo que querias era dejar una lista de 4 elementos, pero el último dejarlo **vacío**:

# In[25]:


Estudiante.append('UNFV')
Estudiante


# In[26]:


#None es como NA en R
Estudiante[3]=None
Estudiante


# Para eliminar la lista:

# In[30]:


lista=['a','b'] 
lista


# In[32]:


del lista #del elimina, en este caso el objeto newList
#newList #si se corre debe arrojar error porque ya el objeto se ha eliminado


# In[33]:


lista


# A veces queremos eliminar valores repetidos:

# In[37]:


dias=['Lunes','Martes','Miércoles','Jueves','Viernes','Sábado','Domingo','Domingo']
dias


# Para ello tenemos la función _set_:

# In[36]:


dias=list(set(dias)) #función set es conjunto (función matemática). Los conjuntos no admiten repetidos
dias


# ### No hay vectores en Python?

# Los vectores no son parte del modulo básico de Python, por lo que necesitan que llames a **numpy** ( *instálalo antes si no lo tienes*):

# In[40]:


import numpy as np
#librería: np
#función: array


# In[41]:


#en R los vectores están integrados. En la función vector=c(23,24,25)
vector=np.array([1,"2",3]) # por poner el 2 entre comillas se convierte todo a texto
vector # aquí hay coerción pues solo debe haber un tipo de datos


# Los nombres de los vectores siguen las mismas reglas que para las listas.
# 
# Acceder a los elementos es igual que en listas:

# In[42]:


vector[2]


# In[43]:


vector[1]=1.5
vector


# Por lo anterior, nótese que ya que el vector es de textos, se coercionará a texto cada valor numérico ingresado.

# Para añadir elementos, también se usa **append()**, pero algo diferente:

# In[45]:


vectora=np.array([1,2,3])
vectorb=np.array([1,2,'3'])
vectora=np.append(vectora,vectorb)
vectora


# Para eliminar elementos:

# In[46]:


vectorc = np.array(['a','b','c','d'])
#index = [1,2] # posiciones
vectorc


# In[47]:


#eliminar vamos a trabajar con la función delete() de la librería np
vectorc = np.delete(vectorc, #elemento tipo vector
                    [1,2]) #debemos señalar la posición de los elementos a eliminar
vectorc


# También hay manera de eliminar valores duplicados:

# In[48]:


objeto =([1, 1, 22, 22, 333, 33])
objeto


# In[49]:


a= np.unique(objeto)
a


# ____
# [Ir a inicio](#beginning)

# <a id='part6'></a>
# ## Tuplas

# En **Python** una tupla es una estructura de datos que representa una colección de objetos, pudiendo estos ser de distintos tipos. Internamente, para representar una **tupla**, **Python** utiliza un *array* de objetos que almacena referencias hacia otros objetos.

# Al principio parace que fueran listas:

# In[56]:


Estudiantetupla=("Omar Escobedo",26,"False")
Estudiantetupla


# In[57]:


Estudiantetupla[0] = "Giancarlo Oviedo"


# Para crearlas puedes usar '(  )', el comando *tuple()* o nada:

# In[58]:


Estudiantetupla='Karolayne Pacherres',23,'True'
Estudiantetupla


# In[59]:


#Se puede realizar la consulta a través del índice que ocupa en la misma.
#exactamente igual que un array
Estudiantetupla[0]


# In[60]:


Estudiantetupla[0] = "Andrea Paz"


# Dado que una **tupla** puede almacenar distintos tipos de objetos, es posible anidar diferentes *tuplas*; veamos un sencillo ejemplo:

# In[61]:


t = (1, ("a", 3), 5.6)


# Una de las peculiaridades de las tuplas es que es un objeto iterable; es decir, con un sencillo bucle *for* podemos recorrer fácilmente todos sus elementos:

# In[62]:


for ele in t:
    print(ele)


# Concatenar dos tuplas es sencillo, se puede hacer directamente a través del operador *+*. Otros de los operadores que se pueden utilizar es *, que sirve para crear una nueva tupla donde los elementos de la original se repiten *n* veces.

# In[63]:


("r", 2) * 3


# Los principales métodos que incluyen las tuplas son **index()** y **count()**. El primero de ellos recibe como parámetro un valor y devuelve el índice de la posición:

# In[64]:


t = (1, 3, 7)
t.index(7)


# El método **count()** sirve para obtener el número de ocurrencias de un elemento en una tupla:

# In[65]:


t = (1, 3, 1, 5, 1)
t.count(1)


# Sobre las tuplas también podemos usar la función integrada **len()**, que nos devolverá el número de elementos de la misma. Obviamente, deberemos usar la variable tupla como argumento de la mencionada función.

# In[66]:


len(t)


# **Nota: La gran diferencia es que una vez creadas, ninguno de sus valores se puede modificar.**

# In[67]:


# genera error
Estudiantetupla[1]=50
# arroja error porque la tuple no es modificable
#R no tiene tuplas en sus paquetes básicos


# ____
# [Ir a inicio](#beginning)

# <a id='part7'></a>
# ## Diccionario

# Los Diccionarios, superficialmente, son lo más similares a las listas de R:

# In[68]:


# creando diccionarios:
EstudianteDict={'Nombres':"Manuel Ponte",
               'edad':23,
               'femenino':False}
#en los diccionarios se deben indicar los nombres de los atributos
# seeing it:
EstudianteDict


# Pero no tienen índices:

# In[69]:


EstudianteDict[0]


# Pare ver un elemento, tienes que saber el nombre de su campo ('key'):

# In[70]:


EstudianteDict['Nombres']


# A partir de ahi, puedes hacer las operaciones comunes:

# In[71]:


EstudianteDict['edad']=24
EstudianteDict


# #### Detalles importantes para estructuras básicas

# __A) Aseguráte de saber qué tienes:__

# In[72]:


type(EstudianteDict)


# In[73]:


type(Estudiante)


# In[74]:


type(Estudiantetupla)


# __B) Asegúrate que las funciones se pueden compartir__
# 
# 

# In[75]:


listTest=[1,2,3,3]
tupleTest=(1,2,3,4,4)
dictTest={'a':1,'b':2,'c':2}
len(listTest), len(tupleTest), len(dictTest)
#len ve la cantidad de elementos en cada tipo de estructura de datos.


# ## Ejercicio
# 
# Cree un diccionario con esta información:
# 
# <center><img src="https://github.com/escuela-alacip/introPython/raw/master/pics/Bachelet.png" width="300"></center>
# 
# * Haga un diccionario de la manera más simple.
# * Haga luego un diccionario usando donde se pueda otras estructuras (listas, tuplas, diccionarios)

# In[67]:


Bachelet={'nombre en español':"Verónica Michelle Bachelet Jeria",
               'nacimiento':"29 de septiembre de 1951",
               'Residencia':"Santiago, Chile",
         'nacionalidad':"Chilena",
         'lengua materna':"Español",
         'religión':"Agnosticismo",
         'partido político':"Partido Socialista",
         'padres':"Ángela Jeria Gómez , Alberto Bachelet Martínez",
         'cónyugue':"Jorge Dávalos Cartes",
         'hijos':"Sebastián , Francisca , Sofía",
         'educada en':"Universidad de Chile",
         'ocupación':"médico",}
Bachelet


# In[68]:


padres=["Ángela Jeria Gómez","Alberto Bachelet Martínez"]
hijos=["Sebastián","Francisca", "Sofía"]


# In[69]:


Bachelet={'nombre en español':"Verónica Michelle Bachelet Jeria",
               'nacimiento':"29 de septiembre de 1951",
               'Residencia':"Santiago, Chile",
         'nacionalidad':"Chilena",
         'lengua materna':"Español",
         'religión':"Agnosticismo",
         'partido político':"Partido Socialista",
         'padres':padres,
         'cónyugue':"Jorge Dávalos Cartes",
         'hijos':hijos,
         'educada en':"Universidad de Chile",
         'ocupación':"médico",}
Bachelet


# In[70]:


type(Bachelet)


# [Ir a inicio](#beginning)
# ____

# <a id='part8'></a>
# ## Data Frames

# Los **Data Frames** pueden interpretarse como estructuras compuestas en base a las simples. Python requiere que llamemos al paquete **pandas** para usar DFs:

# In[76]:


import pandas as pd


# In[77]:


# estas son columnas:
#listas de columnas

nombres=["Manuel", "Karen", "Karolayne", "Omar"]
edad=[23,29,23,26]
pais=["Ecuador", "Perú", "Brasil", "Argentina"]
educacion=["Bach", "Lic", "Bach", "PhD"]


# In[79]:


# las llevamos a diccionario:
data={'nombres':nombres, 'edad':edad, 'pais':pais, 'educacion':educacion}
data


# ...y de  dict a DF:

# In[80]:


estudiantes=pd.DataFrame(data)
# check it:
estudiantes


# También podría ser a partir de filas:

# In[82]:


# Listas por filas
row1=["Manuel", 23,"Ecuador", "Bach"]
row2=["Karen", 29, "Perú", "Lic"]
row3=["Karolayne", 23, "Brasil", "Bach"]
row4=["Omar", 26, "Argentina", "PhD"]


# In[83]:


#Lista de listas de filas
listOfRows=[row1,row2,row3,row4]
listOfRows


# In[86]:


#creandolo:
DF_lists=pd.DataFrame(listOfRows,
                      columns=['nombres','edad','pais','educacion'])
DF_lists.head(1)


# In[89]:


DF_lists.tail(2)


# Tendremos un data frame? Recuerda que **type**  te lo dice:

# In[90]:


type(estudiantes)


# Pero Pandas da más detalles con 'dtypes':

# In[150]:


estudiantes.dtypes # es como la función str en R
# object es un texto


# Además de _dtypes()_, es bueno saber que puedes usar:

# In[91]:


# cuantas filas y columnas tienes:
estudiantes.shape #en R es el dim


# No hay función específica para saber cuantas filas o columnas hay independientemente, pero **len** ayuda:

# In[153]:


len(estudiantes.index) # or students.shape[0]


# In[92]:


len(estudiantes.columns) # or students.shape[1]


# También son muy útiles las función __head()__, que te permite ver las filas al inicio del DF:

# In[93]:


estudiantes.head(2) # función head de R


# Y su antónimo también está disponible:

# In[94]:


estudiantes.tail(2)


# Claro que es bueno saber qué variables tenemos:

# In[96]:


variables = list(estudiantes.columns)
variables


# Lo anterior no es una lista, pero si la necesitas:

# Tu DF es la tabla de datos a la que estás acostumbrado a utilizar. Si quieres ver algun elemento en particular:

# In[97]:


# una columna
estudiantes.nombres


# In[101]:


edades = estudiantes["edad"].values
edades


# In[102]:


# o
estudiantes['nombres']


# In[105]:


# # varias columnas (con posiciones)
estudiantes.iloc[:,[1,3]]
#iloc[filas,columnas]


# In[106]:


# varias columnas (con nombres)
estudiantes[['edad','educacion']]


# In[107]:


# o
var_selec = ['edad','educacion']
estudiantes.loc[:,var_selec]


# In[110]:


# tambien:

estudiantes.loc[:,'edad':'educacion']


# In[111]:


# varias columnas (con posiciones)
estudiantes.iloc[:,1:4]


# In[112]:


# sino:

estudiantes.iloc[:,[1,3]]


# In[114]:


# una fila
estudiantes.iloc[1,]


# In[116]:


# varias filas
estudiantes.iloc[[2,3],:]


# In[117]:


estudiantes


# Nótese en los casos anteriores, que si no indicabas filas, tenías toda la fila; y que si no indicas columnas, vienen todas las columnas. Si solo quieres un valor:

# In[118]:


estudiantes.iloc[1,3]


# Es muy común, y necesario, crear **subsets** del DF:

# In[119]:


estudiantesNoEd=estudiantes.iloc[:,[0,1,2]]
estudiantesNoEd


# Voy a hacer algunos cambios a este DF. Sin embargo, es común primero crear una copia del original:

# In[120]:


estudiantes


# In[143]:


estudiantesCopy=estudiantes.copy()
estudiantesCopy


# Ahora, a la copia le hago modificaciones.

# In[144]:


# cambio el valor de una edad:
estudiantesCopy.iloc[0,1]=25 # No hay advertencia, el cambio ya se hizo:
estudiantesCopy


# In[145]:


# Podemos tener una nueva columna con valores vacios
estudiantesCopy.pais=None
estudiantesCopy


# In[146]:


# Y puedeo eliminar una columna:
estudiantesCopy.drop('edad',
                     axis=1,# axis=1 es columna #axis=0 es fila 
                     inplace=True) 
estudiantesCopy


# In[147]:


get_ipython().run_line_magic('pinfo', 'estudiantesCopy.drop')


# ##### _CONSULTAS_ en Data Frames:

# Una de las primeras cosas que hacemos con los DF es hacerle consultas:

# In[148]:


max(estudiantes.edad)


# In[150]:


# ¿Quién es el más viejo del grupo?
estudiantes[estudiantes.edad==max(estudiantes.edad)].nombres


# In[152]:


# ¿Quién es el más joven del grupo?
estudiantes[estudiantes.edad==min(estudiantes.edad)].nombres


# In[155]:


# ¿Quién tiene más de 25 y es de Perú?
data_set=estudiantes[(estudiantes.edad>25) & (estudiantes.pais!='Perú')] # parentesis requeridos


# In[156]:


data_set


# In[158]:


# ¿Quién no viene de Perú?
estudiantes[estudiantes.pais!="Perú"].nombres


# In[160]:


# ¿Quién no viene de estos lugares?
lugares=["Perú", "Brasil"]
estudiantes[~estudiantes.pais.isin(lugares)]


# In[162]:


# Muestrame el DF ordenado decrecientemente por edad**
toSort=["edad"]
Order=[False]
estudiantes.sort_values(by=toSort,#caracter por el cual se va ordenar
                        ascending=Order) #orden 


# **sort.values()**: función que sirve para ordenar

# In[211]:


# Muestrame el DF ordenado crecientemente, por educacion y luego por edad

toSort=["educacion","edad"]
Order=[True,True]
estudiantes.sort_values(by=toSort,
                        ascending=Order)

