from classes.tipo_grafo import TipoGrafo
from classes.grafo import Grafo
from classes.tipo_aresta import TipoAresta
from config import INPUT_FILE_LOCATION


class LeitorArquivo:
    __arquivo_em_string: list[str] = ''
    __grafo: Grafo

    def ler_arquivo_entrada(self, input_file: str = INPUT_FILE_LOCATION) -> Grafo:
        with open(input_file, 'r') as arquivo_input:
            self.__arquivo_em_string = arquivo_input.readlines()
            self.__definir_tipo_grafo()
        self.__adicionar_arestas_e_vertices()
        return self.__grafo

    def __definir_tipo_grafo(self) -> None:
        tipo_grafo_em_string: str = self.__arquivo_em_string[0].replace('\n', '')
        if tipo_grafo_em_string == TipoGrafo.NAO_DIRECIONADO.value:
            self.__grafo = Grafo(TipoGrafo.NAO_DIRECIONADO)
            return
        self.__grafo = Grafo(TipoGrafo.DIRECIONADO)

    def __adicionar_arestas_e_vertices(self) -> None:
        # Percorre cada linha após header (primeira linha)
        tipo_aresta: TipoAresta = TipoAresta.NAO_DIRECIONADO
        if self.__grafo.get_tipo_grafo().value == TipoGrafo.DIRECIONADO.value:
            tipo_aresta = TipoAresta.ENTRADA
        for linha in self.__arquivo_em_string[1:]:
            linha_formatada: str = linha.replace('\n', '')
            elementos_linha: list[str] = linha_formatada.split(' ');
            primeiro_valor_vertice, segundo_valor_vertice, peso = elementos_linha[0], elementos_linha[1], elementos_linha[2]
            vertice_inicio, vertice_fim = self.__grafo.get_vertice(primeiro_valor_vertice), self.__grafo.get_vertice(segundo_valor_vertice)
            self.__grafo.adicionar_aresta(vertice_inicio, vertice_fim, tipo_aresta, int(peso))
