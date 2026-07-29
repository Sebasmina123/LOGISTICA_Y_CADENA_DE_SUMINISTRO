

#####  ====================================================================================================
##### CAPA: BRONZE
#####  ====================================================================================================


#####  ----------------------------------------------------------------------------------------------------
TABLA: bronze.bronze_cal_destinatarios
#####  ----------------------------------------------------------------------------------------------------
```text
root
 |-- id_calificacion: long (nullable = true)
 |-- id_envio: long (nullable = true)
 |-- fec_calificacion: date (nullable = true)
 |-- puntaje_1_5: long (nullable = true)
 |-- comentario_texto: string (nullable = true)
 |-- canal_calificacion: string (nullable = true)
 |-- Marca_tiempo_ingesta: timestamp (nullable = true)
 |-- sistema_fuente: string (nullable = true)
 |-- id_lote_proc: string (nullable = true)
 |-- year_intake: integer (nullable = true)
 |-- month_intake: integer (nullable = true)
 |-- day_intake: integer (nullable = true)

```


#####  ----------------------------------------------------------------------------------------------------
TABLA: bronze.bronze_cli_remitentes
#####  ----------------------------------------------------------------------------------------------------
```text
root
 |-- id_remitente: long (nullable = true)
 |-- razon_social: string (nullable = true)
 |-- tipo_cliente: string (nullable = true)
 |-- ciudad_principal: string (nullable = true)
 |-- sla_entrega_horas: long (nullable = true)
 |-- penalidad_porc: double (nullable = true)
 |-- activo: string (nullable = true)
 |-- Marca_tiempo_ingesta: timestamp (nullable = true)
 |-- sistema_fuente: string (nullable = true)
 |-- id_lote_proc: string (nullable = true)
 |-- year_intake: integer (nullable = true)
 |-- month_intake: integer (nullable = true)
 |-- day_intake: integer (nullable = true)

```


#####  ----------------------------------------------------------------------------------------------------
TABLA: bronze.bronze_dir_novedades
#####  ----------------------------------------------------------------------------------------------------
```text
root
 |-- id_novedad: long (nullable = true)
 |-- id_envio: long (nullable = true)
 |-- fec_novedad: date (nullable = true)
 |-- tip_novedad: string (nullable = true)
 |-- desc_novedad: string (nullable = true)
 |-- id_agente_registro: long (nullable = true)
 |-- requiere_accion: string (nullable = true)
 |-- Marca_tiempo_ingesta: timestamp (nullable = true)
 |-- sistema_fuente: string (nullable = true)
 |-- id_lote_proc: string (nullable = true)
 |-- year_intake: integer (nullable = true)
 |-- month_intake: integer (nullable = true)
 |-- day_intake: integer (nullable = true)

```


#####  ----------------------------------------------------------------------------------------------------
TABLA: bronze.bronze_geo_zonas
#####  ----------------------------------------------------------------------------------------------------
```text
root
 |-- id_zona: long (nullable = true)
 |-- nom_zona: string (nullable = true)
 |-- id_ciudad: string (nullable = true)
 |-- barrio_referencia: string (nullable = true)
 |-- latitud_centroide: double (nullable = true)
 |-- longitud_centroide: double (nullable = true)
 |-- nivel_trafico_prom: double (nullable = true)
 |-- tip_zona: string (nullable = true)
 |-- distancia_bodega_km: double (nullable = true)
 |-- Marca_tiempo_ingesta: timestamp (nullable = true)
 |-- sistema_fuente: string (nullable = true)
 |-- id_lote_proc: string (nullable = true)
 |-- year_intake: integer (nullable = true)
 |-- month_intake: integer (nullable = true)
 |-- day_intake: integer (nullable = true)

```


#####  ----------------------------------------------------------------------------------------------------
TABLA: bronze.bronze_gps_rutas
#####  ----------------------------------------------------------------------------------------------------
```text
root
 |-- id_ruta: long (nullable = true)
 |-- cond_id: long (nullable = true)
 |-- fec_ruta: date (nullable = true)
 |-- hra_inicio: timestamp (nullable = true)
 |-- hra_fin: timestamp (nullable = true)
 |-- km_recorridos: double (nullable = true)
 |-- num_paradas_plan: integer (nullable = true)
 |-- num_paradas_real: integer (nullable = true)
 |-- desviacion_ruta_km: double (nullable = true)
 |-- consumo_combustible: string (nullable = true)
 |-- Marca_tiempo_ingesta: timestamp (nullable = true)
 |-- sistema_fuente: string (nullable = true)
 |-- id_lote_proc: string (nullable = true)
 |-- year_intake: integer (nullable = true)
 |-- month_intake: integer (nullable = true)
 |-- day_intake: integer (nullable = true)

```


#####  ----------------------------------------------------------------------------------------------------
TABLA: bronze.bronze_ope_conductores
#####  ----------------------------------------------------------------------------------------------------
```text
root
 |-- cond_id: long (nullable = true)
 |-- nomb_cond: string (nullable = true)
 |-- apell_cond: string (nullable = true)
 |-- tip_doc: string (nullable = true)
 |-- num_doc_hash: string (nullable = true)
 |-- fec_ingreso: date (nullable = true)
 |-- id_ciudad_base: string (nullable = true)
 |-- tip_vehiculo: string (nullable = true)
 |-- cod_zona_asignada: long (nullable = true)
 |-- activo: string (nullable = true)
 |-- calific_promedio_acum: double (nullable = true)
 |-- Marca_tiempo_ingesta: timestamp (nullable = true)
 |-- sistema_fuente: string (nullable = true)
 |-- id_lote_proc: string (nullable = true)
 |-- year_intake: integer (nullable = true)
 |-- month_intake: integer (nullable = true)
 |-- day_intake: integer (nullable = true)

```


#####  ----------------------------------------------------------------------------------------------------
TABLA: bronze.bronze_tms_envios
#####  ----------------------------------------------------------------------------------------------------
```text
root
 |-- id_envio: long (nullable = true)
 |-- id_remitente: long (nullable = true)
 |-- cond_id: long (nullable = true)
 |-- id_zona_destino: integer (nullable = true)
 |-- tip_paquete: string (nullable = true)
 |-- peso_kg: double (nullable = true)
 |-- fec_recepcion: date (nullable = true)
 |-- hra_recepcion: timestamp (nullable = true)
 |-- fec_entrega_programada: date (nullable = true)
 |-- fec_intento1: date (nullable = true)
 |-- hra_intento1: timestamp (nullable = true)
 |-- resultado_intento1: string (nullable = true)
 |-- fec_intento2: date (nullable = true)
 |-- hra_intento2: timestamp (nullable = true)
 |-- resultado_intento2: string (nullable = true)
 |-- fec_entrega_real: date (nullable = true)
 |-- estado_final: string (nullable = true)
 |-- motivo_fallo_cod: string (nullable = true)
 |-- vr_declarado: double (nullable = true)
 |-- Marca_tiempo_ingesta: timestamp (nullable = true)
 |-- sistema_fuente: string (nullable = true)
 |-- id_lote_proc: string (nullable = true)
 |-- year_intake: integer (nullable = true)
 |-- month_intake: integer (nullable = true)
 |-- day_intake: integer (nullable = true)

```


#####  ====================================================================================================
##### CAPA: SILVER
#####  ====================================================================================================


#####  ----------------------------------------------------------------------------------------------------
TABLA: silver.silver_cal_destinatarios
#####  ----------------------------------------------------------------------------------------------------
```text
root
 |-- id_calificacion: long (nullable = true)
 |-- id_envio: long (nullable = true)
 |-- fec_calificacion: date (nullable = true)
 |-- puntaje_1_5: long (nullable = true)
 |-- comentario_texto: string (nullable = true)
 |-- canal_calificacion: string (nullable = true)
 |-- Marca_tiempo_ingesta: timestamp (nullable = true)
 |-- sistema_fuente: string (nullable = true)
 |-- id_lote_proc: string (nullable = true)
 |-- year_intake: integer (nullable = true)
 |-- month_intake: integer (nullable = true)
 |-- day_intake: integer (nullable = true)

```


#####  ----------------------------------------------------------------------------------------------------
TABLA: silver.silver_cli_remitentes
#####  ----------------------------------------------------------------------------------------------------
```text
root
 |-- id_remitente: long (nullable = true)
 |-- razon_social: string (nullable = true)
 |-- tipo_cliente: string (nullable = true)
 |-- ciudad_principal: string (nullable = true)
 |-- sla_entrega_horas: long (nullable = true)
 |-- penalidad_porc: double (nullable = true)
 |-- activo: string (nullable = true)
 |-- Marca_tiempo_ingesta: timestamp (nullable = true)
 |-- sistema_fuente: string (nullable = true)
 |-- id_lote_proc: string (nullable = true)
 |-- year_intake: integer (nullable = true)
 |-- month_intake: integer (nullable = true)
 |-- day_intake: integer (nullable = true)

```


#####  ----------------------------------------------------------------------------------------------------
TABLA: silver.silver_dir_novedades
#####  ----------------------------------------------------------------------------------------------------
```text
root
 |-- id_novedad: long (nullable = true)
 |-- id_envio: long (nullable = true)
 |-- fec_novedad: date (nullable = true)
 |-- tip_novedad: string (nullable = true)
 |-- desc_novedad: string (nullable = true)
 |-- id_agente_registro: long (nullable = true)
 |-- requiere_accion: string (nullable = true)
 |-- Marca_tiempo_ingesta: timestamp (nullable = true)
 |-- sistema_fuente: string (nullable = true)
 |-- id_lote_proc: string (nullable = true)
 |-- year_intake: integer (nullable = true)
 |-- month_intake: integer (nullable = true)
 |-- day_intake: integer (nullable = true)

```


#####  ----------------------------------------------------------------------------------------------------
TABLA: silver.silver_geo_zonas
#####  ----------------------------------------------------------------------------------------------------
```text
root
 |-- id_zona: long (nullable = true)
 |-- nom_zona: string (nullable = true)
 |-- id_ciudad: string (nullable = true)
 |-- barrio_referencia: string (nullable = true)
 |-- latitud_centroide: double (nullable = true)
 |-- longitud_centroide: double (nullable = true)
 |-- nivel_trafico_prom: double (nullable = true)
 |-- tip_zona: string (nullable = true)
 |-- distancia_bodega_km: double (nullable = true)
 |-- Marca_tiempo_ingesta: timestamp (nullable = true)
 |-- sistema_fuente: string (nullable = true)
 |-- id_lote_proc: string (nullable = true)
 |-- year_intake: integer (nullable = true)
 |-- month_intake: integer (nullable = true)
 |-- day_intake: integer (nullable = true)

```


#####  ----------------------------------------------------------------------------------------------------
TABLA: silver.silver_gps_rutas
#####  ----------------------------------------------------------------------------------------------------
```text
root
 |-- id_ruta: long (nullable = true)
 |-- cond_id: long (nullable = true)
 |-- fec_ruta: date (nullable = true)
 |-- hra_inicio: timestamp (nullable = true)
 |-- hra_fin: timestamp (nullable = true)
 |-- km_recorridos: double (nullable = true)
 |-- num_paradas_plan: integer (nullable = true)
 |-- num_paradas_real: integer (nullable = true)
 |-- desviacion_ruta_km: double (nullable = true)
 |-- consumo_combustible: string (nullable = true)
 |-- Marca_tiempo_ingesta: timestamp (nullable = true)
 |-- sistema_fuente: string (nullable = true)
 |-- id_lote_proc: string (nullable = true)
 |-- year_intake: integer (nullable = true)
 |-- month_intake: integer (nullable = true)
 |-- day_intake: integer (nullable = true)

```


#####  ----------------------------------------------------------------------------------------------------
TABLA: silver.silver_ope_conductores
#####  ----------------------------------------------------------------------------------------------------
```text
root
 |-- cond_id: long (nullable = true)
 |-- nomb_cond: string (nullable = true)
 |-- apell_cond: string (nullable = true)
 |-- tip_doc: string (nullable = true)
 |-- num_doc_hash: string (nullable = true)
 |-- fec_ingreso: date (nullable = true)
 |-- id_ciudad_base: string (nullable = true)
 |-- tip_vehiculo: string (nullable = true)
 |-- cod_zona_asignada: long (nullable = true)
 |-- activo: string (nullable = true)
 |-- calific_promedio_acum: double (nullable = true)
 |-- Marca_tiempo_ingesta: timestamp (nullable = true)
 |-- sistema_fuente: string (nullable = true)
 |-- id_lote_proc: string (nullable = true)
 |-- year_intake: integer (nullable = true)
 |-- month_intake: integer (nullable = true)
 |-- day_intake: integer (nullable = true)

```


#####  ----------------------------------------------------------------------------------------------------
TABLA: silver.silver_tms_envios
#####  ----------------------------------------------------------------------------------------------------
```text
root
 |-- id_envio: long (nullable = true)
 |-- id_remitente: long (nullable = true)
 |-- cond_id: long (nullable = true)
 |-- id_zona_destino: integer (nullable = true)
 |-- tip_paquete: string (nullable = true)
 |-- peso_kg: double (nullable = true)
 |-- fec_recepcion: date (nullable = true)
 |-- hra_recepcion: timestamp (nullable = true)
 |-- fec_entrega_programada: date (nullable = true)
 |-- fec_intento1: date (nullable = true)
 |-- hra_intento1: timestamp (nullable = true)
 |-- resultado_intento1: string (nullable = true)
 |-- fec_intento2: date (nullable = true)
 |-- hra_intento2: timestamp (nullable = true)
 |-- resultado_intento2: string (nullable = true)
 |-- fec_entrega_real: date (nullable = true)
 |-- estado_final: string (nullable = true)
 |-- motivo_fallo_cod: string (nullable = true)
 |-- vr_declarado: double (nullable = true)
 |-- Marca_tiempo_ingesta: timestamp (nullable = true)
 |-- sistema_fuente: string (nullable = true)
 |-- id_lote_proc: string (nullable = true)
 |-- year_intake: integer (nullable = true)
 |-- month_intake: integer (nullable = true)
 |-- day_intake: integer (nullable = true)

```


#####  ====================================================================================================
##### CAPA: GOLD
#####  ====================================================================================================


#####  ----------------------------------------------------------------------------------------------------
TABLA: gold.dim_conductores
#####  ----------------------------------------------------------------------------------------------------
```text
root
 |-- sk_conductor: integer (nullable = true)
 |-- cond_id: long (nullable = true)
 |-- nomb_cond: string (nullable = true)
 |-- apell_cond: string (nullable = true)
 |-- tip_doc: string (nullable = true)
 |-- num_doc_hash: string (nullable = true)
 |-- fec_ingreso: date (nullable = true)
 |-- antiguedad_anios: long (nullable = true)
 |-- id_ciudad_base: string (nullable = true)
 |-- tip_vehiculo: string (nullable = true)
 |-- cod_zona_asignada: long (nullable = true)
 |-- activo: string (nullable = true)
 |-- calific_promedio_acum: double (nullable = true)

```


#####  ----------------------------------------------------------------------------------------------------
TABLA: gold.dim_remitentes
#####  ----------------------------------------------------------------------------------------------------
```text
root
 |-- sk_remitente: integer (nullable = true)
 |-- id_remitente: long (nullable = true)
 |-- razon_social: string (nullable = true)
 |-- segmento_industria: string (nullable = true)
 |-- ciudad_principal: string (nullable = true)
 |-- sla_entrega_horas: integer (nullable = true)
 |-- penalidad_porc: double (nullable = true)
 |-- activo: string (nullable = true)

```


#####  ----------------------------------------------------------------------------------------------------
TABLA: gold.dim_zonas
#####  ----------------------------------------------------------------------------------------------------
```text
root
 |-- sk_zona: integer (nullable = true)
 |-- id_zona: long (nullable = true)
 |-- nom_zona: string (nullable = true)
 |-- municipio: string (nullable = true)
 |-- barrio_referencia: string (nullable = true)
 |-- latitud_centroide: double (nullable = true)
 |-- longitud_centroide: double (nullable = true)
 |-- nivel_trafico_prom: double (nullable = true)
 |-- distancia_bodega_km: double (nullable = true)
 |-- indice_dificultad_operativa: double (nullable = true)
 |-- tip_zona: string (nullable = true)

```


#####  ----------------------------------------------------------------------------------------------------
TABLA: gold.fact_desempeno_conductor
#####  ----------------------------------------------------------------------------------------------------
```text
root
 |-- cond_id: long (nullable = true)
 |-- total_envios: long (nullable = true)
 |-- envios_exitosos: long (nullable = true)
 |-- tasa_exito: double (nullable = true)
 |-- promedio_intentos: double (nullable = true)
 |-- adherencia_ruta: double (nullable = true)
 |-- velocidad_promedio: double (nullable = true)
 |-- calificacion_promedio: double (nullable = true)
 |-- score_desempeno: double (nullable = true)

```


#####  ----------------------------------------------------------------------------------------------------
TABLA: gold.fact_envios
#####  ----------------------------------------------------------------------------------------------------
```text
root
 |-- sk_envio: integer (nullable = true)
 |-- id_envio: long (nullable = true)
 |-- id_remitente: long (nullable = true)
 |-- cond_id: long (nullable = true)
 |-- id_zona_destino: integer (nullable = true)
 |-- fec_recepcion: date (nullable = true)
 |-- fec_entrega_programada: date (nullable = true)
 |-- fec_entrega_real: date (nullable = true)
 |-- estado_final: string (nullable = true)
 |-- sla_entrega_horas: integer (nullable = true)
 |-- tiempo_entrega_real_horas: double (nullable = true)
 |-- horas_retraso: double (nullable = true)
 |-- flag_cumplimiento_sla: string (nullable = true)
 |-- clasificacion_retraso: string (nullable = true)
 |-- numero_intentos: integer (nullable = true)
 |-- motivo_fallo_cod: string (nullable = true)
 |-- tip_paquete: string (nullable = true)
 |-- peso_kg: double (nullable = true)
 |-- vr_declarado: double (nullable = true)

```


#####  ----------------------------------------------------------------------------------------------------
TABLA: gold.fact_rutas
#####  ----------------------------------------------------------------------------------------------------
```text
root
 |-- sk_ruta: integer (nullable = true)
 |-- id_ruta: long (nullable = true)
 |-- cond_id: long (nullable = true)
 |-- fec_ruta: date (nullable = true)
 |-- hra_inicio: timestamp (nullable = true)
 |-- hra_fin: timestamp (nullable = true)
 |-- km_recorridos: double (nullable = true)
 |-- horas_trabajadas: double (nullable = true)
 |-- num_paradas_plan: integer (nullable = true)
 |-- num_paradas_real: integer (nullable = true)
 |-- desviacion_ruta_km: double (nullable = true)
 |-- eficiencia_ruta: double (nullable = true)
 |-- velocidad_promedio_kmh: double (nullable = true)
 |-- desviacion_porc: double (nullable = true)

```


#####  ----------------------------------------------------------------------------------------------------
TABLA: gold.fact_trazabilidad_envio
#####  ----------------------------------------------------------------------------------------------------
```text
root
 |-- id_envio: long (nullable = true)
 |-- evento: string (nullable = true)
 |-- descripcion: string (nullable = true)
 |-- fecha_evento: timestamp (nullable = true)
 |-- evento_anterior: string (nullable = true)
 |-- horas_desde_evento_anterior: double (nullable = true)

```
