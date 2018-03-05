from collections import deque


class GraphNode:
    def __init__(self, index, weight):
        self.index = index
        self.weight = weight
        self.visited = False
        self.next = None

    def __str__(self):
        return '({0}, {1})'.format(self.index, self.weight)


class GraphAdjacencyList:
    def __init__(self, num_vertices, is_directed=True):
        self.num_vertices = num_vertices
        self.heads_list = [None] * num_vertices
        self.is_directed = is_directed

    def _add_edge(self, source, destination, weight):
        new_node = GraphNode(destination, weight)
        curr = self.heads_list[source]
        if curr is None:
            self.heads_list[source] = new_node
            return

        # add edge to the end of the linked list. If the edge already exists, update its weight
        prev = curr
        while curr is not None:
            if curr.index == destination:
                curr.weight = weight
                return
            prev = curr
            curr = curr.next
        prev.next = new_node
        return

    def add_edge(self, source, destination, weight):
        self._add_edge(source, destination, weight)
        if not self.is_directed:
            self._add_edge(destination, source, weight)
        return

    def _delete_edge(self, source, destination):
        curr = self.heads_list[source]
        if curr is None:
            return

        if curr.next is None:
            if curr.index == destination:
                self.heads_list[source] = None
                del curr
                return
            return

        prev = curr
        curr = curr.next
        while curr is not None:
            if curr.index == destination:
                prev.next = curr.next
                del curr
                return
            prev = curr
            curr = curr.next
        return

    def delete_edge(self, source, destination):
        self._delete_edge(source, destination)
        if not self.is_directed:
            self._delete_edge(destination, source)
        return

    def get_edge(self, source, destination):
        curr = self.heads_list[source]
        while curr is not None:
            if curr.index == destination:
                return curr
            curr = curr.next
        return None

    def print_graph(self):
        # this edge list is only for testing purposes. see test_graph.py
        edge_list = []
        for i in range(self.num_vertices):
            curr = self.heads_list[i]
            print('Adjacency list of vertex {0}:'.format(i))
            if curr is None:
                print('Empty List')
            print_string = ''
            while curr is not None:
                print_string += curr.__str__() + ', '
                edge_list.append((i, curr.index))
                curr = curr.next
            print(print_string)
        return edge_list

    def bfs(self, start_node):
        queue = deque()
        bfs_list = [] # storing the bfs mainly for testing purposes
        visited_vertices = [False] * self.num_vertices
        queue.append(start_node)
        while len(queue) > 0:
            while len(queue) > 0:
                node = queue.popleft()
                bfs_list.append(node)
                print(node)
                visited_vertices[node] = True

                curr = self.heads_list[node]
                while curr is not None:
                    if not visited_vertices[curr.index]:
                        queue.append(curr.index)
                        visited_vertices[curr.index] = True
                    curr = curr.next
            for i in range(self.num_vertices):
                if not visited_vertices[i]:
                    queue.append(i)
                    break
        return bfs_list

    def dfs(self, start_vertex):
        visited_vertices = [False] * self.num_vertices
        dfs_traversal = []
        self._dfs(start_vertex, visited_vertices, dfs_traversal)
        for i in range(self.num_vertices):
            if not visited_vertices[i]:
                self._dfs(i, visited_vertices, dfs_traversal)
        return dfs_traversal

    def _dfs(self, vertex, visited_vertices, dfs_traversal):
        visited_vertices[vertex] = True
        dfs_traversal.append(vertex)
        print(vertex)
        curr = self.heads_list[vertex]
        while curr is not None:
            if not visited_vertices[curr.index]:
                self._dfs(curr.index, visited_vertices, dfs_traversal)
            curr = curr.next
        return


graph = GraphAdjacencyList(5, False)
graph.add_edge(0,1,1)
graph.add_edge(0,4,1)
graph.add_edge(1, 2, 1)
graph.add_edge(1,3,1)
graph.add_edge(1,4,1)
graph.add_edge(2,3,1)
graph.add_edge(3,4,1)
graph.delete_edge(3,4)

graph.print_graph()

graph = GraphAdjacencyList(7, False)
graph.add_edge(4, 6, 1)
graph.add_edge(5, 6, 1)
graph.add_edge(4, 5, 1)
graph.add_edge(2, 4, 1)
graph.add_edge(2, 5, 1)
graph.add_edge(1, 2, 1)
graph.add_edge(1, 3, 1)
graph.add_edge(3, 5, 1)
bfs_result = graph.bfs(1)
dfs_result = graph.dfs(1)
print(dfs_result)




