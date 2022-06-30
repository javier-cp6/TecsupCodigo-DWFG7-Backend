-- Structured Query Language (lenguaje de consultas estructurado)
-- Registro: es un conjunto de datos
-- Dato: un valor que por sí solo no da una buena referencia
-- BD: está compuesta por una o varias tablas. Cada Tabla puede contener uno o varios registros
-- En el lenguaje de BD, el ";" sirve para indicar que una instrucción ha terminado

CREATE DATABASE prueba;
USE prueba;

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
