# **Informe Semana 3**

En el siguiente informe presentamos el trabajo realizado durante la semana 3 del proyecto, la cual se centró en las áreas de Data Analytics y Machine Learning, en base al análisis de las reviews de bares en Estados Unidos. Con los datos procesados se implementó un modelo de similitud del coseno el cual involucró la selección y diseño de características adecuadas, así como la implementación y evaluación del modelo. El objetivo de dicho modelo consiste en identificar patrones y similitudes en las reseñas de los clientes sobre los bares analizados.

Además, se diseñó un dashboard que permite visualizar y analizar de manera efectiva los datos relevantes, incluyendo los indicadores clave de rendimiento (KPIs) relevantes para el análisis.

El resultado final fue la integración del dashboard y el modelo de similitud.

# Informe sobre el modelo de machine learning: SVM para predicción de incremento en puntaje de bares

El modelo de machine learning que vamos a analizar en este informe es una implementación de Support Vector Machines (SVM) para predecir el incremento en el puntaje de los bares. El objetivo es utilizar este modelo para brindar una estimación cuantitativa del incremento en el puntaje promedio de un bar específico en un plazo de tiempo medio.

El diseño de este modelo sigue los siguientes pasos de ingeniería:

## 1. Recopilación y preparación de datos

Para entrenar este modelo, recopilamos datos de los reviews de Google Maps. Se eliminaron las reseñas que no contenían ningún texto en ellas. Además, se filtraron los bares que tenían menos de 50 reviews para estandarizar el mínimo de reviews devueltas. Luego, se realizó un preprocesamiento del texto, que incluyó la eliminación de caracteres Unicode, mayúsculas y números, así como la eliminación de palabras vacías, la reducción de palabras a su forma base (stemming) y la tokenización de las palabras restantes. Estos datos procesados se guardaron en una nueva columna llamada 'processed_text' para evitar tener que repetir el preprocesamiento en cada consulta.

## 2. Representación vectorial de los documentos

Para representar los documentos de texto, se tomaron los reviews basados en la búsqueda de un bar específico y se transformaron en vectores numéricos utilizando el enfoque de matriz TF-IDF (Term Frequency-Inverse Document Frequency). Los reviews se dividieron en dos grupos: aquellos con puntaje 2 o menos y aquellos con puntaje 4 o más. Se crearon matrices TF-IDF separadas para cada grupo, donde se asignó la etiqueta 0 a los reviews de puntaje bajo y la etiqueta 1 a los reviews de puntaje alto. Finalmente, se concatenaron ambas matrices en una matriz principal de referencia para el modelo.

## 3. Entrenamiento y evaluación del modelo SVM

En esta etapa, se dividió la matriz TF-IDF en conjuntos de entrenamiento y prueba utilizando la función de división train_test_split. Se entrenó un modelo SVM de regresión lineal utilizando los datos de entrenamiento, donde el modelo aprendió los coeficientes y el sesgo necesarios para realizar predicciones. Luego, se realizaron predicciones utilizando los datos de prueba y el modelo entrenado. La evaluación del modelo se realizó calculando el error cuadrático medio (RMSE) entre las predicciones y los valores reales de los puntajes.

## 4. Uso del modelo en aplicaciones

El modelo entrenado se puede utilizar en aplicaciones para proporcionar una estimación del incremento en el puntaje promedio de un bar específico en un plazo de tiempo medio. Al ingresar el nombre del bar como input, el modelo aplicará sus conocimientos previos y las relaciones aprendidas durante el entrenamiento para realizar una predicción cuantitativa.

Es importante tener en cuenta que las predicciones del modelo se basan únicamente en las características y relaciones extraídas de los datos de entrenamiento. Se recomienda utilizar los resultados como una guía aproximada y complementarlos con conocimientos y análisis adicionales.



# Modelo de machine learning: Análisis de Categorías y Palabras Clave, Regresión logística

El modelo de análisis de categorías y palabras clave se utiliza para identificar áreas de mejora en un local de negocios basándose en las reseñas de los clientes. Mediante el procesamiento de texto y el cálculo de la frecuencia de palabras en diferentes categorías, este modelo proporciona información valiosa sobre las áreas específicas en las que el local puede enfocarse para mejorar la experiencia del cliente.

## Recopilación y preparación de datos:

**Paso 1: Cargar los nombres de los locales y los gmap_id correspondientes**

Se carga la información de los locales y sus identificadores desde el archivo "locales.json".

**Paso 2: Cargar las reseñas y las calificaciones filtradas por el gmap_id**

Se cargan las reseñas y las calificaciones asociadas al local especificado por el usuario desde el archivo "resenas.json".

## Representación vectorial de los documentos:

**Paso 3: Convertir las calificaciones en etiquetas**

Las calificaciones se convierten en etiquetas binarias (0 para calificaciones bajas y 1 para calificaciones altas).

**Paso 4: Dividir los datos en conjuntos de entrenamiento y prueba**

Los datos se dividen en conjuntos de entrenamiento y prueba para su posterior evaluación y ajuste del modelo.

## Cálculo de regresión logística:

**Paso 5: Vectorizar los textos de las reseñas utilizando TF-IDF**

Se utiliza la técnica TF-IDF para convertir los textos de las reseñas en representaciones numéricas.

## Evaluación y ajuste del modelo:

**Paso 6: Análisis de categorías y palabras clave**

Se analizan las reseñas para determinar las categorías con mayor frecuencia de palabras repetidas y las tres palabras más repetidas en cada categoría.

## Uso del modelo en aplicaciones:

**Paso 7: Obtener las categorías con mayor frecuencia de palabras y las palabras más repetidas**

Se obtienen las categorías con mayor frecuencia de palabras repetidas y las tres palabras más repetidas en cada categoría a partir de las reseñas del local especificado.

**Paso 8: Mostrar las categorías y las palabras más repetidas**

Se muestra en pantalla las categorías que requieren mayor atención en el local especificado, junto con la cantidad de palabras repetidas y las tres palabras más repetidas en cada categoría.

El modelo de análisis de categorías y palabras clave es una herramienta poderosa en el campo del procesamiento de texto y el análisis de similitud. Su enfoque no supervisado permite obtener información valiosa sin intervención manual en la configuración de parámetros. Con su capacidad para identificar áreas clave de mejora en los negocios, este modelo se convierte en una herramienta estratégica para optimizar la satisfacción del cliente y mejorar la calidad de los servicios ofrecidos.


## Stack Tecnológico

- **Lenguaje de programación:** Python: Python es ampliamente utilizado en el campo del análisis de texto y machine learning debido a su versatilidad, amplias bibliotecas y facilidad de uso.

- **Bibliotecas de procesamiento de texto:** La biblioteca `nltk` proporciona herramientas para el procesamiento de texto, como tokenización, lematización y análisis de sentimientos. También se utiliza la clase `SentimentIntensityAnalyzer` de `nltk.sentiment` para analizar la polaridad de las reseñas.

- **Bibliotecas de machine learning:** Scikit-learn es una biblioteca popular en Python que proporciona una amplia gama de algoritmos y técnicas de machine learning. En el código proporcionado se utiliza la clase `LinearRegression` para realizar una regresión lineal.

- **Bibliotecas de vectorización de texto:** Scikit-learn ofrece la clase `TfidfVectorizer` para convertir el texto en representaciones vectoriales utilizando la técnica de TF-IDF. Esta clase se utiliza en el código proporcionado para vectorizar las reseñas.

- **Bibliotecas de evaluación del modelo:** La biblioteca `sklearn.metrics` proporciona métricas de evaluación de modelos, como el error cuadrático medio (`mean_squared_error`), que se utiliza en el código proporcionado para evaluar el rendimiento del modelo.

- **Bibliotecas para manipulación de matrices dispersas:** La biblioteca `scipy.sparse` se utiliza para manipular matrices dispersas, como las representaciones vectoriales generadas por `TfidfVectorizer`. Las funciones `vstack` y `csr_matrix` se utilizan en el código proporcionado para concatenar y convertir matrices dispersas.

## Dashboard

Para realizar la integración de lo desarrollado hasta el momento decidimos utilizar un dashboard en Power BI, ya que consideramos que es una herramienta clave para visualizar y presentar de manera efectiva las recomendaciones de mejoras generadas a partir del modelo. 
A continuación, enumeramos 3 fundamentos por los cuales elegimos esta herramienta y procedamos a describir el desarrollo de esta integración:

- Proporciona una interfaz intuitiva y visualmente atractiva para mostrar información relevante de manera clara y concisa.

- Permite a los usuarios acceder y comprender fácilmente las recomendaciones de mejoras generadas por el sistema, lo que facilita la toma de decisiones y la implementación de acciones correctivas.

- Incluye visualizaciones interactivas, tablas, gráficos y otros elementos visuales que ayuden a presentar los datos de manera comprensible y atractiva.

Establecidos los fundamentos procedemos a detallar el contenido estructurado en las distintas páginas del dashboard:

**Introducción:**

El dashboard que hemos desarrollado ofrece una visión integral de diversos aspectos clave relacionados con la satisfacción del cliente y la reputación del establecimiento. En esta documentación, presentaremos las distintas páginas que componen el dashboard, destacando los indicadores clave de rendimiento (KPIs) y sus cualidades relevantes. Nuestro objetivo es proporcionar una herramienta que permita evaluar y mejorar continuamente la satisfacción del cliente y la percepción general del establecimiento.

**Página de Inicio:**

La página de inicio es la página de presentación de nuestra consultora y muestra una vista general del dashboard. Aquí, se pueden apreciar las distintas páginas en las que se ha estructurado el dashboard, brindando una visión general de su contenido y organización.

**Satisfacción del Cliente:**

En esta página, se presenta el índice de satisfacción del cliente tanto de Google como de Yelp. Se muestra el promedio actual de calificaciones, el promedio objetivo deseado y la brecha existente para alcanzar dicho objetivo, que en este caso es un aumento del 20% en el promedio de estrellas. Este KPI refleja el nivel de satisfacción de los clientes en base al promedio de las calificaciones, lo que permite evaluar la situación del establecimiento y su evolución a lo largo del tiempo.

**Índice de Participación y Retroalimentación:**

En esta página, se pueden visualizar gráficos que muestran la evolución del índice de participación de los usuarios, es decir, la cantidad de reseñas que reciben los bares. Además, se presenta el siguiente KPI:

**KPI: Participación y Retroalimentación Anual**

Este KPI evalúa la imagen del establecimiento basándose en el puntaje de calificaciones recibidas. Se utiliza el porcentaje de calificaciones positivas y se comparan con el de las negativas para determinar el índice de reputación. El objetivo es aumentar el porcentaje de calificaciones positivas en al menos un 10%, lo cual indica una mejora en la percepción del establecimiento por parte de los clientes.
