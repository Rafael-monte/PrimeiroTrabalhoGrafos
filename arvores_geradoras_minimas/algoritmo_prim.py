import copy
import heapq
from classes.grafo import Grafo
from classes.vertice import Vertice
from funcoes_auxiliares.initialize_single_source import initialize_single_source
from funcoes_auxiliares.extract_min import extract_min
from funcoes_auxiliares.create_min_tree import create_min_tree


def prim(grafo: Grafo, vertice_inicial: Vertice) -> dict[str, list[str]]:
    initialize_single_source(grafo, vertice_inicial)
    vertices_grafo = grafo.get_vertices()[:]
    arestas = [(0, vertice_inicial.get_valor())]
    mst = {}
    visited = set()
    heapq.heapify(arestas)
    while arestas:
        # Get the node with the minimum weight from the priority queue
        weight, node = heapq.heappop(arestas)
        # If the node has already been visited, continue to the next iteration
        if node in visited:
            continue

        # Mark the node as visited
        visited.add(node)
        if node != vertice_inicial.get_valor():
            mst[node] = weight
        # # Process the adjacent nodes
        for adj_node, adj_weight in grafo.get_adjacentes_as_dict(node)[node]:
            # If the adjacent node has not been visited yet, add it to the priority queue
            if adj_node.get_valor() not in visited:
                heapq.heappush(arestas, (adj_weight, adj_node.get_valor()))

        # # Return the visited set
    return mst
