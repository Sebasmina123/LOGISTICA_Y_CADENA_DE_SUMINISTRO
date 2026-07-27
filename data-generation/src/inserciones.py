import oracledb
from datetime import date, time, datetime
from data_generation import data_OPE_CONDUCTORES, data_cli_remitentes, data_geo_zona, data_TMS_envios
try:
    connection = oracledb.connect(
        user = 'SYSTEM',
        password = '123456',
        dsn = 'localhost:1521/XE'
    )
    print(connection.version)
    print("conectando...")

    if connection: #CONDUCTORES
        cursor = connection.cursor()
        cursor.executemany("""INSERT INTO OPE_CONDUCTORES (cond_id, nomb_cond, apell_cond, tip_doc, num_doc_hash, fec_ingreso, id_ciudad_base, tip_vehiculo, cod_zona_asignada, activo, calific_promedio_acum) 
                           VALUES (:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11)""", data_OPE_CONDUCTORES)
        if len(data_OPE_CONDUCTORES) == cursor.rowcount:
            connection.commit()
            print("Data inserted successfully.")
        else:
            connection.rollback()
            print("Data insertion failed. Rolling back changes.")

    if connection: #REMITENTES
        cursor = connection.cursor()
        cursor.executemany("""INSERT INTO CLI_REMITENTES (id_remitente, razon_social, tipo_cliente, ciudad_principal, sla_entrega_horas, penalidad_porc, activo) 
                            VALUES (:1,:2,:3,:4,:5,:6,:7)""", data_cli_remitentes)
        
        if len(data_cli_remitentes) == cursor.rowcount:
            connection.commit()
            print("Data inserted successfully.")
        else:
            connection.rollback()
            print("Data insertion failed. Rolling back changes.")

    if connection: #GEO_ZONA
        cursor = connection.cursor()
        cursor.executemany("""INSERT INTO GEO_ZONAS (id_zona, nom_zona , id_ciudad, barrio_referencia, latitud_centroide, longitud_centroide, nivel_trafico_prom, tip_zona, distancia_bodega_km) 
                            VALUES (:1,:2,:3,:4,:5,:6,:7,:8,:9)""", data_geo_zona)
        
        if len(data_geo_zona) == cursor.rowcount:
            connection.commit()
            print("Data inserted successfully.")
        else:
            connection.rollback()
            print("Data insertion failed. Rolling back changes.")

    
    data_TMS_envios_corregida = []
        
    for fila in data_TMS_envios:
        fila_lista = list(fila)
        for i in range(len(fila_lista)):
            if isinstance(fila_lista[i], time):
                # Convierte el objeto time al formato de texto 'HH:MI:SS'
                fila_lista[i] = fila_lista[i].strftime("%H:%M:%S")
        data_TMS_envios_corregida.append(tuple(fila_lista))
    # ----------------------------------------------------
    if connection: #TMS_ENVIOS 
        cursor = connection.cursor()
        cursor.executemany("""INSERT INTO TMS_ENVIOS (id_envio,id_remitente, cond_id, id_zona_destino, 
        tip_paquete,  peso_kg, fec_recepcion, hra_recepcion, fec_entrega_programada, fec_intento1, hra_intento1, 
        resultado_intento1, fec_intento2, hra_intento2, resultado_intento2, fec_entrega_real, estado_final, motivo_fallo_cod, vr_declarado) 
        VALUES (:1,:2,:3,:4,:5,:6,:7,TO_DATE(:8, 'HH24:MI:SS'),:9,:10,TO_DATE(:11, 'HH24:MI:SS'),:12,:13,TO_DATE(:14, 'HH24:MI:SS'),:15,:16,:17,:18,:19)""", data_TMS_envios_corregida)

        if len(data_TMS_envios) == cursor.rowcount:
            connection.commit()
            print("Data inserted successfully.")
        else:
            connection.rollback()
            print("Data insertion failed. Rolling back changes.")

except Exception as ex:
    print("Error during connection: {}".format(ex))
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Connection closed.")