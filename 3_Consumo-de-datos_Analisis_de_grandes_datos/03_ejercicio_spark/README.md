# Big Data: Ejercicio con Spark Streaming.
19/mayo/2018


## Indicaciones

### Iniciar Docker
### Eliminar todos los contenedores creados en clases anteriores
### Copiar los ejemplos para hoy:
- https://github.com/cerouno-examples/cerouno-ds
- https://github.com/israelzuniga/cerouno-ds-israelzuniga

### Crear un nuevo contenedor de PySpark:
Primero, nos situamos en el directorio donde tengamos nuestro código para hoy.

```bash
docker run -e GRANT_SUDO=yes --user root -p 8888:8888 -p 4040:4040 -v $PWD:/home/jovyan/work jupyter/pyspark-notebook start-notebook.sh
```
Abrimos con nuestro navegador la URL que nos menciona la consola.

### En el contenedor de PySpark instalamos netcat
```bash
$ sudo su
# apt-get update && apt-get install netcat
# su jovyan
$ nc -lkv 127.0.0.1 -p 9999
```
