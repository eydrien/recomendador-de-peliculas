# Importa las funciones necesarias
import sys
import os

# Agrega el directorio raíz al PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from algorithms.recommendation_logic import recomendar_peliculas
from data.movies import get_movies
from data.users import get_user_history

def main():
    print("¡Bienvenido al Sistema de Recomendación de Películas!")
    # Obtener lista de películas desde la base de datos
    peliculas = get_movies()
    print("\nCatálogo de Películas:")
    for idx, pelicula in enumerate(peliculas):
        print(f"{idx + 1}. {pelicula}")

    # Obtener historial del usuario (simulado)
    user_id = input("\nIntroduce tu ID de usuario para recomendaciones: ")
    peliculas_vistas = get_user_history(user_id)
    print("\nHas visto las siguientes películas:")
    for pelicula in peliculas_vistas:
        print(f"- {pelicula}")

    # Generar recomendaciones
    print("\nCalculando recomendaciones...")
    recomendaciones = recomendar_peliculas(user_id)
    
    if recomendaciones:
        print("\nTe recomendamos estas películas:")
        for pelicula in recomendaciones:
            print(f"- {pelicula}")
    else:
        print("\nNo encontramos recomendaciones para ti. ¡Explora nuestro catálogo!")

if __name__ == "__main__":
    main()
