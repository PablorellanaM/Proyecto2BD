-- Insertar un evento
INSERT INTO eventos (nombre, fecha_evento)
VALUES ('Concierto Rock 2025', '2025-06-15 20:00:00');

-- Insertar 10 asientos para el evento con id_evento = 1
DO $$
BEGIN
    FOR i IN 1..10 LOOP
        INSERT INTO asientos (id_evento, numero)
        VALUES (1, CONCAT('A', i));
    END LOOP;
END;
$$;

-- Insertar reservas iniciales para los asientos con id 1 a 3
INSERT INTO reservas (id_asiento, usuario)
VALUES 
    (1, 'usuario1@example.com'),
    (2, 'usuario2@example.com'),
    (3, 'usuario3@example.com');

-- Marcar esos asientos como reservados
UPDATE asientos SET reservado = TRUE WHERE id_asiento IN (1, 2, 3);


--Insertar asientos del 4 al 50 
DO $$
BEGIN
    FOR i IN 4..50 LOOP
        INSERT INTO asientos (id_evento, numero)
        VALUES (1, CONCAT('A', i));
    END LOOP;
END;
$$;


-- Insertar reservas para asientos 4 a 10
DO $$
DECLARE
    i INT;
BEGIN
    FOR i IN 4..10 LOOP
        INSERT INTO reservas (id_asiento, usuario)
        VALUES (i, CONCAT('usuario', i, '@example.com'));

        -- Marcar asiento como reservado
        UPDATE asientos SET reservado = TRUE WHERE id_asiento = i;
    END LOOP;
END;
$$;
