
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __str__(self):
        return "'{}': '{}'".format(self.key, self.value)

