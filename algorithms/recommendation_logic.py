
def recomendar_peliculas(grafo, usuario, peliculas_vistas, peliculas_totales):
    recomendaciones = []
    for pelicula in peliculas_totales:
        if pelicula not in peliculas_vistas:
            if any(bfs(grafo, pelicula, vista) for vista in peliculas_vistas):
                recomendaciones.append(pelicula)
    return recomendaciones
