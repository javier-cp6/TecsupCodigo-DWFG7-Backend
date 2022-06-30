-- Structured Query Language (lenguaje de consultas estructurado)
-- Registro: es un conjunto de datos
-- Dato: un valor que por sí solo no da una buena referencia
-- BD: está compuesta por una o varias tablas. Cada Tabla puede contener uno o varios registros
-- En el lenguaje de BD, el ";" sirve para indicar que una instrucción ha terminado

CREATE DATABASE prueba;
USE prueba;

-- DDL
-- DDL Data Definition Language
-- definir la estructura a manejar en la bd (crear, modificar y eliminar tablas o DB)

creAte TabLe productos(
	-- por convención se declara con mayúsculas y se nombra a una tabla en plural
	-- para crear una tabla, obligatoriamente debe declararse al menos una columna
    -- se puede usar auto_increment una sola vez por tabla
    -- Primary Key: indica que la columna se comporta como identificadora del registro
    -- Nombre | Tipo de dato | [configuraciones adicionales]
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50),
    fecha_vencimiento DATE
);

-- DML Data Manipulation Language
-- extraer, insertar o elimnar información

-- INSERT (insertar nueva información)
INSERT INTO productos (id, nombre, fecha_vencimiento) VALUES (DEFAULT, 'Aguaymanto', '2022-07-01');
INSERT INTO productos (id, nombre, fecha_vencimiento) VALUES (DEFAULT, 'Cebolla', '2022-07-10'),
															 (DEFAULT, 'Limón', '2022-06-30');

-- SELECT
SELECT nombre FROM productos;
SELECT nombre, fecha_vencimiento, id FROM productos;
SELECT * FROM productos;
SELECT nombre, fecha_vencimiento AS 'Fecha de Vencimiento', id FROM productos;
SELECT * FROM productos WHERE nombre = 'Cebolla';

-- AND
SELECT * FROM productos WHERE nombre= 'Cebolla' AND id = 2;
-- OR
SELECT * FROM productos WHERE nombre= 'Cebolla' OR id = 1;

SELECT * FROM productos
WHERE nombre = 'Cebolla' OR
	  id = 1 OR
	  (id = 3 AND
      nombre = 'Limón');

-- % representa un número no determinado de caracteres
SELECT * FROM productos WHERE NOMBRE LIKE 'Agua%';

SELECT * FROM productos WHERE NOMBRE LIKE '%a%o%';

-- _ reperesenta un caracter y respeta la posición
SELECT * FROM productos WHERE NOMBRE LIKE '___a%';

-- EN MS SQL SERVER: permite indicar entre corchetes el primer caracter []:
-- SELECT * FROM productos WHERE NOMBRE LIKE '[CL]%';

-- UPDATE
UPDATE productos SET nombre = 'Cebolla china' WHERE nombre = 'ceBollA'; 
-- Devuelve error porque MySQl se encuentra por defecto en modo seguro, el cual impide actualizar columnas si es que no se tiene en la condición a una columna UNIQUE o que sea una KEY
-- Desactivar modo seguro (no recomendado, dado que podrían ejecutarse modificaciones o eliminaciones masivas que no pueden deshacerse)
SET SQL_SAFE_UPDATES = false;

