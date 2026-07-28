## Aqui se encuentra los archivos del codigo generador de datos Dummy

Aqui se guarda los archivos tanto del generador hecho en python, como el DDL de la base de datos generado con el software de oracle sql developer data modeler.
Se interpretó que de los archivos exportados aqui, se subirían a la plataforma de cloud (en este caso, fabric) para usar el SQL endpoint y poder hacer la ingesta de datos.

## Para usar el generador no es necesario tener la carpeta "db". El archivo de esa carpeta (un .sql), se puede ejecutar en el oracle sql developer para comprobar la veracidad de la base de datos. 

Se ha tenido mucha dificultad en la generación de los datos, principalmente por las capacidades del computador. Asi que en el momento de usar el generador, puede que demore un tiempo la generación de los datos minimos pedidos en el caso de logistica y envios (+2M).

## Para ejecutar el generador se recomienda: 
- debe de tener los archivos y carpetas en una sola carpeta
- En un entorno virtual, descargar las liberias requeridas en requeriments.txt
- llamar al archivo en la terminal como "python src/data_generation.py" 
