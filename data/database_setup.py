import sqlite3

def crear_base_datos():
    conexion = sqlite3.connect("recomendador.db")
    cursor = conexion.cursor()

    # Crear tabla de usuarios
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            genero_preferido TEXT
        )
    """)

    # Crear tabla de películas
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS peliculas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            genero TEXT,
            puntuacion REAL
        )
    """)

    # Crear tabla de usuarios y películas vistas
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios_peliculas (
            usuario_id INTEGER,
            pelicula_id INTEGER,
            FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
            FOREIGN KEY (pelicula_id) REFERENCES peliculas(id)
        )
    """)

    conexion.commit()
    conexion.close()
    print("Base de datos creada con éxito.")

if __name__ == "__main__":
    crear_base_datos()
