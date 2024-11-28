
# Lista de películas simulada
peliculas = [
    "Inception",
    "The Matrix",
    "Interstellar",
    "The Dark Knight",
    "Pulp Fiction",
    "The Godfather",
    "Titanic",
    "Avatar",
    "Forrest Gump",
    "The Shawshank Redemption"
]

# Función para obtener todas las películas
def get_movies():
    return peliculas

# Función para obtener una película por su índice (si es necesario)
def get_movie_by_id(movie_id):
    if 0 <= movie_id < len(peliculas):
        return peliculas[movie_id]
    return None
