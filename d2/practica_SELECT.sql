CREATE DATABASE vacunaciones;
USE vacunaciones;

-- Eliminar tabla
-- DROP TABLE nombreTabla;

-- Crear tabla vacunas con las siguientes columnas:
-- id numérico autoincrementado y primary key
-- nombre de vacuna hasta 100 chars
-- procedencia hasta 20 chars
-- lote hasta  chars
CREATE TABLE vacunas(
	id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) UNIQUE NOT NULL, -- UNIQUE TOGETHER (conjungicón de dos o más columnas que sean UNIQUE)
    procedencia VARCHAR(20) NOT NULL,
    lote VARCHAR(6)
);

INSERT INTO vacunas (id, nombre, procedencia, lote) VALUES (DEFAULT, 'PFIZER', 'EEUU', '123abc'), 
														   (DEFAULT, 'SPUTNIK', 'RUSA', '3d3afg'),
                                                           (DEFAULT, 'ASTRAZENECA', 'CHINA', '5d8jh5'),
                                                           (DEFAULT, 'CHINOPHARM', 'CHINA', 'n8gg84'),
                                                           (DEFAULT, 'JHONSON & JHONSON', 'CHINA', 'b55b47');

SET SQL_SAFE_UPDATES = false;
UPDATE vacunas SET procedencia = 'EEUU' WHERE nombre = 'JHONSON & JHONSON'; 

SELECT * FROM vacunas;

-- devolver vacunas con id 3
SELECT * FROM vacunas WHERE id = 3;

-- hechas en China
SELECT * FROM vacunas WHERE procedencia = 'china';

-- que tengan un espacio en el nombre
SELECT * FROM vacunas WHERE nombre LIKE '% %';

-- tercer caracter la letra I y quinto la letra O
SELECT * FROM vacunas WHERE nombre LIKE '__i%' AND nombre LIKE '____o%'; 


-- TABLE vacunatorios
-- id primary key entero
-- dirección hasta 100 chars
-- número entero no nulo
-- atención preferencia boolean no nulo
-- latitud decimal de 2 enteros y 2 flotantes
-- longitud decimal de 2 enteros y 2 flotantes
CREATE TABLE vacunatorios(
	id INT AUTO_INCREMENT PRIMARY KEY,
    direccion VARCHAR(100),
    numero INT NOT NULL,
    atencion_preferencial BOOLEAN NOT NULL DEFAULT TRUE, -- TRUE, True, 1
    latitud FLOAT(4, 2), -- FLOAT O DECIMAL es lo mismo
    longitud FLOAT(4, 2),
    
    -- columnas que van a cumplir como relaciones
    vacuna_id INT,
    
    -- RELACIONES
    -- crea una referencia entre las tablas vacunatorios (columna vacuna_id) y vacuna (columna id)
    -- se recomienda declarar al final
    -- formato recomendado: nombretabla_columna
    FOREIGN KEY (vacuna_id) REFERENCES vacunas(id)
);

-- faltó agregar AUTO_INCREMENT en columna id. solución DDL!
ALTER TABLE vacunatorios DROP COLUMN id; -- elimina columna id
ALTER TABLE vacunatorios ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY FIRST; -- FIRST para que se agregue como primera columna


INSERT INTO vacunatorios (id, direccion, numero, atencion_preferencial, latitud, longitud, vacuna_id) VALUES 
						 (DEFAULT, 'CALLE LOS PALITOS', 123, TRUE, 10.53, 14.80, 1),
                         (DEFAULT, 'AV GIRASOL', 1213, FALSE, 12.53, 19.80, 1),
                         (DEFAULT, 'HOSP. GNRAL.', 111, DEFAULT, 12.49, 80.15, 2),
                         (DEFAULT, 'POSTA CERRO 7 COLORES', 1485, DEFAULT, 10.53, 14.80, 3),
                         (DEFAULT, 'ESTADIO LOS AGUATEROS', 1489, FALSE, 20.52, 18.10, 4),
                         (DEFAULT, 'PLAZA DE ARMAS', 1256, FALSE, 12.54, 17.26, 4);

SELECT * FROM vacunatorios;

-- devolver lo siguiente:
-- direcciones y números con atención preferencial
SELECT direccion, numero FROM vacunatorios WHERE atencion_preferencial = 1;

-- direcciones que se encuentren entre lat > 20.00 y long < 20.00
SELECT direccion, numero FROM vacunatorios WHERE latitud > 20.00 AND longitud < 20.00;

-- direcciones que sean pfizer (1) y que tengan atención preferencial
SELECT direccion, numero FROM vacunatorios WHERE vacuna_id = 1 AND atencion_preferencial =  TRUE;

-- direcciones cuya vacuna no sea pfizer(1) (diferente que != ) o tengan atención preferencial
SELECT direccion, numero FROM vacunatorios WHERE vacuna_id != 1 OR atencion_preferencial =  TRUE;

-- JOINS
-- INNER JOIN
-- devuelve todas las columnas de la intersección de las tablas vacunas y vacunatorios
-- la intersección se forma con una columna en común a partir de los valores de id y vacuna_id
SELECT * FROM vacunas INNER JOIN vacunatorios; -- incorrecto
SELECT * FROM vacunas INNER JOIN vacunatorios ON vacunas.id = vacunatorios.vacuna_id; -- correcto

-- INNER JOIN renombrar columnas
SELECT vacunas.id, vacunatorios.id FROM vacunas INNER JOIN vacunatorios ON vacunas.id = vacunatorios.vacuna_id;
SELECT A.id as 'ID de las vacunas', B.id AS 'ID de los vacunatorios'
FROM vacunas AS A INNER JOIN vacunatorios AS B ON A.id = B.vacuna_id;

INSERT INTO vacunatorios (id, direccion, numero, atencion_preferencial, latitud, longitud, vacuna_id) VALUES 
						 (default, 'CALLE SIN NUMERO', 123, False, 10.00, 10.00, null);

-- LEFT JOIN
-- devuelve todo lo de la izquierda y lo de la derecha que coincida. En caso no coincida, será null
SELECT  * FROM vacunas LEFT JOIN vacunatorios ON vacunas.id = vacunatorios.vacuna_id; 

-- RIGHT JOIN
SELECT  * FROM vacunas RIGHT JOIN vacunatorios ON vacunas.id = vacunatorios.vacuna_id; 

CREATE TABLE campanias(
	id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100),
    fecha DATE,
    descripcion TEXT -- es como el VARCHAR pero sin límite de caracteres
);

INSERT INTO campanias (id, nombre, fecha, descripcion) VALUES 
					  (DEFAULT, 'PONGO EL HOMBRO', '2022-01-01', 'Campaña de vacunacion para personas adultas'),
                      (DEFAULT, 'VACUNA WARMA', '2022-03-10', 'Campaña de vacunacion para niños menores de 18 años'),
                      (DEFAULT, 'MAYORCITOS', '2021-11-04', 'Campaña de vacunacion para personas mayores a 65 años');
                      
-- RELACIÓN N a N 
-- tabla intermedia de vacunatorios y campanias 
CREATE TABLE vacunatorios_campanias(
	id INT PRIMARY KEY AUTO_INCREMENT,
    vacunatorio_id INT NOT NULL,
    campania_id INT NOT NULL,
	-- RELACIONES
    FOREIGN KEY (vacunatorio_id) REFERENCES vacunatorios(id),
	FOREIGN KEY (campania_id) REFERENCES campanias(id)
);

INSERT INTO vacunatorios_campanias (id, vacunatorio_id, campania_id) VALUES 
								   (DEFAULT, 1, 1),
								   (DEFAULT, 2, 1),
                                   (DEFAULT, 3, 1),
                                   (DEFAULT, 2, 2),
                                   (DEFAULT, 1, 2),
                                   (DEFAULT, 3, 3),
                                   (DEFAULT, 4, 3),
                                   (DEFAULT, 5, 3);

-- Desde la campania hacia el vacunatorio_campania
SELECT * FROM campanias as C INNER JOIN vacunatorios_campanias as VC ON C.id = VC.campania_id;