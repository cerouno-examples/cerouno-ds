# Actividades

## Introducción a Docker


- [Docker Birthday #3 - Intro to Docker Slides
](https://www.slideshare.net/Docker/docker-birthday-3-intro-to-docker-slides)
- [Docker Bday #5, SF Edition: Introduction to Docker](https://www.slideshare.net/Docker/docker-bday-5-sf-edition-introduction-to-docker)
- [Docker 101: Introduction to Docker
](https://es.slideshare.net/Docker/docker-101-introduction-to-docker)

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

Hacerlo primero en Pandas. Luego Bash+Pandas:

- Cambiar la descarga del archivo con un operador de Bash o HTTP en vez de Pandas


### Quandl.

Crear un DAG que descargue información de Quandl, y obtenga el promedio entre High & Low del día anterior.
- Crear una cuenta en Quandl y generar un Token de API
- Seleccionar cualquier símbolo de Stock en NASDAQ
- Descargar el DAG
- Procesar
- Desplegar en un Log el resultado del promedio y la fecha
- Programarlo para ejecutarse de lun-vie una hora después del cierre del mercado (16:00)
