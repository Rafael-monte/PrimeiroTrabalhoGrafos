from classes.criador_grafo_transposto import CriadorGrafoTransposto
from classes.grafo import Grafo
from classes.vertice import Vertice
from classes.aresta import Aresta
from classes.tipo_aresta import TipoAresta
from classes.leitor_arquivo import LeitorArquivo
# autores: Rafael Monteiro Zancanaro & Robson Oliveira de Souza

if __name__ == '__main__':
    leitor: LeitorArquivo = LeitorArquivo()
    grafo: Grafo = leitor.ler_arquivo_entrada()
    #grafo_complemento: Grafo = CriadorGrafoTransposto.criar_grafo_transposto_a_partir_de_grafo(grafo)
