import psycopg2

# Configuración de la conexión
connection_params = {
    'dbname': 'tienda_edutecno_DB', 
    'user': 'postgres',          
    'password': 'admin1234',    
    'host': 'localhost',           
    'port': '5432'                 
}

# Función para establecer la conexión a la base de datos
def connect_to_db():
    try:
        conn = psycopg2.connect(**connection_params)
        return conn
    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None
