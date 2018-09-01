# Actividades del sábado

## Introducción a Docker


- [Docker Birthday #3 - Intro to Docker Slides
](https://www.slideshare.net/Docker/docker-birthday-3-intro-to-docker-slides)
- [Docker Bday #5, SF Edition: Introduction to Docker](https://www.slideshare.net/Docker/docker-bday-5-sf-edition-introduction-to-docker)
- [Docker 101: Introduction to Docker
](https://es.slideshare.net/Docker/docker-101-introduction-to-docker)

## Pasos para crear un ambiente:

### Opción 1:
Obtener la imagen base de DockerHub
```bash
docker pull puckel/docker-airflow
```

### Opción 2:
Construimos la imagen base:

```bash
docker build --rm -t puckel/docker-airflow .
```


Si tenemos más de 4GB de RAM y un procesador arriba de Core i5 o equivalente:

```bash
$ docker-compose -f docker-compose-CeleryExecutor.yml up -d
```

En caso contrario:

```bash
docker-compose -f docker-compose-LocalExecutor.yml up -d
```
O aún más compacto:

```bash
docker run -d -p 8080:8080 puckel/docker-airflow
```



### Extras:
- Cargar ejemplos es mediante la variable de ambiente `LOAD_EX=n` al momento de crear la infraestructura

    docker run -d -p 8080:8080 -e LOAD_EX=y puckel/docker-airflow


## Ejercicios:
- Iniciar un ambiente de Airflow con Docker
    - Local o distribuido.
- Colocar nuestro DAG de la clase anterior en la plataforma de Airflow y probar su ejecución
- Realizar los ejercicios para este DAG

### Ejercicio ETL:

Crear un DAG que realice lo siguiente:

1. Descargar un CSV: `https://archive.ics.uci.edu/ml/machine-learning-databases/00382/c2k_data_comma.csv`
1. Eliminar registros NaN
1. Reemplace caracteres "extraños"
1. Convierta el tipo de dato de todas las columnas a float64
1. Guarde el DataFrame resultante

Hacerlo primero en Pandas. Luego Bash+Pandas:

- Cambiar la descarga del archivo con un operador de Bash o HTTP en vez de Pandas

### HackerNews

Crear un DAG que consulte la API de HN https://news.ycombinator.com/ cada media hora, obtenga las 500 nuevas noticias para representarlas en una nueva API.

Documentación de acceso a la API: https://github.com/HackerNews/API

- Consultar la API con una query
- Procesar
- Obtener los títulos y la liga a la discusión en HN
- Presentar los resultados en una API nueva (flask_restful)

Bonus points:

- Usando NLP, analizar con la técnica análisis de sentimiento (sentiment-analysis). TextBlob, NLTK, SpaCy, TensorFlow, etc.
- Representar el título de la noticia con su score de sentimiento

Extra points:
- Sumarizar las noticias por sentimiento


### Quandl.

Crear un DAG que descargue información de Quandl, y obtenga el promedio entre High & Low del día anterior.
- Crear una cuenta en Quandl y generar un Token de API
- Seleccionar cualquier símbolo de Stock en NASDAQ
- Consultar la API con una query
- Procesar
- Desplegar en un Log el resultado del promedio y la fecha
- Programarlo para ejecutarse de lun-vie una hora después del cierre del mercado (16:00)
