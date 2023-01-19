from classes.grafo import Grafo
from classes.tipo_grafo import TipoGrafo
from classes.vertice import Vertice
from classes.tipo_aresta import TipoAresta

class CriadorGrafoTransposto:
    @staticmethod
    def criar_grafo_transposto_a_partir_de_grafo(grafo: Grafo) -> Grafo:
        grafo_transposto: Grafo = Grafo(grafo.get_tipo_grafo())
        if grafo.get_tipo_grafo() == TipoGrafo.NAO_DIRECIONADO:
            grafo_transposto.set_arestas(grafo.get_arestas())
            return grafo_transposto
        arestas_grafo: list[Aresta] = grafo.get_arestas()[:]
        for aresta in arestas_grafo:
            grafo_transposto.adicionar_aresta(aresta.get_fim_aresta(), aresta.get_inicio_aresta(), aresta.get_tipo_aresta())
        return grafo_transposto

