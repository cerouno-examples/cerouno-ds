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
- Context Manager: DAGs que asignan nuevos operadores al mismo DAG u otro. Algo así como la herencia en OOP.
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
## 2. Workflows
## 3. Ejercicios
## 4. Recursos
* [Airflow documentation](https://airflow.apache.org/index.html)
* [ETL best practices with Airflow](https://gtoonstra.github.io/etl-with-airflow/)
* [Airflow: Tips, Tricks, and Pitfalls](https://medium.com/handy-tech/airflow-tips-tricks-and-pitfalls-9ba53fba14eb)
