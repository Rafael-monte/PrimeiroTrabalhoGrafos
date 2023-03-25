from classes.tipo_aresta import TipoAresta
from classes.vertice import Vertice

class Aresta:
    pass
class Aresta:
    __inicio_aresta: Vertice
    __fim_aresta: Vertice
    __tipo_aresta: TipoAresta
    __peso: int

    def __init__(self, inicio_aresta: Vertice, fim_aresta: Vertice, tipo_aresta: TipoAresta, peso: int = 0):
        self.__inicio_aresta = inicio_aresta
        self.__fim_aresta = fim_aresta
        self.__tipo_aresta = tipo_aresta
        self.__peso = peso

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

    def set_peso_aresta(self, peso: int) -> None:
        self.__peso = peso

    def get_peso_aresta(self) -> int:
        return self.__peso

    def __eq__(self, other: Aresta) -> bool:
        NOT_EQUAL, EQUAL = False, True
        if self.__peso != other.get_peso_aresta():
            return NOT_EQUAL
        if self.__inicio_aresta != other.__inicio_aresta:
            return NOT_EQUAL
        if self.__fim_aresta != other.__fim_aresta:
            return NOT_EQUAL
        if self.__peso != other.__peso:
            return NOT_EQUAL
        if self.__tipo_aresta != other.__tipo_aresta:
            return NOT_EQUAL

        return EQUAL
