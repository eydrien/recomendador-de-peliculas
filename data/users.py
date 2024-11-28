
# Diccionario simulando usuarios y las películas que han visto
usuarios = {
    "user1": ["Inception", "The Matrix", "Interstellar"],
    "user2": ["The Dark Knight", "Avatar", "Forrest Gump"],
    "user3": ["Pulp Fiction", "The Godfather", "Titanic"],
    "user4": ["The Shawshank Redemption", "Avatar", "Inception"]
}

# Función para obtener el historial de películas vistas de un usuario
def get_user_history(user_id):
    return usuarios.get(user_id, [])
