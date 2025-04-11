import psycopg2
import threading
import time
import random

DB_CONFIG = {
    'dbname': 'proyecto2bd',
    'user': 'postgres',
    'password': 'Pablorellana2005',
    'host': 'localhost',
    'port': '5432'
}


# Configura aquí el nivel de aislamiento: 'READ COMMITTED', 'REPEATABLE READ', 'SERIALIZABLE'
ISOLATION_LEVEL = 'SERIALIZABLE'

asiento_id = 4  # El asiento que todos intentarán reservar

def reservar_asiento(usuario):
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        conn.set_session(isolation_level=ISOLATION_LEVEL)
        cursor = conn.cursor()

        cursor.execute("BEGIN;")

        # Bloquear el asiento que se intenta reservar
        cursor.execute("SELECT reservado FROM asientos WHERE id_asiento = %s FOR UPDATE;", (asiento_id,))
        resultado = cursor.fetchone()

        if resultado and not resultado[0]:
            cursor.execute("""
                INSERT INTO reservas (id_asiento, usuario)
                VALUES (%s, %s);
            """, (asiento_id, usuario))

            cursor.execute("UPDATE asientos SET reservado = TRUE WHERE id_asiento = %s;", (asiento_id,))
            print(f"[✔️] {usuario} reservó el asiento.")
        else:
            print(f"[❌] {usuario} no pudo reservar. Ya está ocupado.")

        conn.commit()
    except Exception as e:
        print(f"[⚠️] Error con {usuario}: {e}")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

def simular_reservas(n_usuarios):
    threads = []
    for i in range(n_usuarios):
        usuario = f"user{i+1}@mail.com"
        t = threading.Thread(target=reservar_asiento, args=(usuario,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

if __name__ == "__main__":
    usuarios_simultaneos = [5, 10, 20, 30]

    for n in usuarios_simultaneos:
        print(f"\n🚀 Simulación con {n} usuarios y nivel '{ISOLATION_LEVEL}'")
        # Reinicia el asiento como disponible
        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor()
        cursor.execute("UPDATE asientos SET reservado = FALSE WHERE id_asiento = %s;", (asiento_id,))
        cursor.execute("DELETE FROM reservas WHERE id_asiento = %s;", (asiento_id,))
        conn.commit()
        cursor.close()
        conn.close()

        simular_reservas(n)
        time.sleep(2)
