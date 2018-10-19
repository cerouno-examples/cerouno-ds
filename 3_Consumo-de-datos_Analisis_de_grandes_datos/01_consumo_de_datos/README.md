
## Python
Desde Anaconda, crear un nuevo virtualenv usando el archivo YAML de este repo. O manualmente con los paquetes:
- Python=3
- Jupyter
- Pandas
- Requests
- Scrapy
- sqlalchemy
- psycopg2

PIP:
- bs4




## Docker:

PostgreSQL

`docker pull postgres:9`



## Cliente para PostgreSQL
Descargar e instalar DBeaver Community Edition:
- ![Dbveaber -  Universal Database Tool ](https://dbeaver.io/)


## El instructor requiere restaurar la DB DVDRENTAL a las instancias de los asistentes. Es necesario tener instalado el comando `pg_restore` de PostgreSQL 9.
- Descargar el backup: http://www.postgresqltutorial.com/wp-content/uploads/2017/10/dvdrental.zip
- Hacer la descompresión del contenedor ZIP y observar el path del directorio.
- Por cada dirección IP de los asistentes ejecutar:
```bash
pg_restore --host <DIRECCION_IP> --port 5432 --username "postgres" --dbname "dvdrental" --no-password  --format directory --verbose "/PATH_HACIA_/dvdrental"\n
```
