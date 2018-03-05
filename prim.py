from collections import defaultdict, deque

import sys


class Heap():
    def __init__(self):
        self.array = []
        self.size = 0
        self.pos = []

    def newMinHeapNode(self, v, dist):
        minHeapNode = [v, dist]
        return minHeapNode

    def swapMinHeapNode(self, a, b):
        t = self.array[a]
        self.array[a] = self.array[b]
        self.array[b] = t

    def minHeapify(self, idx):
        smallest = idx
        left = 2 * idx + 1
        right = 2 * idx + 2

        if left < self.size and self.array[left][1] < self.array[smallest][1]:
            smallest = left

        if right < self.size and self.array[right][1] < self.array[smallest][1]:
            smallest = right

        # The nodes to be swapped in min heap
        # if idx is not smallest
        if smallest != idx:
            # Swap positions
            self.pos[self.array[smallest][0]] = idx
            self.pos[self.array[idx][0]] = smallest

            # Swap nodes
            self.swapMinHeapNode(smallest, idx)

            self.minHeapify(smallest)

    def extractMin(self):

        # Return NULL wif heap is empty
        if self.isEmpty():
            return

        # Store the root node
        root = self.array[0]

        # Replace root node with last node
        lastNode = self.array[self.size - 1]
        self.array[0] = lastNode

        # Update position of last node
        self.pos[lastNode[0]] = 0
        self.pos[root[0]] = self.size - 1

        # Reduce heap size and heapify root
        self.size -= 1
        self.minHeapify(0)

        return root

    def isEmpty(self):
        return True if self.size == 0 else False

    def decreaseKey(self, v, dist):

        # Get the index of v in  heap array

        i = self.pos[v]

        # Get the node and update its dist value
        self.array[i][1] = dist

        # Travel up while the complete tree is not
        # hepified. This is a O(Logn) loop
        while i > 0 and self.array[i][1] < self.array[(i - 1) // 2][1]:
            # Swap this node with its parent
            self.pos[self.array[i][0]] = (i - 1) // 2
            self.pos[self.array[(i - 1) // 2][0]] = i
            self.swapMinHeapNode(i, (i - 1) // 2)
            # move to parent index
            i = (i - 1) // 2

    def isInMinHeap(self, v):

        if self.pos[v] < self.size:
            return True
        return False


def printArr(parent, n):
    for i in range(1,n):
        print("{0} - {1}".format(parent[i], i))


class GraphAdjList:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_list = defaultdict(list)

    def add_edge(self, source, destination, weight):
        self._add_edge(source, destination, weight)
        self._add_edge(destination, source, weight)

    def _add_edge(self, source, destination, weight):
        for i in range(len(self.adj_list[source])):
            if self.adj_list[source][i][0] == destination:
                self.adj_list[source][i][1] = weight
                return
        self.adj_list[source].append([destination, weight])
        return

    def bfs(self, start_vertex):
        bfs_result = []
        visited = [False] * self.num_vertices
        q = deque()
        q.append(start_vertex)
        visited[start_vertex] = True
        while len(q) > 0:
            while len(q) > 0:
                vertex = q.popleft()
                bfs_result.append(vertex)
                for [dest, weight] in self.adj_list[vertex]:
                    if not visited[dest]:
                        q.append(dest)
                        visited[dest] = True
            for i in range(self.num_vertices):
                if not visited[i]:
                    q.append(i)
                    visited[i] = True
        return bfs_result

    def PrimMST(self):
        # Get the number of vertices in graph
        V = self.num_vertices

        # key values used to pick minimum weight edge in cut
        key = []

        # List to store contructed MST
        parent = []

        # minHeap represents set E
        minHeap = Heap()

        #  Initialize min heap with all vertices. Key values of all
        # vertices (except the 0th vertex) is is initially infinite
        for v in range(V):
            parent.append(-1)
            key.append(1e10)
            minHeap.array.append(minHeap.newMinHeapNode(v, key[v]))
            minHeap.pos.append(v)

        # Make key value of 0th vertex as 0 so
        # that it is extracted first
        minHeap.pos[0] = 0
        key[0] = 0
        minHeap.decreaseKey(0, key[0])

        # Initially size of min heap is equal to V
        minHeap.size = V;

        # In the following loop, min heap contains all nodes
        # not yet added in the MST.
        while minHeap.isEmpty() == False:

            # Extract the vertex with minimum distance value
            newHeapNode = minHeap.extractMin()
            u = newHeapNode[0]

            # Traverse through all adjacent vertices of u
            # (the extracted vertex) and update their
            # distance values
            for pCrawl in self.adj_list[u]:

                v = pCrawl[0]

                # If shortest distance to v is not finalized
                # yet, and distance to v through u is less than
                # its previously calculated distance
                if minHeap.isInMinHeap(v) and pCrawl[1] < key[v]:
                    key[v] = pCrawl[1]
                    parent[v] = u

                    # update distance value in min heap also
                    minHeap.decreaseKey(v, key[v])

        printArr(parent, V)

graph = GraphAdjList(9)
graph.add_edge(0, 1, 4)
graph.add_edge(0, 7, 8)
graph.add_edge(1, 2, 8)
graph.add_edge(1, 7, 11)
graph.add_edge(2, 3, 7)
graph.add_edge(2, 8, 2)
graph.add_edge(2, 5, 4)
graph.add_edge(3, 4, 9)
graph.add_edge(3, 5, 14)
graph.add_edge(4, 5, 10)
graph.add_edge(5, 6, 2)
graph.add_edge(6, 7, 1)
graph.add_edge(6, 8, 6)
graph.add_edge(7, 8, 7)
graph.PrimMST()