from classes.grafo import Grafo
from classes.vertice import Vertice
from classes.aresta import Aresta
from funcoes_auxiliares.initialize_single_source import initialize_single_source
from funcoes_auxiliares.extract_min import extract_min


def prim(grafo: Grafo, vertice_inicial: Vertice):
    initialize_single_source(grafo, vertice_inicial)
    Q = grafo.get_vertices()
    while len(Q) != 0:
        u = extract_min(Q)
        for v in grafo.buscar_vertices_adjacentes(u):
            if v in Q and grafo.buscar_aresta(u, v).get_peso_aresta() < v.get_distancia():
                v.set_antecessor(u)
                v.set_distancia(grafo.buscar_aresta(u, v).get_peso_aresta())
