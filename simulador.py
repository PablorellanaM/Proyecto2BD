import psycopg2
import threading
import time
import sys

# Leer parámetros desde línea de comandos
ISOLATION_LEVEL = sys.argv[1] if len(sys.argv) > 1 else 'SERIALIZABLE'
N_USUARIOS = int(sys.argv[2]) if len(sys.argv) > 2 else 5

DB_CONFIG = {
    'dbname': 'proyecto2bd',
    'user': 'postgres',
    'password': 'Pablorellana2005',
    'host': 'localhost',
    'port': '5432'
}

asiento_id = 4  # El asiento a reservar

def reservar_asiento(usuario):
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        conn.set_session(isolation_level=ISOLATION_LEVEL)
        cursor = conn.cursor()

        cursor.execute("BEGIN;")
        cursor.execute("SELECT reservado FROM asientos WHERE id_asiento = %s FOR UPDATE;", (asiento_id,))
        resultado = cursor.fetchone()

        if resultado and not resultado[0]:
            cursor.execute("""
                INSERT INTO reservas (id_asiento, usuario)
                VALUES (%s, %s);
            """, (asiento_id, usuario))

            cursor.execute("UPDATE asientos SET reservado = TRUE WHERE id_asiento = %s;", (asiento_id,))
            print(f"[OK] {usuario} reservó el asiento.")
        else:
            print(f"[NO] {usuario} no pudo reservar. Ya está ocupado.")

        conn.commit()
    except Exception as e:
        print(f"[ERR] Error con {usuario}: {e}")
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
    print(f"\n--- Simulación con {N_USUARIOS} usuarios y nivel '{ISOLATION_LEVEL}' ---")

    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor()
        cursor.execute("UPDATE asientos SET reservado = FALSE WHERE id_asiento = %s;", (asiento_id,))
        cursor.execute("DELETE FROM reservas WHERE id_asiento = %s;", (asiento_id,))
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"[ERR] Error al reiniciar el asiento: {e}")

    simular_reservas(N_USUARIOS)
