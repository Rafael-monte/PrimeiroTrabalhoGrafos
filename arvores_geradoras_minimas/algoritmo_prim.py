import copy
import heapq
from classes.grafo import Grafo
from classes.vertice import Vertice
from funcoes_auxiliares.initialize_single_source import initialize_single_source


def prim(grafo: Grafo, vertice_inicial: Vertice):
    initialize_single_source(grafo, vertice_inicial)
    arestas = [(0, vertice_inicial.get_valor())]
    arvore_geradora_minima = {}
    visitados = set()
    heapq.heapify(arestas)
    while arestas:
        # Tira o vertice com menor distancia da heap
        peso_aresta, valor_vertice = heapq.heappop(arestas)
        # Se o vertice já tiver sido visitado, pula a iteração
        if valor_vertice in visitados:
            continue

        # Coloca o vertice na lista de visitados
        visitados.add(valor_vertice)

        # Se o valor do vertice é diferente do valor do vertice inicial, adiciona uma nova entrada no dicionário que será a mst
        if valor_vertice != vertice_inicial.get_valor():
            # O formato do vertice representa => {folha que está conectada: peso da aresta que liga ele com o vertice anterior}
            arvore_geradora_minima[valor_vertice] = peso_aresta
        
        # Pega os vertices adjacentes e o peso das arestas que ligam o vertice sendo processado a elas
        for vertice_adj, peso_aresta_adj in grafo.get_adjacentes_as_dict(valor_vertice)[valor_vertice]:
            # Se o vertice não foi visitado, é colocado na heap
            if vertice_adj.get_valor() not in visitados:
                heapq.heappush(arestas, (peso_aresta_adj, vertice_adj.get_valor()))
    
    return arvore_geradora_minima
