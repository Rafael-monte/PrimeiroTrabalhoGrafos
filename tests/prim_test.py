import unittest
from classes.grafo import Grafo
from classes.leitor_arquivo import LeitorArquivo
from arvores_geradoras_minimas.algoritmo_prim import prim
from utils.iterators import map_and_list


class PrimTest(unittest.TestCase):
    reader: LeitorArquivo
    arvore_minima_partindo_de_a = dict[str, int]
    arvore_minima_partindo_de_f = dict[str, int]
    arvore_minima_partindo_de_e = dict[str, int]
    caminho_arquivo_grafo: str

    @classmethod
    def setUpClass(cls) -> None:
        cls.reader = LeitorArquivo()
        cls.arvore_minima_partindo_de_a = {'d': 1, 'e': 3, 'b': 7, 'c': 2, 'f': 4};
        cls.arvore_minima_partindo_de_f = {'c': 4, 'b': 2, 'e': 7, 'd': 3, 'a': 1};
        cls.arvore_minima_partindo_de_e = {'d': 3, 'a': 1, 'b': 7, 'c': 2, 'f': 4};
        cls.caminho_arquivo_grafo = '/home/user/grafos/PrimeiroTrabalhoGrafos/input/grafo.txt'


    def test_ao_informar_vertice_inicial_a_trazer_menor_arvore(self):
        grafo: Grafo = self.reader.ler_arquivo_entrada(self.caminho_arquivo_grafo)
        arvore_minima_partindo_de_a = prim(grafo, grafo.get_vertice('a'))
        self.assertEqual(arvore_minima_partindo_de_a, self.arvore_minima_partindo_de_a)

    def test_ao_informar_vertice_inicial_f_trazer_menor_arvore(self):
        grafo: Grafo = self.reader.ler_arquivo_entrada(self.caminho_arquivo_grafo)
        arvore_minima_partindo_de_f = prim(grafo, grafo.get_vertice('f'))
        self.assertEqual(arvore_minima_partindo_de_f, self.arvore_minima_partindo_de_f)

    def test_ao_informar_vertice_inicial_e_trazer_menor_arvore(self):
        grafo: Grafo = self.reader.ler_arquivo_entrada(self.caminho_arquivo_grafo)
        arvore_minima_partindo_de_e = prim(grafo, grafo.get_vertice('e'))
        self.assertEqual(arvore_minima_partindo_de_e, self.arvore_minima_partindo_de_e)


if __name__ == '__main__':
    unittest.main()
