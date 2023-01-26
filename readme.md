# Aplicación Web Registro de movimientos de criptomonedas

- Programa App Registro Criptomonedas hecho en Python con el framework Flask, motor de base de datos SQLite y utilizando las consultas de valores relativos entre las criptomonedas a través de la api https://www.coinapi.io/

## Instalación
- Obtener la apikey en https://www.coinapi.io/
- Renombrar el fichero 'config_template.py' a 'config.py' y en él poner tu apikey obtenida en la variable 'APIKEY'
```
APIKEY = "4545df4df545d4f5d4f545d"
```

## Instalación de dependencias
- En su entorno de Python ejecutar el siguiente comando

```
pip install -r requirements.txt
```
La libreria utilizada flask https://flask.palletsprojects.com/en/2.2.x/

## Renombrar el archivo .env_template a .env y agregar las siguientes lineas
```
FLASK_APP = main.py
FLASK_DEBUG = true
```

## Comando para ejecutar el servidor:
```
flask run
```
