from classes.grafo import Grafo
from classes.vertice import Vertice
from funcoes_auxiliares.relax import relax
from funcoes_auxiliares.initialize_single_source import initialize_single_source


def bellman_ford(g: Grafo, s: Vertice) -> bool:
    initialize_single_source(g, s)
    for i in range(len(g.get_vertices())):
        for aresta in g.get_arestas():
            relax(aresta.get_inicio_aresta(), aresta.get_fim_aresta(), aresta)
    for aresta in g.get_arestas():
        if aresta.get_fim_aresta().get_distancia() > aresta.get_inicio_aresta().get_distancia() + aresta.get_peso_aresta():
            return False
    return True
