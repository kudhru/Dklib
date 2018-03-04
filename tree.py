from collections import deque


class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key
        self.visited = False
        self.height = 1 # difference between the heights of left and right sub-trees

    def __str__(self):
        return '{0}: {1}'.format(self.key, self.height)


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def put(self, key, rebalance=True):
        if self.root is None:
            self.root = TreeNode(key)
            return
        self.root = self._add_node(self.root, key, rebalance)
        return

    def _add_node(self, node, key, rebalance=True):
        if node.key >= key:
            if node.left is None:
                node.left = TreeNode(key)
            else:
                node.left = self._add_node(node.left, key, rebalance)
        else:
            if node.right is None:
                node.right = TreeNode(key)
            else:
                node.right = self._add_node(node.right, key, rebalance)
        node.height = self._compute_height(node)
        if rebalance and self.is_unbalanced(node):
            node = self._rebalance(node, key)
        return node

    def _print(self, node):
        if node is None:
            return

        self._print(node.left)
        print(node)
        self._print(node.right)
        return

    def delete(self, key):
        result = self._delete(self.root, key)
        if result == 0:
            return 0
        else:
            self.root = result
            return 1

    def _delete(self, node, key):
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
                temp = self._get_smallest_node(node.right)
                node.key = temp.key
                node.right = self._delete(node.right, temp.key)
                return node
        elif node.key < key:
            node.right = self._delete(node.right, key)
            return node
        else:
            node.left = self._delete(node.left, key)
            return node

    def debug_print(self):
        print('in-order traversal:\n')
        if self.root is None:
            print('Empty Tree\n')
            return

        self._print(self.root)

    def _get_smallest_node(self, node):
        if node.left is None:
           return node
        return self._get_smallest_node(node.left)

    def _compute_height(self, node):
        if node.left is not None:
            height_left = node.left.height
        else:
            height_left = 0
        if node.right is not None:
            height_right = node.right.height
        else:
            height_right = 0
        return max(height_left, height_right) + 1

    def is_unbalanced(self, node):
        if node.left is not None:
            height_left = node.left.height
        else:
            height_left = 0
        if node.right is not None:
            height_right = node.right.height
        else:
            height_right = 0
        if abs(height_left - height_right) > 1:
            return True
        else:
            return False

    def _rebalance(self, node, key):
        z = node
        if z.key < key:
            y = z.right
            # t1 = z.left
            if y.key < key:
                # right right case

                # x = y.right
                t2 = y.left
                # t3 = x.left
                # t4 = x.right

                # rotate
                y.left = z
                z.right = t2

                z.height = self._compute_height(z)
                y.height = self._compute_height(y)
                return y
            else:
                # right left case

                x = y.left
                t2 = x.left
                t3 = x.right
                # t4 = y.right

                # first rotation
                z.right = x
                x.right = y
                y.left = t3

                # second rotation
                x.left = z
                z.right = t2

                z.height = self._compute_height(z)
                y.height = self._compute_height(y)
                x.height = self._compute_height(x)
                return x
        else:
            y = z.left
            # t4 = z.right
            if y.key < key:
                # left right case

                x = y.right
                # t1 = y.left
                t2 = x.left
                t3 = x.right

                # first rotation
                z.left = x
                x.left = y
                y.right = t2

                # second rotation
                x.right = z
                z.left = t3

                z.height = self._compute_height(z)
                y.height = self._compute_height(y)
                x.height = self._compute_height(x)
                return x
            else:
                # left left case

                # x = y.left
                # t1 = x.left
                # t2 = x.right
                t3 = y.right

                # rotate
                y.right = z
                z.left = t3

                z.height = self._compute_height(z)
                y.height = self._compute_height(y)
                return y



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
# bst.put(10)
# bst.put(4)
# bst.put(17)
# bst.put(1)
# bst.put(9)
# bst.put(18)
# bst.put(12)
# bst.debug_print()
# bfs(bst)
# result = dfs(bst)
# print(result)
# bst.delete(4)
# bst.put(4)
# bst.delete(18)
# bst.put(18)
# bst.delete(1)
# bst.delete(10)
# result = dfs(bst)
# print(result)
bst.put(13)
bst.put(10)
bst.put(15)
bst.put(5)
bst.put(11)
bst.put(16)
bst.put(4)
bst.put(6)
# bst.put(14)
bst.debug_print()
bst.put(7, False)
print(bst.is_unbalanced(bst.root))
bst.debug_print()

