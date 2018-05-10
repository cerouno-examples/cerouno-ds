# Airflow para CeroUno
 Una guía para conocer los aspectos básicos de Airflow y crear nuestro primer datapipeline.

Airflow es una plataforma para crear, asignar horarios de ejecución y monitorear pipelines de datos.

![](https://airflow.apache.org/_images/airflow.gif)

Creado por AirBnB, publicado como Open Source y transferido a la Apache Software Foundation como proyecto de primer nivel. Mantiene los siguientes principios:
- Dinámico: Configuración como Código
- Extensible: Facilidad de definir componentes a la medida (operadores y ejecutores) de nuestra organización.
- Elegante: Pipelines explicitos.
- Escalable

## Algunos conceptos iniciales

- DAGs: Directed Acyclic Graph. Es una colección de todas las tareas que quieres correr, organizada en una forma de percebir sus relaciones y dependencias.
- Scope: Ámbito de ejecución (similar al de Python). Airflow cargará cualquier objeto `DAG` de los DAGfiles que encuentre a su paso. Pero solo entrará en contexto el `DAG` que sea global.
- Default Arguments: Diccionario de `default_args` que se pasa a un DAG y aplicará en cualquiera de los operadores. Esto permite aplicar parámetros comunes a muchos operadores sin escribirlos de manera repetitiva.
- Context Manager: DAGs que asignan nuevos operadores al mismo DAG u otro. Algo así como la herencia en OOP. Introducido en la versión 1.8
- Operators: La descripción de las tareas. Mientras que los DAGs describen como correr un Workflow, los `Operators` determinan que se hace.
Hay distintos tipos de operadores:
  - `BashOperator` - executes a bash command
  - `PythonOperator` - calls an arbitrary Python function
  - `EmailOperator` - sends an email
  - `HTTPOperator` - sends an HTTP request
  - `MySqlOperator`, `SqliteOperator`, `PostgresOperator`, `MsSqlOperator`, `OracleOperator`, `JdbcOperator`, etc. - executes a SQL command
  - `Sensor` - waits for a certain time, file, database row, S3 key, etc…
- DAG Assigment & Bitshift Composition: Asignación de dependencias entre operadores.  

### DAG
![A topological ordering of a directed acyclic graph: every edge goes from earlier in the ordering (upper left) to later in the ordering (lower right). A directed graph is acyclic if and only if it has a topological ordering.](https://upload.wikimedia.org/wikipedia/commons/f/f8/Transitive_Closure.svg)
> A topological ordering of a directed acyclic graph: every edge goes from earlier in the ordering (upper left) to later in the ordering (lower right). A directed graph is acyclic if and only if it has a topological ordering.

## Arquitectura de Airflow
![Airflow's General Architecture](https://cdn-images-1.medium.com/max/1000/1*czjWSmrjiRY1goA0emv7IA.png)

## 1. Setup

### Instalación de Airflow
La forma más sencilla de instalar la plataforma es usando  `pip`: `pip install apache-airflow`. Usando de forma separada un virtualenv para este framework.

Para la clase de hoy, usaremos el ambiente virtual definido en el archivo `environment.yml` de Conda.

* Creando el ambiente virtual:
```bash
$ conda env create -f environment.yml
```
* Activación
```bash
$ source activate airflow-cerouno
```
De igual manera, nos podemos hacer cargo de las dependencias e instalar Airflow así:
```bash
$ pip install apache-airflow
```
### Instanciando Airflow

Antes de usar Airflow, tenemos que inicializar su base de datos.
Esta DB almacena información acerca de los Workflows y sus datos históricos, conexiones a fuentes de datos externas, usuarios, etc.
Una vez que la DB está configurada, podemos usar la UI de Airflow para administrar los pipelines.

La DB default, es SQLite, que funciona bien para esta clase.
En un ambiente de producción, lo ideal sería usar una DB como PostgreSQL.


**AIRFLOW_HOME**
Airflow usa la variable de ambiente `AIRFLOW_HOME` para elegir el directorio donde almacena sus configuraciones y DB. De no definirse, usará `~/airflow/`.
**Para hoy, si usamos la ubicación por default, está bien.**

* Si queremos cambiar el valor, elegimos el folder deseado y ejecutamos:
```bash
$ export AIRFLOW_HOME="$(pwd)"
```
* Para crear la DB:
```bash
$ airflow initdb
```

Después iniciamos el servidor web y vamos a [localhost:8080](http://localhost:8080/) para ver la UI:
```bash
$ airflow webserver --port 8080
```

Y se debe ver algo similar a esto:
![](https://airflow.incubator.apache.org/_images/dags.png)

Con el servidor web corriendo, abrimos una nueva terminal de comandos, nos situamos en el folder de Airflow y volvemos a activar el virtualenv:

```{bash}
$ source activate airflow-cerouno
# En caso de AIRFLOW_HOME
$ export AIRFLOW_HOME="$(pwd)"
```

Ejecutamos uno de los ejemplos:
```{bash}
$ airflow run example_bash_operator runme_0 2018-05-01
```
Y revisamos en la Web UI que ha funcionado: Browse -> Task Instances.


#### Tips

## 2. Workflows

Crearemos un worflow especificando accciones en forma de DAG en Python.
Las tareas de un Workflow/Pipeline hacen un grafo, el grafo es dirigido por que las tareas están ordenadas en secuencia; y no queremos atascarnos en un loop infinito, por eso el grafo tiene que ser acíclico.

Así se ve un DAG de ejemplo:

![Example DAG](https://airflow.incubator.apache.org/_images/subdag_before.png)

El primer DAG que crearemos es más sencillo. Consistirá en las siguientes tareas:

* Imprimir un mensaje (print `'hello'`)
* Esperar cinco segundos
* Imprimir otro mensaje (print `'hello'`)
* Y tendrá un plan de ejecución diario.


### DAG File
Vamos nuestro folder de Airflow y encontraremos el subfolder `dags/`.
Crearemos un archivo de python para contener nuestro DAG. El archivo será: `airflow_cerouno.py`.

Primero vamos a configurar todas las propiedades que son compartidas por nuestras tareas.
Recordemos que podemos definir parámetros por defecto en un diccionario.

Agregamos el siguiente bloque a `airflow_cerouno.py` para especificar propietario, tiempo de inicio e intentos de ejecución como configuraciones compartidas en las tareas.

### Default Arguments

```python
import datetime as dt

default_args = {
    'owner': 'Ricky Rick',
    'start_date': dt.datetime(2018, 5, 1),
    'retries': 1,
    'retry_delay': dt.timedelta(minutes=5),
}
```
Estas configuraciones le indican a Airflow que este Workflow el dueño es `'Ricky Rick'`, que es un worflow válido desde el 1ro de mayo de 2018, y está permitido volver a intentar su ejecución una vez en caso de fallar (con una espera de cinco minutos).

### Creación del DAG

Ahora creamos un objeto DAG para nuestras tareas:


```python
from airflow import DAG

with DAG('airflow_cerouno_v01',
         default_args=default_args,
         schedule_interval='0 * * * *',
         ) as dag:
```
Con `schedule_interval='0 0 * * *'` especificamos una ejecución cada hora 0; el DAG correrá cada día a las 00:00.
Para decifrar la expresión del Cron Schedule, consulta [crontab.guru](https://crontab.guru/#0_*_*_*_*). Cron también permite expresiones como `'@daily'` y `'@hourly'`

#### Notas sobre nuestro DAG:

* Estamos usando [context manager](https://jeffknupp.com/blog/2016/03/07/python-with-context-managers/) para crear el DAG. Todas las tareas deben especificarse como parte de este DAG, o se tendrá que indicar e instanciar de forma manual.

* Airflow generará las ejecuciones desde `start_date` correspondientes a  `schedule_interval`.
Una vez que el DAG está activo, Airflow verifica que se tenga el cumplimiento desde `start_date`. Cualquier ejecución faltante se programará de forma automática.
**¿Qué pasará si inicializamos el 2017-05-13 un DAG con `start_date` de 2017-05-01 y un `schedule_interval` diario?**

* Una ejecución inicia **después** de que estaba asignado en la siguiente forma:
El worflow diario para 2017-06-02 corre después de 2016-06-02 23:59 y el worflow a cada hora para 2017-07-03 01:00 inicia después de 2016-07-03 01:59.
  * El momento en que el workflow inició se llama `execution_date`.
* Desde el punto de vista en ETL funciona así: solo puedes procesar los datos diarios el día después de lo ocurrido.

* Airflow guarda en su DB todas las fechas asignadas para un DAG registrado, por lo tanto se sugiere no cambiar los parámetros  `start_date` y `schedule_interval` de un DAG.
Es mejor versionar nuestro DAG (por ejemplo  `airflow_cerouno_v02`) y evitar problemas de scheduling o tareas con la web UI/CLI.

* Timezone: UTC


### Creación de tareas

Las tareas se representan por operadores que realizan una acción, transfieren datos o evaluan si algo ha sido hecho.
Algunos ejemplos son: ejecutar un script de Bash o llamar a una función de Python, transferir  tablas entre DBs, o copiar archivos entre servidores. Y los sensores revisan  si un archivo existe o los datos fueron agregados a una DB.

Nuestro workflow será de tres tareas:
- Mostrar la cadena 'hello'
- Esperar cinco segundos
- Imprimir 'world'.

Los primeros dos con el operador `BashOperator` y el tercero con `PythonOperator`.

Cada operador tiene un ID único de tarea y algo por hacer:

```python
    from airflow.operators.bash_operator import BashOperator
    from airflow.operators.python_operator import PythonOperator




    def print_world():
        print('world')

    print_hello = BashOperator(task_id='print_hello',
                               bash_command='echo "hello"')
    sleep = BashOperator(task_id='sleep',
                         bash_command='sleep 5')
    print_world = PythonOperator(task_id='print_world',
                                 python_callable=print_world)
```
**¿Qué notamos en `bash_command` y `python_callable`?**


Las dependencias entre tareas pueden ser ascendentes y descendentes (upstream vs downstream). Las encadenamos de forma que `sleep` correrá después de `print_hello` y seguirá `print_world`; `print_hello` -> `sleep` -> `print_world`:
```python
print_hello >> sleep >> print_world
```
Esto es usando [Bitshift Composition](https://airflow.apache.org/concepts.html#bitshift-composition), similar a [bitwise operators de Python](https://wiki.python.org/moin/BitwiseOperators).



Una vez que acomodamos el código del DAG, se verá similar a este:
```python
import datetime as dt

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator


def print_world():
    print('world')


default_args = {
    'owner': 'me',
    'start_date': dt.datetime(2018, 5, 1),
    'retries': 1,
    'retry_delay': dt.timedelta(minutes=5),
}


with DAG('airflow_cerouno_v01',
         default_args=default_args,
         schedule_interval='0 * * * *',
         ) as dag:

    print_hello = BashOperator(task_id='print_hello',
                               bash_command='echo "hello"')
    sleep = BashOperator(task_id='sleep',
                         bash_command='sleep 5')
    print_world = PythonOperator(task_id='print_world',
                                 python_callable=print_world)


print_hello >> sleep >> print_world
```


### Testing

Revisamos que el DAGfile contiene código válido de Python:
```{bash}
$ python airflow_tutorial.py
```

Podemos probar una tarea con una fecha supuesta  (parámetro  `execution_date` y usando el comando `airflow test`:

```bash
$ airflow test airflow_cerouno_v01 print_world 2018-01-01
```

Esto corre de manera local como si fuera 2018-01-01, ignorando otras tareas y sin comunicarse con la DB.

### Graduación en la escuela del ETL: Activando nuestro DAG

Ya sabes como funciona tu DAG para Airflow, es hora de ejecutarlo de modo automático!
Para hacerlo, necesitamos tener el servicio de Scheduler encendido.
**¿Para qué funciona este servicio?**
Se encarga de monitorear todas las tareas y todos los DAGs, cuando una tarea se ha cumplido acciona las nuevas instancias de tarea que están marcadas como dependencia.

Al igual que iniamos el servidor web para la UI, lo haremos para el Scheduler. Abrimos una nueva terminal de comandos, activamos el virtualenv y nos dirigimos al directorio de Airflow (por defecto en ~/airflow). Y si usamos la variable AIRFLOW_HOME, la volvemos a activar.

Ejecutamos:

```bash
$ airflow scheduler
```

Listo. Esperamos un instante y nuestro DAG está en la UI. En la lista, junto al nombre del DAG (`airflow_cerouno_v01`) tenemos un switch de encendido/apagado.

Encendemos nuestro DAG y esperamos que el Scheduler propague los cambios para correr nuestro DAG.

### Tips

* La ejecución continua de un DAG debe dar siempre el mismo resultado
* Es preferible usar la notación propia de Cron para `schedule_interval` en vz de  `@daily` y `@hourly`
## 3. Ejercicios

Ahora conocemos lo básico de Airflow, creación de DAGs y su puesta en marcha. Te toca:

* Cambiar el intervalo a cada 30 minutos
* Usar un sensor para añadir un retraso de 5 minutos antes de iniciar las tareas
* [Consultar la documentación de Templating](https://airflow.incubator.apache.org/tutorial.html#templating-with-jinja) e implementarlo con `BashOperator`. Mostrar en pantalla  `execution_date` en vez de `hello`
* [Implementar templating](https://airflow.incubator.apache.org/code.html#airflow.operators.PythonOperator) para `PythonOperator`: Imprimir en pantalla `execution_date` en la función `print_world()`
## 4. Recursos
* [Airflow documentation](https://airflow.apache.org/index.html)
* [ETL best practices with Airflow](https://gtoonstra.github.io/etl-with-airflow/)
* [Airflow: Tips, Tricks, and Pitfalls](https://medium.com/handy-tech/airflow-tips-tricks-and-pitfalls-9ba53fba14eb)
