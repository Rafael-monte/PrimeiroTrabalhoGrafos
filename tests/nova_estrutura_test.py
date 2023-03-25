import unittest
from classes.leitor_arquivo import LeitorArquivo
from classes.grafo import Grafo
from config import INPUT_FILE_LOCATION
from classes.vertice import Vertice
from classes.aresta import Aresta
from classes.tipo_aresta import TipoAresta
class MyTestCase(unittest.TestCase):
    reader: LeitorArquivo
    grafo: Grafo
    arestas_com_peso: list[Aresta]
    @classmethod
    def setUpClass(cls) -> None:
        cls.reader = LeitorArquivo()
        # Colocar como argumento o caminho absoluto do arquivo de grafo
        cls.grafo: Grafo = cls.reader.ler_arquivo_entrada()
        cls.arestas_com_peso = [
            Aresta(Vertice('a'), Vertice('b'), TipoAresta.NAO_DIRECIONADO, 9),
            Aresta(Vertice('a'), Vertice('d'), TipoAresta.NAO_DIRECIONADO, 1),
            Aresta(Vertice('d'), Vertice('e'), TipoAresta.NAO_DIRECIONADO, 3),
            Aresta(Vertice('b'), Vertice('c'), TipoAresta.NAO_DIRECIONADO, 2),
            Aresta(Vertice('e'), Vertice('f'), TipoAresta.NAO_DIRECIONADO, 8),
            Aresta(Vertice('c'), Vertice('f'), TipoAresta.NAO_DIRECIONADO, 4),
            Aresta(Vertice('a'), Vertice('e'), TipoAresta.NAO_DIRECIONADO, 5),
            Aresta(Vertice('b'), Vertice('f'), TipoAresta.NAO_DIRECIONADO, 6),
        ]

    def test_ao_buscar_arestas_grafo_trazer_pesos(self):
        arestas_sem_peso_grafo = filter(lambda aresta: aresta.get_peso_aresta() <= 0, self.grafo.get_arestas())
        self.assertTrue(len(list(arestas_sem_peso_grafo)) == 0, "Não deve existir aresta sem peso")

    def test_ao_buscar_vertices_trazer_sem_peso_e_com_distancia_negativa(self):
        vertices = self.grafo.get_vertices()
        vertices_com_distancia = filter(lambda vertice: vertice.get_distancia() > -1, vertices)
        vertices_com_antecessor = filter(lambda vertice: vertice.get_antecessor() is not None, vertices)

        self.assertTrue(len(list(vertices_com_distancia)) == 0, "Não deveria existir vertice com distancia")
        self.assertTrue(len(list(vertices_com_antecessor)) == 0, "Não deveria existir vertice com antecessor")

    def test_ao_buscar_arestas_trazer_pesos_corretos(self):
        for aresta in self.arestas_com_peso:
            self.assertIn(aresta, self.grafo.get_arestas(), "A aresta deveria existir no grafo")
            # Buscando aresta no grafo
            aresta_grafo = list(filter(lambda a: a.get_inicio_aresta().get_valor() == aresta.get_inicio_aresta().get_valor() and a.get_fim_aresta().get_valor() == aresta.get_fim_aresta().get_valor(), self.grafo.get_arestas()))
            self.assertEqual(aresta_grafo[0].get_peso_aresta(), aresta.get_peso_aresta(), "Os pesos deveriam ser iguais")

if __name__ == '__main__':
    unittest.main()
