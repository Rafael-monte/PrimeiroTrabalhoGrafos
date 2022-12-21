from classes.tipo_grafo import TipoGrafo
from classes.aresta import Aresta
from classes.tipo_aresta import TipoAresta
from classes.vertice import Vertice


class Grafo:
    __arestas: list[Aresta] = []
    __vertices: list[Vertice] = []
    __tipo_grafo: TipoGrafo

    def __init__(self, tipo_grafo: TipoGrafo):
        self.__tipo_grafo = tipo_grafo

    def adicionar_vertice(self, valor: any) -> None:
        self.__vertices.append(Vertice(valor))
        # Ordena os vertices em ordem alfabetica
        self.__vertices.sort(key=lambda vertice: vertice.get_valor())

    def adicionar_aresta(self, inicio: Vertice, fim: Vertice, tipo_aresta: TipoAresta) -> None:
        self.__arestas.append(Aresta(inicio, fim, tipo_aresta))
        if self.__tipo_grafo.value == TipoGrafo.NAO_DIRECIONADO.value:
            self.__arestas.append(Aresta(fim, inicio, tipo_aresta))

    def __procurar_vertice_no_grafo(self, valor_vertice: any) -> list[Vertice]:
        filtro_vertices: filter = filter(lambda vertice: vertice.get_valor() == valor_vertice, self.__vertices)
        return list(filtro_vertices)

    def get_tipo_grafo(self) -> TipoGrafo:
        return self.__tipo_grafo

    def get_vertice(self, valor: any):
        vertices: list[Vertice] = self.__procurar_vertice_no_grafo(valor)
        if len(vertices) > 0:
            return vertices[0]
        vertice: Vertice = Vertice(valor)
        self.__vertices.append(vertice)
        return vertice

    def __existe_relacao_entre_vertices(self, vertice_inicio: Vertice, vertice_fim: Vertice) -> bool:
        filtro_relacao: filter = filter(lambda aresta: aresta.get_inicio_aresta().get_valor() == vertice_inicio.get_valor() and aresta.get_fim_aresta().get_valor() == vertice_fim.get_valor(), self.__arestas)
        return len(list(filtro_relacao)) > 0

    def aresta_pertence_ao_grafo(self, aresta: Aresta):
        return self.__existe_relacao_entre_vertices(aresta.get_inicio_aresta(), aresta.get_fim_aresta())

    def mostrar_grafo(self):
        print('Vertices')
        for vertice in self.__vertices:
            print(vertice.get_valor())
        print('Arestas')
        tipo_relacao: str = '<->'
        if self.get_tipo_grafo() == TipoGrafo.DIRECIONADO:
            tipo_relacao = '->'
        for aresta in self.__arestas:
            print(f'{aresta.get_inicio_aresta().get_valor()} {tipo_relacao} {aresta.get_fim_aresta().get_valor()}')

    def criar_matriz_adjacencias(self) -> None:
        matriz: list[list[int]] = []
        for i in range(len(self.__vertices)):
            matriz.append([])
            for j in range(len(self.__vertices)):
                if self.__existe_relacao_entre_vertices(self.__vertices[i], self.__vertices[j]):
                    matriz[i].append(1)
                else:
                    matriz[i].append(0)
        self.__printar_matriz_adjacencias(matriz)

    def __printar_matriz_adjacencias(self, matriz):
        for i in range(len(self.__vertices)):
            print(f'{self.__vertices[i].get_valor()} |{" ".join(str(matriz[i]))}|')

