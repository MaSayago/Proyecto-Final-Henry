# <h1 align=center>**`Informe Sprint 2`**</h1>

# Introducción

Elaboramos este documento con el objetivo de proporcionar detalles adicionales sobre las actividades y tareas realizadas durante la segunda semana. En dicho período, nuestro enfoque principal fue la ingeniería de datos, que incluyó la planificación, diseño y construcción de la infraestructura del proyecto. Dentro de estas tareas, se dio prioridad a la transformación de dataos junto a la determinación del flujo de trabajo. Asimismo, nos enfocamos en la creación y posterior automatización de los pipelines necesarios para llevar a cabo el proceso de extracción, transformación y carga (ETL), con el propósito de almacenar los datos en un Data Warehouse.

Con el fin de abordar el tema desde lo más general a lo más específico a continuación describimos los Pipelines de manera abarcativa y luego mas en detalle en el WorkFlow.

# Extracción

Para esta etapa utilizamos los datasets disponibles de ambas plataformas, posteriormente se extraerán dichos datos a través de consultas a  Yelp Open Dataset y Google Places para hacer cargas de datos automáticas.
Dichos Datasets contienen información de las calificaciones y opiniones de los usuarios acerca de los distintos establecimientos, además de los datos geográficos de los mismos. El formato de los datos es principalmente json.

# Transformación

Con los datos extraídos procedemos a darles coherencia, consistencia y finalmente los preparamos para la posterior carga. A continuación, los pasos realizados:

1. Limpieza: En este punto corregimos las inconsistencias y eliminamos los registros duplicados o irrelevantes para garantizar la calidad de los datos.
2. Filtrado: En pos de nuestro objetivo el cual se centrar en bares realizamos el filtrado por categoría de establecimiento para obtener solo los pertinentes a este proyecto.
3. Validación: Chequeamos y corregimos la estructura y consistencia de los datos para obtener resultados confiables y precisos.
4. Transformación: Antes de proceder a la carga les otorgamos a los archivos que utilizaremos el json.

En esta etapa también se realizó el análisis exploratorio de datos en el cual profundizamos en el Workflow.

# Carga

Con los archivos ya limpios y en el formato corresponidente procedemos al almacenado de los mismos en GCP (Google Cloud Plataform) La carga se realizó de la siguiente manera:

1. Creamos un proyecto en GCP.
2. Seleccionamos un servicio de almacenamiento que en este caso es Cloud Storage (CS).
3. Creamos un bucket en CS, que va a ser el contenedor de los archivos donde se almacenarán los datos.
4. Finalmente, ingestamos los datos en el servicio de análisis de dicha plataforma BigQuery.

# <h1 align=center>**Workflow detallado**</h1>

En esta sección detallamos las distintas etapas y tecnologías utilizadas en la ingeniería de datos. Nuestro objetivo principal se centró en extraer información relevante de los establecimientos de tipo Bar en Estados Unidos junto con sus calificaciones y reseñas. Aplicamos tanto limpieza como transformación a los datos obtenidos, realizamos un análisis exploratorio y utilizamos los servicios en la nube de Google Cloud Platform (GCP) para almacenar, procesar y automatizar el flujo de datos.

En la primera etapa, se extrageron y disponibilizaron los datasets de Google Places y Yelp  que nos brinda información de la reseñas estructurada en distintos archivos.

Posteriormente, se llevó a cabo la limpieza, filtrado, validación y transformación de los datos utilizando Python y bibliotecas como pandas, json, re y os.. Se aplicaron filtros por categoría y se eliminaron datos irrelevantes

A continuación, se realizó un análisis exploratorio detallado de los datos utilizando Python y seaborn, matplotlib. Se examinaron los puntajes de los lugares en Google Maps y Yelp, identificando patrones y distribuciones significativas. Esto proporcionó una comprensión más profunda de la calidad y popularidad de los lugares analizados.

Por último, se utilizaron los servicios en la nube de Google Cloud Platform (GCP) para almacenar los datos limpios en Cloud Storage. Además, se emplearon los servicios de BigQuery y DataFlow para crear la base de datos necesaria y  su posterior automatización  de tareas relacionadas con el procesamiento y análisis de los datos.

El proceso completo abarcó desde la extracción de datos hasta su almacenamiento y análisis en la nube, permitiéndonos obtener información valiosa que utilizaremos más adelante para desarrollar un modelo de machine learning. A continuación, se detallan las diferentes etapas y tecnologías utilizadas en cada una de ellas.

## **Extracción de datos:**

   * Tecnología: Google Places, Yelp Open Dataset.

   * Descripción: Utilizamos para la carga inicial los dataset provenientes de la API de Google Places y de Yelp Open Dataset para extraer datos de los establecimienots y las reseñas.

   *	Detalles adicionales:

   *	Utilizamos dichos dataset de Google para extraer datos de reseñas y metadatos de sitios/localizaciones.

   **a.**	Los datos de Google Places se dividieron en dos partes:

   1.	Metadata de sitios: Contiene información sobre los lugares, como nombres, direcciones, categorías, etc.

   2.	Reviews por estado: Se crea 51 carpetas, una por cada estado de Estados Unidos, donde se almacenaron las reseñas correspondientes a los bares en cada estado.

   **b.**	Los datos de Yelp se extrajeron  de los datasets provenientes de Yelp Open Dataset con datos similares a los de Google pero estructurados de la siguiente manera:

   1.	Business.pkl: Contiene información ordenada por establecimientos.

   2.	Checkin.json: Información acerca de las fechas de ingreso a los distintos establecimientos.

   3.	 Review.json: Contiene información de las reseñas realizadas a cada establecimiento agrupadas por el usuario que la emitió, junto con las interacciones.

   4.	 tip.json:  Contiene información más detallada de la reseña de cada usuario.

   5.	user.parque: Detalla le información y relación que guardan los usuario entre sí.

## **Limpieza y transformación de datos:**

   *	Tecnología: Python, pandas, json, re, os, pyarrow, pyarrow.parquet, Fastparquet.

   *	Descripción: Utilizamos Python junto con las bibliotecas detalladas en el inciso a. para limpiar y transformar los datos extraídos.

   *	Detalles adicionales:

   **a.**	Se filtraron los datos por la categoría "bar" para obtener únicamente los datos relevantes.

   **b.**	Se realizó un filtrado manual adicional para eliminar categorías no relevantes como "barber shop", "eyebrow bar", etc.

   **c.**	Los datos limpios se guardaron en formato json.

## **Análisis exploratorio de datos:**

   **a.**	Tecnología: Python, pandas, numpy, matplotlib, seaborn

   **b.**	Descripción: Utilizamos Python junto con las bibliotecas destalladas previamente para realizar un análisis exploratorio de los datos.

   **c.**	Detalles adicionales:

   ### ***Google Maps:***

   **a.** Se observa que la mayoría de las puntuaciones en Google Maps para bares se encuentran entre 4 y 5 estrellas, con una inclinación notable hacia las 5 estrellas.

   **b.**	Como referencia para el trabajo, consideraremos puntajes bajos aquellos inferiores a 3.0, donde parece haber un primer pico notable de distinción en la frecuencia. Los puntajes altos serán considerados aquellos por encima de 4.5, debido a la alta frecuencia de las 5 estrellas. Los puntajes moderados estarán en el rango de 3.0 a 4.5.

   **c.**   Bares: 5,095

   **d.**	Total de reviews de bares: 1,116,687

   **e.**	Puntaje promedio de los bares: 4.28

   **f.**	Principales tipos de bares en Google Maps:

   *	Girl Bars: Los girl bars son lugares donde las mesas son atendidas exclusivamente por mujeres, haciendo del servicio la atracción principal.

   *	Cider Bars: Los cider bars son lugares donde la cidra es la principal atracción.

   *	Cocktail Bars: Los cocktail bars tienen como atracción principal los tragos en general.

   *	Poke Bars: Los poke bars son bares hawaianos.

   ### ***Yelp***

   **a.** Se observa que un gran porcentaje de las puntuaciones se encuentran entre 4 y 5 estrellas si bien tambien el numero de calificaciones de 1 estrella es alta, lo que se contice con el objetivo de la plataforma que se enofca principalmente en calificar los establecimientos de forma mas critica.

   **b.**	Bares: 12,546

   **c.**   Total de reviews de bares: 1,521,965

   **d.**	Puntaje promedio de los bares: 3.80

   **e.**	Principales tipos de bares en Yelp:

   *	Nightlife Bar: establecimientos que se centran principalmente en ofrecer entretenimiento nocturno y actividades relacionadas con la vida nocturna.

   *	Sushi Bar: establecimientos especializados en la preparación y servicio de sushi

   *	Tapas Bar: establecimientos que se especializan en servir tapas, que son pequeñas porciones de platos tradicionales españoles
    
## **Servicios en la nube de Google Cloud Platform (GCP):**

   **a.**	Tecnología: GCP, Cloud Storage, BigQuery, Cloud run.

   **b.**	Descripción: Utilizamos los servicios de GCP para almacenar, procesar y automatizar el flujo de datos.

   **c.**	Detalles adicionales:

   * En primer lugar utilizamos Cloud Storage para almacenar los datos limpios en formato json dentro de un Bucket.

   * En segundo lugar utilizamos BigQuery para crear la base de datos y las tablas necesarias para el análisis de datos, importado los mismos desde el Bucket

   * Finalmente utilizamos Cloud run para la automatización de tareas relacionadas con el procesamiento y carga de datos.

# Pipeline

En resumen, para poder entender mejor de forma visual este proceso, los estructuramos en base a las tres instancias del ETL (Extracción, Transformación y Carga).

•	**_Extracción:_** Captura de datos.

•	**_Transformación_**: Limpieza, filtrado de datos, validación y transformación.

•	**_Carga_**: Almacenamiento de los datos el Data Werehouse.

Finalmente y a modo ilustrativo, este sería el recorrido completo de los datos:

<p align = "center">
<img src = ../imgs/Diagrama_Pipeline.png >
</p>

# Modelo De Entidad-Relación

El modelo de entidad-relación es una forma de modelar la forma en la que las entidades se relacionan entre sí en una base de datos. Esto hace que sea fácil de comprender y utilizar para los usuarios.
En nuestro caso, al utilizar Google BigQuery como sistema de gestión de bases de datos, las relaciones del modelo tradicional no son necesarias ya que es una base de datos relacional distribuida, no utiliza claves foráneas para establecer relaciones de manera explícita como lo haría un sistema de gestión de bases de datos relacional tradicional.
Si bien las relaciones en un modelo de entidad-relación tradicional no se aplican directamente en BigQuery, sigue siendo importante comprender la estructura y la semántica de los datos tanto para poder diseñar consultas eficientes y obtener los resultados deseados como para combinar y filtrar los dato.

Por dichos motivos generamos un Diagrama de Entidad-Relación (DER) para visualizar las relaciones.

<p align="center">
<img src= ../imgs/DiagramaER.PNG >
</p>
