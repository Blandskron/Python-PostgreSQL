# Proyecto Tienda EduTecno - Sistema de Gestión de Ventas

Este proyecto implementa un sistema de gestión de ventas en Python con conexión a una base de datos PostgreSQL. El sistema permite insertar vendedores y ventas, consultar datos de las tablas, y realizar una consulta para obtener el mejor vendedor del mes.

## Tabla de Contenidos

- [Descripción del Proyecto](#descripción-del-proyecto)
- [Requisitos](#requisitos)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Configuración](#configuración)
- [Base de Datos](#base-de-datos)
- [Funciones Principales](#funciones-principales)
- [Uso](#uso)
- [Ejemplo de Flujo de Trabajo](#ejemplo-de-flujo-de-trabajo)
- [Archivo `.gitignore`](#archivo-gitignore)

## Descripción del Proyecto

El sistema se desarrolló en Python utilizando la librería `psycopg2` para conectar con una base de datos PostgreSQL llamada `tienda_edutecno_DB`. Este sistema incluye un menú principal que permite:
1. Insertar un nuevo vendedor.
2. Insertar una nueva venta.
3. Consultar todos los vendedores.
4. Consultar todas las ventas.
5. Consultar el mejor vendedor del mes.

## Requisitos

- Python 3
- PostgreSQL
- Librería `psycopg2` para Python (se puede instalar con `pip install psycopg2`)

## Estructura del Proyecto

El proyecto se ha modularizado, separando cada función en archivos individuales para facilitar el mantenimiento y la expansión.

```
project-root/
│
├── db_connection.py           # Conexión a la base de datos
├── insert_vendedor.py         # Función para insertar un vendedor
├── insert_venta.py            # Función para insertar una venta
├── consult_vendedores.py      # Función para consultar vendedores
├── consult_ventas.py          # Función para consultar ventas
├── consult_mejor_vendedor.py   # Función para consultar el mejor vendedor del mes
├── main.py                    # Menú principal que gestiona todas las funciones
├── .gitignore                 # Ignorar el entorno virtual 'venv'
└── README.md                  # Archivo de documentación
```

## Configuración

1. Clona este repositorio y navega al directorio del proyecto:

    ```bash
    git clone https://github.com/tu_usuario/tu_proyecto.git
    cd tu_proyecto
    ```

2. Crea y activa un entorno virtual (opcional pero recomendado):

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # En Linux/macOS
    venv\Scripts\activate      # En Windows
    ```

3. Instala la librería `psycopg2` para conectar Python con PostgreSQL:

    ```bash
    pip install psycopg2
    ```

4. Modifica los parámetros de conexión en el archivo `db_connection.py` para que coincidan con la configuración de tu base de datos PostgreSQL.

## Base de Datos

### Creación de Tablas

Usa el siguiente código SQL para crear las tablas necesarias en PostgreSQL:

```sql
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
```

### Relación de Tablas

La tabla `ventas` está relacionada con `vendedor` a través del campo `vendedor_id`, lo que permite consultar las ventas de cada vendedor.

## Funciones Principales

Cada funcionalidad está separada en un archivo individual para facilitar la modularidad.

1. **`db_connection.py`**: Contiene la función `connect_to_db()` para establecer la conexión con la base de datos.
2. **`insert_vendedor.py`**: Permite insertar un nuevo vendedor pidiendo `nombre` y `apellido` al usuario.
3. **`insert_venta.py`**: Permite insertar una venta, solicitando el `vendedor_id`, `fecha`, y `monto` de la venta.
4. **`consult_vendedores.py`**: Muestra una lista de todos los vendedores.
5. **`consult_ventas.py`**: Muestra una lista de todas las ventas.
6. **`consult_mejor_vendedor.py`**: Realiza una consulta para obtener el mejor vendedor de un mes y año específicos, basándose en el monto total de ventas.

## Uso

1. Ejecuta el archivo `main.py` para acceder al menú principal:

    ```bash
    python main.py
    ```

2. Sigue las instrucciones del menú para realizar cada acción.

### Menú Principal

- Opción 1: Inserta un nuevo vendedor solicitando el `nombre` y `apellido`.
- Opción 2: Inserta una venta pidiendo el `vendedor_id`, `fecha`, y `monto`.
- Opción 3: Consulta todos los vendedores y muestra sus detalles.
- Opción 4: Consulta todas las ventas y muestra sus detalles.
- Opción 5: Consulta el mejor vendedor del mes y año especificados, mostrando su `nombre`, `apellido`, y `total de ventas`.
- Opción 6: Salir del programa.

## Ejemplo de Flujo de Trabajo

### Ejemplo de inserción de datos y consulta en el sistema:

1. Ejecuta el menú principal:

    ```bash
    python main.py
    ```

2. Selecciona **Opción 1** e ingresa un nuevo vendedor (ej., Juan Pérez).
3. Selecciona **Opción 2** e ingresa una venta (ej., vendedor_id = 1, fecha = 2024-11-15, monto = 500).
4. Selecciona **Opción 3** para ver la lista de vendedores.
5. Selecciona **Opción 4** para ver la lista de ventas.
6. Selecciona **Opción 5**, ingresa el mes y año (11 y 2024) para ver el mejor vendedor del mes.

## Archivo `.gitignore`

Para ignorar el entorno virtual en Git, incluye un archivo `.gitignore` en el directorio raíz del proyecto con el siguiente contenido:

```plaintext
# Ignorar el entorno virtual
venv/
```

De esta forma, el entorno `venv` no se subirá al repositorio en GitHub.

## Notas Finales

Este sistema es una implementación básica para gestionar y consultar ventas en una base de datos PostgreSQL, permitiendo una estructura modular y clara. Se puede expandir fácilmente para incluir más funcionalidades, como reportes automáticos y gráficos de análisis.
