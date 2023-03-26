from classes.vertice import Vertice
from classes.aresta import Aresta


def relax(u: Vertice, v: Vertice, u_v: Aresta):
    if v.get_distancia() > u.get_distancia() + u_v.get_peso_aresta():
        v.set_distancia(u.get_distancia() + u_v.get_peso_aresta())
        v.set_antecessor(u)
