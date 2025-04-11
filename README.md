Manual de usuario — simulador de reservas concurrentes
Este sistema permite simular múltiples usuarios intentando reservar el mismo asiento en un evento, evaluando el comportamiento bajo diferentes niveles de aislamiento de transacciones en PostgreSQL.

Requisitos
Antes de ejecutar el sistema, asegúrese de tener instalado lo siguiente:

Python 3.11 o superior

PostgreSQL y pgAdmin 4

Paquetes de Python:

bash
Copy
Edit
pip install flask psycopg2-binary
Preparación de la Base de Datos
Crear la base de datos en PostgreSQL:

sql
Copy
Edit
CREATE DATABASE proyecto2bd;
Ejecutar el script ddl.sql para crear las tablas:

sql
Copy
Edit
* En pgAdmin o el Query Tool
* Cargar ddl.sql
* Ejecutar data.sql para insertar el evento y asientos de prueba.

Cómo ejecutar la simulación
Desde la línea de comandos:

bash
Copy
Edit
python simulador.py SERIALIZABLE 10
SERIALIZABLE = nivel de aislamiento (READ COMMITTED, REPEATABLE READ, SERIALIZABLE)

10 = número de usuarios simulados

Uso desde la interfaz web
Ejecuta el servidor Flask:

bash
Copy
Edit
python app.py
Abre tu navegador en:

cpp
Copy
Edit
http://127.0.0.1:5000
Selecciona el nivel de aislamiento y la cantidad de usuarios.

Haz clic en “Iniciar Simulación”.

Los resultados aparecerán en pantalla con estados por usuario (reserva exitosa, fallida o error de concurrencia).

Notas
Solo un usuario puede reservar el asiento con éxito.

El sistema detecta y reporta conflictos de concurrencia dependiendo del nivel de aislamiento.

Se recomienda ejecutar varias pruebas con distintos niveles y cantidades de usuarios para observar diferencias.

