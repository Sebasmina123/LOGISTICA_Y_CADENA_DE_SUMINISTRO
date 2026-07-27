## Aqui se encuentra los archivos del codigo generador de datos Dummy

Aqui se guarda los archivos tanto del generador hecho en python, como el DDL de la base de datos generado con el software de oracle sql developer data modeler.

## Para usar el generador no es necesario tener la carpeta "db". El archivo de esa carpeta (un .sql), se puede ejecutar en el oracle sql developer para comprobar la veracidad de la base de datos. 

Se ha tenido mucha dificultad en la generación de los datos, principalmente por las capacidades del computador. Asi que en el momento de usar el generador, puede que demore un tiempo la generación de los datos minimos pedidos en el caso de logistica y envios (+2M).

## Para ejecutar el generador se recomienda: 
- 1. debe de descargar el archivo
  2. dejarlo en una carpeta
  3. En un entorno virtual, descargar las liberias requeridas en requeriments.txt
  4. llamar al archivo en la terminal como "python src/data_generation.py" 
