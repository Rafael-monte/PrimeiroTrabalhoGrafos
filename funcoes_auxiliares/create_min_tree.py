from classes.vertice import Vertice
from classes.aresta import Aresta
from classes.grafo import Grafo
from utils.iterators import filter_map_and_list


def create_min_tree(vertices: list[Vertice], lista_arestas: list[tuple[str, str, int]]) -> dict[str, list[str]]:
    vertices_grafo = vertices
    min_tree: dict[str, list[str]] = {}
    for vtx in vertices_grafo:
        vertices_conectados = filter_map_and_list(lambda t: t[0] == vtx.get_valor(), lambda t: t[1], lista_arestas)
        min_tree[vtx.get_valor()] = vertices_conectados
    return min_tree
