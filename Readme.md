# <h1 align=center>**`PROYECTO FINAL - Sistema de Recomendación para Mejora De Bares`**</h1>

# <h1 align=center> ![ia](https://emoji.slack-edge.com/TPRS7H4PN/henry-pm/4658c1bc769b53ae.png) </h1>


# Entendimiento de la situación actual

A través de las plataformas de Google map y Yelp los usuarios pueden dejar reseñas  y calificaciones de los bares, hoteles y otros negocios a fines. Lo que permite tener al alcanze una gran cantidad de datos de los cuales se pueden usar para mejorar la experiencia de los clientes.

En representación de la consultora QUINQUE, nos complace compartir con ustedes un emocionante proyecto en el que nos hemos embarcado recientemente. Hemos sido contratados por un cliente que se encuentra en el rubro de bares y busca mejorar la calidad de sus establecimientos y la experiencia de sus clientes.



## Objetivos


- Mejorar 

- Crecer/Expandir


# Alcance

El alcance de este proyecto incluye analizar las reseñas de bares con baja y alta calificacion de los clientes. Tambien sus opiniones y consejos de estos mismo, para identificar patrones o tendencias que puedan determinar las áreas que requieren mejoras. Además, exploraremos las localizaciones de bares para poder determinar oportunidades de expansión en nuevas ubicaciones geográficas y brindaremos asesoramiento estratégico para lograr un crecimiento en un plazo de 6 a 12 meses.


# Objetivos y KPIs asociados

## KPIs de mejora:

- **_Promedio de calificaciones:_** Calcula el promedio de calificaciones (estrellas) de los bares utilizando las reseñas de los clientes. El objetivo será aumentar este promedio en al menos un 20% a medida que se implementen las mejoras. Esto indicará una mejora general en la calidad y la satisfacción del cliente.

- **_Número total de reseñas:_** Determina cuántas reseñas ha recibido cada bar para evaluar su nivel de popularidad y participación de los clientes. El objetivo será aumentar el número total de reseñas en por lo menos 5%, lo cual reflejará una mayor interacción y retroalimentación de los clientes.

- **_Porcentaje de reseñas positivas:_** Calcula el porcentaje de reseñas con calificaciones altas (por ejemplo, 4 o 5 estrellas) para evaluar el nivel de satisfacción general de los clientes. El objetivo será aumentar este porcentaje entre un 5% y 15%, lo cual indicará una mejora en la percepción positiva de los clientes sobre los bares.

- **_Palabras clave más frecuentes en las reseñas:_** Utilizando técnicas de procesamiento de lenguaje natural, identifica las palabras clave más frecuentes asociadas con experiencias positivas o negativas. Este KPI permitirá comprender mejor las preferencias de los clientes y las áreas específicas que requieren mejora. El objetivo será identificar y abordar al menos 3 áreas de mejora relevantes según las palabras clave extraídas.

## KPIs de ubicación y expansión:

- **_Densidad de bares por ubicación:_** Utiliza la información de ubicación (latitud y longitud) para calcular la densidad de bares en diferentes áreas o ciudades. El objetivo será identificar áreas con alta densidad de bares y evaluar su potencial de expansión. El objetivo consistirá en aumentar el umbral de densidad en un 5% en los casos que demuestren potencial de expansión 

 - **_Índice de competencia:_** Utiliza la información de categorías de los bares para evaluar la competencia en diferentes segmentos de mercado, como "Mexican", "Burgers", "Gastropubs", entre otros. Este KPI permitirá identificar áreas con baja competencia y oportunidades de nicho. El objetivo consistirá en establecer un índice objetivo de competencia basado en el número de bares y su categoría para incrementarlo en al menos 5% en los segmentos que representen una oportunidad de nicho.

- **_Evaluación de características locales:_** Analiza la presencia de atracciones turísticas, universidades, oficinas corporativas u otras características locales que puedan influir en el potencial de un bar. El objetivo será establecer un índice, mediante el establecimiento de criterios específicos, que represente las ubicaciones con características favorables para la expansión y el crecimiento del negocio, con el fin de identificar puntos relevantes para incrementar dicho índice en un 5%.


# Solución propuesta

## Tareas:

a. Recopilar y explorar los datos disponibles sobre bares.

b. Realizar un análisis exploratorio de los datos para identificar patrones y tendencias.

c. Aplicar técnicas de limpieza y preprocesamiento de datos para garantizar su calidad.

d. Realizar análisis estadísticos y modelos de correlación para identificar las variables más relevantes para el éxito de los bares.

e. Desarrollar un modelo predictivo utilizando técnicas de aprendizaje automático para estimar el éxito potencial de nuevos locales.

f. Evaluar el rendimiento del modelo y ajustar los parámetros según sea necesario.

g. Generar recomendaciones accionables basadas en los hallazgos del análisis.

## **Stack tecnológico**

**_Herramientas de colaboración y gestión de proyectos_**

- Discord
- Google meet
- GitHub
 
**_Lenguaje de programación:_** 

- Python 

**_Bibliotecas y frameworks:_** 
- Wordcloud 
- Python
- Pandas / NumPy
- Scikit-learn 
- Matplotlib / Seaborn

**_Herramientas de visualización de datos:_**

- Prezi
- PowerBI 

**_Base de Datos_:**

- Google Cloud Plataform
   - Cloud Storage
   - Bucket
   - BigQuery
   - DataFlow


## Metodología de trabajo:

Se utilizará la metodología ágil Scrum para el desarrollo del proyecto. El equipo se organizará en sprints de una semana de duración, con reuniones diarias de seguimiento y una reunión de revisión al final de cada sprint. Se obtendrá más información del cronograma general en el siguiente diagrama de Gantt:
 <p align="center">
<img src= [img/Diagrama_de_Gantt-Semana-2.jpeg](https://github.com/kevinbamba/Proyecto-Final-Henry/blob/main/img/Diagrama_de_Gantt-Semana-2.jpeg)>
</p>

## Análisis preliminar de calidad de datos:
 Este informe de Análisis Exploratorio de Datos (EDA) presenta los resultados obtenidos a partir de los datos recopilados de Google Maps y Yelp. Nuestro objetivo principal fue analizar la información de bares y establecimientos similares con el fin de mejorar la calidad de los negocios y la experiencia de los clientes. Mediante el uso de diversas técnicas de análisis de datos, exploramos los factores que contribuyen a la excelencia en los establecimientos y proporcionamos recomendaciones clave para optimizar el rendimiento y brindar una experiencia excepcional a los clientes. A continuación, presentamos los principales hallazgos y recomendaciones derivados de nuestro análisis que se puede encontrar en el Informe-EDA.md 
 
## Ingeniería de datos

 En la carpeta Ingenieria de datos, se podra encontrar todo el proceso de ETL(Extract, Transform and Load) junto con su Pipelines y la creación del Data Warehouse  con el Modelo Entidad-Relación donde estan los archivo que genera la carga de los datos ya limpios en el Data Warehouse. Con su correspondiente documentacion que esta en el archivo Informe_Pipelines_y_Workflow.docx y su diccionario de datos.


# Roles:

- **_Data Analyst_**: Kevin Bambozzi, Martin Sayago

- **_Data Engineer_**: Yamil Pintos, Alex Dalpiaz, Jeremias Ramirez

- **_Data Science_**: Alex Dalpiaz, Jeremias Ramirez

## Link De Repositorio: 

**_Github:_** <https://github.com/alexDRandom/Proyecto-Final-Henry>


Agradecemos su atención y estamos disponibles para responder cualquier pregunta que puedan tener. Esperamos poder llevar a cabo este proyecto exitosamente y lograr mejoras significativas en los bares de nuestro cliente. ¡Gracias!
