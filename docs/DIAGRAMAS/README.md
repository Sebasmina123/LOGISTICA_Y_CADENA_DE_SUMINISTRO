## Diagramas ERD

Se realizaron los diagramas en el software Oracle SQL Developer Data Modeler. A los siguientes atributos, se les asignó su tipo y su tamaño pensando en lo siguiente:

- tip_paquete: sobres, bolsas plasticas, cajas de carton, contenedores de manera.
- tipo_cliente: Natural, E-commerce, corporativos.
- activo: "1" indica Sí; "0" indica No.
- tip_doc: cédula de ciudadanía, cédula de extranjería.
- num_doc_hash: código hash aleatorio con formato MD5(Message Digest 5).
- tip_vehiculo: moto, bicicleta de carga, Van, Camión.
- Canal_calificacion: correo electronico, llamada, SMS, App
- tip_novedad: Depende de la situación: dirección erronea, información incompleta, dificil acceso, Ausente, rechazado, retenido, pérdida, fuerza mayor.
- requiere_accion: "1" indica sí; "0" indica No.
- Los id en general: Todos los id tienen una precisión de 10 para tener una gran combinación máxima de valores y tener menos limitación a la hora de ña inserción.
 
