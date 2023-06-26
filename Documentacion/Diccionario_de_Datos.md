# Diccionario de datos

## Google Maps

### **metadata_sitios.parquet**

Es un archivo parquet donde se dispone la metadata, que contiene información de los locales:

* 'name': string, nombre del bar,

```python
        'name': 'Walgreens Pharmacy',
```

* 'address': string, dirección del bar,

```python
        'address': 'Walgreens Pharmacy, 124 E North St, Kendallville, IN 46755', 
```

* 'gmap_id': string, identificador único de Google Maps para el bar,

```python
        'gmap_id': '0x881614ce7c13acbb:0x5c7b18bbf6ec4f7e', 
```

* 'description': string, descripción del bar,

```python
        'description': 'Department of the Walgreens chain providing prescription medications & other health-related items.', 
```

* 'latitude': float, coordenada de la latitud en Google Maps,

```python
        'latitude': 41.451859999999996,
```

* 'longitude': float, coordenada de la longitud en Google Maps,

```python
   	    'longitude': -85.2666757, 
```

* 'category': lista con las categorías a las que pertenece el bar,

```python
	    'category': ['Pharmacy'],
```

* 'avg_rating': float, puntuación promedio del bar,

```python
        'avg_rating': 4.2,
```

* 'num_of_reviews': entero, cantidad de reseñas que tiene el bar,

```python
        'num_of_reviews': 5,
```

* 'price': string, el rango de costo del bar,

```python
	    'price': '$$',
```

* 'hours': lista, horarios de apertura y cierre del bar,

```python
        'hours': [['Thursday', '8AM–1:30PM'], ['Friday', '8AM–1:30PM'], ['Saturday', '9AM–1:30PM'], ['Sunday', '10AM–1:30PM'], ['Monday', '8AM–1:30PM'], ['Tuesday', '8AM–1:30PM'], ['Wednesday', '8AM–1:30PM']],
```

* 'MISC': objeto, diccionario con características del bar o servicios adicionales,

```python
	    'MISC': {
   	    'Service options': ['Curbside pickup', 'Drive-through', 'In-store pickup', 'In-store shopping'], 
   	    'Health & safety': ['Mask required', 'Staff wear masks', 'Staff get temperature checks'], 
   	    'Accessibility': ['Wheelchair accessible entrance', 'Wheelchair accessible parking lot'], 
    	'Planning': ['Quick visit'], 
   	    'Payments': ['Checks', 'Debit cards']
                }
```

* 'state': string, estado del bar en el momento que fue tomado el dataset

```python
        'state': 'Closes soon ⋅ 1:30PM ⋅ Reopens 2PM', 
```

* 'relative_results': lista con resultados de busqueda relacionados al bar,

```python
        'relative_results': ['0x881614cd49e4fa33:0x2d507c24ff4f1c74', '0x8816145bf5141c89:0x535c1d605109f94b', '0x881614cda24cc591:0xca426e3a9b826432', '0x88162894d98b91ef:0xd139b34de70d3e03', '0x881615400b5e57f9:0xc56d17dbe420a67f'], 
```

* 'url': string, dirección web a Google Maps del bar

```python
        'url': 'https://www.google.com/maps/place//data=!4m2!3m1!1s0x881614ce7c13acbb:0x5c7b18bbf6ec4f7e?authuser=-1&hl=en&gl=us'
```

### **Carpeta review-estados**

Los archivos donde se disponibiliza las reviews de los usuarios (51 archivos .parquet con las reseñas de los bares, cada uno representa un estado de Estados Unidos) se conforman de la siguiente manera:

* 'user_id': string, id del usuario que hizo la reseña,

```python
        'user_id': '101463350189962023774',
```

* 'name': string, nombre del usuario,

```python
        'name': 'Jordan Adams',
```

* 'time': entero, hora en la que realizó la reseña,

```python
        'time': 1627750414677,
```

* 'rating': entero, puntaje que asignó al bar,

```python
        'rating': 5,
```

* 'text': string, reseña del usuario,

```python
        'text': 'Cool place, great people, awesome dentist!', 

```

* 'pics': objeto, foto subida por el usuario,

```python
        'pics': [
        {
        'url': ['https://lh5.googleusercontent.com/p/AF1QipNq2nZC5TH4_M7h5xRAd61hoTgvY1o9lozABguI=w150-h150-k-no-p']
        }
                ]
```

* 'resp': objeto, respuesta del encargado del bar, con el horario en el que fue posteada y el texto.

```python
        'resp': {
                'time': 1628455067818, 
                'text': 'Thank you for your five-star review! -Dr. Blake'
                }, 
```

* 'gmap_id': string, ID del bar.

```python
    'gmap_id': '0x87ec2394c2cd9d2d:0xd1119cfbee0da6f3'
```

## Dataset de Yelp!

### **business.parquet**

Contiene información del comercio, incluyendo localización, atributos y categorías.

* "business_id": string, id del bar, refiere al bar.

```python
    "business_id": "tnhfDv5Il8EaGSXZGiuQGg",
```

* "name": "Garaje": string, nombre del bar

```python
    "name": "Garaje",
```

"address": string, direccion completa del bar

```python
    "address": "475 3rd St",
```

* "city": string, ciudad

```python
    "city": "San Francisco",
```

* "state": string, codigo de 2 letras del Estado donde se ubica el bar

```python
    "state": "CA",
```

* "postal code": string, el codigo postal

```python
    "postal code": "94107",

```

* "latitude": float, coordenadas de latitud en Google Maps

```python
    "latitude": 37.7817529521,
```

* "longitude": float, coordenadas longitud en Google Maps

```python
    "longitude": -122.39612197,
```

* "stars": float, rating en estrellas, redondeado a 0 o 0.5

```python
    "stars": 4.5,
```

* "review_count": entero, numero de reseñas

```python
    "review_count": 1198,
```

* "is_open": entero, 0 si está cerrado, 1 si está abierto

```python
    "is_open": 1,
```

* "attributes": objeto, atributos del bar como valores. Algunos valores de atributos también pueden ser objetos.

```python
    "attributes": {
                "RestaurantsTakeOut": true,
                "BusinessParking": {
                "garage": false,
                "street": true,
                "validated": false,
                "lot": false,
                "valet": false
                                },
                },
```

* "categories": lista de categorias de los bars

```python
    "categories": [
                    "Mexican",
                    "Burgers",
                    "Gastropubs"
                    ],
```

* "hours": objeto, de dia a hora, las horas son en 24hr

```python
    "hours": {
                "Monday": "10:00-21:00",
                "Tuesday": "10:00-21:00",
                "Friday": "10:00-21:00",
                "Wednesday": "10:00-21:00",
                "Thursday": "10:00-21:00",
                "Sunday": "11:00-18:00",
                "Saturday": "10:00-21:00"
                },
```

### **review.parquet**

Contiene las reseñas completas, incluyendo el user_id que escribió el review y el business_id por el cual se escribe la reseña

* "review_id": string, id de reseña

```python
    "review_id": "zdSx_SD6obEhz9VrW9uAWA",

```

* "user_id": string, id único de usuario, refiere al usuario en user.parquet

```python
    "user_id": "Ha3iJu77CxlrFm-vQRs_8g",
```

* "business_id": string, id del bar, refiere al bar en business.parquet

```python
    "business_id": "tnhfDv5Il8EaGSXZGiuQGg",
```

* "stars": entero, puntaje que deja el usuario en estrellas de 1 al 5

```python
    "stars": 4,
```

* "date": string, fecha formato YYYY-MM-DD,

```python
    "date": "2016-03-09",
```

* "text": string, la reseña en inglés

```python
    "text": "Great place to hang out after work: the prices are decent, and the ambience is fun. It's a bit loud, but very lively. The staff is friendly, and the food is good. They have a good selection of drinks.",
```

* "useful": entero, números de votos como reseña útil

```python
    "useful": 0,
```

* "funny": entero, número de votos como reseña graciosa

```python
    "funny": 0,
```

* "cool": entero, número de votos como reseña cool.

```python
    "cool": 0
```

### **user.parquet**

Data del usuario incluyendo referencias a otros usuarios amigos y a toda la metadata asociada al usuario.

* "user_id": string, id de usuario que refiere al usuario

```python
    "user_id": "Ha3iJu77CxlrFm-vQRs_8g",
```

* "name": string, nombre del usuario

```python
    "name": "Sebastien",
```

*"review_count": entero, numero de reseñas escritas

```python
    "review_count": 56,
```

* "yelping_since": string, fecha de creacion del usuario en Yelp en formato YYYY-MM-DD

```python
    "yelping_since": "2011-01-01",
```

* "friends": lista con los id de usuarios que son amigos de ese usuario

```python
    "friends": [
                "wqoXYLWmpkEH0YvTmHBsJQ",
                "KUXLLiJGrjtSsapmxmpvTA",
                "6e9rJKQC3n0RSKyHLViL-Q"
                ],

```

* "useful": entero, número de votos marcados como útiles por el usuario

```python
    "useful": 21,
```

* "funny": entero, número de votos marcados como graciosos por el usuario

```python
    "funny": 88,
```

* "cool": entero, número de votos marcados como cool por el usuario

```python
    "cool": 15,
```

* "fans": entero, número de fans que tiene el usuario

```python
    "fans": 1032,
```

* "elite": lista de enteros, años en los que el usuario fue miembro elite

```python
    "elite": [
                2012,
                2013
            ],

```

* "average_stars": float, promedio del valor de las reseñas

```python
    "average_stars": 4.31,
```

* "compliment_hot": entero, total de cumplidos 'hot' recibidos por el usuario

```python
    "compliment_hot": 339,
```

* "compliment_more": entero, total de cumplidos varios recibidos por el usuario

```python
    "compliment_more": 668,
```

* "compliment_profile": entero, total de cumplidos por el perfil recibidos por el usuario

```python
    "compliment_profile": 42,
```

* "compliment_cute": entero, total de cumplidos 'cute' recibidos por el usuario

```python
    "compliment_cute": 62,
```

* "compliment_list": entero, total de listas de cumplidos recibidos por el usuario

```python
    "compliment_list": 37,
```

* "compliment_note": entero, total de cumplidos recibidos como notas por el usuario

```python
    "compliment_note": 356,
```

* "compliment_plain": entero, total de cumplidos planos recibidos por el usuario

```python
    "compliment_plain": 68,
```

* "compliment_cool": entero, total de cumplidos 'cool' recibidos por el usuario

```python
    "compliment_cool": 91,
```

* "compliment_funny": entero, total de cumplidos graciosos recibidos por el usuario

```python
    "compliment_funny": 99,
```

* "compliment_writer": entero, número de complidos escritos recibidos por el usuario

```python
    "compliment_writer": 95,
```

* "compliment_photos": entero, número de cumplidos en foto recibidos por el usuario

```python
    "compliment_photos": 50
```

### **checkin.parquet**

Registros en el bar.

* "business_id": string, id del bar que se refiere al bar en business.parquet

```python
    "business_id": "tnhfDv5Il8EaGSXZGiuQGg"
```

* "date": string que es una lista de fechas separados por coma, en formato YYYY-MM-DD HH:MM:SS

```python
    "date": "2016-04-26 19:49:16, 2016-08-30 18:36:57, 2016-10-15 02:45:18, 2016-11-18 01:54:50, 2017-04-20 18:39:06, 2017-05-03 17:58:02"
```

### **tip.parquet**

Tips (consejos) escritos por el usuario. Los tips son más cortas que las reseñas y tienden a dar sugerencias rápidas.

* "text": string, texto del tip

```python
    "text": "Secret menu - fried chicken sando is da bombbbbbb Their zapatos are good too.",
```

* "date": string, fecha cuando se escribio el tip YYYY-MM-DD

```python
    "date": "2013-09-20",
```

* "compliment_count": entero, cuantos cumplidos totales tiene

```python
    "compliment_count": 172,
```

* "business_id": string,, id del bar que se refiere al bar en business.parquet

```python
    "business_id": "tnhfDv5Il8EaGSXZGiuQGg",
```

* "user_id": string, id de usuario, que se refieren al usuario en user.parquet

```python
    "user_id": "49JhAJh8vSQ-vM4Aourl0g"
```
