import copy

from classes.grafo import Grafo
from classes.vertice import Vertice
from funcoes_auxiliares.initialize_single_source import initialize_single_source
from funcoes_auxiliares.extract_min import extract_min
from funcoes_auxiliares.create_min_tree import create_min_tree


def prim(grafo: Grafo, vertice_inicial: Vertice) -> dict[str, list[str]]:
    initialize_single_source(grafo, vertice_inicial)
    vertices_grafo = grafo.get_vertices()[:]
    arestas = []
    Q = grafo.get_vertices()
    while len(Q) != 0:
        u = extract_min(Q)
        for v in grafo.buscar_vertices_adjacentes(u):
            aresta_u_v = grafo.buscar_aresta(u, v)
            if v in Q and aresta_u_v.get_peso_aresta() < v.get_distancia():
                v.set_antecessor(u)
                v.set_distancia(aresta_u_v.get_peso_aresta())
                arestas.append((u.get_valor(), v.get_valor(), aresta_u_v.get_peso_aresta()))
    return create_min_tree(vertices_grafo, arestas)
