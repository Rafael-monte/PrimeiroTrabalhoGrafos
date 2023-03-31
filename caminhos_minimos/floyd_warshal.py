from math import inf
from classes.grafo import Grafo
import pprint

def print_matrix_floyd_warshall(graph, caminho_minimo):
    print("     ", end="")
    print(" ".join(f"{vertice:3}" for vertice in graph))
    print("")
    for i, row in enumerate(caminho_minimo):
        print(f"{list(graph.keys())[i]:3}", end="")
        print(" ".join(f"{x:3}" for x in row))

def floyd_warshall(graph: Grafo):
    dict_vertexes = graph.get_arestas_as_dict()
    n = len(dict_vertexes)
    # Cria a matriz com todos os valores como infinito
    matriz = [[inf for _ in range(n)] for _ in range(n)]

    # Coloca 0 na diagonal principal
    for i in range(n):
        matriz[i][i] = 0

    row = 0
    valores_vertices = list(map(lambda x: x.get_valor(), graph.get_vertices()))
    valores_vertices.sort()

    print(valores_vertices)
    for vertex in valores_vertices:
        tup = list(map(lambda tup: (tup[0].get_valor(), tup[1]), graph.get_adjacentes_as_dict(vertex)[vertex]))
        tup.sort()
        for neighbor, weight in tup:
            matriz[row][valores_vertices.index(neighbor)] = weight
        row += 1
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                matriz[i][j] = min(matriz[i][j], matriz[i][k] + matriz[k][j])
    pprint.pprint(matriz)
    return matriz
