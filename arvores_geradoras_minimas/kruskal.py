from classes.grafo import Grafo

def kruskal(graph: Grafo):
    mst = []
    sets = {node.get_valor(): set([node.get_valor()]) for node in graph.get_vertices()}

    edges = [(peso, u.get_valor(), v.get_valor()) for u in graph.get_vertices() for v, peso in graph.get_adjacentes_as_dict(u.get_valor())[u.get_valor()]]
    edges.sort()

    for peso, u, v in edges:
        set_u = sets[u]
        set_v = sets[v]
        if set_u != set_v:
            mst.append((u, v, peso))
            set_u.update(set_v)
            for node in set_v:
                sets[node] = set_u
    return mst
