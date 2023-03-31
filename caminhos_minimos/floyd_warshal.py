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

    row, col = 0, 0
    valores_vertices = list(map(lambda x: x.get_valor(), graph.get_vertices()))
    valores_vertices.sort()
    for vertex in valores_vertices:
        for neighbor, weight in graph.get_adjacentes_as_dict(vertex)[vertex]:
            matriz[row][col] = weight
            col += 1
        row += 1
        col = 0
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                matriz[i][j] = min(matriz[i][j], matriz[i][k] + matriz[k][j])

    return matriz
