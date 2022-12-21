from classes.tipo_aresta import TipoAresta
from classes.vertice import Vertice


class Aresta:
    __inicio_aresta: Vertice
    __fim_aresta: Vertice
    __tipo_aresta: TipoAresta

    def __init__(self, inicio_aresta: Vertice, fim_aresta: Vertice, tipo_aresta: TipoAresta):
        self.__inicio_aresta = inicio_aresta
        self.__fim_aresta = fim_aresta
        self.__tipo_aresta = tipo_aresta

    def set_inicio_aresta(self, inicio_aresta: Vertice) -> None:
        self.__inicio_aresta = inicio_aresta

    def get_inicio_aresta(self) -> Vertice:
        return self.__inicio_aresta

    def set_fim_aresta(self, fim_aresta: Vertice) -> None:
        self.__fim_aresta = fim_aresta

    def get_fim_aresta(self) -> Vertice:
        return self.__fim_aresta

    def set_tipo_aresta(self, tipo_aresta: TipoAresta) -> None:
        self.__tipo_aresta = tipo_aresta

    def get_tipo_aresta(self) -> TipoAresta:
        return self.__tipo_aresta
