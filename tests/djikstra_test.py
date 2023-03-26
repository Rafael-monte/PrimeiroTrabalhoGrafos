import unittest

from classes.grafo import Grafo
from classes.leitor_arquivo import LeitorArquivo
from caminhos_minimos.dijkstra import dijkstra
from utils.iterators import map_and_list


class MyTestCase(unittest.TestCase):
    reader: LeitorArquivo
    caminho_minimo_partindo_de_d = list[str]
    caminho_minimo_partindo_de_c = list[str]
    caminho_arquivo_grafo: str

    @classmethod
    def setUpClass(cls) -> None:
        cls.reader = LeitorArquivo()
        cls.caminho_minimo_partindo_de_d = ['d', 'a', 'e', 'b', 'f', 'c']
        cls.caminho_minimo_partindo_de_c = ['c', 'b', 'f', 'e', 'a', 'd']
        cls.caminho_arquivo_grafo = '/home/rafael/Downloads/trabalho-grafos/Trabalho_1_Rafael_Robson/PrimeiroTrabalhoGrafos/input/grafo.txt'

    # Fazer um teste de cada vez

    def test_ao_informar_vertice_d_trazer_menor_caminho(self):
        grafo: Grafo = self.reader.ler_arquivo_entrada(self.caminho_arquivo_grafo)
        caminho_partindo_de_c = dijkstra(grafo, grafo.get_vertice('c'))
        valores_caminho_minimo_partindo_de_c = map_and_list(lambda vtx: vtx.get_valor(), caminho_partindo_de_c)
        self.assertEqual(valores_caminho_minimo_partindo_de_c, self.caminho_minimo_partindo_de_c)

    # def test_ao_informar_vertice_c_trazer_menor_caminho(self):
    #     grafo: Grafo = self.reader.ler_arquivo_entrada(self.caminho_arquivo_grafo)
    #     caminho_partindo_de_d = dijkstra(grafo, grafo.get_vertice('d'))
    #     valores_caminho_minimo_partindo_de_d = map_and_list(lambda vtx: vtx.get_valor(), caminho_partindo_de_d)
    #     self.assertEqual(valores_caminho_minimo_partindo_de_d, self.caminho_minimo_partindo_de_d)


if __name__ == '__main__':
    unittest.main()
