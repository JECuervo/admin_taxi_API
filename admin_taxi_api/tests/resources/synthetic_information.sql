/* carga de datos sinteticos para la base de test */

INSERT INTO app_admin (id, cel, usuario, password) VALUES
    (0, 3000000000, 'pedro', 'pedro');

INSERT INTO taxis (placa, lateral,  i_dia_corriente,  i_dia_festivo, total_km,  inicial_km, km_cambio_aceite, estado, inicio_admin) VALUES
    ('AAA000', 'A000', 100000, 90000, 1,10000,5000, 1,'01/01/2024'),
    ('BBB111', 'D111', 110000, 100000, 1,10000,5000, 1,'01/01/2024'),
    ('CCC222', 'H222', 120000, 110000, 1,10000,5000, 1,'01/01/2024');

INSERT INTO usuarios (id, cel, nombre) VALUES
    (0, 3111111111, 'juan'),
    (1, 3222222222, 'carlos'),
    (2, 3333333333, 'mario');

INSERT INTO administradores (id, placa) VALUES
    (0, 'AAA000'),
    (0, 'BBB111'),
    (1, 'CCC222');

INSERT INTO visualizadores (id, placa, permisos) VALUES
    (2, 'AAA000', 'all');

INSERT INTO ingresos (placa, fecha, valor) VALUES
    ('AAA000', '01/01/2024', 100000),
    ('BBB111', '01/01/2024', 110000),
    ('CCC222', '01/01/2024', 120000),
    ('AAA000', '02/01/2024', 100000),
    ('BBB111', '02/01/2024', 110000),
    ('CCC222', '02/01/2024', 0),
    ('AAA000', '03/01/2024', 100000),
    ('BBB111', '03/01/2024', 50000),
    ('CCC222', '03/01/2024', 50000);

INSERT INTO gastos (id_gasto, placa, fecha, valor, tipo, descripcion) VALUES
    (0, 'AAA000', '01/01/2024', 80000, 'fijo mensual', 'cambio aceite'),
    (1, 'CCC222', '02/01/2024', 170000, 'arreglo', 'cambio banda'),
    (2, 'BBB111', '03/01/2024', 50000, 'arreglo', 'pastillas de frenos'),
    (3, 'CCC222', '03/01/2024', 320000, 'arreglo', 'pintura');


INSERT INTO kilometraje (placa, fecha, km, estado) VALUES
    ('AAA000', '01/01/2024', 150, 1),
    ('BBB111', '01/01/2024', 165, 1),
    ('CCC222', '01/01/2024', 170, 1),
    ('AAA000', '02/01/2024', 180, 1),
    ('BBB111', '02/01/2024', 100, 1),
    ('CCC222', '02/01/2024', 0, 1),
    ('AAA000', '03/01/2024', 115, 1),
    ('BBB111', '03/01/2024', 130, 1),
    ('CCC222', '03/01/2024', 70, 1),
    ('AAA000', '04/01/2024', 0, 0),
    ('BBB111', '04/01/2024', 0, 0),
    ('CCC222', '04/01/2024', 0, 0);

INSERT INTO mantenimientos (placa, total_km, servicio, vencido) VALUES
    ('AAA000', 10300, 'cambio correa dentada', 0),
    ('CCC222', 10310, 'cambio aceite', 0);
