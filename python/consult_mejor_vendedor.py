from db_connection import connect_to_db

def consultar_mejor_vendedor():
    mes = int(input("Ingrese el número de mes (1-12): "))
    anio = int(input("Ingrese el año (YYYY): "))
    
    conn = connect_to_db()
    if conn:
        try:
            query = """
                SELECT v.nombre, v.apellido, SUM(ve.monto) AS total_ventas
                FROM vendedor v
                JOIN ventas ve ON v.vendedor_id = ve.vendedor_id
                WHERE DATE_PART('month', ve.fecha) = %s AND DATE_PART('year', ve.fecha) = %s
                GROUP BY v.vendedor_id, v.nombre, v.apellido
                ORDER BY total_ventas DESC
                LIMIT 1;
            """
            with conn.cursor() as cursor:
                cursor.execute(query, (mes, anio))
                result = cursor.fetchone()
                
                if result:
                    nombre, apellido, total_ventas = result
                    print(f"Mejor vendedor del mes: {nombre} {apellido} con ventas totales de {total_ventas}")
                else:
                    print("No se encontraron resultados para el mes y año especificados.")
        except Exception as e:
            print(f"Error en la consulta: {e}")
        finally:
            conn.close()
