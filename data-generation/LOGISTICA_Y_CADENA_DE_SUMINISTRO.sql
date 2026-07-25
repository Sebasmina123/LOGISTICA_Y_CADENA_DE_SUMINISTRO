-- Generado por Oracle SQL Developer Data Modeler 24.3.1.351.0831
--   en:        2026-07-25 16:47:13 COT
--   sitio:      Oracle Database 21c
--   tipo:      Oracle Database 21c



DROP TABLE CAL_DESTINATARIOS CASCADE CONSTRAINTS 
;

DROP TABLE CLI_REMITENTES CASCADE CONSTRAINTS 
;

DROP TABLE DIR_NOVEDADES CASCADE CONSTRAINTS 
;

DROP TABLE GEO_ZONAS CASCADE CONSTRAINTS 
;

DROP TABLE GPS_RUTAS CASCADE CONSTRAINTS 
;

DROP TABLE OPE_CONDUCTORES CASCADE CONSTRAINTS 
;

DROP TABLE TMS_ENVIOS CASCADE CONSTRAINTS 
;

-- predefined type, no DDL - MDSYS.SDO_GEOMETRY

-- predefined type, no DDL - XMLTYPE

CREATE TABLE CAL_DESTINATARIOS 
    ( 
     id_calificacion    NUMBER (10)  NOT NULL , 
     id_envio           NUMBER (10)  NOT NULL , 
     fec_calificacion   DATE , 
     puntaje_1_5        NUMBER (1) , 
     comentario_texto   VARCHAR2 (2000 CHAR) , 
     canal_calificacion VARCHAR2 (20 CHAR) 
    ) 
;

ALTER TABLE CAL_DESTINATARIOS 
    ADD CONSTRAINT CAL_DESTINATARIOS_PK PRIMARY KEY ( id_calificacion ) ;

CREATE TABLE CLI_REMITENTES 
    ( 
     id_remitente      NUMBER (10)  NOT NULL , 
     razon_social      VARCHAR2 (250 CHAR)  NOT NULL , 
     tipo_cliente      VARCHAR2 (15 CHAR) , 
     ciudad_principal  VARCHAR2 (30 CHAR) , 
     sla_entrega_horas NUMBER (2)  NOT NULL , 
     penalidad_porc    VARCHAR2 (10 CHAR)  NOT NULL , 
     activo            NUMBER 
    ) 
;

ALTER TABLE CLI_REMITENTES 
    ADD CONSTRAINT CLI_REMITENTES_PK PRIMARY KEY ( id_remitente ) ;

CREATE TABLE DIR_NOVEDADES 
    ( 
     id_novedad         NUMBER (10)  NOT NULL , 
     id_envio           NUMBER (10)  NOT NULL , 
     fec_novedad        DATE , 
     tip_novedad        VARCHAR2 (30 CHAR) , 
     desc_novedad       VARCHAR2 (2000 CHAR) , 
     id_agente_registro NUMBER (10)  NOT NULL , 
     requiere_accion    NUMBER 
    ) 
;

ALTER TABLE DIR_NOVEDADES 
    ADD CONSTRAINT DIR_NOVEDADES_PK PRIMARY KEY ( id_novedad ) ;

CREATE TABLE GEO_ZONAS 
    ( 
     id_zona             NUMBER (10)  NOT NULL , 
     nom_zona            VARCHAR2 (27 CHAR)  NOT NULL , 
     id_ciudad           NUMBER (10)  NOT NULL , 
     barrio_referencia   VARCHAR2 (30 CHAR) , 
     latitud_centroide   NUMBER (10,8) , 
     longitud_centroide  NUMBER (11,8) , 
     nivel_trafico_prom  NUMBER (4,2) , 
     tip_zona            VARCHAR2 (4 CHAR) , 
     distancia_bodega_km NUMBER (6,2) 
    ) 
;

ALTER TABLE GEO_ZONAS 
    ADD CONSTRAINT GEO_ZONAS_PK PRIMARY KEY ( id_zona ) ;

CREATE TABLE GPS_RUTAS 
    ( 
     id_ruta             NUMBER (10)  NOT NULL , 
     cond_id             NUMBER (10)  NOT NULL , 
     fec_ruta            DATE , 
     hra_inicio          DATE , 
     hra_fin             DATE , 
     " km_recorridos"    NUMBER (6,2) , 
     num_paradas_plan    NUMBER (2) , 
     num_paradas_real    NUMBER (2) , 
     desviacion_ruta_km  NUMBER (6,2) , 
     consumo_combustible VARCHAR2 (10 CHAR) 
    ) 
;

ALTER TABLE GPS_RUTAS 
    ADD CONSTRAINT GPS_RUTAS_PK PRIMARY KEY ( id_ruta ) ;

CREATE TABLE OPE_CONDUCTORES 
    ( 
     cond_id               NUMBER (10)  NOT NULL , 
     nomb_cond             VARCHAR2 (15 CHAR)  NOT NULL , 
     apell_cond            VARCHAR2 (20 CHAR)  NOT NULL , 
     tip_doc               VARCHAR2 (21 CHAR)  NOT NULL , 
     num_doc_hash          CHAR (32 CHAR) , 
     fec_ingreso           DATE , 
     id_ciudad_base        VARCHAR2 (20 CHAR)  NOT NULL , 
     tip_vehiculo          VARCHAR2 (20 CHAR)  NOT NULL , 
     cod_zona_asignada     NUMBER (10) , 
     activo                NUMBER , 
     calific_promedio_acum NUMBER (4,2)  NOT NULL 
    ) 
;

ALTER TABLE OPE_CONDUCTORES 
    ADD CONSTRAINT OPE_CONDUCTORES_PK PRIMARY KEY ( cond_id ) ;

CREATE TABLE TMS_ENVIOS 
    ( 
     id_envio               NUMBER (10)  NOT NULL , 
     id_remitente           NUMBER (10)  NOT NULL , 
     cond_id                NUMBER (10)  NOT NULL , 
     id_zona_destino        NUMBER (10) , 
     tip_paquete            VARCHAR2 (30 CHAR) , 
     peso_kg                NUMBER (4,2) , 
     fec_recepcion          DATE , 
     hra_recepcion          DATE , 
     fec_entrega_programada DATE , 
     fec_intento1           DATE , 
     hra_intento1           DATE , 
     resultado_intento1     VARCHAR2 (20 CHAR) , 
     fec_intento2           DATE , 
     hra_intento2           DATE , 
     resultado_intento2     VARCHAR2 (20 CHAR) , 
     fec_entrega_real       DATE , 
     estado_final           VARCHAR2 (30 CHAR) , 
     motivo_fallo_cod       VARCHAR2 (2000 CHAR) , 
     vr_declarado           NUMBER (10,2) 
    ) 
;

ALTER TABLE TMS_ENVIOS 
    ADD CONSTRAINT TMS_ENVIOS_PK PRIMARY KEY ( id_envio ) ;

ALTER TABLE TMS_ENVIOS 
    ADD CONSTRAINT cond_id FOREIGN KEY 
    ( 
     cond_id
    ) 
    REFERENCES OPE_CONDUCTORES 
    ( 
     cond_id
    ) 
;

ALTER TABLE GPS_RUTAS 
    ADD CONSTRAINT cond_idv2 FOREIGN KEY 
    ( 
     cond_id
    ) 
    REFERENCES OPE_CONDUCTORES 
    ( 
     cond_id
    ) 
;

ALTER TABLE CAL_DESTINATARIOS 
    ADD CONSTRAINT id_envio FOREIGN KEY 
    ( 
     id_envio
    ) 
    REFERENCES TMS_ENVIOS 
    ( 
     id_envio
    ) 
;

ALTER TABLE DIR_NOVEDADES 
    ADD CONSTRAINT id_enviov2 FOREIGN KEY 
    ( 
     id_envio
    ) 
    REFERENCES TMS_ENVIOS 
    ( 
     id_envio
    ) 
;

ALTER TABLE TMS_ENVIOS 
    ADD CONSTRAINT id_remitente FOREIGN KEY 
    ( 
     id_remitente
    ) 
    REFERENCES CLI_REMITENTES 
    ( 
     id_remitente
    ) 
;

SELECT * FROM GPS_RUTAS;
SELECT * FROM CAL_DESTINATARIOS;
SELECT * FROM CLI_REMITENTES;
SELECT * FROM DIR_NOVEDADES;
SELECT * FROM GEO_ZONAS;
SELECT * FROM OPE_CONDUCTORES;
SELECT * FROM TMS_ENVIOS;
-- Informe de Resumen de Oracle SQL Developer Data Modeler: 
-- 
-- CREATE TABLE                             7
-- CREATE INDEX                             0
-- ALTER TABLE                             12
-- CREATE VIEW                              0
-- ALTER VIEW                               0
-- CREATE PACKAGE                           0
-- CREATE PACKAGE BODY                      0
-- CREATE PROCEDURE                         0
-- CREATE FUNCTION                          0
-- CREATE TRIGGER                           0
-- ALTER TRIGGER                            0
-- CREATE COLLECTION TYPE                   0
-- CREATE STRUCTURED TYPE                   0
-- CREATE STRUCTURED TYPE BODY              0
-- CREATE CLUSTER                           0
-- CREATE CONTEXT                           0
-- CREATE DATABASE                          0
-- CREATE DIMENSION                         0
-- CREATE DIRECTORY                         0
-- CREATE DISK GROUP                        0
-- CREATE ROLE                              0
-- CREATE ROLLBACK SEGMENT                  0
-- CREATE SEQUENCE                          0
-- CREATE MATERIALIZED VIEW                 0
-- CREATE MATERIALIZED VIEW LOG             0
-- CREATE SYNONYM                           0
-- CREATE TABLESPACE                        0
-- CREATE USER                              0
-- 
-- DROP TABLESPACE                          0
-- DROP DATABASE                            0
-- 
-- REDACTION POLICY                         0
-- 
-- ORDS DROP SCHEMA                         0
-- ORDS ENABLE SCHEMA                       0
-- ORDS ENABLE OBJECT                       0
-- 
-- ERRORS                                   0
-- WARNINGS                                 0
