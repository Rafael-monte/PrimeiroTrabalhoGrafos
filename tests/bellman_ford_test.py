import unittest
from classes.leitor_arquivo import LeitorArquivo
from classes.grafo import Grafo
from caminhos_minimos.bellman_ford import bellman_ford


class BellmanFordTest(unittest.TestCase):
    reader: LeitorArquivo
    caminho_arquivo_grafo: str

    @classmethod
    def setUpClass(cls) -> None:
        cls.reader = LeitorArquivo()
        cls.caminho_arquivo_grafo = '/home/rafael/Downloads/trabalho-grafos/Trabalho_1_Rafael_Robson/PrimeiroTrabalhoGrafos/input/grafo.txt'

    def test_ao_informar_vertice_mostrar_se_existe_ciclo(self):
        grafo: Grafo = self.reader.ler_arquivo_entrada(self.caminho_arquivo_grafo)
        existe_ciclo = bellman_ford(grafo, grafo.get_vertice('a'))
        self.assertTrue(existe_ciclo)


if __name__ == '__main__':
    unittest.main()
