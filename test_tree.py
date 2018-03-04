from tree import BinarySearchTree, bfs, dfs


def test_bfs():
    bst = BinarySearchTree()
    bst.put(10)
    bst.put(4)
    bst.put(17)
    bst.put(1)
    bst.put(9)
    bst.put(18)
    bst.put(12)
    assert bfs(bst) == [10, 4, 17, 1, 9, 12, 18]


def test_dfs():
    bst = BinarySearchTree()
    bst.put(10)
    bst.put(4)
    bst.put(17)
    bst.put(1)
    bst.put(9)
    bst.put(18)
    bst.put(12)
    assert dfs(bst) == [1, 4, 9, 10, 12, 17, 18]


def test_delete():
    bst = BinarySearchTree()
    bst.put(10)
    bst.put(4)
    bst.put(17)
    bst.put(1)
    bst.put(9)
    bst.put(18)
    bst.put(12)

    bst.delete(4)
    bst.put(4)
    bst.delete(18)
    bst.put(18)
    bst.delete(1)
    bst.delete(10)
    bst.delete(4)
    assert dfs(bst) == [9, 12, 17, 18]
