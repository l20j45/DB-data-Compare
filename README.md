# DB-data-Compare

Este script puede ayudar a comparar dos tablas puestas en un servidor para poder comprar los ids.

te mandara los ids que no se encuentran registrados de la base de datos nueva a la anterior, te manda los que no son iguales por algun valor, "Cuidar aqui que ambos sean con el mismo encoding", y te permite generar consultas select dinamicas.

para utilizrlo lo que tienes que hacer primero es modificar el .env de la siguiente manera 

primero realizamos una copia del archivo env

## Dependencias:
mysql-connector-python==8.0.26
python-dotenv==0.20.0

### Copiamos el archivo .env

```bash
cp .env.example .env
```
### instalamos las dependencias

```python
pip install -r requirements.txt
```

### Modificamos el archivo env

```env
###Database Server 2
DatabaseServer1 = "" #direccion del servidor de base de datos
User1 = "" #usuario de la base de datos con permisos para lectura
Password1 = "" #password del usuario de la base de datos
Bd1 = "" #base de datos a consultar
Port1 = "" #puerto donde se encuentra la base de datos

#Database Server 2
DatabaseServer2 = ""
User2 = ""
Password2 = ""
Bd2 = ""
Port2 = ""

#Files configuration
FileCodeNotExistInServer2 = "" #nombre del archivo sin .csv donde se guardaran los registros que no coincidan
FileWithDiferentValues = "" #nombre del archivo sin .csv donde se guardaran los archivos que sean diferentes

#TableToCheck
TableToCheck = "" #tabla de la base de datos donde se haran las consultas
```

luego ejecutamos el script de manera normal

### Ejecutamos

```python
python3 DB-data-Compare.py
```