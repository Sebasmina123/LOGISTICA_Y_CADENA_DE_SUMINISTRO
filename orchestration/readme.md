### Orquestación del Pipeline.

#### El pipeline se creó de manera manual en Microsoft Fabric

- iniciando desde el notebook de 00_ingesta_datos, donde se hizo la conversion de los archivos en la carpeta Files a las delta tables.
- se hizo una actividad de Wait configurada con 15 segundos para que fabric pueda terminar la sesión del notebook previo y no excediera la capacidad
- Prosiguió el notebook de 01_bronze, donde se agrego meta data y particiones a las delta tables y pasaron al schema de bronze
- Nuevamente una actividad Wait con la misma configuración y propósito que la anterior.
- inicia el 02_silver donde se hace proceso de detección y limpieza de duplicados, rellenado de columnas con nulos si era la mejor opción, y posterior guardado en el schema de silver
- tercer actividad wait.
- Prosigue la ultima capa de medallion, el 03_gold, donde se crean las dimensiones y las tablas de hechos según lo necesario y con los datos que dejó silver.
- y por ultimo, una actividad de mensajería mediante un chat grupal de Teams con un reporte básico del pipeline.

