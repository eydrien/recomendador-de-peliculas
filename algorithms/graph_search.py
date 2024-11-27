from collections import deque

def bfs(grafo, inicio, objetivo):
    visitados = set()
    cola = deque([inicio])

    while cola:
        nodo_actual = cola.popleft()

        if nodo_actual == objetivo:
            return True  # Encontrado

        if nodo_actual not in visitados:
            visitados.add(nodo_actual)
            cola.extend(grafo.lista_adyacencia[nodo_actual])

    return False  # No encontrado
