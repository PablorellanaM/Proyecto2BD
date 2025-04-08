-- Crear tabla de eventos
CREATE TABLE eventos (
    id_evento SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    fecha_evento TIMESTAMP NOT NULL
);

-- Crear tabla de asientos
CREATE TABLE asientos (
    id_asiento SERIAL PRIMARY KEY,
    id_evento INT REFERENCES eventos(id_evento) ON DELETE CASCADE,
    numero VARCHAR(10) NOT NULL,
    reservado BOOLEAN DEFAULT FALSE
);

-- Crear tabla de reservas
CREATE TABLE reservas (
    id_reserva SERIAL PRIMARY KEY,
    id_asiento INT REFERENCES asientos(id_asiento) ON DELETE CASCADE,
    usuario VARCHAR(100) NOT NULL,
    fecha_reserva TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
