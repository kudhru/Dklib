from node import Node


def _hash(key):
    hash = 5381
    byte_array = key.encode('utf-8')

    for byte in byte_array:
        # the modulus keeps it 32-bit, python ints don't overflow
        hash = ((hash * 33) ^ byte) % 0x100000000
    return hash


class HashTable:
    def __init__(self, array_size=64):
        self.bucket_array = [None for i in range(array_size)]
        self.size = array_size

    def put(self, key, value):
        key_hash = _hash(key)
        bucket_index = key_hash % self.size
        self.__insert__(bucket_index, key, value)
        return

    def __insert__(self, index, key, value):
        curr = self.bucket_array[index]

        if curr is None:
            node = Node(key, value)
            self.bucket_array[index] = node
            return

        while curr.next is not None:
            if curr.key == key:
                curr.value = value
                return
            curr = curr.next

        if curr.key == key:
            curr.value = value
            return
        else:
            node = Node(key, value)
            curr.next = node
        return

    def get(self, key):
        key_hash = _hash(key)
        bucket_index = key_hash % self.size

        curr = self.bucket_array[bucket_index]

        if curr is None:
            return None

        while curr is not None:
            if curr.key == key:
                return curr.value
            curr = curr.next

        return None

    def delete(self, key):
        key_hash = _hash(key)
        bucket_index = key_hash % self.size

        curr = self.bucket_array[bucket_index]

        if curr is None:
            return 0
        elif curr.key == key:
            temp = curr
            self.bucket_array[bucket_index] = curr.next
            del temp
            return 1
        elif curr.next is None:
            if curr.key == key:
                del curr
                self.bucket_array[bucket_index] = None
                return 1
            else:
                return 0

        prev = curr
        curr = curr.next
        while curr is not None:
            if curr.key == key:
                prev.next = curr.next
                del curr
                return 1
            prev = curr
            curr = curr.next

        return 0

    def debug_print(self):
        for i in range(self.size):
            print('Bucket {0}:\n'.format(i))
            if self.bucket_array[i] is None:
                print('\tEmpty\n')
                continue
            curr = self.bucket_array[i]
            while curr is not None:
                print('\t{0}\n'.format(curr))
                curr = curr.next
        return



hash_table = HashTable(5)

hash_table.put('abc', 23)
assert hash_table.get('abc') == 23

hash_table.put('abc', 25)
assert hash_table.get('abc') == 25

hash_table.put('xyz', 12)
assert hash_table.get('xyz') == 12

# hash_table.delete('xyz')
# assert hash_table.get('xyz') is None

assert hash_table.get('uvw') is None

hash_table.put('def', 10)
hash_table.put('jkl', 34)

# hash_table.delete('abc')
# assert hash_table.get('abc') is None

assert hash_table.get('def') == 10
assert hash_table.get('jkl') == 34

hash_table.debug_print()

