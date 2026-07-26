import oracledb
from data_generation import data
try:
    connection = oracledb.connect(
        user = 'SYSTEM',
        password = '123456',
        dsn = 'localhost:1521/XE'
    )
    print(connection.version)
    if connection:
        cursor = connection.cursor()
        cursor.executemany("""INSERT INTO OPE_CONDUCTORES (cond_id, nomb_cond, apell_cond, tip_doc, num_doc_hash, fec_ingreso, id_ciudad_base, tip_vehiculo, cod_zona_asignada, activo, calific_promedio_acum) 
                           VALUES (:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11)""", data)
        
        if len(data) == cursor.rowcount:
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