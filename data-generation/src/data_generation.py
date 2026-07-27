from faker import Faker
from datetime import date, timedelta, time, datetime
import hashlib
import random
import json
import pandas as pd
import os

# ---------------- CONFIG -----------------

with open("config.json", encoding="utf-8") as f:
    config = json.load(f)

SEED = config["seed"]

random.seed(SEED)
Faker.seed(SEED)

fake = Faker("es_CO")
fake.seed_instance(SEED)

FECHA_INICIO = datetime.strptime(config["fecha_inicio"],"%Y-%m-%d").date()
FECHA_FIN = datetime.strptime(config["fecha_fin"],"%Y-%m-%d").date()
os.makedirs("exports", exist_ok=True)

#----------------------FUNCIONES------------------------------#
#creamos la hora según su pico. Iniciando en 8-11, (de 12-2 descanso), 14-17 pico y 18-21 terminando el día
def hora_aleatoria():
    #creamos la hora según el pico que puede tener en el día de manera random
    pico = random.random()

    if pico < 0.70:
        hora = random.randint(8,11)
    elif pico < 0.90:
        hora = random.randint(14,17)
    else:
        hora = random.randint(18,21)

    return time(hora, random.randint(0, 59), random.randint(0, 59))


#hacemos una fecha aleatoria con las configuraciones
def fecha_aleatoria():
    return fake.date_between(start_date=FECHA_INICIO, end_date=FECHA_FIN)

#hacemos un comentario aleatorio, pero un 5% de ellos serán nulos
def comentario_realista():
    if random.random() < 0.05:
        return None

    return fake.text(max_nb_chars=50)


#exportación
def exportar(nombre, columnas, data):
    print(f"Exportando {nombre}...")
    df = pd.DataFrame(data, columns=columnas)
    print(df.head())

    df.to_csv( f"exports/{nombre}.csv",index=False, encoding="utf-8-sig")

    df.to_json( f"exports/{nombre}.json", orient="records", indent=4, force_ascii=False)
    print(f"{nombre} listo")


#penalización porcentual
def penalizacion_porc():
    valor_producto = random.randint(10000, 1000000)
    porc = round(random.uniform(0.02, 0.08), 2)  # Genera un porcentaje aleatorio entre 2% y 8%
    print(porc)
    penalizacion = valor_producto * porc  # del 2% al 8% de la valor del producto
    return valor_producto, round(penalizacion, 2)


#nombre de la zona
def nombre_zona(id_ciudad_aleatorio):
    if id_ciudad_aleatorio == "BOG" or id_ciudad_aleatorio == "CAL" or id_ciudad_aleatorio == "MDE" or id_ciudad_aleatorio == "BGA" or id_ciudad_aleatorio == "PER" or id_ciudad_aleatorio == "MZL" or id_ciudad_aleatorio == "CUC":
        return "Región Andina"
    else:
        return "Región Caribe"


#referencias de los barrios
def barrio_referencia(id_ciudad_aleatorio):
    #barrios de referencia
    medellin = ["El Poblado", "Laureles", "El estadio", "Belén", "Prado"]
    bogota = ["Usaquén", "Chapinero", "La Candelaria", "Santa Fe", "Teusaquillo"]
    cali = ["San Antonio", "El Peñón", "Ciudad Jardín", "San Fernando", "Obrero"]
    barranquilla = ["El Prado", "Alto Prado", "Riomar", "El Recreo", "Boston"]
    bucaramanga = ["Cabecera del Llano", "Sotomayor", "El Centro", "San Alonso", "La Concordia"]
    pereira = ["El Poblado", "Álamos", "Circunvalar", "Pinares", "Corales"]
    manizales = ["El Cable", "Palermo", "Chipre", "La Enea", "Milán"]
    cartagena = ["Bocagrande", "El Laguito", "Getsemaní", "Centro Histórico", "Manga"]
    santa_marta = ["El Rodadero", "Centro Histórico", "Taganga", "Bastidas", "Mamatoco"]
    cucuta = ["Caobos", "La Playa", "San Luis", "El Centro", "Guaimaral"]

    if id_ciudad_aleatorio == "BOG":
        return random.choice(bogota)
    elif id_ciudad_aleatorio == "CAL":
        return random.choice(cali)
    elif id_ciudad_aleatorio == "MDE":
        return random.choice(medellin)
    elif id_ciudad_aleatorio == "BAQ":
        return random.choice(barranquilla)
    elif id_ciudad_aleatorio == "BGA":
        return random.choice(bucaramanga)
    elif id_ciudad_aleatorio == "PER":
        return random.choice(pereira)
    elif id_ciudad_aleatorio == "MZL":
        return random.choice(manizales)
    elif id_ciudad_aleatorio == "CTG":
        return random.choice(cartagena)
    elif id_ciudad_aleatorio == "SMR":
        return random.choice(santa_marta)
    elif id_ciudad_aleatorio == "CUC":
        return random.choice(cucuta)


#trafico promedio
def trafico_promedio(id_ciudad_aleatorio):
    if id_ciudad_aleatorio == "BOG":
        return float(18.9)  # Tráfico promedio en Bogotá
    elif id_ciudad_aleatorio == "CAL":
        return float(20.6)   # Tráfico promedio en Cali
    elif id_ciudad_aleatorio == "MDE":
        return float(20.7)   # Tráfico promedio en Medellín
    elif id_ciudad_aleatorio == "BAQ":
        return float(16.4)   # Tráfico promedio en Barranquilla
    elif id_ciudad_aleatorio == "BGA":
        return float(28.5)   # Tráfico promedio en Bucaramanga
    elif id_ciudad_aleatorio == "PER":
        return float(33.5)   # Tráfico promedio en Pereira
    elif id_ciudad_aleatorio == "MZL":
        return float(38.0)   # Tráfico promedio en Manizales
    elif id_ciudad_aleatorio == "CTG":
        return float(26.0)   # Tráfico promedio en Cartagena
    elif id_ciudad_aleatorio == "SMR":
        return float(35.0)   # Tráfico promedio en Santa Marta
    elif id_ciudad_aleatorio == "CUC":
        return float(31.0)   # Tráfico promedio en Cúcuta


# peso del paquete segun su tipo
def peso(paquete):
    if paquete == "Sobre":
        return round(random.uniform(0.1, 1.0), 2)  # Peso entre 0.1 y 1 kg
    elif paquete == "Bolsas Plasticas":
        return round(random.uniform(0.5, 5.0), 2)  # Peso entre 0.5 y 5 kg
    elif paquete == "Cajas de cartón":
        return round(random.uniform(1.0, 20.0), 2)  # Peso entre 1 y 20 kg
    elif paquete == "Contenedores de madera":
        return round(random.uniform(10.0, 100.0), 2)  # Peso entre 10 y 100 kg

#funcion para generar resultados de la tabla de envios (como fechas, horas, intentos...)
def fechas(hra_recepcion, fec_recepcion, vr_declarado):
    if hra_recepcion < time(10, 0, 0):
        fec_entrega_programada = fec_recepcion
    else:
        fec_entrega_programada = fec_recepcion + timedelta(days=1)

    lista_motivos = ["Estaba Ausente", "Dirección incorrecta", "Rechazado", "Retenido"]
    exito_final = random.choice([True, False])
    intento_entrega_exitosa = random.randint(1, 2) if exito_final else None

    fecha_intento_1 = fec_entrega_programada
    hra_intento_1 = hora_aleatoria()
    resultado_1 = "Entregado" if intento_entrega_exitosa == 1 else "No entregado"

    fecha_intento_2 = None
    hra_intento_2 = None
    resultado_2 = None

    if intento_entrega_exitosa == 1:
        fec_entrega_real = fecha_intento_1
        estado_final = "Entregado"
        motivo_fallo_final = None
        return (fec_recepcion, hra_recepcion, fec_entrega_programada, fecha_intento_1, hra_intento_1, resultado_1, fecha_intento_2, hra_intento_2, resultado_2, fec_entrega_real, estado_final, motivo_fallo_final, vr_declarado)

    fecha_intento_2 = fec_entrega_programada + timedelta(days=1)
    hra_intento_2 = hora_aleatoria()
    if intento_entrega_exitosa == 2:
        resultado_2 = "Entregado"
        fec_entrega_real = fecha_intento_2
        estado_final = "Entregado"
        motivo_fallo_final = None
    else:
        resultado_2 = "No entregado"
        fec_entrega_real = None
        estado_final = "Devuelto al Almacén"
        motivo_fallo_final = random.choice(lista_motivos)

    return (fec_recepcion, hra_recepcion, fec_entrega_programada, fecha_intento_1, hra_intento_1, resultado_1, fecha_intento_2, hra_intento_2, resultado_2, fec_entrega_real, estado_final, motivo_fallo_final,vr_declarado)



#id de la zona y de la ciudad se pone aqui porq se usan en varias variables y funciones para mantener la coherencia
id_zona = []
for i in range(1, 300):
    id_zona.append(i)

# id_de la ciudad y su respectivo codigo. Esta se utilizara en otras varibales 
id_ciudad = { "Bogotá": "BOG", "Cali": "CAL", "Barranquilla": "BAQ", "Medellín": "MDE", 
               "Bucaramanga": "BGA", "Pereira": "PER", "Manizales": "MZL", "Cartagena": "CTG", 
               "Santa Marta": "SMR", "Cucuta": "CUC" }




#------------- OPE_CONDUCTORES -----------#

tip_doc = ["Cedula de ciudadania","Cedula de extranjeria"] #tipo de documento
#ciudad base de los conductores, toma el codigo de la ciudad del diccionario id_ciudad
ciudad_base = list(id_ciudad.values())

#tipo de vehuculo que puede manejar el conductor
tip_vehiculo = ["Moto", "Bicicleta de carga", "Van", "camión"]
activo = ["activo","inactivo"]
data_OPE_CONDUCTORES = []

ids_c = []
for i in range(3):
    # Generar un ID único por cada conductor
    rn_ope_conduc = random.sample(range(0000000000, 9999999999), 1)[0]
    ids_c.append(rn_ope_conduc)
    doc_hash = hashlib.md5(str(rn_ope_conduc).encode('utf-8')).hexdigest()
    cal_promedio_acumulado = round(random.uniform(1.0, 5.0), 2) 

    data_OPE_CONDUCTORES.append((rn_ope_conduc, fake.first_name(), fake.last_name(), random.choice(tip_doc), 
                                 doc_hash, fecha_aleatoria(), random.choice(list(ciudad_base)), random.choice(tip_vehiculo), 
                                 random.choice(id_zona), random.choice(activo), cal_promedio_acumulado)) 


#------------------ CLI_REMITENTES --------------#
data_cli_remitentes = []
ids_r = []
dict_remitentes = {}
tip_cliente = ["Natural","E-commerce","Corporativo"] #tipo de cliente
vr_producto = []


for i in range(3):
    # Generar un ID único por cada remitente
    rn_remitente = random.sample(range(0000000000, 9999999999), 1)[0]
    ids_r.append(rn_remitente)
    vr_producto, penalizacion = penalizacion_porc()
    sla_entrega_horas = random.randint(1, 72)  # SLA de entrega entre 1 y 72 horas
    data_cli_remitentes.append((rn_remitente, fake.company(), random.choice(tip_cliente),
                 random.choice(list(ciudad_base)), sla_entrega_horas, penalizacion, random.choice(activo)))

    dict_remitentes[rn_remitente] = { "valor_declarado": vr_producto, "penalizacion": penalizacion }


#--------------------- GEO_ZONA -------------#

data_geo_zona = []

#tipo de zona
tip_zona = ["Local", "Regional"]

for i in range(config["zonas"]):
    #latitud y longitud
    latitud = fake.local_latlng(country_code='CO')[0]
    longitud = fake.local_latlng(country_code='CO')[1]
    id_ciudad_aleatorio = random.choice(list(id_ciudad.values()))
    #distancia a la bodega
    distancia_bodega = round(random.uniform(1, 100), 2)  # Distancia aleatoria entre 1 y 100 km
    data_geo_zona.append((random.choice(id_zona), nombre_zona(id_ciudad_aleatorio), id_ciudad_aleatorio,barrio_referencia(id_ciudad_aleatorio), 
                          float(latitud), float(longitud), trafico_promedio(id_ciudad_aleatorio),random.choice(tip_zona), distancia_bodega))


#----------- TMS_Envios -----------#

data_TMS_envios = []
ids_e = []
estado = []
tip_paquete = ["Sobre", "Bolsas Plasticas", "Cajas de cartón", "Contenedores de madera"]

for i in range(config["envios"]):
    rn_tms_envios = random.sample(range(0000000000, 9999999999), 1)[0]
    ids_e.append(rn_tms_envios)
    random_tip_paquete = random.choice(tip_paquete)
    fec_recepcion = fecha_aleatoria()
    hra_recepcion = hora_aleatoria()

    remitente_ = random.choice(ids_r)
    datos_finan_remi = dict_remitentes[remitente_]
    valor_declarado_real = float(datos_finan_remi["valor_declarado"])

    resultado_fechas = fechas(hra_recepcion, fec_recepcion, valor_declarado_real)
    estado.append(resultado_fechas[10])
    data_TMS_envios.append((rn_tms_envios, random.choice(ids_r), random.choice(ids_c), random.choice(id_zona), random_tip_paquete, peso(random_tip_paquete), *resultado_fechas))


#-------- ANOMALÍA INTENCIONAL 1, DUPLICADOS ---------------- #

#calculamos un porcentaje (1%) para la cantidad de duplicados que queremos
cantidad_duplicados = max(1, int(len(data_TMS_envios) * 0.01))
duplicados = random.sample(data_TMS_envios, cantidad_duplicados) 

#hacemos un for para insertar una nueva tupla, pero con ids diferentes
for envio in duplicados:
    nuevo = list(envio)
    nuevo[0] = random.sample(range(1000000000,9999999999), 1)[0]
    data_TMS_envios.append(tuple(nuevo))

print(f"{cantidad_duplicados} envíos duplicados agregados.")


#--------- ANOMALÍA INTENCIONAL 2, FECHA INCONSISTENTE ----------- #

cantidad_fechas = max(1, int(len(data_TMS_envios) * 0.005)) # un 0.5%
indices = random.sample(range(len(data_TMS_envios)), cantidad_fechas) 

for indice in indices:
    fila = list(data_TMS_envios[indice])
    # fec_entrega_real será un día antes de la recepción
    if fila[15] is not None:
        fila[15] = fila[6] - timedelta(days=1)

    data_TMS_envios[indice] = tuple(fila)

print(f"{cantidad_fechas} registros con fechas inconsistentes.")


#----------- ANOMALÍA INTENCIONAL 3, PESOS INCOHERENTES -------------#
cantidad_pesos = max(1, int(len(data_TMS_envios) * 0.005)) 
indices = random.sample(range(len(data_TMS_envios)), cantidad_pesos)

for indice in indices:
    fila = list(data_TMS_envios[indice])
    if random.random() < 0.5:
        fila[5] = -round(random.uniform(1,10),2)
    else:
        fila[5] = round(random.uniform(300,500),2)

    data_TMS_envios[indice] = tuple(fila)

print(f"{cantidad_pesos} registros con pesos incoherentes.")


#---------------- GPS_RUTAS  ---------------- #

data_GPS_rutas = []

for i in range(config["gps_rutas"]):
    hora_inicio = hora_aleatoria()
    hora_fin = hora_aleatoria()
    km_recorridos = round(random.uniform(1, 1000), 2)
    rn_gps_rutas = random.sample(range(0000000000, 9999999999), 1)[0]
    num_paradas_plan = random.randint(1,99)
    num_paradas_real = random.randint(1,250)
    desviacion_ruta_km = round(random.uniform(0,100), 2)

    if (km_recorridos + desviacion_ruta_km) < 100:
        consumo_combustible = "Bajo"
    elif   (km_recorridos + desviacion_ruta_km) >= 100 and  (km_recorridos + desviacion_ruta_km) <= 700:
        consumo_combustible = "Medio"
    else:
        consumo_combustible = "Alto"
    
    data_GPS_rutas.append((rn_gps_rutas, random.choice(ids_c),resultado_fechas[2],hora_inicio, hora_fin, km_recorridos, num_paradas_plan, num_paradas_real, desviacion_ruta_km,consumo_combustible))




#--------------- CAL_DESTINATARIOS ---------------#
data_CAL_destinatarios = []

for i in range(config["calificaciones"]):
    rn_cal_destinatarios = random.sample(range(0000000000, 9999999999), 1)[0]
    puntaje_1_5 = random.randint(1,5)
    comentario = comentario_realista()
    canal_calificacion = ["Correo Electronico", "Llamada", "SMS", "App"]
    data_CAL_destinatarios.append((rn_cal_destinatarios, random.choice(ids_e),resultado_fechas[9], puntaje_1_5, comentario, random.choice(canal_calificacion)))


#----------------- DIR_NOVEDADES ---------------#
data_DIR_novedades = []

for i in range(config["novedades"]):
    rn_dir_novedades = random.sample(range(0000000000, 9999999999), 1)[0]
    tip_novedad = ["Dirección Erronea", "Información Incompleta", "Dificil Acceso", "Ausente", "Rechazado", "Retenido", "Pérdida"]
    desc_novedad = fake.text(max_nb_chars=50)
    id_agente_registro = random.sample(range(0000000000, 9999999999),1)[0]
    requiere_accion = ["Si", "No"]

    data_DIR_novedades.append((rn_dir_novedades, random.choice(ids_e), resultado_fechas[9], random.choice(tip_novedad), desc_novedad,id_agente_registro, random.choice(requiere_accion)))


# ----------------- EXPORTACIÓN ---------------------#

exportar("OPE_CONDUCTORES",["cond_id", "nomb_cond", "apell_cond", "tip_doc", "num_doc_hash", "fec_ingreso", "id_ciudad_base", "tip_vehiculo", "cod_zona_asignada", "activo", "calific_promedio_acum"], data_OPE_CONDUCTORES)

exportar("CLI_REMITENTES",["id_remitente", "razon_social", "tipo_cliente", "ciudad_principal", "sla_entrega_horas", "penalidad_porc", "activo"], data_cli_remitentes)

exportar( "GEO_ZONAS", [ "id_zona", "nom_zona", "id_ciudad", "barrio_referencia", "latitud_centroide", "longitud_centroide", "nivel_trafico_prom", "tip_zona", "distancia_bodega_km"], data_geo_zona)

exportar("TMS_ENVIOS",["id_envio","id_remitente","cond_id", "id_zona_destino","tip_paquete", "peso_kg", "fec_recepcion", "hra_recepcion", "fec_entrega_programada", 
                       "fec_intento1", "hra_intento1", "resultado_intento1", "fec_intento2", "hra_intento2", "resultado_intento2", "fec_entrega_real", "estado_final", 
                       "motivo_fallo_cod", "vr_declarado"], data_TMS_envios)

exportar("GPS_RUTAS",["id_ruta","cond_id","fec_ruta","hra_inicio","hra_fin","km_recorridos","num_paradas_plan","num_paradas_real","desviacion_ruta_km","consumo_combustible"],data_GPS_rutas)

exportar("DIR_NOVEDADES",[ "id_novedad", "id_envio", "fec_novedad", "tip_novedad", "desc_novedad", "id_agente_registro", "requiere_accion"], data_DIR_novedades)

exportar("CAL_DESTINATARIOS",["id_calificacion","id_envio","fec_calificacion","puntaje_1_5","comentario_texto","canal_calificacion"], data_CAL_destinatarios)

print("\nArchivos CSV y JSON exportados correctamente.")