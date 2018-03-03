from hash_table import HashTable


def test_hash_table():
    hash_table = HashTable(5)

    hash_table.put('abc', 23)
    assert hash_table.get('abc') == 23

    hash_table.put('abc', 25)
    assert hash_table.get('abc') == 25

    hash_table.put('xyz', 12)
    assert hash_table.get('xyz') == 12

    hash_table.delete('xyz')
    assert hash_table.get('xyz') is None

    assert hash_table.get('uvw') is None

    hash_table.put('def', 10)
    hash_table.put('jkl', 34)

    hash_table.delete('abc')
    assert hash_table.get('abc') is None

    assert hash_table.get('def') == 10
    assert hash_table.get('jkl') == 34