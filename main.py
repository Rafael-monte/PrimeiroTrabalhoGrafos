from classes.grafo import Grafo
from classes.leitor_arquivo import LeitorArquivo

if __name__ == '__main__':
    leitor: LeitorArquivo = LeitorArquivo()
    grafo: Grafo = leitor.ler_arquivo_entrada()
    grafo.criar_matriz_adjacencias()

