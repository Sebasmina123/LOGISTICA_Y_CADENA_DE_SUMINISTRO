from faker import Faker
from datetime import date
import hashlib
import random

fake = Faker('es_CO')

tip_doc = ["Cedula de ciudadania","Cedula de extranjeria"]
ciudad_base = { "Bogotá": "BOG", "Cali": "CAL", "Barranquilla": "BAQ", "Medellín": "MDE", 
               "Bucaramanga": "BGA", "Pereira": "PER", "Manizales": "MZL", "Cartagena": "CTG", 
               "Santa Marta": "SMR", "Cucuta": "CUC" }

tip_vehiculo = ["Moto", "Bicicleta de carga", "Van", "camión"]

id_zona = []
for i in range(1, 300):
    id_zona.append(i)
activo = ["activo","inactivo"]
rn = random.sample(range(0000000000, 9999999999), 1)[0]
data = []

for i in range(5):
    # Generar un ID único por cada conductor
    rn = random.randint(10000000, 99999999)
    doc_hash = hashlib.md5(str(rn).encode('utf-8')).hexdigest()
    cal_promedio_acumulado = round(random.uniform(1.0, 5.0), 2) 
    data.append((rn, fake.first_name(), fake.last_name(), random.choice(tip_doc), doc_hash, 
                 fake.date_between(start_date='-10y', end_date="now"), 
                 random.choice(list(ciudad_base.values())), random.choice(tip_vehiculo), 
                 random.choice(id_zona), random.choice(activo), cal_promedio_acumulado)) 


print(data)