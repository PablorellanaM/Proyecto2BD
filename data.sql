-- Insertar un evento
INSERT INTO eventos (nombre, fecha_evento)
VALUES ('Concierto Rock 2025', '2025-06-15 20:00:00');

-- Asumimos que el evento tiene id_evento = 1
-- Insertar 10 asientos para el evento
DO $$
BEGIN
    FOR i IN 1..10 LOOP
        INSERT INTO asientos (id_evento, numero)
        VALUES (1, CONCAT('A', i));
    END LOOP;
END;
$$;

-- Insertar reservas iniciales
-- Supongamos que los asientos con id 1 a 3 están reservados
INSERT INTO reservas (id_asiento, usuario)
VALUES 
    (1, 'usuario1@example.com'),
    (2, 'usuario2@example.com'),
    (3, 'usuario3@example.com');

-- Marcar esos asientos como reservados
UPDATE asientos SET reservado = TRUE WHERE id_asiento IN (1, 2, 3);
