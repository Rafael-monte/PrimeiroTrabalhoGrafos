from classes.grafo import Grafo
from classes.vertice import Vertice
from classes.aresta import Aresta
import sys
def arvore_geradora_minima_prim(grafo: Grafo, vertice_inicial: Vertice) -> list[Vertice]:
    for vertice in grafo.get_vertices():
        vertice.set_distancia(2 ** 63)
        vertice.set_antecessor(None)
    vertice_inicial.set_distancia(0)
    vertice_final = vertice_inicial
    q = grafo.get_vertices()
    while len(q) != 0:
        u = __extract_min(q, vertice_inicial, grafo)
        for v in grafo.buscar_vertices_adjacentes(u):
            if v in q and grafo.buscar_aresta(u, v).get_peso_aresta() < v.get_distancia():
                v.set_antecessor(u)
                v.set_distancia(grafo.buscar_aresta(u, v).get_peso_aresta())
                vertice_final = v
    return __criar_arvore_geradora(vertice_final, grafo)

def __criar_arvore_geradora(vertice_final: Vertice) -> list[Vertice]:
    lista = []
    vertice_atual = vertice_final
    while vertice_atual.get_antecessor() is not None:
        lista.append(vertice_atual)
        vertice_atual = vertice_atual.get_antecessor()
    lista.reverse()
    return lista

def __extract_min(queue: list[Vertice], vertice_inicial: Vertice, grafo: Grafo) -> Vertice:
    menor_distancia = 2 ** 63
    menor_vertice = None
    for vertice in queue:
        aresta_entre_incial_e_adj = grafo.buscar_aresta(vertice_inicial, vertice)
        if aresta_entre_incial_e_adj.get_peso_aresta() < menor_distancia:
            menor_vertice = vertice
            menor_distancia = aresta_entre_incial_e_adj.get_peso_aresta()
    queue.remove(vertice_inicial)
    return menor_vertice
