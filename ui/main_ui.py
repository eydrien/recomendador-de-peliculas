from algorithms.recommendation_logic import recomendar_peliculas
from data.graph_representation import Grafo

import sys
import os

# Agrega el directorio raíz al PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def interfaz_usuario():
    print("¡Bienvenido al sistema de recomendación de películas!")
    usuarios = ["Carlos", "María", "Ana"]
    peliculas = ["Inception", "Titanic", "Matrix", "Avengers"]

    print("\nUsuarios disponibles:")
    for idx, usuario in enumerate(usuarios):
        print(f"{idx}. {usuario}")

    usuario_idx = int(input("\nSelecciona tu usuario: "))
    usuario = usuarios[usuario_idx]

    print("\nPelículas disponibles:")
    for idx, pelicula in enumerate(peliculas):
        print(f"{idx}. {pelicula}")

    peliculas_vistas = [int(x) for x in input("\nSelecciona las películas vistas (separadas por coma): ").split(",")]

    grafo = Grafo(len(peliculas))
    grafo.agregar_arista(0, 1)  # Conectar películas similares
    grafo.agregar_arista(1, 2)
    grafo.agregar_arista(2, 3)

    recomendaciones = recomendar_peliculas(grafo, usuario, peliculas_vistas, range(len(peliculas)))

    print("\nPelículas recomendadas:")
    for rec in recomendaciones:
        print(peliculas[rec])

if __name__ == "__main__":
    interfaz_usuario()
