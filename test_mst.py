from prim import GraphAdjList


def test_bfs():
    graph = GraphAdjList(10)
    graph.add_edge(4, 6, 1)
    graph.add_edge(5, 6, 1)
    graph.add_edge(4, 5, 1)
    graph.add_edge(2, 4, 1)
    graph.add_edge(2, 5, 1)
    graph.add_edge(1, 2, 1)
    graph.add_edge(1, 3, 1)
    graph.add_edge(3, 5, 1)

    assert graph.bfs(1) == [1, 2, 3, 4, 5, 6, 0, 7, 8, 9]