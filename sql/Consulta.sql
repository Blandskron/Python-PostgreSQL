SELECT v.nombre, v.apellido, SUM(ve.monto) AS total_ventas
FROM vendedor v
JOIN ventas ve ON v.vendedor_id = ve.vendedor_id
WHERE DATE_PART('month', ve.fecha) = 11 AND DATE_PART('year', ve.fecha) = 2024
GROUP BY v.vendedor_id, v.nombre, v.apellido
ORDER BY total_ventas DESC
LIMIT 1;
