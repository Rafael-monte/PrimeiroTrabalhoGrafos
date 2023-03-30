from classes.grafo import Grafo

def kruskal(graph: Grafo):
    arvore_minima = []
    # Cria um dicionário com os vértices e seus respectivos valores
    sets = {vtx.get_valor(): set([vtx.get_valor()]) for vtx in graph.get_vertices()}

    arestas_as_tuple = []

    # Converte as classes de aresta para um tipo mais flexível (no caso uma tupla de (int, str str))
    for u_vtx in graph.get_vertices():
        for v_vtx, weight in graph.get_adjacentes_as_dict(u_vtx.get_valor())[u_vtx.get_valor()]:
            arestas_as_tuple.append((weight, u_vtx.get_valor(), v_vtx.get_valor()))
    
    # Ordena as arestas pelo peso
    arestas_as_tuple.sort()

    for peso, u, v in arestas_as_tuple:
        set_vtx_u = sets[u]
        set_vtx_v = sets[v]
        if set_vtx_u != set_vtx_v:
            arvore_minima.append((u, v, peso))
            set_vtx_u.update(set_vtx_v)
            for vtx_value in set_vtx_v:
                sets[vtx_value] = set_vtx_u
    return arvore_minima
