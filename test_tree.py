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


def test_balanced():
    bst = BinarySearchTree()
    bst.put(13)
    bst.put(10)
    bst.put(15)
    bst.put(5)
    bst.put(11)
    bst.put(16)
    bst.put(4)
    bst.put(6)
    bst.put(7, False)
    assert bst.is_unbalanced(bst.root) is True

    bst.delete(7)
    bst.put(7, True)
    assert bst.is_unbalanced(bst.root) is False
