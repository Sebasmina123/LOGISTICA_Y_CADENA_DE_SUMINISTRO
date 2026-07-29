# changelog

## fecha: 28/07/2026.
## Autor: Juan Sebastian Mina Quintero.

se añaden las versiones más recientes de los notebooks del pipeliney se añadieron evidencias de la fase 3.

## Added:
- docs/evidencias/fase 3
- capturas de pantallas con pruebas de la fase 3

## Changed
- 00_ingesta_datos.ipynb
- 01_bronze.ipynb
- 02_silver.ipynb
- 03_gold.ipynb


## fecha: 28/07/2026.
## Autor: Juan Sebastian Mina Quintero.
Se creó la carpeta de /infra para almacenar todos los archivos de el código de Iac para  Microsoft fabric. Y también se creó la carpeta /pipelines para guardar los notebooks con programación de las capas del pipeline.

## Added:
- carpeta /pipelines
- archivo 00_ingesta_datos.ipynb
- archivo 01_bronze.ipynb
- archivo 02_silver.ipynb
- archivo 03_gold.ipynb
- carpeta /infra
- README.md
- backend.tf
- dev.tfvars
- dev.tfvars
- main.tf
- notebooks.tf
- outputs.tf
- pipeline.tf
- prod.tfvars
- providers.tf
- terraform.tfvars
- variables.tf
- versions.tf

## fecha: 27/07/2026.
## Autor: Juan Sebastian Mina Quintero.
Se hizo una gran actualización, eliminación y agregación en los archivos de data-generation; se actualizó el diagrama relational_1.; se creó una carpeta para guardar las capturas de pantalla de la fase uno.

## Added:
- carpeta /data-generation/exports
- archivos ejemplares de  las exportaciones parquet y CSV en exports
- config.json
- exportar(): función para exportación en data_generation.py
- algoritmos para 3 anomalías controladas
- carpeta /docs/evidencias/fase1 creada.


## Changed:
- fecha_aleatoria(): ahora está parametrizada con las configuraciones
- hora_aleatoria(): genera horas randoms desde las 8am hasta las 9pm, estableciendo condiciones para las horas picos y con descanso entre 12-2pm.
- comentario_realista(): genera comentarios con un 5% de nulos.
- requeriments.txt fue actualizada.
  
## Removed
- archivo inserciones.py fue eliminado porque ya no era relevante.

## Fixed:
- nombre_zona(): se corrigió la condición de comparación para retornar el nombre de la zona.
- Algunas variables fueron cambiadas por las funciones actualizadas.
- estructura de código re organizando las funciones al principio.
- Se actualizó el diagrama relational_1 en la carpeta de doc/DIAGRAMAS

## fecha: 26/07/2026.
## Autor: Juan Sebastian Mina Quintero.

Se hizo actualizaciones en el DDL de la base de datos, al igual que se mejoró los scripts de generación de datos dummy, aunque sin terminar.

## changed:
- inserciones.py
- data_generation.py
- LOGISTICA_Y_CADENA_DE_SUMINISTRO.sql


## fecha: 25/07/2026. 
## Autor: Juan Sebastian Mina Quintero.

Se eliminó las carpeta de docs debido a la Nula conección con oracle SQL developer datamodeler. Esta se agregó después cuando se tuvo hecho el ERD de la base de datos. Se agregó también una carpeta interna llamada "Diagramas" para guardar el modelo lógico y relacional. Además, se añadió un readme dentro de la misma carpeta dando detalles de algunas decisiones tomadas en el diseño de la DB.

## Added
- /docs
- /DIAGRAMAS
- logical.png
- Relational_1.png
- README.md

### Removed
- /docs

## fecha: 24/07/2026. 
## Autor: Juan Sebastian Mina Quintero.

Aqui se escribirán los cambios más notables que se haga cada día.

### added
- readme.md
- changelog.md
