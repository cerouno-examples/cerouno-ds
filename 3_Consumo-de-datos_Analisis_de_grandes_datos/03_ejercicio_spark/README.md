# Big Data: Ejercicio con Spark Streaming.
19/mayo/2018


## Indicaciones para la primera parte

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
Problemas con Windows: * https://medium.com/@neil.avery_68603/running-docker-from-windows-cmd-prompt-6540daebedad#.lae8p2oiz
* ??

Abrimos con nuestro navegador la URL que nos menciona la consola.

### En el contenedor de PySpark instalamos netcat
Usamos una nueva "terminal" de Jupyter

```bash
$ sudo su
# apt-get update && apt-get install netcat
# su jovyan
$ nc -lkv 127.0.0.1 -p 9999
```

### Abrimos el notebook **Spark_Streaming.ipynb**


## Segunda parte de hoy
### Crear una cuenta de Twiter y obtener las llaves de  Streaming API:
- Registramos una App a nuestro nombre: https://apps.twitter.com/
- Las llaves están en **Keys and Access Tokens** de nuestra App
    - CONSUMER KEY
    - CONSUMER SECRET
    - ACCESS TOKEN
    - ACCESS SECRET

### Instalar Tweepy
```bash
/opt/conda/bin/pip install tweepy
```

### Completar el siguiente código de python

Para esto, necesitamos investigar acerca de biblioteca `socket` de Python: [`socket` — Low-level networking interface](https://docs.python.org/3.6/library/socket.html)

`read.py`
```python
import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import socket
import json

# Crear nueva app aqui: https://apps.twitter.com/

consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''

class TweetsListener(StreamListener):

  def __init__(self, csocket):
      self.client_socket = csocket

  def on_data(self, data):
      try:
          msg = json.loads( data )
          print( msg['text'].encode('utf-8') )
          self.client_socket.send( msg['text'].encode('utf-8') )
          return True
      except BaseException as e:
          print("Error on_data: %s" % str(e))
      return True

  def on_error(self, status):
      print(status)
      return True

def sendData(c_socket):
  auth = OAuthHandler(consumer_key, consumer_secret)
  auth.set_access_token(access_token, access_secret)

  twitter_stream = Stream(auth, TweetsListener(c_socket))
  # Sustituir la cadena '####' por cualquier otra palabra
  twitter_stream.filter(track=['####'])

if __name__ == "__main__":
           # Create a socket object
# Crear un objeto socket
# Configurar el nombre de nuestro equipo/host
# Reservar ante el SO el puerto para el servicio
# Enlazar al puerto

# Imprimir en que puerto estamos escuchando

# Esperar por una conexión de cliente
# Establecer una conexión con el cliente


#

  print( "Received request from: " + str( addr ) )

  sendData( c )
```

### Cuando sea requerido, ejecutar *read.py*

```bash
/opt/conda/bin/python read.py
```
