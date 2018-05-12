# Actividades

## Introducción a Docker

<iframe src="//www.slideshare.net/slideshow/embed_code/key/b7J4ckRJtNCXhA" width="595" height="485" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen> </iframe> <div style="margin-bottom:5px"> <strong> <a href="//www.slideshare.net/Docker/docker-birthday-3-intro-to-docker-slides" title="Docker Birthday #3 - Intro to Docker Slides" target="_blank">Docker Birthday #3 - Intro to Docker Slides</a> </strong> de <strong><a href="https://www.slideshare.net/Docker" target="_blank">Docker, Inc.</a></strong> </div>


<iframe src="//www.slideshare.net/slideshow/embed_code/key/bKB1BkitzwwJd" width="595" height="485" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen> </iframe> <div style="margin-bottom:5px"> <strong> <a href="//www.slideshare.net/Docker/docker-bday-5-sf-edition-introduction-to-docker" title="Docker Bday #5, SF Edition: Introduction to Docker" target="_blank">Docker Bday #5, SF Edition: Introduction to Docker</a> </strong> de <strong><a href="https://www.slideshare.net/Docker" target="_blank">Docker, Inc.</a></strong> </div>

## Pasos para crear un ambiente:
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

- Primero en Pandas
- Luego Bash+Pandas
    - Cambiar la descarga del archivo con un operador de Bash o HTTP en vez de Pandas


### Quandl.

Crear un DAG que descargue información de Quandl, y obtenga el promedio entre High & Low del día anterior.
    - Crear una cuenta en Quandl y generar un Token de API
    - Seleccionar cualquier símbolo de Stock en NASDAQ
    - Descargar el DAG
    - Procesar
    - Desplegar en un Log el resultado del promedio y la fecha
