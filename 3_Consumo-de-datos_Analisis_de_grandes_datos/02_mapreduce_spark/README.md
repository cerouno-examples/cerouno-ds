- Iniciar Docker
- Iniciar la consola de comandos, y situarse en la ubicación donde descargaron el repositorio de la clase
- 



##

docker run -d -e GRANT_SUDO=yes \
   --user root \
   -p 4040:4040 \
   -p 4041:4041 \
   -p 4042:4042 \
   -p 4043:4043 \
   -p 8888:8888 \
   -p 18080:18080 \
   -v $PWD:/home/jovyan/work \
   jupyter/pyspark-notebook start-notebook.sh
