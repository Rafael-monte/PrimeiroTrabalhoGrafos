from classes.criador_grafo_transposto import CriadorGrafoTransposto
from classes.grafo import Grafo
from classes.vertice import Vertice
from classes.aresta import Aresta
from classes.tipo_aresta import TipoAresta
from classes.leitor_arquivo import LeitorArquivo
from arvores_geradoras_minimas.algoritmo_prim import arvore_geradora_minima_prim
# autores: Rafael Monteiro Zancanaro & Robson Oliveira de Souza

if __name__ == '__main__':
    leitor: LeitorArquivo = LeitorArquivo()
    grafo: Grafo = leitor.ler_arquivo_entrada()
    vertices: list[Vertice] = arvore_geradora_minima_prim(grafo, grafo.get_vertice('a'))
    [print(f'{vertice.get_valor()}') for vertice in vertices]
