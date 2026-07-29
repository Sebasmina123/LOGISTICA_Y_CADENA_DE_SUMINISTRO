### Notas:

- El pipeline se ejecutó varias veces, pues se dio la oportunidad de reconocer errores en un notebook
- En la orquestación se añadieron 2 wait's, configurados de 15 segundos cada uno. Esto porque si se dejaban los notebooks conectados de seguidos sin tiempo de espera suficiente, daba error por llegar al máximo de capacidad posible en mi caso. (Se aprendió a resolver ese error mientras que se estaba desarrollando 00_ingesta y 01_bronze, pues tocaba esperar a que se detuviera la sesión de uno correctamente antes de iniciar en otra y hacer procesos con archivos tan grandes)
