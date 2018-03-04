from collections import deque


class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key
        self.visited = False

    def __str__(self):
        return '{0}'.format(self.key)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def put(self, key):
        if self.root is None:
            self.root = TreeNode(key)
            return
        self.__add_node__(self.root, key)

    def __add_node__(self, node, key):
        if node.key >= key:
            if node.left is None:
                node.left = TreeNode(key)
            else:
                self.__add_node__(node.left, key)
        else:
            if node.right is None:
                node.right = TreeNode(key)
            else:
                self.__add_node__(node.right, key)

    def __print__(self, node):
        if node is None:
            return

        self.__print__(node.left)
        print('{0}\n'.format(node.key))
        self.__print__(node.right)
        return

    def delete(self, key):
        result = self.__delete__(self.root, key)
        if result == 0:
            return 0
        else:
            self.root = result
            return 1

    def __delete__(self, node, key):
        if node is None:
            return 0
        if node.key == key:
            if node.left is None and node.right is None:
                del node
                return None
            elif node.left is None:
                temp = node.right
                del node
                return temp
            elif node.right is None:
                temp = node.left
                del node
                return temp
            else:
                temp = self.__get__smallest_node__(node.right)
                node.key = temp.key
                node.right = self.__delete__(node.right, temp.key)
                return node
        elif node.key < key:
            node.right = self.__delete__(node.right, key)
            return node
        else:
            node.left = self.__delete__(node.left, key)
            return node

    def debug_print(self):
        print('in-order traversal:\n')
        if self.root is None:
            print('Empty Tree\n')
            return

        self.__print__(self.root)

    def __get__smallest_node__(self, node):
        if node.left is None:
           return node
        return self.__get__smallest_node__(node.left)


def bfs(tree):
    bfs_traversed_result = []
    print('Printing BFS of tree\n')
    root = tree.root
    q = deque()
    q.append(root)
    while len(q) > 0:
        node = q.popleft()
        print(node)
        bfs_traversed_result.append(node.key)
        if node.left is not None:
            q.append(node.left)
        if node.right is not None:
            q.append(node.right)
    return bfs_traversed_result


def _dfs(node, dfs_result):
    if node is None:
        return
    _dfs(node.left, dfs_result)
    dfs_result.append(node.key)
    _dfs(node.right, dfs_result)
    return


def dfs(tree):
    print('Printing depth first traversal of tree')
    dfs_result = []
    _dfs(tree.root, dfs_result)
    return dfs_result


bst = BinarySearchTree()
bst.put(10)
bst.put(4)
bst.put(17)
bst.put(1)
bst.put(9)
bst.put(18)
bst.put(12)
bst.debug_print()
bfs(bst)
result = dfs(bst)
print(result)
bst.delete(4)
bst.put(4)
bst.delete(18)
bst.put(18)
bst.delete(1)
bst.delete(10)
result = dfs(bst)
print(result)




