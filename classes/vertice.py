class Vertice:
    __valor: any

    def __init__(self, valor: any):
        self.__valor = valor

    def get_valor(self) -> any:
        return self.__valor

    def set_valor(self, valor: any) -> None:
        self.__valor = valor
