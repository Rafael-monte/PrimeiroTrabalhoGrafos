from classes.grafo import Grafo
from classes.leitor_arquivo import LeitorArquivo
from classes.vertice import Vertice

if __name__ == '__main__':
    leitor: LeitorArquivo = LeitorArquivo()
    grafo: Grafo = leitor.ler_arquivo_entrada()
    grafo.mostrar_grafo()
    vertices_incidentes_ao_b = grafo.buscar_vertices_incidentes(Vertice('b'))
    vertices_incidentes_ao_e = grafo.buscar_vertices_incidentes(Vertice('e'))
