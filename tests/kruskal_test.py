import unittest
from classes.grafo import Grafo
from classes.leitor_arquivo import LeitorArquivo
from arvores_geradoras_minimas.kruskal import kruskal
from utils.iterators import map_and_list


class KruskalTest(unittest.TestCase):
    reader: LeitorArquivo
    arvore_minima_partindo_de_a = list[tuple[str,str, int]]
    arvore_minima_partindo_de_f = dict[str, int]
    arvore_minima_partindo_de_e = dict[str, int]
    caminho_arquivo_grafo: str

    @classmethod
    def setUpClass(cls) -> None:
        cls.reader = LeitorArquivo()
        cls.arvore_minima_partindo_de_a = [('a', 'd', 1), ('b', 'c', 2), ('d', 'e', 3), ('c', 'f', 4), ('b', 'e', 7)];
        cls.caminho_arquivo_grafo = '/home/user/grafos/PrimeiroTrabalhoGrafos/input/grafo.txt'


    def test_ao_informar_grafo_trazer_menor_arvore(self):
        grafo: Grafo = self.reader.ler_arquivo_entrada(self.caminho_arquivo_grafo)
        arvore_minima_partindo_de_a = kruskal(grafo)
        self.assertEqual(arvore_minima_partindo_de_a, self.arvore_minima_partindo_de_a)


if __name__ == '__main__':
    unittest.main()
