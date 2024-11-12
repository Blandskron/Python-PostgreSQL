from db_connection import connect_to_db

def insertar_vendedor():
    nombre = input("Ingrese el nombre del vendedor: ")
    apellido = input("Ingrese el apellido del vendedor: ")
    
    conn = connect_to_db()
    if conn:
        try:
            with conn.cursor() as cursor:
                cursor.execute("INSERT INTO vendedor (nombre, apellido) VALUES (%s, %s);", (nombre, apellido))
                conn.commit()
                print(f"Vendedor {nombre} {apellido} insertado correctamente")
        except Exception as e:
            print(f"Error al insertar vendedor: {e}")
        finally:
            conn.close()
