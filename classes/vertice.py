class Vertice:
    pass
class Vertice:
    __valor: any
    __antecessor: Vertice = None
    __distancia: int = -1

    def __init__(self, valor: any, antecessor: Vertice = None, distancia: int = -1):
        self.__valor = valor
        self.__antecessor = antecessor
        self.__distancia = distancia

    def get_valor(self) -> any:
        return self.__valor

    def set_valor(self, valor: any) -> None:
        self.__valor = valor

    def get_distancia(self) -> int:
        return self.__distancia

    def set_distancia(self, distancia: int) -> None:
        self.__distancia = distancia

    def get_antecessor(self) -> Vertice:
        return self.__antecessor

    def set_antecessor(self, vertice: Vertice) -> None:
        self.__antecessor = vertice

    def __eq__(self, other: Vertice) -> bool:
        NOT_EQUAL, EQUAL = False, True

        if self.__distancia != other.__distancia:
            return NOT_EQUAL

        if self.__antecessor != other.__antecessor:
            return NOT_EQUAL

        if self.__valor != other.__valor:
            return NOT_EQUAL

        return EQUAL
