# Aplicación Web registro de movimientos de criptomonedas

- Aplicación Web de registro de criptomonedas realizado en Python con el framework Flask, motor de base de datos SQLite y utilizando las consultas de valores relativos entre las criptomonedas a través del api https://www.coinapi.io/

## Instalación
- Crear el entorno virtual.

- Renombrar el fichero 'config_template.py' a 'config.py' y en él realizar los siguientes pasos:

    1. Obtener la apikey en https://www.coinapi.io/u e introducirla en la variable 'APIKEY':
    ```
    APIKEY = "4545df4df545d4f5d4f545d"
    ```
    2. Generar la clave secreta en https://randomkeygen.com/ en introducirla en la variable 'SECRET_KEY':
    ```
    SECRET_KEY = "4545df4df545d4f5d4f545d"
    ```
    Se recomienda elegir clave de tipo "CodeIgniter Encryption Keys"

- Obtener de la carpeta app_cripto\data\create las plantillas SQL para crear las tablas e insertar los datos necesarios de nuestra BBDD:
```
coins_create.sql
movements_create.sql
```

## Instalación de dependencias
- En su entorno de Python ejecutar el siguiente comando:

```
pip install -r requirements.txt
```
Las librerias utilizadas flask https://flask.palletsprojects.com/en/2.2.x/

## Renombrar el archivo .env_template a .env y agregar las siguientes lineas:
```
FLASK_APP = main.py
FLASK_DEBUG = true
```

## Comando para ejecutar el servidor:
```
flask run
```

