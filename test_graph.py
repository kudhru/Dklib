from graph import GraphAdjacencyList


def test_graph():
    graph = GraphAdjacencyList(5, False)
    graph.add_edge(0, 1, 1)
    graph.add_edge(0, 4, 1)
    graph.add_edge(1, 2, 1)
    graph.add_edge(1, 3, 1)
    graph.add_edge(1, 4, 1)
    graph.add_edge(2, 3, 1)
    graph.add_edge(3, 4, 1)
    graph.delete_edge(3, 4)
    
    assert graph.print_graph() == [(0,1), (0,4), (1, 0), (1, 2), (1, 3), (1, 4), (2,1), (2,3), (3,1), (3,2), (4, 0), (4, 1)]


def test_bfs():
    graph = GraphAdjacencyList(10, False)
    graph.add_edge(4, 6, 1)
    graph.add_edge(5, 6, 1)
    graph.add_edge(4, 5, 1)
    graph.add_edge(2, 4, 1)
    graph.add_edge(2, 5, 1)
    graph.add_edge(1, 2, 1)
    graph.add_edge(1, 3, 1)
    graph.add_edge(3, 5, 1)

    assert graph.bfs(1) == [1, 2, 3, 4, 5, 6, 0, 7, 8, 9]


def test_dfs():
    graph = GraphAdjacencyList(10, False)
    graph.add_edge(4, 6, 1)
    graph.add_edge(5, 6, 1)
    graph.add_edge(4, 5, 1)
    graph.add_edge(2, 4, 1)
    graph.add_edge(2, 5, 1)
    graph.add_edge(1, 2, 1)
    graph.add_edge(1, 3, 1)
    graph.add_edge(3, 5, 1)
    assert graph.dfs(1) == [1, 2, 4, 6, 5, 3, 0, 7, 8, 9]