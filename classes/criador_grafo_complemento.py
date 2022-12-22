from classes.aresta import Aresta
from classes.grafo import Grafo
from classes.tipo_aresta import TipoAresta
from classes.tipo_grafo import TipoGrafo
from classes.vertice import Vertice
from config import ALLOW_REFLEXIVE_RELATIONSHIP


class CriadorGrafoComplemento:
    @staticmethod
    def criar_grafo_complemento_a_partir_de_grafo(grafo: Grafo) -> Grafo:
        grafo_completo: Grafo = Grafo(grafo.get_tipo_grafo())
        tipo_arestas_grafo = TipoAresta.NAO_DIRECIONADO
        if grafo_completo.get_tipo_grafo() == TipoGrafo.DIRECIONADO:
            tipo_arestas_grafo = TipoAresta.ENTRADA
        valores_grafo: list[any] = list(map(lambda vertice: vertice.get_valor(), grafo.get_vertices()))
        [grafo_completo.adicionar_vertice(valor) for valor in valores_grafo]
        for valor_inicial_aresta in valores_grafo:
            vertice_inicial = Vertice(valor_inicial_aresta)
            for vertice_final in grafo_completo.get_vertices():
                if vertice_final.get_valor() == vertice_inicial.get_valor():
                    continue
                if not grafo.aresta_pertence_ao_grafo(Aresta(vertice_inicial, vertice_final, tipo_arestas_grafo)):
                    if not grafo_completo.aresta_pertence_ao_grafo(Aresta(vertice_inicial, vertice_final, tipo_arestas_grafo)):
                        grafo.adicionar_aresta(vertice_inicial, vertice_final, tipo_arestas_grafo)
        grafo_completo.set_vertices([])
        [grafo_completo.adicionar_vertice(valor) for valor in valores_grafo]
        return CriadorGrafoComplemento.__subtrair_grafo_completo_pelo_grafo_atual(grafo_completo, grafo)

    @staticmethod
    def __subtrair_grafo_completo_pelo_grafo_atual(grafo_completo: Grafo, grafo_parcial: Grafo) -> Grafo:
        for aresta in grafo_parcial.get_arestas():
            grafo_completo.remover_aresta(aresta.get_inicio_aresta(), aresta.get_fim_aresta())
        return grafo_completo
