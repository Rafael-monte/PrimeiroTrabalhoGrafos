from classes.criador_grafo_complemento import CriadorGrafoComplemento
from classes.grafo import Grafo
from classes.leitor_arquivo import LeitorArquivo

if __name__ == '__main__':
    leitor: LeitorArquivo = LeitorArquivo()
    grafo: Grafo = leitor.ler_arquivo_entrada()
    grafo.criar_matriz_adjacencias()
    print('----------------------------------------------------')
    grafo_complemento: Grafo = CriadorGrafoComplemento.criar_grafo_complemento_a_partir_de_grafo(grafo)
    #grafo_complemento.mostrar_grafo()
    grafo_complemento.criar_matriz_adjacencias()
