from db_connection import connect_to_db

def consultar_vendedores():
    conn = connect_to_db()
    if conn:
        try:
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM vendedor;")
                vendedores = cursor.fetchall()
                print("Vendedores:")
                for vendedor in vendedores:
                    print(vendedor)
        except Exception as e:
            print(f"Error al consultar vendedores: {e}")
        finally:
            conn.close()