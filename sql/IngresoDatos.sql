-- Ingresar vendedores
INSERT INTO vendedor (nombre, apellido) VALUES
('Carlos', 'Perez'),
('Maria', 'Gomez'),
('Juan', 'Lopez'),
('Ana', 'Martinez'),
('Pedro', 'Jimenez');

-- Ingresar ventas
INSERT INTO ventas (fecha, monto, vendedor_id) VALUES
('2024-11-01', 500.00, 1),
('2024-11-02', 700.00, 2),
('2024-11-03', 650.00, 1),
('2024-11-05', 800.00, 3),
('2024-11-07', 900.00, 2),
('2024-11-10', 750.00, 4),
('2024-11-12', 300.00, 5),
('2024-11-15', 1000.00, 1),
('2024-11-18', 450.00, 3),
('2024-11-20', 600.00, 4);
