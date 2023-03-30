from classes.criador_grafo_transposto import CriadorGrafoTransposto
from classes.grafo import Grafo
from classes.vertice import Vertice
from classes.aresta import Aresta
from classes.tipo_aresta import TipoAresta
from classes.leitor_arquivo import LeitorArquivo
from arvores_geradoras_minimas.algoritmo_prim import prim
from caminhos_minimos.dijkstra import dijkstra
from caminhos_minimos.bellman_ford import bellman_ford
from funcoes_auxiliares.create_min_tree import create_min_tree
from arvores_geradoras_minimas.kruskal import kruskal
# autores: Rafael Monteiro Zancanaro & Robson Oliveira de Souza

if __name__ == '__main__':
    leitor: LeitorArquivo = LeitorArquivo()
    grafo: Grafo = leitor.ler_arquivo_entrada()
    # lista_djikstra = dijkstra(grafo, grafo.get_vertice('a'))
    # print(f"{list(map(lambda vtx: vtx.get_valor(), lista_djikstra))}")
    # resultado_bellman_ford = bellman_ford(grafo, grafo.get_vertice('a'))
    # print(f"{resultado_bellman_ford}")
    # print(prim(grafo, grafo.get_vertice('a')))
    print(kruskal(grafo))