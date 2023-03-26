from classes.vertice import Vertice
from classes.aresta import Aresta
from classes.grafo import Grafo
from config import INFINITE


def initialize_single_source(g: Grafo, s: Vertice):
    for v in g.get_vertices():
        v.set_distancia(INFINITE)
        v.set_antecessor(None)
    s.set_distancia(0)
