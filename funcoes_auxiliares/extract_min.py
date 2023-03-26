from classes.vertice import Vertice
from config import INFINITE


def extract_min(q: list[Vertice]) -> Vertice:
    min_vtx = None
    min_distance = INFINITE
    vertice_escolhido = None
    for vertice in q:
        if vertice.get_distancia() < min_distance:
            min_vtx = vertice
            min_distance = vertice.get_distancia()
            vertice_escolhido = vertice
    q.remove(vertice_escolhido)
    return min_vtx
