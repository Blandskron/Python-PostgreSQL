from db_connection import connect_to_db

def insertar_venta():
    vendedor_id = int(input("Ingrese el ID del vendedor: "))
    fecha = input("Ingrese la fecha de la venta (YYYY-MM-DD): ")
    monto = float(input("Ingrese el monto de la venta: "))
    
    conn = connect_to_db()
    if conn:
        try:
            with conn.cursor() as cursor:
                cursor.execute("INSERT INTO ventas (vendedor_id, fecha, monto) VALUES (%s, %s, %s);", 
                               (vendedor_id, fecha, monto))
                conn.commit()
                print(f"Venta de {monto} insertada correctamente para el vendedor con ID {vendedor_id}")
        except Exception as e:
            print(f"Error al insertar venta: {e}")
        finally:
            conn.close()
