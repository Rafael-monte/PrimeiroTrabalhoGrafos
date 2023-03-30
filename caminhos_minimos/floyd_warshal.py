from math import inf
from classes.grafo import Grafo

def floyd_warshall(graph: Grafo):
    vertex_map = graph.get_arestas_as_dict()
    n = len(vertex_map)
    # Cria a matriz com todos os valores como infinito
    matriz = [[inf for _ in range(n)] for _ in range(n)]

    # Coloca 0 na diagonal principal
    for i in range(n):
        matriz[i][i] = 0
    
    for vertex in graph.get_vertices():
        i = vertex_map[vertex.get_valor()]
        for neighbor, weight in graph.get_adjacentes_as_dict(vertex.get_valor())[vertex.get_valor()]:
            j = vertex_map[neighbor.get_valor()]
            matriz[i][j] = weight
    
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                matriz[i][j] = min(matriz[i][j], matriz[i][k] + matriz[k][j])

    return matriz