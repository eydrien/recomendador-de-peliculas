class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices
        self.matriz_adyacencia = [[0 for _ in range(vertices)] for _ in range(vertices)]
        self.lista_adyacencia = {i: [] for i in range(vertices)}

    def agregar_arista(self, origen, destino):
        # Matriz de adyacencia
        self.matriz_adyacencia[origen][destino] = 1
        self.matriz_adyacencia[destino][origen] = 1  # No dirigido

        # Lista de adyacencia
        self.lista_adyacencia[origen].append(destino)
        self.lista_adyacencia[destino].append(origen)

    def mostrar_grafo(self):
        print("Matriz de Adyacencia:")
        for fila in self.matriz_adyacencia:
            print(fila)

        print("\nLista de Adyacencia:")
        for vertice, adyacentes in self.lista_adyacencia.items():
            print(f"{vertice}: {adyacentes}")
