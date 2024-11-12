CREATE TABLE vendedor (
    vendedor_id SERIAL PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL
);

CREATE TABLE ventas (
    venta_id SERIAL PRIMARY KEY,
    fecha DATE NOT NULL,
    monto DECIMAL(10, 2) NOT NULL,
    vendedor_id INT NOT NULL,
    FOREIGN KEY (vendedor_id) REFERENCES vendedor(vendedor_id)
);
