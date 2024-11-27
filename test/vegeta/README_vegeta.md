# vegeta:

Vegeta is a versatile HTTP load testing tool built out of a need to drill
HTTP services with a constant request rate. [It's over 9000!](https://en.wikipedia.org/wiki/It's_Over_9000)

## Descargar
[https://github.com/tsenart/vegeta/tags]
## Uso
Ejemplo para métodos POST, PUT:

`vegeta attack -rate=10000 -duration=30s -targets=./test_carga.txt | tee resultado.bin | vegeta report`

### Paraetros:
- **`-rate=10000`**: Establece la tasa de solicitudes en 10,000 solicitudes por segundo.
- **`-duration=30s`**: Establece la duración del ataque en 30 segundos.
- **`-targets=./test_carga.txt`**: Especifica el archivo que contiene las direcciones URL a donde se enviarán las solicitudes.
- **`| tee resultado.bin`**: Guarda los resultados del ataque en un archivo binario llamado `resultado.bin`.
- **`| vegeta report`**: Genera un informe de los resultados del ataque.

### Contenido de test_carga.txt
```
POST http://localhost:5000/api/v1/inventarios/retirar
Content-Type: application/json
@/PATH/HASTA/EL/ARCHIVO/test.json
```
Ejemplo simple para método GET:

`echo "GET http://localhost:5000/api/v1/" | vegeta attack -rate=10000 -duration=30s | tee resultado.bin | vegeta report`


vegeta attack -rate=60 -duration=30s -targets=./test_carga.txt | tee resultado.bin | vegeta report | tee resultados.txt


