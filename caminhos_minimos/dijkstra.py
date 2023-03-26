from classes.grafo import Grafo
from classes.vertice import Vertice
from funcoes_auxiliares.relax import relax
from funcoes_auxiliares.initialize_single_source import initialize_single_source
from funcoes_auxiliares.extract_min import extract_min


def dijkstra(g: Grafo, s: Vertice) -> list[Vertice]:
    initialize_single_source(g, s)
    S = []
    Q = g.get_vertices()
    while len(Q) != 0:
        u = extract_min(Q)
        S.append(u)
        for v in g.buscar_vertices_adjacentes(u):
            relax(u, v, g.buscar_aresta(u, v))
    return S

