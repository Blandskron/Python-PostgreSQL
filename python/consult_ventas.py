from db_connection import connect_to_db

def consultar_ventas():
    conn = connect_to_db()
    if conn:
        try:
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM ventas;")
                ventas = cursor.fetchall()
                print("Ventas:")
                for venta in ventas:
                    print(venta)
        except Exception as e:
            print(f"Error al consultar ventas: {e}")
        finally:
            conn.close()
