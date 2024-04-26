# Configuraciones iniciales
PRAGMA foreign_keys = ON;


/* Tablas para valores fijos */

CREATE TABLE IF NOT EXISTS tipos_gastos(
    tipos TEXT PRIMARY KEY
);
INSERT INTO tipos_gastos(tipos) values ('fijo mensual');
INSERT INTO tipos_gastos(tipos) values ('fijo anual');
INSERT INTO tipos_gastos(tipos) values ('arreglo');

CREATE TABLE IF NOT EXISTS binaria(
    valor INTEGER PRIMARY KEY
);
INSERT INTO binaria(valor) values (1);
INSERT INTO binaria(valor) values (0);

CREATE TABLE IF NOT EXISTS permisos(
    valor TEXT PRIMARY KEY
);
INSERT INTO permisos(valor) values ('all');
INSERT INTO permisos(valor) values ('reporte');


/* Tablas para logica de la app */

CREATE TABLE IF NOT EXISTS app_admin (
    id INTEGER PRIMARY KEY,
    cel INTEGER NOT NULL UNIQUE, 
    usuario TEXT NOT NULL UNIQUE, 
    password TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS taxis (
    placa TEXT PRIMARY KEY,
    lateral TEXT NOT NULL UNIQUE, 
    i_dia_corriente REAL NOT NULL, 
    i_dia_festivo REAL NOT NULL, 
    total_km REAL NOT NULL DEFAULT 0,
    inicial_km REAL NOT NULL,
    km_cambio_aceite REAL NOT NULL, 
    estado INTEGER NOT NULL REFERENCES binaria(valor),
    inicio_admin TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY,
    cel INTEGER NOT NULL UNIQUE,
    nombre TEXT
);

CREATE TABLE IF NOT EXISTS administradores(
    id INTEGER REFERENCES usuarios(id),
    placa TEXT REFERENCES taxis(placa)
);

CREATE TABLE IF NOT EXISTS visualizadores(
    id INTEGER REFERENCES usuarios(id),
    placa TEXT REFERENCES taxis(placa),
    permisos TEXT REFERENCES permisos(valor)
);

CREATE TABLE IF NOT EXISTS ingresos(
    placa TEXT REFERENCES taxis(placa),
    fecha TEXT,
    valor REAL
);

CREATE TABLE IF NOT EXISTS gastos(
    id_gastos INTEGER PRIMARY KEY,
    placa TEXT REFERENCES taxis(placa),
    fecha TEXT,
    valor REAL,
    tipo TEXT,
    descripcion TEXT
);

CREATE TABLE IF NOT EXISTS facturas(
    id_gastos INTEGER REFERENCES gastos(id_gastos),
    imagen BLOB
);

CREATE TABLE IF  NOT EXISTS kilometraje(
    placa TEXT REFERENCES taxis(placa),
    fecha TEXT,
    km REAL,
    estado INTEGER REFERENCES binaria(valor)
);

drop TABLE mantenimientos;

CREATE TABLE IF  NOT EXISTS mantenimientos(
    placa TEXT REFERENCES taxis(placa),
    total_km REAL,
    servicio TEXT,
    vencido INTEGER REFERENCES binaria(valor) DEFAULT 0
);

CREATE TABLE IF NOT EXISTS gps_taxis(
    placa TEXT PRIMARY KEY REFERENCES taxis(placa),
    url_aplicacion TEXT,
    usuario TEXT,
    password TEXT
);

/* TRIGGERS */

/* actualización automatica de los km totales */

/* No se considera realizar el mismo procedimiento cuando se crea
un nuevo registro ya que este esta planteado en siempre empezar por 0
y se quiere ahorrar costos en la base de datos. De igual manera por la forma
en la que esta construido en caso de crear valores diferentes de 0 Estos se
actulizaran en el kilometraje total apenas se actualice el valor de un registro */

CREATE TRIGGER actualizar_kilometraje
    AFTER UPDATE ON kilometraje
BEGIN
    UPDATE taxis SET total_km = taxis.inicial_km + (
            SELECT sum(km) FROM kilometraje 
                WHERE new.placa=kilometraje.placa
        )
        WHERE new.placa=taxis.placa;
END;

/* Actualización de estado en mantenimientos */

/* Cambia el estado de los mantenimientos a vencidos cuando el km total es superado */
CREATE TRIGGER actualizar_estado_mantenimientos
    AFTER UPDATE ON taxis
BEGIN
    UPDATE mantenimientos SET vencido = 1
        WHERE new.total_km>mantenimientos.total_km and new.placa=mantenimientos.placa;
END;

CREATE TRIGGER actualizar_total_km_update
    AFTER UPDATE ON taxis
BEGIN
    UPDATE taxis SET total_km = inicial_km + (
            SELECT sum(km) FROM kilometraje 
                WHERE new.placa=kilometraje.placa
        )
        WHERE new.placa=taxis.placa;
END;

CREATE TRIGGER actualizar_total_km_insert
    AFTER INSERT ON taxis
BEGIN
    UPDATE taxis SET total_km = inicial_km + (
            SELECT sum(km) FROM kilometraje 
                WHERE new.placa=kilometraje.placa
        )
        WHERE new.placa=taxis.placa;
END;
